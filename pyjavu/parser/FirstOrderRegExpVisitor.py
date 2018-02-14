# Generated from FirstOrderRegExp.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FirstOrderRegExpParser import FirstOrderRegExpParser
else:
    from FirstOrderRegExpParser import FirstOrderRegExpParser

# This class defines a complete generic visitor for a parse tree produced by FirstOrderRegExpParser.

class FirstOrderRegExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FirstOrderRegExpParser#namedExpr.
    def visitNamedExpr(self, ctx:FirstOrderRegExpParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Concat.
    def visitConcat(self, ctx:FirstOrderRegExpParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Star.
    def visitStar(self, ctx:FirstOrderRegExpParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Exists.
    def visitExists(self, ctx:FirstOrderRegExpParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#True.
    def visitTrue(self, ctx:FirstOrderRegExpParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Atomic.
    def visitAtomic(self, ctx:FirstOrderRegExpParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Grouping.
    def visitGrouping(self, ctx:FirstOrderRegExpParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Question.
    def visitQuestion(self, ctx:FirstOrderRegExpParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Plus.
    def visitPlus(self, ctx:FirstOrderRegExpParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Union.
    def visitUnion(self, ctx:FirstOrderRegExpParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#VarConst.
    def visitVarConst(self, ctx:FirstOrderRegExpParser.VarConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#VarBind.
    def visitVarBind(self, ctx:FirstOrderRegExpParser.VarBindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Prop.
    def visitProp(self, ctx:FirstOrderRegExpParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#Pred.
    def visitPred(self, ctx:FirstOrderRegExpParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderRegExpParser#idlist.
    def visitIdlist(self, ctx:FirstOrderRegExpParser.IdlistContext):
        return self.visitChildren(ctx)



del FirstOrderRegExpParser