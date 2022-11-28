# Generated from ../grammars/Number.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u01c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\5\2B\n\2\3\2\3\2\5\2F\n\2\3\2\3\2")
        buf.write("\5\2J\n\2\5\2L\n\2\3\2\5\2O\n\2\5\2Q\n\2\3\2\5\2T\n\2")
        buf.write("\3\2\3\2\5\2X\n\2\6\2Z\n\2\r\2\16\2[\3\2\3\2\5\2`\n\2")
        buf.write("\3\2\3\2\5\2d\n\2\5\2f\n\2\3\2\5\2i\n\2\7\2k\n\2\f\2\16")
        buf.write("\2n\13\2\3\2\5\2q\n\2\3\3\5\3t\n\3\3\3\3\3\3\3\5\3y\n")
        buf.write("\3\3\3\3\3\5\3}\n\3\5\3\177\n\3\3\3\5\3\u0082\n\3\5\3")
        buf.write("\u0084\n\3\3\3\5\3\u0087\n\3\3\3\3\3\5\3\u008b\n\3\6\3")
        buf.write("\u008d\n\3\r\3\16\3\u008e\3\3\3\3\3\3\5\3\u0094\n\3\3")
        buf.write("\3\3\3\5\3\u0098\n\3\5\3\u009a\n\3\3\3\5\3\u009d\n\3\5")
        buf.write("\3\u009f\n\3\7\3\u00a1\n\3\f\3\16\3\u00a4\13\3\3\3\5\3")
        buf.write("\u00a7\n\3\3\4\5\4\u00aa\n\4\3\4\3\4\5\4\u00ae\n\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u00b5\n\4\3\4\3\4\5\4\u00b9\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4\u00c0\n\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u00c7\n\4\3\4\3\4\5\4\u00cb\n\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\u00d1\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00d9\n\5\3\6\5")
        buf.write("\6\u00dc\n\6\3\6\3\6\5\6\u00e0\n\6\3\6\5\6\u00e3\n\6\3")
        buf.write("\6\5\6\u00e6\n\6\3\6\5\6\u00e9\n\6\3\6\5\6\u00ec\n\6\3")
        buf.write("\6\5\6\u00ef\n\6\3\7\5\7\u00f2\n\7\3\7\3\7\5\7\u00f6\n")
        buf.write("\7\3\7\5\7\u00f9\n\7\3\7\5\7\u00fc\n\7\3\7\5\7\u00ff\n")
        buf.write("\7\3\7\5\7\u0102\n\7\3\7\5\7\u0105\n\7\3\b\5\b\u0108\n")
        buf.write("\b\3\b\3\b\5\b\u010c\n\b\3\b\5\b\u010f\n\b\3\b\5\b\u0112")
        buf.write("\n\b\3\b\5\b\u0115\n\b\3\b\5\b\u0118\n\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b\u0121\n\b\3\b\5\b\u0124\n\b\3\t\5\t")
        buf.write("\u0127\n\t\3\t\3\t\5\t\u012b\n\t\3\t\5\t\u012e\n\t\3\t")
        buf.write("\5\t\u0131\n\t\3\t\5\t\u0134\n\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t\u0141\n\t\3\n\3\n\5\n\u0145")
        buf.write("\n\n\3\n\3\n\5\n\u0149\n\n\5\n\u014b\n\n\3\n\5\n\u014e")
        buf.write("\n\n\3\n\5\n\u0151\n\n\3\13\3\13\5\13\u0155\n\13\3\13")
        buf.write("\5\13\u0158\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u015f\n\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u0166\n\r\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u016c\n\16\3\17\3\17\3\17\3\17\5\17\u0172\n\17\3\20\3")
        buf.write("\20\3\20\5\20\u0177\n\20\3\21\3\21\3\21\5\21\u017c\n\21")
        buf.write("\3\22\3\22\5\22\u0180\n\22\3\23\3\23\5\23\u0184\n\23\3")
        buf.write("\24\3\24\3\24\5\24\u0189\n\24\3\25\3\25\3\25\5\25\u018e")
        buf.write("\n\25\3\25\3\25\5\25\u0192\n\25\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\5\37\u01b0\n\37\3\37\3\37\5\37\u01b4\n\37\7")
        buf.write("\37\u01b6\n\37\f\37\16\37\u01b9\13\37\3 \5 \u01bc\n \3")
        buf.write(" \3 \5 \u01c0\n \7 \u01c2\n \f \16 \u01c5\13 \3 \2\2!")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>\2\4\4\2\n\n\22\22\4\2\t\t\21\21\2\u0221\2A")
        buf.write("\3\2\2\2\4s\3\2\2\2\6\u00d0\3\2\2\2\b\u00d8\3\2\2\2\n")
        buf.write("\u00ee\3\2\2\2\f\u0104\3\2\2\2\16\u0123\3\2\2\2\20\u0140")
        buf.write("\3\2\2\2\22\u014a\3\2\2\2\24\u0152\3\2\2\2\26\u015e\3")
        buf.write("\2\2\2\30\u0165\3\2\2\2\32\u016b\3\2\2\2\34\u0171\3\2")
        buf.write("\2\2\36\u0176\3\2\2\2 \u017b\3\2\2\2\"\u017f\3\2\2\2$")
        buf.write("\u0183\3\2\2\2&\u0185\3\2\2\2(\u0191\3\2\2\2*\u0193\3")
        buf.write("\2\2\2,\u0196\3\2\2\2.\u0199\3\2\2\2\60\u019d\3\2\2\2")
        buf.write("\62\u01a0\3\2\2\2\64\u01a3\3\2\2\2\66\u01a6\3\2\2\28\u01a9")
        buf.write("\3\2\2\2:\u01ab\3\2\2\2<\u01b7\3\2\2\2>\u01c3\3\2\2\2")
        buf.write("@B\5<\37\2A@\3\2\2\2AB\3\2\2\2BP\3\2\2\2CK\5\b\5\2DF\7")
        buf.write("\3\2\2ED\3\2\2\2EF\3\2\2\2FG\3\2\2\2GI\7\30\2\2HJ\7\3")
        buf.write("\2\2IH\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KE\3\2\2\2KL\3\2\2\2")
        buf.write("LN\3\2\2\2MO\5:\36\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PC\3")
        buf.write("\2\2\2PQ\3\2\2\2Ql\3\2\2\2RT\7\3\2\2SR\3\2\2\2ST\3\2\2")
        buf.write("\2TU\3\2\2\2UW\7\30\2\2VX\7\3\2\2WV\3\2\2\2WX\3\2\2\2")
        buf.write("XZ\3\2\2\2YS\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\")
        buf.write("]\3\2\2\2]e\5\b\5\2^`\7\3\2\2_^\3\2\2\2_`\3\2\2\2`a\3")
        buf.write("\2\2\2ac\7\30\2\2bd\7\3\2\2cb\3\2\2\2cd\3\2\2\2df\3\2")
        buf.write("\2\2e_\3\2\2\2ef\3\2\2\2fh\3\2\2\2gi\5:\36\2hg\3\2\2\2")
        buf.write("hi\3\2\2\2ik\3\2\2\2jY\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3")
        buf.write("\2\2\2mp\3\2\2\2nl\3\2\2\2oq\5> \2po\3\2\2\2pq\3\2\2\2")
        buf.write("q\3\3\2\2\2rt\5<\37\2sr\3\2\2\2st\3\2\2\2t\u0083\3\2\2")
        buf.write("\2u\u0084\5\6\4\2v~\5\b\5\2wy\7\3\2\2xw\3\2\2\2xy\3\2")
        buf.write("\2\2yz\3\2\2\2z|\7\30\2\2{}\7\3\2\2|{\3\2\2\2|}\3\2\2")
        buf.write("\2}\177\3\2\2\2~x\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2")
        buf.write("\2\u0080\u0082\5:\36\2\u0081\u0080\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0084\3\2\2\2\u0083u\3\2\2\2\u0083v\3\2")
        buf.write("\2\2\u0083\u0084\3\2\2\2\u0084\u00a2\3\2\2\2\u0085\u0087")
        buf.write("\7\3\2\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u008a\7\30\2\2\u0089\u008b\7\3\2")
        buf.write("\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d")
        buf.write("\3\2\2\2\u008c\u0086\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u009e\3\2\2\2")
        buf.write("\u0090\u009f\5\6\4\2\u0091\u0099\5\b\5\2\u0092\u0094\7")
        buf.write("\3\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0097\7\30\2\2\u0096\u0098\7\3\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2")
        buf.write("\u0099\u0093\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3")
        buf.write("\2\2\2\u009b\u009d\5:\36\2\u009c\u009b\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u0090\3\2\2\2\u009e")
        buf.write("\u0091\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u008c\3\2\2\2")
        buf.write("\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3")
        buf.write("\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7")
        buf.write("\5> \2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\5")
        buf.write("\3\2\2\2\u00a8\u00aa\7\3\2\2\u00a9\u00a8\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\7\4\2\2")
        buf.write("\u00ac\u00ae\7\3\2\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3")
        buf.write("\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\5\b\5\2\u00b0\u00b1")
        buf.write("\7\17\2\2\u00b1\u00b2\5\b\5\2\u00b2\u00d1\3\2\2\2\u00b3")
        buf.write("\u00b5\7\3\2\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b8\7\4\2\2\u00b7\u00b9\7")
        buf.write("\3\2\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\5\b\5\2\u00bb\u00bc\7\5\2\2\u00bc")
        buf.write("\u00bd\5\b\5\2\u00bd\u00d1\3\2\2\2\u00be\u00c0\7\3\2\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00c2\5\b\5\2\u00c2\u00c3\7\5\2\2\u00c3\u00c4")
        buf.write("\5\b\5\2\u00c4\u00d1\3\2\2\2\u00c5\u00c7\7\3\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00ca\7\6\2\2\u00c9\u00cb\7\3\2\2\u00ca\u00c9\3")
        buf.write("\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd")
        buf.write("\5\b\5\2\u00cd\u00ce\7\17\2\2\u00ce\u00cf\5\b\5\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00a9\3\2\2\2\u00d0\u00b4\3\2\2\2")
        buf.write("\u00d0\u00bf\3\2\2\2\u00d0\u00c6\3\2\2\2\u00d1\7\3\2\2")
        buf.write("\2\u00d2\u00d9\5\n\6\2\u00d3\u00d9\5\f\7\2\u00d4\u00d9")
        buf.write("\5\16\b\2\u00d5\u00d9\5\20\t\2\u00d6\u00d9\5\22\n\2\u00d7")
        buf.write("\u00d9\5\24\13\2\u00d8\u00d2\3\2\2\2\u00d8\u00d3\3\2\2")
        buf.write("\2\u00d8\u00d4\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\t\3\2\2\2\u00da\u00dc")
        buf.write("\5\26\f\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00e0\7\16\2\2\u00de\u00e0\5\66\34")
        buf.write("\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\u00e2")
        buf.write("\3\2\2\2\u00e1\u00e3\7\17\2\2\u00e2\u00e1\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\5\30\r")
        buf.write("\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8")
        buf.write("\3\2\2\2\u00e7\u00e9\7\17\2\2\u00e8\u00e7\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00ec\7\b\2\2")
        buf.write("\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ef\3")
        buf.write("\2\2\2\u00ed\u00ef\7\26\2\2\u00ee\u00db\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef\13\3\2\2\2\u00f0\u00f2\5\32\16\2")
        buf.write("\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f5\3")
        buf.write("\2\2\2\u00f3\u00f6\7\r\2\2\u00f4\u00f6\5\64\33\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f8\3\2\2\2")
        buf.write("\u00f7\u00f9\7\17\2\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00fc\5\34\17\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2")
        buf.write("\u00fd\u00ff\7\17\2\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u0102\7\b\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0105\3\2\2\2")
        buf.write("\u0103\u0105\7\25\2\2\u0104\u00f1\3\2\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\r\3\2\2\2\u0106\u0108\5\36\20\2\u0107\u0106")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write("\u010c\7\f\2\2\u010a\u010c\5\62\32\2\u010b\u0109\3\2\2")
        buf.write("\2\u010b\u010a\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010f")
        buf.write("\7\17\2\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u0112\5 \21\2\u0111\u0110\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0115\7")
        buf.write("\17\2\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115")
        buf.write("\u0117\3\2\2\2\u0116\u0118\7\b\2\2\u0117\u0116\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118\u0124\3\2\2\2\u0119\u0124\7")
        buf.write("\24\2\2\u011a\u011b\t\2\2\2\u011b\u0124\t\2\2\2\u011c")
        buf.write("\u0120\7\24\2\2\u011d\u0121\5\20\t\2\u011e\u0121\5\22")
        buf.write("\n\2\u011f\u0121\5\24\13\2\u0120\u011d\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0124\7\24\2\2\u0123\u0107\3\2\2\2\u0123\u0119\3\2\2")
        buf.write("\2\u0123\u011a\3\2\2\2\u0123\u011c\3\2\2\2\u0123\u0122")
        buf.write("\3\2\2\2\u0124\17\3\2\2\2\u0125\u0127\5\"\22\2\u0126\u0125")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u012a\7\13\2\2\u0129\u012b\7\17\2\2\u012a\u0129\3\2\2")
        buf.write("\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u012e")
        buf.write("\5$\23\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u0130\3\2\2\2\u012f\u0131\7\17\2\2\u0130\u012f\3\2\2")
        buf.write("\2\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0134")
        buf.write("\7\b\2\2\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0141\3\2\2\2\u0135\u0141\5(\25\2\u0136\u0141\5*\26\2")
        buf.write("\u0137\u0141\5,\27\2\u0138\u0141\5.\30\2\u0139\u0141\5")
        buf.write("\60\31\2\u013a\u0141\7\23\2\2\u013b\u013c\t\3\2\2\u013c")
        buf.write("\u013d\t\3\2\2\u013d\u0141\t\3\2\2\u013e\u013f\t\3\2\2")
        buf.write("\u013f\u0141\t\2\2\2\u0140\u0126\3\2\2\2\u0140\u0135\3")
        buf.write("\2\2\2\u0140\u0136\3\2\2\2\u0140\u0137\3\2\2\2\u0140\u0138")
        buf.write("\3\2\2\2\u0140\u0139\3\2\2\2\u0140\u013a\3\2\2\2\u0140")
        buf.write("\u013b\3\2\2\2\u0140\u013e\3\2\2\2\u0141\21\3\2\2\2\u0142")
        buf.write("\u0144\7\n\2\2\u0143\u0145\5\24\13\2\u0144\u0143\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0145\u014b\3\2\2\2\u0146\u0148")
        buf.write("\7\22\2\2\u0147\u0149\5\24\13\2\u0148\u0147\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0142\3\2\2\2")
        buf.write("\u014a\u0146\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014e\7")
        buf.write("\17\2\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u0150\3\2\2\2\u014f\u0151\7\b\2\2\u0150\u014f\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\23\3\2\2\2\u0152\u0154\t\3")
        buf.write("\2\2\u0153\u0155\7\17\2\2\u0154\u0153\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0158\7\b\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158\25\3\2\2\2\u0159")
        buf.write("\u015f\5\24\13\2\u015a\u015f\5\22\n\2\u015b\u015f\5\20")
        buf.write("\t\2\u015c\u015f\5\16\b\2\u015d\u015f\5\f\7\2\u015e\u0159")
        buf.write("\3\2\2\2\u015e\u015a\3\2\2\2\u015e\u015b\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015f\27\3\2\2\2\u0160")
        buf.write("\u0166\5\24\13\2\u0161\u0166\5\22\n\2\u0162\u0166\5\20")
        buf.write("\t\2\u0163\u0166\5\16\b\2\u0164\u0166\5\f\7\2\u0165\u0160")
        buf.write("\3\2\2\2\u0165\u0161\3\2\2\2\u0165\u0162\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166\31\3\2\2\2\u0167")
        buf.write("\u016c\5\24\13\2\u0168\u016c\5\22\n\2\u0169\u016c\5\20")
        buf.write("\t\2\u016a\u016c\5\16\b\2\u016b\u0167\3\2\2\2\u016b\u0168")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c")
        buf.write("\33\3\2\2\2\u016d\u0172\5\24\13\2\u016e\u0172\5\22\n\2")
        buf.write("\u016f\u0172\5\20\t\2\u0170\u0172\5\16\b\2\u0171\u016d")
        buf.write("\3\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\35\3\2\2\2\u0173\u0177\5\24\13\2")
        buf.write("\u0174\u0177\5\22\n\2\u0175\u0177\5\20\t\2\u0176\u0173")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\37\3\2\2\2\u0178\u017c\5\24\13\2\u0179\u017c\5\22\n\2")
        buf.write("\u017a\u017c\5\20\t\2\u017b\u0178\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017a\3\2\2\2\u017c!\3\2\2\2\u017d\u0180")
        buf.write("\5\24\13\2\u017e\u0180\5\22\n\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180#\3\2\2\2\u0181\u0184\5\24\13\2\u0182")
        buf.write("\u0184\5\22\n\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2")
        buf.write("\2\u0184%\3\2\2\2\u0185\u0186\7\5\2\2\u0186\u0188\t\3")
        buf.write("\2\2\u0187\u0189\7\3\2\2\u0188\u0187\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\'\3\2\2\2\u018a\u018b\7\5\2\2\u018b\u018d")
        buf.write("\t\2\2\2\u018c\u018e\7\3\2\2\u018d\u018c\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018e\u0192\3\2\2\2\u018f\u0190\7\5\2\2")
        buf.write("\u0190\u0192\7\13\2\2\u0191\u018a\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192)\3\2\2\2\u0193\u0194\5&\24\2\u0194\u0195")
        buf.write("\t\3\2\2\u0195+\3\2\2\2\u0196\u0197\t\3\2\2\u0197\u0198")
        buf.write("\5&\24\2\u0198-\3\2\2\2\u0199\u019a\t\3\2\2\u019a\u019b")
        buf.write("\t\3\2\2\u019b\u019c\58\35\2\u019c/\3\2\2\2\u019d\u019e")
        buf.write("\5&\24\2\u019e\u019f\58\35\2\u019f\61\3\2\2\2\u01a0\u01a1")
        buf.write("\7\5\2\2\u01a1\u01a2\7\f\2\2\u01a2\63\3\2\2\2\u01a3\u01a4")
        buf.write("\7\5\2\2\u01a4\u01a5\7\r\2\2\u01a5\65\3\2\2\2\u01a6\u01a7")
        buf.write("\7\5\2\2\u01a7\u01a8\7\16\2\2\u01a8\67\3\2\2\2\u01a9\u01aa")
        buf.write("\7\7\2\2\u01aa9\3\2\2\2\u01ab\u01ac\7\5\2\2\u01ac\u01ad")
        buf.write("\7\30\2\2\u01ad;\3\2\2\2\u01ae\u01b0\7\3\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01b3\7\30\2\2\u01b2\u01b4\7\3\2\2\u01b3\u01b2\3\2\2")
        buf.write("\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01af")
        buf.write("\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8=\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bc\7\3\2\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01bd\3\2\2\2\u01bd\u01bf\7\30\2\2\u01be\u01c0")
        buf.write("\7\3\2\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01bb\3\2\2\2\u01c2\u01c5\3\2\2\2")
        buf.write("\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4?\3\2\2")
        buf.write("\2\u01c5\u01c3\3\2\2\2^AEIKNPSW[_cehlpsx|~\u0081\u0083")
        buf.write("\u0086\u008a\u008e\u0093\u0097\u0099\u009c\u009e\u00a2")
        buf.write("\u00a6\u00a9\u00ad\u00b4\u00b8\u00bf\u00c6\u00ca\u00d0")
        buf.write("\u00d8\u00db\u00df\u00e2\u00e5\u00e8\u00eb\u00ee\u00f1")
        buf.write("\u00f5\u00f8\u00fb\u00fe\u0101\u0104\u0107\u010b\u010e")
        buf.write("\u0111\u0114\u0117\u0120\u0123\u0126\u012a\u012d\u0130")
        buf.write("\u0133\u0140\u0144\u0148\u014a\u014d\u0150\u0154\u0157")
        buf.write("\u015e\u0165\u016b\u0171\u0176\u017b\u017f\u0183\u0188")
        buf.write("\u018d\u0191\u01af\u01b3\u01b7\u01bb\u01bf\u01c3")
        return buf.getvalue()


class NumberParser ( Parser ):

    grammarFileName = "Number.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'between'", "'to '", "'of'", "'to to '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WORD_NUMBER_FRACTIONS", 
                      "WORD_NUMBER_UNITS", "WORD_NUMBER_TENS", "WORD_NUMBER_HUNDREDS", 
                      "WORD_NUMBER_THOUSANDS", "WORD_NUMBER_LAKHS", "WORD_NUMBER_CRORES", 
                      "CONJUNCTION", "ART", "NUMBER_UNITS", "NUMBER_TENS", 
                      "NUMBER_HUNDREDS", "NUMBER_THOUSANDS", "NUMBER_LAKHS", 
                      "NUMBER_CRORES", "WHITESPACE", "WORD", "NUMBER" ]

    RULE_numbers_utterance = 0
    RULE_ranges_utterance = 1
    RULE_range_pattern = 2
    RULE_number_pattern = 3
    RULE_crores_format = 4
    RULE_lakhs_format = 5
    RULE_thousands_format = 6
    RULE_hundreds_format = 7
    RULE_tens_format = 8
    RULE_units_format = 9
    RULE_prefix_crores = 10
    RULE_suffix_crores = 11
    RULE_prefix_lakhs = 12
    RULE_suffix_lakhs = 13
    RULE_prefix_thousands = 14
    RULE_suffix_thousands = 15
    RULE_prefix_hundreds = 16
    RULE_suffix_hundreds = 17
    RULE_spl_tens = 18
    RULE_spl_hundreds = 19
    RULE_spl_hundreds_1 = 20
    RULE_spl_hundreds_2 = 21
    RULE_spl_hundreds_3 = 22
    RULE_spl_hundreds_4 = 23
    RULE_spl_thousands = 24
    RULE_spl_lakhs = 25
    RULE_spl_crores = 26
    RULE_spl_epilogue = 27
    RULE_spl_discard = 28
    RULE_prefix = 29
    RULE_suffix = 30

    ruleNames =  [ "numbers_utterance", "ranges_utterance", "range_pattern", 
                   "number_pattern", "crores_format", "lakhs_format", "thousands_format", 
                   "hundreds_format", "tens_format", "units_format", "prefix_crores", 
                   "suffix_crores", "prefix_lakhs", "suffix_lakhs", "prefix_thousands", 
                   "suffix_thousands", "prefix_hundreds", "suffix_hundreds", 
                   "spl_tens", "spl_hundreds", "spl_hundreds_1", "spl_hundreds_2", 
                   "spl_hundreds_3", "spl_hundreds_4", "spl_thousands", 
                   "spl_lakhs", "spl_crores", "spl_epilogue", "spl_discard", 
                   "prefix", "suffix" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    WORD_NUMBER_FRACTIONS=6
    WORD_NUMBER_UNITS=7
    WORD_NUMBER_TENS=8
    WORD_NUMBER_HUNDREDS=9
    WORD_NUMBER_THOUSANDS=10
    WORD_NUMBER_LAKHS=11
    WORD_NUMBER_CRORES=12
    CONJUNCTION=13
    ART=14
    NUMBER_UNITS=15
    NUMBER_TENS=16
    NUMBER_HUNDREDS=17
    NUMBER_THOUSANDS=18
    NUMBER_LAKHS=19
    NUMBER_CRORES=20
    WHITESPACE=21
    WORD=22
    NUMBER=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Numbers_utteranceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefix(self):
            return self.getTypedRuleContext(NumberParser.PrefixContext,0)


        def number_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Number_patternContext)
            else:
                return self.getTypedRuleContext(NumberParser.Number_patternContext,i)


        def suffix(self):
            return self.getTypedRuleContext(NumberParser.SuffixContext,0)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD)
            else:
                return self.getToken(NumberParser.WORD, i)

        def spl_discard(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Spl_discardContext)
            else:
                return self.getTypedRuleContext(NumberParser.Spl_discardContext,i)


        def getRuleIndex(self):
            return NumberParser.RULE_numbers_utterance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumbers_utterance" ):
                listener.enterNumbers_utterance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumbers_utterance" ):
                listener.exitNumbers_utterance(self)




    def numbers_utterance(self):

        localctx = NumberParser.Numbers_utteranceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_numbers_utterance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 62
                self.prefix()


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.T__2) | (1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.WORD_NUMBER_HUNDREDS) | (1 << NumberParser.WORD_NUMBER_THOUSANDS) | (1 << NumberParser.WORD_NUMBER_LAKHS) | (1 << NumberParser.WORD_NUMBER_CRORES) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS) | (1 << NumberParser.NUMBER_HUNDREDS) | (1 << NumberParser.NUMBER_THOUSANDS) | (1 << NumberParser.NUMBER_LAKHS) | (1 << NumberParser.NUMBER_CRORES))) != 0):
                self.state = 65
                self.number_pattern()
                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 66
                        self.match(NumberParser.T__0)


                    self.state = 69
                    self.match(NumberParser.WORD)
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        self.state = 70
                        self.match(NumberParser.T__0)




                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__2:
                    self.state = 75
                    self.spl_discard()




            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 81
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==NumberParser.T__0:
                            self.state = 80
                            self.match(NumberParser.T__0)


                        self.state = 83
                        self.match(NumberParser.WORD)
                        self.state = 85
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                        if la_ == 1:
                            self.state = 84
                            self.match(NumberParser.T__0)


                        self.state = 89 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==NumberParser.T__0 or _la==NumberParser.WORD):
                            break

                    self.state = 91
                    self.number_pattern()
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        self.state = 93
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==NumberParser.T__0:
                            self.state = 92
                            self.match(NumberParser.T__0)


                        self.state = 95
                        self.match(NumberParser.WORD)
                        self.state = 97
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                        if la_ == 1:
                            self.state = 96
                            self.match(NumberParser.T__0)




                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__2:
                        self.state = 101
                        self.spl_discard()

             
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 109
                self.suffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ranges_utteranceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefix(self):
            return self.getTypedRuleContext(NumberParser.PrefixContext,0)


        def range_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Range_patternContext)
            else:
                return self.getTypedRuleContext(NumberParser.Range_patternContext,i)


        def suffix(self):
            return self.getTypedRuleContext(NumberParser.SuffixContext,0)


        def number_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Number_patternContext)
            else:
                return self.getTypedRuleContext(NumberParser.Number_patternContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD)
            else:
                return self.getToken(NumberParser.WORD, i)

        def spl_discard(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Spl_discardContext)
            else:
                return self.getTypedRuleContext(NumberParser.Spl_discardContext,i)


        def getRuleIndex(self):
            return NumberParser.RULE_ranges_utterance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRanges_utterance" ):
                listener.enterRanges_utterance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRanges_utterance" ):
                listener.exitRanges_utterance(self)




    def ranges_utterance(self):

        localctx = NumberParser.Ranges_utteranceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ranges_utterance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 112
                self.prefix()


            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 115
                self.range_pattern()

            elif la_ == 2:
                self.state = 116
                self.number_pattern()
                self.state = 124
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 117
                        self.match(NumberParser.T__0)


                    self.state = 120
                    self.match(NumberParser.WORD)
                    self.state = 122
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 121
                        self.match(NumberParser.T__0)




                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__2:
                    self.state = 126
                    self.spl_discard()




            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 132
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==NumberParser.T__0:
                                self.state = 131
                                self.match(NumberParser.T__0)


                            self.state = 134
                            self.match(NumberParser.WORD)
                            self.state = 136
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                            if la_ == 1:
                                self.state = 135
                                self.match(NumberParser.T__0)



                        else:
                            raise NoViableAltException(self)
                        self.state = 140 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                    self.state = 156
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        self.state = 142
                        self.range_pattern()
                        pass

                    elif la_ == 2:
                        self.state = 143
                        self.number_pattern()
                        self.state = 151
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                        if la_ == 1:
                            self.state = 145
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==NumberParser.T__0:
                                self.state = 144
                                self.match(NumberParser.T__0)


                            self.state = 147
                            self.match(NumberParser.WORD)
                            self.state = 149
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                            if la_ == 1:
                                self.state = 148
                                self.match(NumberParser.T__0)




                        self.state = 154
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==NumberParser.T__2:
                            self.state = 153
                            self.spl_discard()


                        pass

             
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 163
                self.suffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Number_patternContext)
            else:
                return self.getTypedRuleContext(NumberParser.Number_patternContext,i)


        def CONJUNCTION(self):
            return self.getToken(NumberParser.CONJUNCTION, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_range_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_pattern" ):
                listener.enterRange_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_pattern" ):
                listener.exitRange_pattern(self)




    def range_pattern(self):

        localctx = NumberParser.Range_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_range_pattern)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 166
                    self.match(NumberParser.T__0)


                self.state = 169
                self.match(NumberParser.T__1)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 170
                    self.match(NumberParser.T__0)


                self.state = 173
                self.number_pattern()
                self.state = 174
                self.match(NumberParser.CONJUNCTION)
                self.state = 175
                self.number_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 177
                    self.match(NumberParser.T__0)


                self.state = 180
                self.match(NumberParser.T__1)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 181
                    self.match(NumberParser.T__0)


                self.state = 184
                self.number_pattern()
                self.state = 185
                self.match(NumberParser.T__2)
                self.state = 186
                self.number_pattern()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 188
                    self.match(NumberParser.T__0)


                self.state = 191
                self.number_pattern()
                self.state = 192
                self.match(NumberParser.T__2)
                self.state = 193
                self.number_pattern()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 195
                    self.match(NumberParser.T__0)


                self.state = 198
                self.match(NumberParser.T__3)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 199
                    self.match(NumberParser.T__0)


                self.state = 202
                self.number_pattern()
                self.state = 203
                self.match(NumberParser.CONJUNCTION)
                self.state = 204
                self.number_pattern()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def crores_format(self):
            return self.getTypedRuleContext(NumberParser.Crores_formatContext,0)


        def lakhs_format(self):
            return self.getTypedRuleContext(NumberParser.Lakhs_formatContext,0)


        def thousands_format(self):
            return self.getTypedRuleContext(NumberParser.Thousands_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_number_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_pattern" ):
                listener.enterNumber_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_pattern" ):
                listener.exitNumber_pattern(self)




    def number_pattern(self):

        localctx = NumberParser.Number_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 208
                self.crores_format()
                pass

            elif la_ == 2:
                self.state = 209
                self.lakhs_format()
                pass

            elif la_ == 3:
                self.state = 210
                self.thousands_format()
                pass

            elif la_ == 4:
                self.state = 211
                self.hundreds_format()
                pass

            elif la_ == 5:
                self.state = 212
                self.tens_format()
                pass

            elif la_ == 6:
                self.state = 213
                self.units_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Crores_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_CRORES(self):
            return self.getToken(NumberParser.WORD_NUMBER_CRORES, 0)

        def spl_crores(self):
            return self.getTypedRuleContext(NumberParser.Spl_croresContext,0)


        def prefix_crores(self):
            return self.getTypedRuleContext(NumberParser.Prefix_croresContext,0)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def suffix_crores(self):
            return self.getTypedRuleContext(NumberParser.Suffix_croresContext,0)


        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

        def NUMBER_CRORES(self):
            return self.getToken(NumberParser.NUMBER_CRORES, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_crores_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrores_format" ):
                listener.enterCrores_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrores_format" ):
                listener.exitCrores_format(self)




    def crores_format(self):

        localctx = NumberParser.Crores_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_crores_format)
        self._la = 0 # Token type
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_LAKHS, NumberParser.WORD_NUMBER_CRORES, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS, NumberParser.NUMBER_LAKHS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 216
                    self.prefix_crores()


                self.state = 221
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_CRORES]:
                    self.state = 219
                    self.match(NumberParser.WORD_NUMBER_CRORES)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 220
                    self.spl_crores()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 224
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 223
                    self.match(NumberParser.CONJUNCTION)


                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 226
                    self.suffix_crores()


                self.state = 230
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 229
                    self.match(NumberParser.CONJUNCTION)


                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_FRACTIONS:
                    self.state = 232
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass
            elif token in [NumberParser.NUMBER_CRORES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(NumberParser.NUMBER_CRORES)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lakhs_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_LAKHS(self):
            return self.getToken(NumberParser.WORD_NUMBER_LAKHS, 0)

        def spl_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Spl_lakhsContext,0)


        def prefix_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Prefix_lakhsContext,0)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def suffix_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Suffix_lakhsContext,0)


        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

        def NUMBER_LAKHS(self):
            return self.getToken(NumberParser.NUMBER_LAKHS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_lakhs_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLakhs_format" ):
                listener.enterLakhs_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLakhs_format" ):
                listener.exitLakhs_format(self)




    def lakhs_format(self):

        localctx = NumberParser.Lakhs_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lakhs_format)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_LAKHS, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 238
                    self.prefix_lakhs()


                self.state = 243
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_LAKHS]:
                    self.state = 241
                    self.match(NumberParser.WORD_NUMBER_LAKHS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 242
                    self.spl_lakhs()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 246
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 245
                    self.match(NumberParser.CONJUNCTION)


                self.state = 249
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 248
                    self.suffix_lakhs()


                self.state = 252
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 251
                    self.match(NumberParser.CONJUNCTION)


                self.state = 255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 254
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass
            elif token in [NumberParser.NUMBER_LAKHS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(NumberParser.NUMBER_LAKHS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Thousands_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_THOUSANDS(self):
            return self.getToken(NumberParser.WORD_NUMBER_THOUSANDS, 0)

        def spl_thousands(self):
            return self.getTypedRuleContext(NumberParser.Spl_thousandsContext,0)


        def prefix_thousands(self):
            return self.getTypedRuleContext(NumberParser.Prefix_thousandsContext,0)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def suffix_thousands(self):
            return self.getTypedRuleContext(NumberParser.Suffix_thousandsContext,0)


        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

        def NUMBER_THOUSANDS(self):
            return self.getToken(NumberParser.NUMBER_THOUSANDS, 0)

        def WORD_NUMBER_TENS(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD_NUMBER_TENS)
            else:
                return self.getToken(NumberParser.WORD_NUMBER_TENS, i)

        def NUMBER_TENS(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.NUMBER_TENS)
            else:
                return self.getToken(NumberParser.NUMBER_TENS, i)

        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_thousands_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThousands_format" ):
                listener.enterThousands_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThousands_format" ):
                listener.exitThousands_format(self)




    def thousands_format(self):

        localctx = NumberParser.Thousands_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_thousands_format)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 260
                    self.prefix_thousands()


                self.state = 265
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_THOUSANDS]:
                    self.state = 263
                    self.match(NumberParser.WORD_NUMBER_THOUSANDS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 264
                    self.spl_thousands()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 268
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 267
                    self.match(NumberParser.CONJUNCTION)


                self.state = 271
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.suffix_thousands()


                self.state = 274
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 273
                    self.match(NumberParser.CONJUNCTION)


                self.state = 277
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 276
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(NumberParser.NUMBER_THOUSANDS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(NumberParser.NUMBER_THOUSANDS)
                self.state = 286
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 283
                    self.hundreds_format()
                    pass

                elif la_ == 2:
                    self.state = 284
                    self.tens_format()
                    pass

                elif la_ == 3:
                    self.state = 285
                    self.units_format()
                    pass


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 288
                self.match(NumberParser.NUMBER_THOUSANDS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hundreds_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_HUNDREDS(self):
            return self.getToken(NumberParser.WORD_NUMBER_HUNDREDS, 0)

        def prefix_hundreds(self):
            return self.getTypedRuleContext(NumberParser.Prefix_hundredsContext,0)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def suffix_hundreds(self):
            return self.getTypedRuleContext(NumberParser.Suffix_hundredsContext,0)


        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

        def spl_hundreds(self):
            return self.getTypedRuleContext(NumberParser.Spl_hundredsContext,0)


        def spl_hundreds_1(self):
            return self.getTypedRuleContext(NumberParser.Spl_hundreds_1Context,0)


        def spl_hundreds_2(self):
            return self.getTypedRuleContext(NumberParser.Spl_hundreds_2Context,0)


        def spl_hundreds_3(self):
            return self.getTypedRuleContext(NumberParser.Spl_hundreds_3Context,0)


        def spl_hundreds_4(self):
            return self.getTypedRuleContext(NumberParser.Spl_hundreds_4Context,0)


        def NUMBER_HUNDREDS(self):
            return self.getToken(NumberParser.NUMBER_HUNDREDS, 0)

        def WORD_NUMBER_UNITS(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD_NUMBER_UNITS)
            else:
                return self.getToken(NumberParser.WORD_NUMBER_UNITS, i)

        def NUMBER_UNITS(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.NUMBER_UNITS)
            else:
                return self.getToken(NumberParser.NUMBER_UNITS, i)

        def WORD_NUMBER_TENS(self):
            return self.getToken(NumberParser.WORD_NUMBER_TENS, 0)

        def NUMBER_TENS(self):
            return self.getToken(NumberParser.NUMBER_TENS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_hundreds_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHundreds_format" ):
                listener.enterHundreds_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHundreds_format" ):
                listener.exitHundreds_format(self)




    def hundreds_format(self):

        localctx = NumberParser.Hundreds_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_hundreds_format)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS))) != 0):
                    self.state = 291
                    self.prefix_hundreds()


                self.state = 294
                self.match(NumberParser.WORD_NUMBER_HUNDREDS)
                self.state = 296
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 295
                    self.match(NumberParser.CONJUNCTION)


                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS))) != 0):
                    self.state = 298
                    self.suffix_hundreds()


                self.state = 302
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 301
                    self.match(NumberParser.CONJUNCTION)


                self.state = 305
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 304
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.spl_hundreds()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.spl_hundreds_1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.spl_hundreds_2()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 310
                self.spl_hundreds_3()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 311
                self.spl_hundreds_4()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 312
                self.match(NumberParser.NUMBER_HUNDREDS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 313
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 314
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 316
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 317
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tens_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONJUNCTION(self):
            return self.getToken(NumberParser.CONJUNCTION, 0)

        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

        def WORD_NUMBER_TENS(self):
            return self.getToken(NumberParser.WORD_NUMBER_TENS, 0)

        def NUMBER_TENS(self):
            return self.getToken(NumberParser.NUMBER_TENS, 0)

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_tens_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTens_format" ):
                listener.enterTens_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTens_format" ):
                listener.exitTens_format(self)




    def tens_format(self):

        localctx = NumberParser.Tens_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tens_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_TENS]:
                self.state = 320
                self.match(NumberParser.WORD_NUMBER_TENS)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 321
                    self.units_format()


                pass
            elif token in [NumberParser.NUMBER_TENS]:
                self.state = 324
                self.match(NumberParser.NUMBER_TENS)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 325
                    self.units_format()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.state = 330
                self.match(NumberParser.CONJUNCTION)


            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.state = 333
                self.match(NumberParser.WORD_NUMBER_FRACTIONS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Units_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_UNITS(self):
            return self.getToken(NumberParser.WORD_NUMBER_UNITS, 0)

        def NUMBER_UNITS(self):
            return self.getToken(NumberParser.NUMBER_UNITS, 0)

        def CONJUNCTION(self):
            return self.getToken(NumberParser.CONJUNCTION, 0)

        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_units_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnits_format" ):
                listener.enterUnits_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnits_format" ):
                listener.exitUnits_format(self)




    def units_format(self):

        localctx = NumberParser.Units_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_units_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.state = 337
                self.match(NumberParser.CONJUNCTION)


            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.state = 340
                self.match(NumberParser.WORD_NUMBER_FRACTIONS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_croresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def thousands_format(self):
            return self.getTypedRuleContext(NumberParser.Thousands_formatContext,0)


        def lakhs_format(self):
            return self.getTypedRuleContext(NumberParser.Lakhs_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_prefix_crores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_crores" ):
                listener.enterPrefix_crores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_crores" ):
                listener.exitPrefix_crores(self)




    def prefix_crores(self):

        localctx = NumberParser.Prefix_croresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_prefix_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 343
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 344
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 345
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 346
                self.thousands_format()
                pass

            elif la_ == 5:
                self.state = 347
                self.lakhs_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Suffix_croresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def thousands_format(self):
            return self.getTypedRuleContext(NumberParser.Thousands_formatContext,0)


        def lakhs_format(self):
            return self.getTypedRuleContext(NumberParser.Lakhs_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_suffix_crores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix_crores" ):
                listener.enterSuffix_crores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix_crores" ):
                listener.exitSuffix_crores(self)




    def suffix_crores(self):

        localctx = NumberParser.Suffix_croresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_suffix_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 350
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 351
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 352
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 353
                self.thousands_format()
                pass

            elif la_ == 5:
                self.state = 354
                self.lakhs_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_lakhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def thousands_format(self):
            return self.getTypedRuleContext(NumberParser.Thousands_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_prefix_lakhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_lakhs" ):
                listener.enterPrefix_lakhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_lakhs" ):
                listener.exitPrefix_lakhs(self)




    def prefix_lakhs(self):

        localctx = NumberParser.Prefix_lakhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_prefix_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 357
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 358
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 359
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 360
                self.thousands_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Suffix_lakhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def thousands_format(self):
            return self.getTypedRuleContext(NumberParser.Thousands_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_suffix_lakhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix_lakhs" ):
                listener.enterSuffix_lakhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix_lakhs" ):
                listener.exitSuffix_lakhs(self)




    def suffix_lakhs(self):

        localctx = NumberParser.Suffix_lakhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_suffix_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 363
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 364
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 365
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 366
                self.thousands_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_thousandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_prefix_thousands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_thousands" ):
                listener.enterPrefix_thousands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_thousands" ):
                listener.exitPrefix_thousands(self)




    def prefix_thousands(self):

        localctx = NumberParser.Prefix_thousandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_prefix_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.state = 369
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 370
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 371
                self.hundreds_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Suffix_thousandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def hundreds_format(self):
            return self.getTypedRuleContext(NumberParser.Hundreds_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_suffix_thousands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix_thousands" ):
                listener.enterSuffix_thousands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix_thousands" ):
                listener.exitSuffix_thousands(self)




    def suffix_thousands(self):

        localctx = NumberParser.Suffix_thousandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_suffix_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.state = 374
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 375
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 376
                self.hundreds_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_hundredsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_prefix_hundreds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_hundreds" ):
                listener.enterPrefix_hundreds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_hundreds" ):
                listener.exitPrefix_hundreds(self)




    def prefix_hundreds(self):

        localctx = NumberParser.Prefix_hundredsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_prefix_hundreds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_UNITS, NumberParser.NUMBER_UNITS]:
                self.state = 379
                self.units_format()
                pass
            elif token in [NumberParser.WORD_NUMBER_TENS, NumberParser.NUMBER_TENS]:
                self.state = 380
                self.tens_format()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Suffix_hundredsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def tens_format(self):
            return self.getTypedRuleContext(NumberParser.Tens_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_suffix_hundreds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix_hundreds" ):
                listener.enterSuffix_hundreds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix_hundreds" ):
                listener.exitSuffix_hundreds(self)




    def suffix_hundreds(self):

        localctx = NumberParser.Suffix_hundredsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_suffix_hundreds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_UNITS, NumberParser.NUMBER_UNITS]:
                self.state = 383
                self.units_format()
                pass
            elif token in [NumberParser.WORD_NUMBER_TENS, NumberParser.NUMBER_TENS]:
                self.state = 384
                self.tens_format()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_tensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_UNITS(self):
            return self.getToken(NumberParser.WORD_NUMBER_UNITS, 0)

        def NUMBER_UNITS(self):
            return self.getToken(NumberParser.NUMBER_UNITS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_tens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_tens" ):
                listener.enterSpl_tens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_tens" ):
                listener.exitSpl_tens(self)




    def spl_tens(self):

        localctx = NumberParser.Spl_tensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_spl_tens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(NumberParser.T__2)
            self.state = 388
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 389
                self.match(NumberParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_hundredsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_TENS(self):
            return self.getToken(NumberParser.WORD_NUMBER_TENS, 0)

        def NUMBER_TENS(self):
            return self.getToken(NumberParser.NUMBER_TENS, 0)

        def WORD_NUMBER_HUNDREDS(self):
            return self.getToken(NumberParser.WORD_NUMBER_HUNDREDS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_hundreds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_hundreds" ):
                listener.enterSpl_hundreds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_hundreds" ):
                listener.exitSpl_hundreds(self)




    def spl_hundreds(self):

        localctx = NumberParser.Spl_hundredsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_spl_hundreds)
        self._la = 0 # Token type
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(NumberParser.T__2)
                self.state = 393
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 395
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                if la_ == 1:
                    self.state = 394
                    self.match(NumberParser.T__0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(NumberParser.T__2)
                self.state = 398
                self.match(NumberParser.WORD_NUMBER_HUNDREDS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_hundreds_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spl_tens(self):
            return self.getTypedRuleContext(NumberParser.Spl_tensContext,0)


        def WORD_NUMBER_UNITS(self):
            return self.getToken(NumberParser.WORD_NUMBER_UNITS, 0)

        def NUMBER_UNITS(self):
            return self.getToken(NumberParser.NUMBER_UNITS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_hundreds_1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_hundreds_1" ):
                listener.enterSpl_hundreds_1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_hundreds_1" ):
                listener.exitSpl_hundreds_1(self)




    def spl_hundreds_1(self):

        localctx = NumberParser.Spl_hundreds_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_spl_hundreds_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.spl_tens()
            self.state = 402
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_hundreds_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spl_tens(self):
            return self.getTypedRuleContext(NumberParser.Spl_tensContext,0)


        def WORD_NUMBER_UNITS(self):
            return self.getToken(NumberParser.WORD_NUMBER_UNITS, 0)

        def NUMBER_UNITS(self):
            return self.getToken(NumberParser.NUMBER_UNITS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_hundreds_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_hundreds_2" ):
                listener.enterSpl_hundreds_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_hundreds_2" ):
                listener.exitSpl_hundreds_2(self)




    def spl_hundreds_2(self):

        localctx = NumberParser.Spl_hundreds_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_spl_hundreds_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 405
            self.spl_tens()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_hundreds_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spl_epilogue(self):
            return self.getTypedRuleContext(NumberParser.Spl_epilogueContext,0)


        def WORD_NUMBER_UNITS(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD_NUMBER_UNITS)
            else:
                return self.getToken(NumberParser.WORD_NUMBER_UNITS, i)

        def NUMBER_UNITS(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.NUMBER_UNITS)
            else:
                return self.getToken(NumberParser.NUMBER_UNITS, i)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_hundreds_3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_hundreds_3" ):
                listener.enterSpl_hundreds_3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_hundreds_3" ):
                listener.exitSpl_hundreds_3(self)




    def spl_hundreds_3(self):

        localctx = NumberParser.Spl_hundreds_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_spl_hundreds_3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 408
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 409
            self.spl_epilogue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_hundreds_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spl_tens(self):
            return self.getTypedRuleContext(NumberParser.Spl_tensContext,0)


        def spl_epilogue(self):
            return self.getTypedRuleContext(NumberParser.Spl_epilogueContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_spl_hundreds_4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_hundreds_4" ):
                listener.enterSpl_hundreds_4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_hundreds_4" ):
                listener.exitSpl_hundreds_4(self)




    def spl_hundreds_4(self):

        localctx = NumberParser.Spl_hundreds_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_spl_hundreds_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.spl_tens()
            self.state = 412
            self.spl_epilogue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_thousandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_THOUSANDS(self):
            return self.getToken(NumberParser.WORD_NUMBER_THOUSANDS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_thousands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_thousands" ):
                listener.enterSpl_thousands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_thousands" ):
                listener.exitSpl_thousands(self)




    def spl_thousands(self):

        localctx = NumberParser.Spl_thousandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_spl_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(NumberParser.T__2)
            self.state = 415
            self.match(NumberParser.WORD_NUMBER_THOUSANDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_lakhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_LAKHS(self):
            return self.getToken(NumberParser.WORD_NUMBER_LAKHS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_lakhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_lakhs" ):
                listener.enterSpl_lakhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_lakhs" ):
                listener.exitSpl_lakhs(self)




    def spl_lakhs(self):

        localctx = NumberParser.Spl_lakhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_spl_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(NumberParser.T__2)
            self.state = 418
            self.match(NumberParser.WORD_NUMBER_LAKHS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_croresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_CRORES(self):
            return self.getToken(NumberParser.WORD_NUMBER_CRORES, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_crores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_crores" ):
                listener.enterSpl_crores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_crores" ):
                listener.exitSpl_crores(self)




    def spl_crores(self):

        localctx = NumberParser.Spl_croresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_spl_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(NumberParser.T__2)
            self.state = 421
            self.match(NumberParser.WORD_NUMBER_CRORES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_epilogueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NumberParser.RULE_spl_epilogue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_epilogue" ):
                listener.enterSpl_epilogue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_epilogue" ):
                listener.exitSpl_epilogue(self)




    def spl_epilogue(self):

        localctx = NumberParser.Spl_epilogueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_spl_epilogue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(NumberParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_discardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(NumberParser.WORD, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_discard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_discard" ):
                listener.enterSpl_discard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_discard" ):
                listener.exitSpl_discard(self)




    def spl_discard(self):

        localctx = NumberParser.Spl_discardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_spl_discard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(NumberParser.T__2)
            self.state = 426
            self.match(NumberParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD)
            else:
                return self.getToken(NumberParser.WORD, i)

        def getRuleIndex(self):
            return NumberParser.RULE_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix" ):
                listener.enterPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix" ):
                listener.exitPrefix(self)




    def prefix(self):

        localctx = NumberParser.PrefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_prefix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 428
                        self.match(NumberParser.T__0)


                    self.state = 431
                    self.match(NumberParser.WORD)
                    self.state = 433
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
                    if la_ == 1:
                        self.state = 432
                        self.match(NumberParser.T__0)

             
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD)
            else:
                return self.getToken(NumberParser.WORD, i)

        def getRuleIndex(self):
            return NumberParser.RULE_suffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix" ):
                listener.enterSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix" ):
                listener.exitSuffix(self)




    def suffix(self):

        localctx = NumberParser.SuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_suffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NumberParser.T__0 or _la==NumberParser.WORD:
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 440
                    self.match(NumberParser.T__0)


                self.state = 443
                self.match(NumberParser.WORD)
                self.state = 445
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
                if la_ == 1:
                    self.state = 444
                    self.match(NumberParser.T__0)


                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





