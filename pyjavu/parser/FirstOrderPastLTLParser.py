# Generated from FirstOrderPastLTL.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\60\n\3\f\3\16\3\63\13\3")
        buf.write("\3\4\3\4\3\4\3\4\5\49\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("A\n\5\3\6\3\6\3\6\7\6F\n\6\f\6\16\6I\13\6\3\6\2\3\4\7")
        buf.write("\2\4\6\b\n\2\5\3\2\7\b\3\2\t\n\3\2\13\f\2Q\2\16\3\2\2")
        buf.write("\2\4$\3\2\2\2\68\3\2\2\2\b@\3\2\2\2\nB\3\2\2\2\f\r\7\24")
        buf.write("\2\2\r\17\7\3\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\20\3\2")
        buf.write("\2\2\20\21\5\4\3\2\21\3\3\2\2\2\22\23\b\3\1\2\23%\5\6")
        buf.write("\4\2\24\25\7\4\2\2\25\26\7\5\2\2\26\27\5\n\6\2\27\30\7")
        buf.write("\6\2\2\30\31\5\4\3\n\31%\3\2\2\2\32\33\t\2\2\2\33%\5\4")
        buf.write("\3\t\34\35\7\r\2\2\35%\5\4\3\6\36\37\7\16\2\2\37%\5\4")
        buf.write("\3\5 !\7\20\2\2!\"\5\4\3\2\"#\7\21\2\2#%\3\2\2\2$\22\3")
        buf.write("\2\2\2$\24\3\2\2\2$\32\3\2\2\2$\34\3\2\2\2$\36\3\2\2\2")
        buf.write("$ \3\2\2\2%\61\3\2\2\2&\'\f\b\2\2\'(\t\3\2\2(\60\5\4\3")
        buf.write("\t)*\f\7\2\2*+\t\4\2\2+\60\5\4\3\b,-\f\4\2\2-.\7\17\2")
        buf.write("\2.\60\5\4\3\5/&\3\2\2\2/)\3\2\2\2/,\3\2\2\2\60\63\3\2")
        buf.write("\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\5\3\2\2\2\63\61\3\2")
        buf.write("\2\2\649\5\b\5\2\65\66\7\24\2\2\66\67\7\22\2\2\679\5\b")
        buf.write("\5\28\64\3\2\2\28\65\3\2\2\29\7\3\2\2\2:A\7\24\2\2;<\7")
        buf.write("\24\2\2<=\7\20\2\2=>\5\n\6\2>?\7\21\2\2?A\3\2\2\2@:\3")
        buf.write("\2\2\2@;\3\2\2\2A\t\3\2\2\2BG\7\24\2\2CD\7\23\2\2DF\7")
        buf.write("\24\2\2EC\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\13\3")
        buf.write("\2\2\2IG\3\2\2\2\t\16$/\618@G")
        return buf.getvalue()


class FirstOrderPastLTLParser ( Parser ):

    grammarFileName = "FirstOrderPastLTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'exists'", "'{'", "'}'", "'!'", 
                     "'not'", "'&&'", "'and'", "'||'", "'or'", "'once'", 
                     "'always'", "'since'", "'('", "')'", "'<='", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "WS" ]

    RULE_namedExpr = 0
    RULE_expr = 1
    RULE_binded_atom = 2
    RULE_atom = 3
    RULE_idlist = 4

    ruleNames =  [ "namedExpr", "expr", "binded_atom", "atom", "idlist" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    IDENTIFIER=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NamedExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.child = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(FirstOrderPastLTLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return FirstOrderPastLTLParser.RULE_namedExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedExpr" ):
                listener.enterNamedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedExpr" ):
                listener.exitNamedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedExpr" ):
                return visitor.visitNamedExpr(self)
            else:
                return visitor.visitChildren(self)




    def namedExpr(self):

        localctx = FirstOrderPastLTLParser.NamedExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_namedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 10
                localctx.name = self.match(FirstOrderPastLTLParser.IDENTIFIER)
                self.state = 11
                self.match(FirstOrderPastLTLParser.T__0)


            self.state = 14
            localctx.child = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FirstOrderPastLTLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DisjunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FirstOrderPastLTLParser.ExprContext)
            else:
                return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class OnceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOnce" ):
                listener.enterOnce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOnce" ):
                listener.exitOnce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnce" ):
                return visitor.visitOnce(self)
            else:
                return visitor.visitChildren(self)


    class ExistsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.args = None # IdlistContext
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def idlist(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.IdlistContext,0)

        def expr(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExists" ):
                listener.enterExists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExists" ):
                listener.exitExists(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExists" ):
                return visitor.visitExists(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FirstOrderPastLTLParser.ExprContext)
            else:
                return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class SinceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FirstOrderPastLTLParser.ExprContext)
            else:
                return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSince" ):
                listener.enterSince(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSince" ):
                listener.exitSince(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSince" ):
                return visitor.visitSince(self)
            else:
                return visitor.visitChildren(self)


    class AtomicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # Binded_atomContext
            self.copyFrom(ctx)

        def binded_atom(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.Binded_atomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic" ):
                listener.enterAtomic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic" ):
                listener.exitAtomic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic" ):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)


    class GroupingContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping" ):
                listener.enterGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping" ):
                listener.exitGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping" ):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlways" ):
                listener.enterAlways(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlways" ):
                listener.exitAlways(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlways" ):
                return visitor.visitAlways(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FirstOrderPastLTLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FirstOrderPastLTLParser.IDENTIFIER]:
                localctx = FirstOrderPastLTLParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                localctx.child = self.binded_atom()
                pass
            elif token in [FirstOrderPastLTLParser.T__1]:
                localctx = FirstOrderPastLTLParser.ExistsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(FirstOrderPastLTLParser.T__1)
                self.state = 19
                self.match(FirstOrderPastLTLParser.T__2)
                self.state = 20
                localctx.args = self.idlist()
                self.state = 21
                self.match(FirstOrderPastLTLParser.T__3)
                self.state = 22
                localctx.child = self.expr(8)
                pass
            elif token in [FirstOrderPastLTLParser.T__4, FirstOrderPastLTLParser.T__5]:
                localctx = FirstOrderPastLTLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                _la = self._input.LA(1)
                if not(_la==FirstOrderPastLTLParser.T__4 or _la==FirstOrderPastLTLParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 25
                localctx.child = self.expr(7)
                pass
            elif token in [FirstOrderPastLTLParser.T__10]:
                localctx = FirstOrderPastLTLParser.OnceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(FirstOrderPastLTLParser.T__10)
                self.state = 27
                localctx.child = self.expr(4)
                pass
            elif token in [FirstOrderPastLTLParser.T__11]:
                localctx = FirstOrderPastLTLParser.AlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(FirstOrderPastLTLParser.T__11)
                self.state = 29
                localctx.child = self.expr(3)
                pass
            elif token in [FirstOrderPastLTLParser.T__13]:
                localctx = FirstOrderPastLTLParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(FirstOrderPastLTLParser.T__13)
                self.state = 31
                localctx.child = self.expr(0)
                self.state = 32
                self.match(FirstOrderPastLTLParser.T__14)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = FirstOrderPastLTLParser.ConjunctionContext(self, FirstOrderPastLTLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        _la = self._input.LA(1)
                        if not(_la==FirstOrderPastLTLParser.T__6 or _la==FirstOrderPastLTLParser.T__7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = FirstOrderPastLTLParser.DisjunctionContext(self, FirstOrderPastLTLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 40
                        _la = self._input.LA(1)
                        if not(_la==FirstOrderPastLTLParser.T__8 or _la==FirstOrderPastLTLParser.T__9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = FirstOrderPastLTLParser.SinceContext(self, FirstOrderPastLTLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 43
                        self.match(FirstOrderPastLTLParser.T__12)
                        self.state = 44
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Binded_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FirstOrderPastLTLParser.RULE_binded_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarBindContext(Binded_atomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.Binded_atomContext
            super().__init__(parser)
            self.varname = None # Token
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(FirstOrderPastLTLParser.IDENTIFIER, 0)
        def atom(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarBind" ):
                listener.enterVarBind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarBind" ):
                listener.exitVarBind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarBind" ):
                return visitor.visitVarBind(self)
            else:
                return visitor.visitChildren(self)


    class VarConstContext(Binded_atomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.Binded_atomContext
            super().__init__(parser)
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarConst" ):
                listener.enterVarConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarConst" ):
                listener.exitVarConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarConst" ):
                return visitor.visitVarConst(self)
            else:
                return visitor.visitChildren(self)



    def binded_atom(self):

        localctx = FirstOrderPastLTLParser.Binded_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_binded_atom)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = FirstOrderPastLTLParser.VarConstContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                localctx.child = self.atom()
                pass

            elif la_ == 2:
                localctx = FirstOrderPastLTLParser.VarBindContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                localctx.varname = self.match(FirstOrderPastLTLParser.IDENTIFIER)
                self.state = 52
                self.match(FirstOrderPastLTLParser.T__15)
                self.state = 53
                localctx.child = self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FirstOrderPastLTLParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(FirstOrderPastLTLParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProp" ):
                listener.enterProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProp" ):
                listener.exitProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProp" ):
                return visitor.visitProp(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FirstOrderPastLTLParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.args = None # IdlistContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(FirstOrderPastLTLParser.IDENTIFIER, 0)
        def idlist(self):
            return self.getTypedRuleContext(FirstOrderPastLTLParser.IdlistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = FirstOrderPastLTLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = FirstOrderPastLTLParser.PropContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                localctx.name = self.match(FirstOrderPastLTLParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = FirstOrderPastLTLParser.PredContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                localctx.name = self.match(FirstOrderPastLTLParser.IDENTIFIER)
                self.state = 58
                self.match(FirstOrderPastLTLParser.T__13)
                self.state = 59
                localctx.args = self.idlist()
                self.state = 60
                self.match(FirstOrderPastLTLParser.T__14)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.param = None # Token

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(FirstOrderPastLTLParser.IDENTIFIER)
            else:
                return self.getToken(FirstOrderPastLTLParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return FirstOrderPastLTLParser.RULE_idlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlist" ):
                listener.enterIdlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlist" ):
                listener.exitIdlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = FirstOrderPastLTLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            localctx.param = self.match(FirstOrderPastLTLParser.IDENTIFIER)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FirstOrderPastLTLParser.T__16:
                self.state = 65
                self.match(FirstOrderPastLTLParser.T__16)
                self.state = 66
                localctx.param = self.match(FirstOrderPastLTLParser.IDENTIFIER)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




