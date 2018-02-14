# Generated from FirstOrderRegExp.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FirstOrderRegExpParser import FirstOrderRegExpParser
else:
    from FirstOrderRegExpParser import FirstOrderRegExpParser

# This class defines a complete listener for a parse tree produced by FirstOrderRegExpParser.
class FirstOrderRegExpListener(ParseTreeListener):

    # Enter a parse tree produced by FirstOrderRegExpParser#namedExpr.
    def enterNamedExpr(self, ctx:FirstOrderRegExpParser.NamedExprContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#namedExpr.
    def exitNamedExpr(self, ctx:FirstOrderRegExpParser.NamedExprContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Concat.
    def enterConcat(self, ctx:FirstOrderRegExpParser.ConcatContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Concat.
    def exitConcat(self, ctx:FirstOrderRegExpParser.ConcatContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Star.
    def enterStar(self, ctx:FirstOrderRegExpParser.StarContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Star.
    def exitStar(self, ctx:FirstOrderRegExpParser.StarContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Exists.
    def enterExists(self, ctx:FirstOrderRegExpParser.ExistsContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Exists.
    def exitExists(self, ctx:FirstOrderRegExpParser.ExistsContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#True.
    def enterTrue(self, ctx:FirstOrderRegExpParser.TrueContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#True.
    def exitTrue(self, ctx:FirstOrderRegExpParser.TrueContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Atomic.
    def enterAtomic(self, ctx:FirstOrderRegExpParser.AtomicContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Atomic.
    def exitAtomic(self, ctx:FirstOrderRegExpParser.AtomicContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Grouping.
    def enterGrouping(self, ctx:FirstOrderRegExpParser.GroupingContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Grouping.
    def exitGrouping(self, ctx:FirstOrderRegExpParser.GroupingContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Question.
    def enterQuestion(self, ctx:FirstOrderRegExpParser.QuestionContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Question.
    def exitQuestion(self, ctx:FirstOrderRegExpParser.QuestionContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Plus.
    def enterPlus(self, ctx:FirstOrderRegExpParser.PlusContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Plus.
    def exitPlus(self, ctx:FirstOrderRegExpParser.PlusContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Union.
    def enterUnion(self, ctx:FirstOrderRegExpParser.UnionContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Union.
    def exitUnion(self, ctx:FirstOrderRegExpParser.UnionContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#VarConst.
    def enterVarConst(self, ctx:FirstOrderRegExpParser.VarConstContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#VarConst.
    def exitVarConst(self, ctx:FirstOrderRegExpParser.VarConstContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#VarBind.
    def enterVarBind(self, ctx:FirstOrderRegExpParser.VarBindContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#VarBind.
    def exitVarBind(self, ctx:FirstOrderRegExpParser.VarBindContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Prop.
    def enterProp(self, ctx:FirstOrderRegExpParser.PropContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Prop.
    def exitProp(self, ctx:FirstOrderRegExpParser.PropContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#Pred.
    def enterPred(self, ctx:FirstOrderRegExpParser.PredContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#Pred.
    def exitPred(self, ctx:FirstOrderRegExpParser.PredContext):
        pass


    # Enter a parse tree produced by FirstOrderRegExpParser#idlist.
    def enterIdlist(self, ctx:FirstOrderRegExpParser.IdlistContext):
        pass

    # Exit a parse tree produced by FirstOrderRegExpParser#idlist.
    def exitIdlist(self, ctx:FirstOrderRegExpParser.IdlistContext):
        pass


