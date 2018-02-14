import numpy as np
import pandas as pd

from antlr4 import *

from pyjavu.parser.FirstOrderRegExpLexer import FirstOrderRegExpLexer
from pyjavu.parser.FirstOrderRegExpParser import FirstOrderRegExpParser
from pyjavu.parser.FirstOrderRegExpVisitor import FirstOrderRegExpVisitor

from pyjavu.datamgr import DataManager

def eval(df, expr, inplace=False, local_dict=dict(), global_dict=dict()):
    "Compile a regular expression, and evaluate."

    lexer = FirstOrderRegExpLexer(InputStream(expr))
    stream = CommonTokenStream(lexer)
    parser = FirstOrderRegExpParser(stream)
    tree = parser.namedExpr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    # Annotate the syntax tree with positions, nullable values, and output positions 
    annotator = FirstOrderRegExpAnnotator()
    annotator.visit(tree)

    # Generate update equations
    builder = FirstOrderRegExpBuilder()
    builder.build(tree)

    code = '\n'.join(builder.statements)
    machine = compile(code, "<string>", "exec")
    db = DataManager(builder.variables)

    # print(code)

    # Initialize the machine
    states = np.array([db.const(value) for value in builder.initialization])
    nstates = np.array([db.const(value) for value in builder.initialization])

    # Initialize the output
    output = np.array([db.const(tree.nullable)])

    data = []
    for letter in df.itertuples():
        exec(machine, globals(), {**local_dict, **locals()})
        states = np.copy(nstates)
        data.append(output[0])
    
    new_frame = pd.DataFrame(columns=[builder.name], data=data)

    if inplace:
        df[builder.name] = new_frame
        return df
    else:
        return new_frame

