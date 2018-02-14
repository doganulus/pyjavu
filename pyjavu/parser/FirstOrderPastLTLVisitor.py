# Generated from FirstOrderPastLTL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FirstOrderPastLTLParser import FirstOrderPastLTLParser
else:
    from FirstOrderPastLTLParser import FirstOrderPastLTLParser

# This class defines a complete generic visitor for a parse tree produced by FirstOrderPastLTLParser.

class FirstOrderPastLTLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FirstOrderPastLTLParser#namedExpr.
    def visitNamedExpr(self, ctx:FirstOrderPastLTLParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Disjunction.
    def visitDisjunction(self, ctx:FirstOrderPastLTLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Negation.
    def visitNegation(self, ctx:FirstOrderPastLTLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Once.
    def visitOnce(self, ctx:FirstOrderPastLTLParser.OnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Exists.
    def visitExists(self, ctx:FirstOrderPastLTLParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Conjunction.
    def visitConjunction(self, ctx:FirstOrderPastLTLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Since.
    def visitSince(self, ctx:FirstOrderPastLTLParser.SinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Atomic.
    def visitAtomic(self, ctx:FirstOrderPastLTLParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Grouping.
    def visitGrouping(self, ctx:FirstOrderPastLTLParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Always.
    def visitAlways(self, ctx:FirstOrderPastLTLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#VarConst.
    def visitVarConst(self, ctx:FirstOrderPastLTLParser.VarConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#VarBind.
    def visitVarBind(self, ctx:FirstOrderPastLTLParser.VarBindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Prop.
    def visitProp(self, ctx:FirstOrderPastLTLParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#Pred.
    def visitPred(self, ctx:FirstOrderPastLTLParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FirstOrderPastLTLParser#idlist.
    def visitIdlist(self, ctx:FirstOrderPastLTLParser.IdlistContext):
        return self.visitChildren(ctx)



del FirstOrderPastLTLParser