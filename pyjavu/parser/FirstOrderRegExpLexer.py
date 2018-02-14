# Generated from FirstOrderRegExp.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\7\20O\n\20\f\20\16\20R\13\20\3\21\6\21U\n\21\r\21")
        buf.write("\16\21V\3\21\3\21\3\22\3\22\3\23\3\23\2\2\24\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\2%\2\3\2\5\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\5\2\13\f\17\17\"\"\2]\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7.\3\2\2\2\t\65\3\2\2")
        buf.write("\2\13\67\3\2\2\2\r9\3\2\2\2\17;\3\2\2\2\21=\3\2\2\2\23")
        buf.write("?\3\2\2\2\25A\3\2\2\2\27C\3\2\2\2\31E\3\2\2\2\33G\3\2")
        buf.write("\2\2\35J\3\2\2\2\37L\3\2\2\2!T\3\2\2\2#Z\3\2\2\2%\\\3")
        buf.write("\2\2\2\'(\7?\2\2(\4\3\2\2\2)*\7V\2\2*+\7t\2\2+,\7w\2\2")
        buf.write(",-\7g\2\2-\6\3\2\2\2./\7g\2\2/\60\7z\2\2\60\61\7k\2\2")
        buf.write("\61\62\7u\2\2\62\63\7v\2\2\63\64\7u\2\2\64\b\3\2\2\2\65")
        buf.write("\66\7}\2\2\66\n\3\2\2\2\678\7\177\2\28\f\3\2\2\29:\7,")
        buf.write("\2\2:\16\3\2\2\2;<\7-\2\2<\20\3\2\2\2=>\7A\2\2>\22\3\2")
        buf.write("\2\2?@\7=\2\2@\24\3\2\2\2AB\7~\2\2B\26\3\2\2\2CD\7*\2")
        buf.write("\2D\30\3\2\2\2EF\7+\2\2F\32\3\2\2\2GH\7>\2\2HI\7?\2\2")
        buf.write("I\34\3\2\2\2JK\7.\2\2K\36\3\2\2\2LP\t\2\2\2MO\t\3\2\2")
        buf.write("NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q \3\2\2\2RP\3")
        buf.write("\2\2\2SU\t\4\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2")
        buf.write("\2WX\3\2\2\2XY\b\21\2\2Y\"\3\2\2\2Z[\4\62;\2[$\3\2\2\2")
        buf.write("\\]\4\63;\2]&\3\2\2\2\5\2PV\3\2\3\2")
        return buf.getvalue()


class FirstOrderRegExpLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    IDENTIFIER = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'True'", "'exists'", "'{'", "'}'", "'*'", "'+'", "'?'", 
            "';'", "'|'", "'('", "')'", "'<='", "','" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "IDENTIFIER", "WS", "DIGIT", "DIGIT_NOT_ZERO" ]

    grammarFileName = "FirstOrderRegExp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