class FirstOrderRegExpAnnotator(FirstOrderRegExpVisitor):

    def __init__(self):
        super().__init__()
        self.num = 1
        self.variables = set()

        self.name = None
        self.statements = list()

    def visitNamedExpr(self, ctx:FirstOrderRegExpParser.NamedExprContext):
        
        self.visit(ctx.child)

        try:
            ctx.name = ctx.name.text
        except AttributeError as e:
            ctx.name = None
        finally:
            ctx.nullable = ctx.child.nullable
            ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    def visitProp(self, ctx:FirstOrderRegExpParser.PropContext):

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num
        ctx.callname = 'letter.{}'.format(ctx.name.text)
        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    def visitPred(self, ctx:FirstOrderRegExpParser.PredContext):
        name = ctx.name.text
        nargs = ["letter.{}".format(arg) for arg in ctx.args.getText().split(',')]

        ctx.callname = "{name}({params})".format(name=name, params=','.join(nargs))

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num

        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    def visitVarConst(self, ctx:FirstOrderRegExpParser.VarConstContext):
        child = self.visit(ctx.child)
        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.position = ctx.child.position

        return self.num, ctx.nullable, ctx.output

    def visitVarBind(self, ctx:FirstOrderRegExpParser.VarBindContext):
        child = self.visit(ctx.child)
        varname = ctx.varname.text
        self.variables.add(varname)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.position = ctx.child.position

        return self.num, ctx.nullable, ctx.output
    # Visit a parse tree produced by FirstOrderRegExpParser#Grouping.
    def visitAtomic(self, ctx:FirstOrderRegExpParser.AtomicContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.position = ctx.child.position

        return self.num, ctx.nullable, ctx.output

    def visitExists(self, ctx:FirstOrderRegExpParser.ExistsContext):
        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = set([self.num])
        ctx.position = self.num

        ctx.varnames = set(ctx.args.getText().split(','))
        ctx.callname = "states[{}]".format(self.num)

        self.num = self.num + 1

        return self.num, ctx.nullable, ctx.output

    def visitUnion(self, ctx:FirstOrderRegExpParser.UnionContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable or ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by FirstOrderRegExpParser#Concat.
    def visitConcat(self, ctx:FirstOrderRegExpParser.ConcatContext):

        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable and ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output if ctx.right.nullable else ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by FirstOrderRegExpParser#Star.
    def visitStar(self, ctx:FirstOrderRegExpParser.StarContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by FirstOrderRegExpParser#Grouping.
    def visitGrouping(self, ctx:FirstOrderRegExpParser.GroupingContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by FirstOrderRegExpParser#Question.
    def visitQuestion(self, ctx:FirstOrderRegExpParser.QuestionContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by FirstOrderRegExpParser#Plus.
    def visitPlus(self, ctx:FirstOrderRegExpParser.PlusContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable 
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

class FirstOrderRegExpBuilder(FirstOrderRegExpVisitor):

    def __init__(self):
        super().__init__()
        self.name = None
        self.statements = list()
        self.variables = set([])
        self.length = 20

    def build(self, tree, trigger_init=set([0])):

        # Start anywhere
        self.statements.append("nstates[0] = db.bdd.true")

        self.walk(tree, trigger_init)

        # Output function -- Some numpy Python/numpy hacking
        self.statements.append("output[0] = True if ({}) == db.bdd.true else False;".format("db.bdd.apply('or', ".join(['nstates[{}]'.format(i) for i in tree.output]) + ")" * (len(tree.output) - 1)))

        # Zeroth state should be True initially
        self.initialization = [True]
        self. initialization.extend([False] * (len(self.statements) -1 ))

    def walk(self, tree, trigger=set([0])):
        tree.trigger = trigger
        self.visit(tree)

    def visitNamedExpr(self, ctx:FirstOrderRegExpParser.NamedExprContext):
        self.name = ctx.name
        self.walk(ctx.child, ctx.trigger)

    def visitAtomic(self, ctx:FirstOrderRegExpParser.AtomicContext):
        self.walk(ctx.child, ctx.trigger)

    # def visitProp(self, ctx:FirstOrderRegExpParser.PropContext):
    #     return ctx.callname

    # def visitPred(self, ctx:FirstOrderRegExpParser.PredContext):
    #     return ctx.callname

    def visitVarConst(self, ctx:FirstOrderRegExpParser.VarConstContext):
        self.walk(ctx.child, ctx.trigger)
        trig_cond = " | ".join(['states[{}]'.format(i) for i in ctx.trigger])
        self.statements.append("nstates[{}] = {} & ({});".format(ctx.position, "db.const({})".format(ctx.child.callname), trig_cond))

    def visitVarBind(self, ctx:FirstOrderRegExpParser.VarBindContext):
        self.walk(ctx.child, ctx.trigger)
        trig_cond = " | ".join(['states[{}]'.format(i) for i in ctx.trigger])
        varname = ctx.varname.text
        self.variables.add(varname)
        self.statements.append("nstates[{}] = {} & ({});".format(ctx.position, "db.encode({}, '{}')".format(ctx.child.callname, varname), trig_cond))

    def visitExists(self, ctx:FirstOrderRegExpParser.ExistsContext):
        child = self.walk(ctx.child, ctx.trigger)
        variables = ['{}{}'.format(var, index)for var in ctx.varnames for index in range(self.length)]
        trig_cond = "db.bdd.exist([{}], {})".format(','.join(["'{}'".format(var) for var in variables]), " || ".join(['nstates[{}]'.format(i) for i in ctx.child.output]))
        self.statements.append("nstates[{}] = {};".format(ctx.position, trig_cond))

    def visitUnion(self, ctx:FirstOrderRegExpParser.UnionContext):
        self.walk(ctx.left, ctx.trigger)
        self.walk(ctx.right, ctx.trigger)

    # Visit a parse tree produced by FirstOrderRegExpParser#Concat.
    def visitConcat(self, ctx:FirstOrderRegExpParser.ConcatContext):

        self.walk(ctx.left, ctx.trigger)

        if ctx.left.nullable:
            self.walk(ctx.right, ctx.left.output | ctx.trigger)
        else:
            self.walk(ctx.right, ctx.left.output)

    # Visit a parse tree produced by FirstOrderRegExpParser#Star.
    def visitStar(self, ctx:FirstOrderRegExpParser.StarContext):
        self.walk(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by FirstOrderRegExpParser#Grouping.
    def visitGrouping(self, ctx:FirstOrderRegExpParser.GroupingContext):
        self.walk(ctx.child, ctx.trigger)

    # Visit a parse tree produced by FirstOrderRegExpParser#Question.
    def visitQuestion(self, ctx:FirstOrderRegExpParser.QuestionContext):
        self.walk(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by FirstOrderRegExpParser#Plus.
    def visitPlus(self, ctx:FirstOrderRegExpParser.PlusContext):
        self.walk(ctx.child, ctx.child.output | ctx.trigger)

