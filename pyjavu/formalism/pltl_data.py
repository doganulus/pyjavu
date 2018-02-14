import numpy as np
import pandas as pd

from antlr4 import *

from pyjavu.parser.FirstOrderPastLTLLexer import FirstOrderPastLTLLexer
from pyjavu.parser.FirstOrderPastLTLParser import FirstOrderPastLTLParser
from pyjavu.parser.FirstOrderPastLTLVisitor import FirstOrderPastLTLVisitor

from pyjavu.datamgr import DataManager

def eval(df, expr, inplace=False, local_dict=dict(), global_dict=dict()):
    "Compile a past linear-time temporal logic formula, and evaluate."

    lexer = FirstOrderPastLTLLexer(InputStream(expr))
    stream = CommonTokenStream(lexer)
    parser = FirstOrderPastLTLParser(stream)
    tree = parser.namedExpr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    builder = FirstOrderPastLTLBuilder()
    builder.build(tree)

    db = DataManager(builder.variables)

    code = '\n'.join(builder.statements)
    machine = compile(code, "<string>", "exec")

    # print(code)

    states = np.array([db.const(value) for value in builder.initialization])
    output = np.array([db.const(False)])


    data = []
    for letter in df.itertuples():
        exec(machine, globals(), {**local_dict, **locals()})
        data.append(output[0])

    new_frame = pd.DataFrame(columns=[builder.name], data=data)

    if inplace:
        df[builder.callname] = new_frame
        return df
    else:
        return new_frame

class FirstOrderPastLTLBuilder(FirstOrderPastLTLVisitor):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.name = None
        self.initialization = list()
        self.statements = list()
        self.variables = set()
        self.length = 20

    def build(self, tree, length=20):
        child = self.visit(tree)
        label = "states[{}]".format(self.num)

        self.length = length
        self.initialization.append(False)
        self.statements.append("{} = {};".format(label, child))
        self.num = self.num + 1

        self.statements.append('output[0] = True if states[-1] == db.bdd.true else False;')

        return self.initialization, self.statements

    def visitNamedExpr(self, ctx:FirstOrderPastLTLParser.NamedExprContext):
        try:
            self.callname = ctx.name.text
        except AttributeError as e:
            self.callname = None

        return self.visit(ctx.child)

    def visitProp(self, ctx:FirstOrderPastLTLParser.PropContext):
        name = ctx.name.text
        return "letter.{}".format(name)

    def visitPred(self, ctx:FirstOrderPastLTLParser.PredContext):
        name = ctx.name.text
        args = ctx.args.getText().split(',')
        nargs = ["letter.{}".format(arg) for arg in args] 

        # return "letter.{}".format(name)
        return "{name}({params})".format(name=name, params=','.join(nargs))

    def visitVarConst(self, ctx:FirstOrderPastLTLParser.VarConstContext):
        child = self.visit(ctx.child)
        return "db.const({})".format(child)

    def visitVarBind(self, ctx:FirstOrderPastLTLParser.VarBindContext):
        child = self.visit(ctx.child)
        varname = ctx.varname.text
        self.variables.add(varname)

        return "db.encode({}, '{}')".format(child, varname)

    def visitExists(self, ctx:FirstOrderPastLTLParser.ExistsContext):
        child = self.visit(ctx.child)
        varnames = set(ctx.args.getText().split(','))
        label = "states[{}]".format(self.num)

        variables = ['{}{}'.format(varname, index)for varname in varnames for index in range(self.length)]

        self.initialization.append(False)
        self.statements.append("{} = db.bdd.exist([{}], {});".format(label, ','.join(["'{}'".format(var) for var in variables]), child))
        self.num = self.num + 1

        return label

    def visitNegation(self, ctx:FirstOrderPastLTLParser.NegationContext):
        child = self.visit(ctx.child)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = db.bdd.apply('not', {});".format(label, child))
        self.num = self.num + 1 

        return label

    def visitDisjunction(self, ctx:FirstOrderPastLTLParser.DisjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = db.bdd.apply('or', {}, {});".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitConjunction(self, ctx:FirstOrderPastLTLParser.ConjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = db.bdd.apply('and', {}, {});".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitSince(self, ctx:FirstOrderPastLTLParser.SinceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{label} = db.bdd.apply('or', {right}, db.bdd.apply('and', {label}, {left}));".format(label=label, left=left, right=right))
        self.num = self.num + 1 

        return label

    def visitAlways(self, ctx:FirstOrderPastLTLParser.AlwaysContext):
        child = self.visit(ctx.child)
        label = "states[{}]".format(self.num)

        self.initialization.append(True)
        self.statements.append("{label} = db.bdd.apply('and', {label}, {child});".format(label=label, child=child))
        self.num = self.num + 1 

        return label

    def visitOnce(self, ctx:FirstOrderPastLTLParser.OnceContext):
        child = self.visit(ctx.child)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{label} = db.bdd.apply('or', {label}, {child});".format(label=label, child=child))
        self.num = self.num + 1 

        return label

    # Visit a parse tree produced by FirstOrderPastLTLParser#Grouping.
    def visitGrouping(self, ctx:FirstOrderPastLTLParser.GroupingContext):
        return self.visit(ctx.child)
