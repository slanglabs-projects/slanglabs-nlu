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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&")
        buf.write("\u028b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\5\2P\n\2\3\2\7\2S\n\2\f\2\16\2V\13\2\3\2")
        buf.write("\3\2\7\2Z\n\2\f\2\16\2]\13\2\3\2\3\2\7\2a\n\2\f\2\16\2")
        buf.write("d\13\2\5\2f\n\2\3\2\5\2i\n\2\5\2k\n\2\3\2\7\2n\n\2\f\2")
        buf.write("\16\2q\13\2\3\2\3\2\7\2u\n\2\f\2\16\2x\13\2\6\2z\n\2\r")
        buf.write("\2\16\2{\3\2\5\2\177\n\2\3\2\7\2\u0082\n\2\f\2\16\2\u0085")
        buf.write("\13\2\3\2\3\2\7\2\u0089\n\2\f\2\16\2\u008c\13\2\5\2\u008e")
        buf.write("\n\2\3\2\5\2\u0091\n\2\7\2\u0093\n\2\f\2\16\2\u0096\13")
        buf.write("\2\3\2\7\2\u0099\n\2\f\2\16\2\u009c\13\2\3\2\5\2\u009f")
        buf.write("\n\2\3\3\3\3\7\3\u00a3\n\3\f\3\16\3\u00a6\13\3\3\3\3\3")
        buf.write("\7\3\u00aa\n\3\f\3\16\3\u00ad\13\3\7\3\u00af\n\3\f\3\16")
        buf.write("\3\u00b2\13\3\3\4\5\4\u00b5\n\4\3\4\3\4\3\4\5\4\u00ba")
        buf.write("\n\4\3\4\3\4\5\4\u00be\n\4\5\4\u00c0\n\4\3\4\5\4\u00c3")
        buf.write("\n\4\5\4\u00c5\n\4\3\4\5\4\u00c8\n\4\3\4\3\4\5\4\u00cc")
        buf.write("\n\4\6\4\u00ce\n\4\r\4\16\4\u00cf\3\4\3\4\3\4\5\4\u00d5")
        buf.write("\n\4\3\4\3\4\5\4\u00d9\n\4\5\4\u00db\n\4\3\4\5\4\u00de")
        buf.write("\n\4\5\4\u00e0\n\4\7\4\u00e2\n\4\f\4\16\4\u00e5\13\4\3")
        buf.write("\4\5\4\u00e8\n\4\3\5\5\5\u00eb\n\5\3\5\3\5\5\5\u00ef\n")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5\u00f6\n\5\3\5\3\5\5\5\u00fa")
        buf.write("\n\5\3\5\3\5\3\5\3\5\3\5\5\5\u0101\n\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u0108\n\5\3\5\3\5\5\5\u010c\n\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0112\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u011d\n\6\3\7\5\7\u0120\n\7\3\7\3\7\5\7\u0124\n\7\6")
        buf.write("\7\u0126\n\7\r\7\16\7\u0127\3\7\5\7\u012b\n\7\3\b\5\b")
        buf.write("\u012e\n\b\3\b\3\b\5\b\u0132\n\b\3\b\5\b\u0135\n\b\3\b")
        buf.write("\5\b\u0138\n\b\3\b\5\b\u013b\n\b\3\b\5\b\u013e\n\b\3\b")
        buf.write("\5\b\u0141\n\b\3\t\5\t\u0144\n\t\3\t\3\t\5\t\u0148\n\t")
        buf.write("\3\t\5\t\u014b\n\t\3\t\5\t\u014e\n\t\3\t\5\t\u0151\n\t")
        buf.write("\3\t\5\t\u0154\n\t\3\t\5\t\u0157\n\t\3\n\5\n\u015a\n\n")
        buf.write("\3\n\3\n\5\n\u015e\n\n\3\n\5\n\u0161\n\n\3\n\5\n\u0164")
        buf.write("\n\n\3\n\5\n\u0167\n\n\3\n\5\n\u016a\n\n\3\n\5\n\u016d")
        buf.write("\n\n\3\13\5\13\u0170\n\13\3\13\3\13\5\13\u0174\n\13\3")
        buf.write("\13\5\13\u0177\n\13\3\13\5\13\u017a\n\13\3\13\5\13\u017d")
        buf.write("\n\13\3\13\5\13\u0180\n\13\3\13\5\13\u0183\n\13\3\f\5")
        buf.write("\f\u0186\n\f\3\f\3\f\5\f\u018a\n\f\3\f\5\f\u018d\n\f\3")
        buf.write("\f\5\f\u0190\n\f\3\f\5\f\u0193\n\f\3\f\5\f\u0196\n\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u019f\n\f\3\f\3\f\3\f\5")
        buf.write("\f\u01a4\n\f\3\f\3\f\3\f\5\f\u01a9\n\f\3\r\5\r\u01ac\n")
        buf.write("\r\3\r\3\r\5\r\u01b0\n\r\3\r\5\r\u01b3\n\r\3\r\5\r\u01b6")
        buf.write("\n\r\3\r\5\r\u01b9\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u01c9\n\r\3\16\3\16\5\16")
        buf.write("\u01cd\n\16\3\16\3\16\5\16\u01d1\n\16\5\16\u01d3\n\16")
        buf.write("\3\16\5\16\u01d6\n\16\3\16\5\16\u01d9\n\16\3\17\3\17\5")
        buf.write("\17\u01dd\n\17\3\17\5\17\u01e0\n\17\3\20\3\20\5\20\u01e4")
        buf.write("\n\20\3\20\3\20\5\20\u01e8\n\20\3\20\7\20\u01eb\n\20\f")
        buf.write("\20\16\20\u01ee\13\20\3\20\5\20\u01f1\n\20\3\20\3\20\5")
        buf.write("\20\u01f5\n\20\3\20\3\20\5\20\u01f9\n\20\3\20\3\20\5\20")
        buf.write("\u01fd\n\20\5\20\u01ff\n\20\5\20\u0201\n\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u0208\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u020f\n\22\3\23\3\23\3\23\3\23\5\23\u0215\n\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u021b\n\24\3\25\3\25\3\25\5")
        buf.write("\25\u0220\n\25\3\26\3\26\3\26\5\26\u0225\n\26\3\27\3\27")
        buf.write("\5\27\u0229\n\27\3\30\3\30\5\30\u022d\n\30\3\31\3\31\3")
        buf.write("\31\5\31\u0232\n\31\3\32\3\32\3\32\5\32\u0237\n\32\3\32")
        buf.write("\3\32\5\32\u023b\n\32\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\7%\u025d")
        buf.write("\n%\f%\16%\u0260\13%\3%\3%\7%\u0264\n%\f%\16%\u0267\13")
        buf.write("%\3%\3%\7%\u026b\n%\f%\16%\u026e\13%\3%\5%\u0271\n%\3")
        buf.write("&\5&\u0274\n&\3&\3&\5&\u0278\n&\7&\u027a\n&\f&\16&\u027d")
        buf.write("\13&\3\'\5\'\u0280\n\'\3\'\3\'\5\'\u0284\n\'\7\'\u0286")
        buf.write("\n\'\f\'\16\'\u0289\13\'\3\'\2\2(\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL\2\b")
        buf.write("\4\2\31\31%%\4\2\21\21\34\34\4\2\22\22\35\35\3\3\3\3\3")
        buf.write("\2\b\t\3\2\13\17\2\u030a\2O\3\2\2\2\4\u00a0\3\2\2\2\6")
        buf.write("\u00b4\3\2\2\2\b\u0111\3\2\2\2\n\u011c\3\2\2\2\f\u0125")
        buf.write("\3\2\2\2\16\u0140\3\2\2\2\20\u0156\3\2\2\2\22\u016c\3")
        buf.write("\2\2\2\24\u0182\3\2\2\2\26\u01a8\3\2\2\2\30\u01c8\3\2")
        buf.write("\2\2\32\u01d2\3\2\2\2\34\u01da\3\2\2\2\36\u0200\3\2\2")
        buf.write("\2 \u0207\3\2\2\2\"\u020e\3\2\2\2$\u0214\3\2\2\2&\u021a")
        buf.write("\3\2\2\2(\u021f\3\2\2\2*\u0224\3\2\2\2,\u0228\3\2\2\2")
        buf.write(".\u022c\3\2\2\2\60\u022e\3\2\2\2\62\u023a\3\2\2\2\64\u023c")
        buf.write("\3\2\2\2\66\u023f\3\2\2\28\u0242\3\2\2\2:\u0246\3\2\2")
        buf.write("\2<\u0249\3\2\2\2>\u024c\3\2\2\2@\u024f\3\2\2\2B\u0252")
        buf.write("\3\2\2\2D\u0255\3\2\2\2F\u0258\3\2\2\2H\u0270\3\2\2\2")
        buf.write("J\u027b\3\2\2\2L\u0287\3\2\2\2NP\5J&\2ON\3\2\2\2OP\3\2")
        buf.write("\2\2PT\3\2\2\2QS\5\4\3\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2")
        buf.write("TU\3\2\2\2Uj\3\2\2\2VT\3\2\2\2We\5\n\6\2XZ\7\3\2\2YX\3")
        buf.write("\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2][\3\2")
        buf.write("\2\2^b\t\2\2\2_a\7\3\2\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2")
        buf.write("bc\3\2\2\2cf\3\2\2\2db\3\2\2\2e[\3\2\2\2ef\3\2\2\2fh\3")
        buf.write("\2\2\2gi\5H%\2hg\3\2\2\2hi\3\2\2\2ik\3\2\2\2jW\3\2\2\2")
        buf.write("jk\3\2\2\2k\u0094\3\2\2\2ln\7\3\2\2ml\3\2\2\2nq\3\2\2")
        buf.write("\2om\3\2\2\2op\3\2\2\2pr\3\2\2\2qo\3\2\2\2rv\t\2\2\2s")
        buf.write("u\7\3\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2wz\3")
        buf.write("\2\2\2xv\3\2\2\2yo\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2\2")
        buf.write("\2|~\3\2\2\2}\177\5\n\6\2~}\3\2\2\2~\177\3\2\2\2\177\u008d")
        buf.write("\3\2\2\2\u0080\u0082\7\3\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u008a\t")
        buf.write("\2\2\2\u0087\u0089\7\3\2\2\u0088\u0087\3\2\2\2\u0089\u008c")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u0083\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0091\5")
        buf.write("H%\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093")
        buf.write("\3\2\2\2\u0092y\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u009a\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0097\u0099\5\4\3\2\u0098\u0097\3\2\2\2")
        buf.write("\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f")
        buf.write("\5L\'\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\3\3\2\2\2\u00a0\u00b0\5H%\2\u00a1\u00a3\7\3\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3")
        buf.write("\2\2\2\u00a7\u00ab\t\2\2\2\u00a8\u00aa\7\3\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\u00a4\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\5\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b3\u00b5\5J&\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00c4\3\2\2\2\u00b6\u00c5\5\b\5\2\u00b7")
        buf.write("\u00bf\5\n\6\2\u00b8\u00ba\7\3\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\7")
        buf.write("%\2\2\u00bc\u00be\7\3\2\2\u00bd\u00bc\3\2\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00c3\5H%\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2")
        buf.write("\u00c4\u00b6\3\2\2\2\u00c4\u00b7\3\2\2\2\u00c4\u00c5\3")
        buf.write("\2\2\2\u00c5\u00e3\3\2\2\2\u00c6\u00c8\7\3\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00cb\7%\2\2\u00ca\u00cc\7\3\2\2\u00cb\u00ca\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00c7\3")
        buf.write("\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00df\3\2\2\2\u00d1\u00e0\5\b\5\2\u00d2")
        buf.write("\u00da\5\n\6\2\u00d3\u00d5\7\3\2\2\u00d4\u00d3\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\7")
        buf.write("%\2\2\u00d7\u00d9\7\3\2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d4\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00de\5H%\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\3\2\2\2")
        buf.write("\u00df\u00d1\3\2\2\2\u00df\u00d2\3\2\2\2\u00e0\u00e2\3")
        buf.write("\2\2\2\u00e1\u00cd\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e8\5L\'\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\7\3\2\2\2\u00e9\u00eb\7\3\2")
        buf.write("\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ec\u00ee\7\4\2\2\u00ed\u00ef\7\3\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f1\5\n\6\2\u00f1\u00f2\7\31\2\2\u00f2\u00f3")
        buf.write("\5\n\6\2\u00f3\u0112\3\2\2\2\u00f4\u00f6\7\3\2\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f9\7\4\2\2\u00f8\u00fa\7\3\2\2\u00f9\u00f8\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc")
        buf.write("\5\n\6\2\u00fc\u00fd\7\5\2\2\u00fd\u00fe\5\n\6\2\u00fe")
        buf.write("\u0112\3\2\2\2\u00ff\u0101\7\3\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\5")
        buf.write("\n\6\2\u0103\u0104\7\5\2\2\u0104\u0105\5\n\6\2\u0105\u0112")
        buf.write("\3\2\2\2\u0106\u0108\7\3\2\2\u0107\u0106\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010b\7\6\2\2")
        buf.write("\u010a\u010c\7\3\2\2\u010b\u010a\3\2\2\2\u010b\u010c\3")
        buf.write("\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\5\n\6\2\u010e\u010f")
        buf.write("\7\31\2\2\u010f\u0110\5\n\6\2\u0110\u0112\3\2\2\2\u0111")
        buf.write("\u00ea\3\2\2\2\u0111\u00f5\3\2\2\2\u0111\u0100\3\2\2\2")
        buf.write("\u0111\u0107\3\2\2\2\u0112\t\3\2\2\2\u0113\u011d\5\16")
        buf.write("\b\2\u0114\u011d\5\20\t\2\u0115\u011d\5\24\13\2\u0116")
        buf.write("\u011d\5\22\n\2\u0117\u011d\5\26\f\2\u0118\u011d\5\30")
        buf.write("\r\2\u0119\u011d\5\32\16\2\u011a\u011d\5\34\17\2\u011b")
        buf.write("\u011d\5\f\7\2\u011c\u0113\3\2\2\2\u011c\u0114\3\2\2\2")
        buf.write("\u011c\u0115\3\2\2\2\u011c\u0116\3\2\2\2\u011c\u0117\3")
        buf.write("\2\2\2\u011c\u0118\3\2\2\2\u011c\u0119\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011b\3\2\2\2\u011d\13\3\2\2\2\u011e\u0120")
        buf.write("\7\3\2\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0123\t\3\2\2\u0122\u0124\7\3\2\2")
        buf.write("\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3")
        buf.write("\2\2\2\u0125\u011f\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\3\2\2\2\u0129")
        buf.write("\u012b\5\36\20\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2")
        buf.write("\2\u012b\r\3\2\2\2\u012c\u012e\5$\23\2\u012d\u012c\3\2")
        buf.write("\2\2\u012d\u012e\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u0132")
        buf.write("\7\30\2\2\u0130\u0132\5D#\2\u0131\u012f\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0135\7\31\2")
        buf.write("\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137")
        buf.write("\3\2\2\2\u0136\u0138\5&\24\2\u0137\u0136\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\7\31\2")
        buf.write("\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d")
        buf.write("\3\2\2\2\u013c\u013e\5\36\20\2\u013d\u013c\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u0141\7#\2\2")
        buf.write("\u0140\u012d\3\2\2\2\u0140\u013f\3\2\2\2\u0141\17\3\2")
        buf.write("\2\2\u0142\u0144\5 \21\2\u0143\u0142\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0148\7\27\2\2\u0146")
        buf.write("\u0148\5B\"\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2")
        buf.write("\u0148\u014a\3\2\2\2\u0149\u014b\7\31\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c")
        buf.write("\u014e\5\"\22\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2")
        buf.write("\2\u014e\u0150\3\2\2\2\u014f\u0151\7\31\2\2\u0150\u014f")
        buf.write("\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152")
        buf.write("\u0154\5\36\20\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2")
        buf.write("\2\u0154\u0157\3\2\2\2\u0155\u0157\7\"\2\2\u0156\u0143")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157\21\3\2\2\2\u0158\u015a")
        buf.write("\5$\23\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u015e\7\25\2\2\u015c\u015e\5> \2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2\u015e\u0160\3")
        buf.write("\2\2\2\u015f\u0161\7\31\2\2\u0160\u015f\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0164\5&\24\2")
        buf.write("\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3")
        buf.write("\2\2\2\u0165\u0167\7\31\2\2\u0166\u0165\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u016a\5\36\20")
        buf.write("\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016d")
        buf.write("\3\2\2\2\u016b\u016d\7 \2\2\u016c\u0159\3\2\2\2\u016c")
        buf.write("\u016b\3\2\2\2\u016d\23\3\2\2\2\u016e\u0170\5$\23\2\u016f")
        buf.write("\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0173\3\2\2\2")
        buf.write("\u0171\u0174\7\26\2\2\u0172\u0174\5@!\2\u0173\u0171\3")
        buf.write("\2\2\2\u0173\u0172\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0177")
        buf.write("\7\31\2\2\u0176\u0175\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\u0179\3\2\2\2\u0178\u017a\5&\24\2\u0179\u0178\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u017d\7")
        buf.write("\31\2\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017f\3\2\2\2\u017e\u0180\5\36\20\2\u017f\u017e\3\2\2")
        buf.write("\2\u017f\u0180\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u0183")
        buf.write("\7!\2\2\u0182\u016f\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("\25\3\2\2\2\u0184\u0186\5(\25\2\u0185\u0184\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u018a\7\24\2")
        buf.write("\2\u0188\u018a\5<\37\2\u0189\u0187\3\2\2\2\u0189\u0188")
        buf.write("\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u018d\7\31\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u0190\5*\26\2\u018f\u018e\3\2\2\2\u018f\u0190\3")
        buf.write("\2\2\2\u0190\u0192\3\2\2\2\u0191\u0193\7\31\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2")
        buf.write("\u0194\u0196\5\36\20\2\u0195\u0194\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u01a9\3\2\2\2\u0197\u01a9\7\37\2\2\u0198")
        buf.write("\u0199\t\4\2\2\u0199\u01a9\t\4\2\2\u019a\u019e\7\37\2")
        buf.write("\2\u019b\u019f\5\30\r\2\u019c\u019f\5\32\16\2\u019d\u019f")
        buf.write("\5\34\17\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a9\3\2\2\2\u01a0\u01a9\7\37\2")
        buf.write("\2\u01a1\u01a3\5(\25\2\u01a2\u01a4\7\3\2\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\7\7\2\2\u01a6\u01a7\t\5\2\2\u01a7\u01a9\3\2\2\2")
        buf.write("\u01a8\u0185\3\2\2\2\u01a8\u0197\3\2\2\2\u01a8\u0198\3")
        buf.write("\2\2\2\u01a8\u019a\3\2\2\2\u01a8\u01a0\3\2\2\2\u01a8\u01a1")
        buf.write("\3\2\2\2\u01a9\27\3\2\2\2\u01aa\u01ac\5,\27\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01af\7\23\2\2\u01ae\u01b0\7\31\2\2\u01af\u01ae\3\2\2")
        buf.write("\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01b3")
        buf.write("\5.\30\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b5\3\2\2\2\u01b4\u01b6\7\31\2\2\u01b5\u01b4\3\2\2")
        buf.write("\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b9")
        buf.write("\5\36\20\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("\u01c9\3\2\2\2\u01ba\u01c9\5\62\32\2\u01bb\u01c9\5\64")
        buf.write("\33\2\u01bc\u01c9\5\66\34\2\u01bd\u01c9\58\35\2\u01be")
        buf.write("\u01c9\5:\36\2\u01bf\u01c9\7\36\2\2\u01c0\u01c1\t\3\2")
        buf.write("\2\u01c1\u01c2\t\3\2\2\u01c2\u01c9\t\3\2\2\u01c3\u01c4")
        buf.write("\t\3\2\2\u01c4\u01c9\t\4\2\2\u01c5\u01c6\t\3\2\2\u01c6")
        buf.write("\u01c7\t\4\2\2\u01c7\u01c9\t\3\2\2\u01c8\u01ab\3\2\2\2")
        buf.write("\u01c8\u01ba\3\2\2\2\u01c8\u01bb\3\2\2\2\u01c8\u01bc\3")
        buf.write("\2\2\2\u01c8\u01bd\3\2\2\2\u01c8\u01be\3\2\2\2\u01c8\u01bf")
        buf.write("\3\2\2\2\u01c8\u01c0\3\2\2\2\u01c8\u01c3\3\2\2\2\u01c8")
        buf.write("\u01c5\3\2\2\2\u01c9\31\3\2\2\2\u01ca\u01cc\7\22\2\2\u01cb")
        buf.write("\u01cd\5\34\17\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2")
        buf.write("\2\u01cd\u01d3\3\2\2\2\u01ce\u01d0\7\35\2\2\u01cf\u01d1")
        buf.write("\5\34\17\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d3\3\2\2\2\u01d2\u01ca\3\2\2\2\u01d2\u01ce\3\2\2\2")
        buf.write("\u01d3\u01d5\3\2\2\2\u01d4\u01d6\7\31\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01d9\5\36\20\2\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2")
        buf.write("\2\u01d9\33\3\2\2\2\u01da\u01dc\t\3\2\2\u01db\u01dd\7")
        buf.write("\31\2\2\u01dc\u01db\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01df\3\2\2\2\u01de\u01e0\5\36\20\2\u01df\u01de\3\2\2")
        buf.write("\2\u01df\u01e0\3\2\2\2\u01e0\35\3\2\2\2\u01e1\u0201\7")
        buf.write("\20\2\2\u01e2\u01e4\7\3\2\2\u01e3\u01e2\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7\t\6\2\2")
        buf.write("\u01e6\u01e8\7\3\2\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8\3")
        buf.write("\2\2\2\u01e8\u01ec\3\2\2\2\u01e9\u01eb\t\3\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u0201\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ef\u01f1\7\3\2\2\u01f0\u01ef\3\2\2\2\u01f0\u01f1\3")
        buf.write("\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f4\t\6\2\2\u01f3\u01f5")
        buf.write("\7\3\2\2\u01f4\u01f3\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5")
        buf.write("\u01fe\3\2\2\2\u01f6\u01f8\7\22\2\2\u01f7\u01f9\5\34\17")
        buf.write("\2\u01f8\u01f7\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01ff")
        buf.write("\3\2\2\2\u01fa\u01fc\7\35\2\2\u01fb\u01fd\5\34\17\2\u01fc")
        buf.write("\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2")
        buf.write("\u01fe\u01f6\3\2\2\2\u01fe\u01fa\3\2\2\2\u01ff\u0201\3")
        buf.write("\2\2\2\u0200\u01e1\3\2\2\2\u0200\u01e3\3\2\2\2\u0200\u01f0")
        buf.write("\3\2\2\2\u0201\37\3\2\2\2\u0202\u0208\5\34\17\2\u0203")
        buf.write("\u0208\5\32\16\2\u0204\u0208\5\30\r\2\u0205\u0208\5\26")
        buf.write("\f\2\u0206\u0208\5\22\n\2\u0207\u0202\3\2\2\2\u0207\u0203")
        buf.write("\3\2\2\2\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208!\3\2\2\2\u0209\u020f\5\34\17\2\u020a")
        buf.write("\u020f\5\32\16\2\u020b\u020f\5\30\r\2\u020c\u020f\5\26")
        buf.write("\f\2\u020d\u020f\5\22\n\2\u020e\u0209\3\2\2\2\u020e\u020a")
        buf.write("\3\2\2\2\u020e\u020b\3\2\2\2\u020e\u020c\3\2\2\2\u020e")
        buf.write("\u020d\3\2\2\2\u020f#\3\2\2\2\u0210\u0215\5\34\17\2\u0211")
        buf.write("\u0215\5\32\16\2\u0212\u0215\5\30\r\2\u0213\u0215\5\26")
        buf.write("\f\2\u0214\u0210\3\2\2\2\u0214\u0211\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0213\3\2\2\2\u0215%\3\2\2\2\u0216\u021b")
        buf.write("\5\34\17\2\u0217\u021b\5\32\16\2\u0218\u021b\5\30\r\2")
        buf.write("\u0219\u021b\5\26\f\2\u021a\u0216\3\2\2\2\u021a\u0217")
        buf.write("\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("\'\3\2\2\2\u021c\u0220\5\34\17\2\u021d\u0220\5\32\16\2")
        buf.write("\u021e\u0220\5\30\r\2\u021f\u021c\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u021f\u021e\3\2\2\2\u0220)\3\2\2\2\u0221\u0225")
        buf.write("\5\34\17\2\u0222\u0225\5\32\16\2\u0223\u0225\5\30\r\2")
        buf.write("\u0224\u0221\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0223\3")
        buf.write("\2\2\2\u0225+\3\2\2\2\u0226\u0229\5\34\17\2\u0227\u0229")
        buf.write("\5\32\16\2\u0228\u0226\3\2\2\2\u0228\u0227\3\2\2\2\u0229")
        buf.write("-\3\2\2\2\u022a\u022d\5\34\17\2\u022b\u022d\5\32\16\2")
        buf.write("\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2\u022d/\3\2\2")
        buf.write("\2\u022e\u022f\7\5\2\2\u022f\u0231\t\3\2\2\u0230\u0232")
        buf.write("\7\3\2\2\u0231\u0230\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write("\61\3\2\2\2\u0233\u0234\7\5\2\2\u0234\u0236\t\4\2\2\u0235")
        buf.write("\u0237\7\3\2\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0237\u023b\3\2\2\2\u0238\u0239\7\5\2\2\u0239\u023b\7")
        buf.write("\23\2\2\u023a\u0233\3\2\2\2\u023a\u0238\3\2\2\2\u023b")
        buf.write("\63\3\2\2\2\u023c\u023d\5\60\31\2\u023d\u023e\t\3\2\2")
        buf.write("\u023e\65\3\2\2\2\u023f\u0240\t\3\2\2\u0240\u0241\5\60")
        buf.write("\31\2\u0241\67\3\2\2\2\u0242\u0243\t\3\2\2\u0243\u0244")
        buf.write("\t\3\2\2\u0244\u0245\5F$\2\u02459\3\2\2\2\u0246\u0247")
        buf.write("\5\60\31\2\u0247\u0248\5F$\2\u0248;\3\2\2\2\u0249\u024a")
        buf.write("\7\5\2\2\u024a\u024b\7\24\2\2\u024b=\3\2\2\2\u024c\u024d")
        buf.write("\7\5\2\2\u024d\u024e\7\25\2\2\u024e?\3\2\2\2\u024f\u0250")
        buf.write("\7\5\2\2\u0250\u0251\7\26\2\2\u0251A\3\2\2\2\u0252\u0253")
        buf.write("\7\5\2\2\u0253\u0254\7\27\2\2\u0254C\3\2\2\2\u0255\u0256")
        buf.write("\7\5\2\2\u0256\u0257\7\30\2\2\u0257E\3\2\2\2\u0258\u0259")
        buf.write("\7\n\2\2\u0259G\3\2\2\2\u025a\u025e\7\5\2\2\u025b\u025d")
        buf.write("\7\3\2\2\u025c\u025b\3\2\2\2\u025d\u0260\3\2\2\2\u025e")
        buf.write("\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0261\3\2\2\2")
        buf.write("\u0260\u025e\3\2\2\2\u0261\u0271\7%\2\2\u0262\u0264\7")
        buf.write("\3\2\2\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0268\3\2\2\2\u0267")
        buf.write("\u0265\3\2\2\2\u0268\u026c\t\7\2\2\u0269\u026b\7\3\2\2")
        buf.write("\u026a\u0269\3\2\2\2\u026b\u026e\3\2\2\2\u026c\u026a\3")
        buf.write("\2\2\2\u026c\u026d\3\2\2\2\u026d\u026f\3\2\2\2\u026e\u026c")
        buf.write("\3\2\2\2\u026f\u0271\7\5\2\2\u0270\u025a\3\2\2\2\u0270")
        buf.write("\u0265\3\2\2\2\u0271I\3\2\2\2\u0272\u0274\7\3\2\2\u0273")
        buf.write("\u0272\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0275\3\2\2\2")
        buf.write("\u0275\u0277\t\2\2\2\u0276\u0278\7\3\2\2\u0277\u0276\3")
        buf.write("\2\2\2\u0277\u0278\3\2\2\2\u0278\u027a\3\2\2\2\u0279\u0273")
        buf.write("\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3\2\2\2\u027b")
        buf.write("\u027c\3\2\2\2\u027cK\3\2\2\2\u027d\u027b\3\2\2\2\u027e")
        buf.write("\u0280\7\3\2\2\u027f\u027e\3\2\2\2\u027f\u0280\3\2\2\2")
        buf.write("\u0280\u0281\3\2\2\2\u0281\u0283\t\2\2\2\u0282\u0284\7")
        buf.write("\3\2\2\u0283\u0282\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0286")
        buf.write("\3\2\2\2\u0285\u027f\3\2\2\2\u0286\u0289\3\2\2\2\u0287")
        buf.write("\u0285\3\2\2\2\u0287\u0288\3\2\2\2\u0288M\3\2\2\2\u0289")
        buf.write("\u0287\3\2\2\2\u0084OT[behjov{~\u0083\u008a\u008d\u0090")
        buf.write("\u0094\u009a\u009e\u00a4\u00ab\u00b0\u00b4\u00b9\u00bd")
        buf.write("\u00bf\u00c2\u00c4\u00c7\u00cb\u00cf\u00d4\u00d8\u00da")
        buf.write("\u00dd\u00df\u00e3\u00e7\u00ea\u00ee\u00f5\u00f9\u0100")
        buf.write("\u0107\u010b\u0111\u011c\u011f\u0123\u0127\u012a\u012d")
        buf.write("\u0131\u0134\u0137\u013a\u013d\u0140\u0143\u0147\u014a")
        buf.write("\u014d\u0150\u0153\u0156\u0159\u015d\u0160\u0163\u0166")
        buf.write("\u0169\u016c\u016f\u0173\u0176\u0179\u017c\u017f\u0182")
        buf.write("\u0185\u0189\u018c\u018f\u0192\u0195\u019e\u01a3\u01a8")
        buf.write("\u01ab\u01af\u01b2\u01b5\u01b8\u01c8\u01cc\u01d0\u01d2")
        buf.write("\u01d5\u01d8\u01dc\u01df\u01e3\u01e7\u01ec\u01f0\u01f4")
        buf.write("\u01f8\u01fc\u01fe\u0200\u0207\u020e\u0214\u021a\u021f")
        buf.write("\u0224\u0228\u022c\u0231\u0236\u023a\u025e\u0265\u026c")
        buf.write("\u0270\u0273\u0277\u027b\u027f\u0283\u0287")
        return buf.getvalue()


class NumberParser ( Parser ):

    grammarFileName = "Number.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'between'", "'to '", "'of'", "'k'", 
                     "'point'", "'dot'", "'to to '", "'amounting'", "'want'", 
                     "'wanting'", "'like'", "'liking'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WORD_NUMBER_FRACTIONS", 
                      "WORD_NUMBER_UNITS", "WORD_NUMBER_TENS", "WORD_NUMBER_HUNDREDS", 
                      "WORD_NUMBER_THOUSANDS", "WORD_NUMBER_LAKHS", "WORD_NUMBER_MILLIONS", 
                      "WORD_NUMBER_CRORES", "WORD_NUMBER_BILLIONS", "CONJUNCTION", 
                      "ART", "PUNCT", "NUMBER_UNITS", "NUMBER_TENS", "NUMBER_HUNDREDS", 
                      "NUMBER_THOUSANDS", "NUMBER_LAKHS", "NUMBER_MILLIONS", 
                      "NUMBER_CRORES", "NUMBER_BILLIONS", "WHITESPACE", 
                      "WORD", "NUMBER" ]

    RULE_numbers_utterance = 0
    RULE_discards = 1
    RULE_ranges_utterance = 2
    RULE_range_pattern = 3
    RULE_number_pattern = 4
    RULE_literal_format = 5
    RULE_billions_format = 6
    RULE_crores_format = 7
    RULE_lakhs_format = 8
    RULE_millions_format = 9
    RULE_thousands_format = 10
    RULE_hundreds_format = 11
    RULE_tens_format = 12
    RULE_units_format = 13
    RULE_fractional_format = 14
    RULE_prefix_crores = 15
    RULE_suffix_crores = 16
    RULE_prefix_lakhs = 17
    RULE_suffix_lakhs = 18
    RULE_prefix_thousands = 19
    RULE_suffix_thousands = 20
    RULE_prefix_hundreds = 21
    RULE_suffix_hundreds = 22
    RULE_spl_tens = 23
    RULE_spl_hundreds = 24
    RULE_spl_hundreds_1 = 25
    RULE_spl_hundreds_2 = 26
    RULE_spl_hundreds_3 = 27
    RULE_spl_hundreds_4 = 28
    RULE_spl_thousands = 29
    RULE_spl_lakhs = 30
    RULE_spl_millions = 31
    RULE_spl_crores = 32
    RULE_spl_billions = 33
    RULE_spl_epilogue = 34
    RULE_spl_discard = 35
    RULE_prefix = 36
    RULE_suffix = 37

    ruleNames =  [ "numbers_utterance", "discards", "ranges_utterance", 
                   "range_pattern", "number_pattern", "literal_format", 
                   "billions_format", "crores_format", "lakhs_format", "millions_format", 
                   "thousands_format", "hundreds_format", "tens_format", 
                   "units_format", "fractional_format", "prefix_crores", 
                   "suffix_crores", "prefix_lakhs", "suffix_lakhs", "prefix_thousands", 
                   "suffix_thousands", "prefix_hundreds", "suffix_hundreds", 
                   "spl_tens", "spl_hundreds", "spl_hundreds_1", "spl_hundreds_2", 
                   "spl_hundreds_3", "spl_hundreds_4", "spl_thousands", 
                   "spl_lakhs", "spl_millions", "spl_crores", "spl_billions", 
                   "spl_epilogue", "spl_discard", "prefix", "suffix" ]

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
    WORD_NUMBER_FRACTIONS=14
    WORD_NUMBER_UNITS=15
    WORD_NUMBER_TENS=16
    WORD_NUMBER_HUNDREDS=17
    WORD_NUMBER_THOUSANDS=18
    WORD_NUMBER_LAKHS=19
    WORD_NUMBER_MILLIONS=20
    WORD_NUMBER_CRORES=21
    WORD_NUMBER_BILLIONS=22
    CONJUNCTION=23
    ART=24
    PUNCT=25
    NUMBER_UNITS=26
    NUMBER_TENS=27
    NUMBER_HUNDREDS=28
    NUMBER_THOUSANDS=29
    NUMBER_LAKHS=30
    NUMBER_MILLIONS=31
    NUMBER_CRORES=32
    NUMBER_BILLIONS=33
    WHITESPACE=34
    WORD=35
    NUMBER=36

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


        def discards(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.DiscardsContext)
            else:
                return self.getTypedRuleContext(NumberParser.DiscardsContext,i)


        def number_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Number_patternContext)
            else:
                return self.getTypedRuleContext(NumberParser.Number_patternContext,i)


        def suffix(self):
            return self.getTypedRuleContext(NumberParser.SuffixContext,0)


        def spl_discard(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NumberParser.Spl_discardContext)
            else:
                return self.getTypedRuleContext(NumberParser.Spl_discardContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD)
            else:
                return self.getToken(NumberParser.WORD, i)

        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

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
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 76
                self.prefix()


            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 79
                    self.discards() 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 85
                self.number_pattern()
                self.state = 99
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==NumberParser.T__0:
                        self.state = 86
                        self.match(NumberParser.T__0)
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 92
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 96
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 93
                            self.match(NumberParser.T__0) 
                        self.state = 98
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)



                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 101
                    self.spl_discard()




            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 109
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==NumberParser.T__0:
                                self.state = 106
                                self.match(NumberParser.T__0)
                                self.state = 111
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 112
                            _la = self._input.LA(1)
                            if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 116
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt==1:
                                    self.state = 113
                                    self.match(NumberParser.T__0) 
                                self.state = 118
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)


                        else:
                            raise NoViableAltException(self)
                        self.state = 121 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        self.state = 123
                        self.number_pattern()


                    self.state = 139
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 129
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==NumberParser.T__0:
                            self.state = 126
                            self.match(NumberParser.T__0)
                            self.state = 131
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 132
                        _la = self._input.LA(1)
                        if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 133
                                self.match(NumberParser.T__0) 
                            self.state = 138
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)



                    self.state = 142
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        self.state = 141
                        self.spl_discard()

             
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 149
                    self.discards() 
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 155
                self.suffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiscardsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spl_discard(self):
            return self.getTypedRuleContext(NumberParser.Spl_discardContext,0)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.WORD)
            else:
                return self.getToken(NumberParser.WORD, i)

        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def getRuleIndex(self):
            return NumberParser.RULE_discards

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiscards" ):
                listener.enterDiscards(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiscards" ):
                listener.exitDiscards(self)




    def discards(self):

        localctx = NumberParser.DiscardsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_discards)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.spl_discard()
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==NumberParser.T__0:
                        self.state = 159
                        self.match(NumberParser.T__0)
                        self.state = 164
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 165
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 169
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 166
                            self.match(NumberParser.T__0) 
                        self.state = 171
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
             
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_ranges_utterance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 177
                self.prefix()


            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 180
                self.range_pattern()

            elif la_ == 2:
                self.state = 181
                self.number_pattern()
                self.state = 189
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 182
                        self.match(NumberParser.T__0)


                    self.state = 185
                    self.match(NumberParser.WORD)
                    self.state = 187
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        self.state = 186
                        self.match(NumberParser.T__0)




                self.state = 192
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.spl_discard()




            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 203 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 197
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==NumberParser.T__0:
                                self.state = 196
                                self.match(NumberParser.T__0)


                            self.state = 199
                            self.match(NumberParser.WORD)
                            self.state = 201
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                            if la_ == 1:
                                self.state = 200
                                self.match(NumberParser.T__0)



                        else:
                            raise NoViableAltException(self)
                        self.state = 205 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                    self.state = 221
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 207
                        self.range_pattern()
                        pass

                    elif la_ == 2:
                        self.state = 208
                        self.number_pattern()
                        self.state = 216
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                        if la_ == 1:
                            self.state = 210
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==NumberParser.T__0:
                                self.state = 209
                                self.match(NumberParser.T__0)


                            self.state = 212
                            self.match(NumberParser.WORD)
                            self.state = 214
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                            if la_ == 1:
                                self.state = 213
                                self.match(NumberParser.T__0)




                        self.state = 219
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                        if la_ == 1:
                            self.state = 218
                            self.spl_discard()


                        pass

             
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 228
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
        self.enterRule(localctx, 6, self.RULE_range_pattern)
        self._la = 0 # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 231
                    self.match(NumberParser.T__0)


                self.state = 234
                self.match(NumberParser.T__1)
                self.state = 236
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 235
                    self.match(NumberParser.T__0)


                self.state = 238
                self.number_pattern()
                self.state = 239
                self.match(NumberParser.CONJUNCTION)
                self.state = 240
                self.number_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 242
                    self.match(NumberParser.T__0)


                self.state = 245
                self.match(NumberParser.T__1)
                self.state = 247
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 246
                    self.match(NumberParser.T__0)


                self.state = 249
                self.number_pattern()
                self.state = 250
                self.match(NumberParser.T__2)
                self.state = 251
                self.number_pattern()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 253
                    self.match(NumberParser.T__0)


                self.state = 256
                self.number_pattern()
                self.state = 257
                self.match(NumberParser.T__2)
                self.state = 258
                self.number_pattern()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 260
                    self.match(NumberParser.T__0)


                self.state = 263
                self.match(NumberParser.T__3)
                self.state = 265
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 264
                    self.match(NumberParser.T__0)


                self.state = 267
                self.number_pattern()
                self.state = 268
                self.match(NumberParser.CONJUNCTION)
                self.state = 269
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

        def billions_format(self):
            return self.getTypedRuleContext(NumberParser.Billions_formatContext,0)


        def crores_format(self):
            return self.getTypedRuleContext(NumberParser.Crores_formatContext,0)


        def millions_format(self):
            return self.getTypedRuleContext(NumberParser.Millions_formatContext,0)


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


        def literal_format(self):
            return self.getTypedRuleContext(NumberParser.Literal_formatContext,0)


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
        self.enterRule(localctx, 8, self.RULE_number_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 273
                self.billions_format()
                pass

            elif la_ == 2:
                self.state = 274
                self.crores_format()
                pass

            elif la_ == 3:
                self.state = 275
                self.millions_format()
                pass

            elif la_ == 4:
                self.state = 276
                self.lakhs_format()
                pass

            elif la_ == 5:
                self.state = 277
                self.thousands_format()
                pass

            elif la_ == 6:
                self.state = 278
                self.hundreds_format()
                pass

            elif la_ == 7:
                self.state = 279
                self.tens_format()
                pass

            elif la_ == 8:
                self.state = 280
                self.units_format()
                pass

            elif la_ == 9:
                self.state = 281
                self.literal_format()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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
            return NumberParser.RULE_literal_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_format" ):
                listener.enterLiteral_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_format" ):
                listener.exitLiteral_format(self)




    def literal_format(self):

        localctx = NumberParser.Literal_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 284
                        self.match(NumberParser.T__0)


                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 288
                        self.match(NumberParser.T__0)



                else:
                    raise NoViableAltException(self)
                self.state = 293 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 295
                self.fractional_format()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Billions_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_BILLIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_BILLIONS, 0)

        def spl_billions(self):
            return self.getTypedRuleContext(NumberParser.Spl_billionsContext,0)


        def prefix_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Prefix_lakhsContext,0)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def suffix_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Suffix_lakhsContext,0)


        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


        def NUMBER_BILLIONS(self):
            return self.getToken(NumberParser.NUMBER_BILLIONS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_billions_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBillions_format" ):
                listener.enterBillions_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBillions_format" ):
                listener.exitBillions_format(self)




    def billions_format(self):

        localctx = NumberParser.Billions_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_billions_format)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_BILLIONS, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 298
                    self.prefix_lakhs()


                self.state = 303
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_BILLIONS]:
                    self.state = 301
                    self.match(NumberParser.WORD_NUMBER_BILLIONS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 302
                    self.spl_billions()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 306
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 305
                    self.match(NumberParser.CONJUNCTION)


                self.state = 309
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 308
                    self.suffix_lakhs()


                self.state = 312
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 311
                    self.match(NumberParser.CONJUNCTION)


                self.state = 315
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 314
                    self.fractional_format()


                pass
            elif token in [NumberParser.NUMBER_BILLIONS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(NumberParser.NUMBER_BILLIONS)
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


        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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
        self.enterRule(localctx, 14, self.RULE_crores_format)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_LAKHS, NumberParser.WORD_NUMBER_CRORES, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS, NumberParser.NUMBER_LAKHS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 320
                    self.prefix_crores()


                self.state = 325
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_CRORES]:
                    self.state = 323
                    self.match(NumberParser.WORD_NUMBER_CRORES)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 324
                    self.spl_crores()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 328
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 327
                    self.match(NumberParser.CONJUNCTION)


                self.state = 331
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 330
                    self.suffix_crores()


                self.state = 334
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 333
                    self.match(NumberParser.CONJUNCTION)


                self.state = 337
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
                if la_ == 1:
                    self.state = 336
                    self.fractional_format()


                pass
            elif token in [NumberParser.NUMBER_CRORES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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


        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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
        self.enterRule(localctx, 16, self.RULE_lakhs_format)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_LAKHS, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 342
                    self.prefix_lakhs()


                self.state = 347
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_LAKHS]:
                    self.state = 345
                    self.match(NumberParser.WORD_NUMBER_LAKHS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 346
                    self.spl_lakhs()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 350
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 349
                    self.match(NumberParser.CONJUNCTION)


                self.state = 353
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 352
                    self.suffix_lakhs()


                self.state = 356
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                if la_ == 1:
                    self.state = 355
                    self.match(NumberParser.CONJUNCTION)


                self.state = 359
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                if la_ == 1:
                    self.state = 358
                    self.fractional_format()


                pass
            elif token in [NumberParser.NUMBER_LAKHS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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


    class Millions_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_MILLIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_MILLIONS, 0)

        def spl_millions(self):
            return self.getTypedRuleContext(NumberParser.Spl_millionsContext,0)


        def prefix_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Prefix_lakhsContext,0)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

        def suffix_lakhs(self):
            return self.getTypedRuleContext(NumberParser.Suffix_lakhsContext,0)


        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


        def NUMBER_MILLIONS(self):
            return self.getToken(NumberParser.NUMBER_MILLIONS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_millions_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMillions_format" ):
                listener.enterMillions_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMillions_format" ):
                listener.exitMillions_format(self)




    def millions_format(self):

        localctx = NumberParser.Millions_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_millions_format)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_MILLIONS, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                if la_ == 1:
                    self.state = 364
                    self.prefix_lakhs()


                self.state = 369
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_MILLIONS]:
                    self.state = 367
                    self.match(NumberParser.WORD_NUMBER_MILLIONS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 368
                    self.spl_millions()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 372
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                if la_ == 1:
                    self.state = 371
                    self.match(NumberParser.CONJUNCTION)


                self.state = 375
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                if la_ == 1:
                    self.state = 374
                    self.suffix_lakhs()


                self.state = 378
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                if la_ == 1:
                    self.state = 377
                    self.match(NumberParser.CONJUNCTION)


                self.state = 381
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 380
                    self.fractional_format()


                pass
            elif token in [NumberParser.NUMBER_MILLIONS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(NumberParser.NUMBER_MILLIONS)
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


        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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


        def EOF(self):
            return self.getToken(NumberParser.EOF, 0)

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
        self.enterRule(localctx, 20, self.RULE_thousands_format)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                if la_ == 1:
                    self.state = 386
                    self.prefix_thousands()


                self.state = 391
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_THOUSANDS]:
                    self.state = 389
                    self.match(NumberParser.WORD_NUMBER_THOUSANDS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 390
                    self.spl_thousands()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 394
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
                if la_ == 1:
                    self.state = 393
                    self.match(NumberParser.CONJUNCTION)


                self.state = 397
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
                if la_ == 1:
                    self.state = 396
                    self.suffix_thousands()


                self.state = 400
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
                if la_ == 1:
                    self.state = 399
                    self.match(NumberParser.CONJUNCTION)


                self.state = 403
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
                if la_ == 1:
                    self.state = 402
                    self.fractional_format()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(NumberParser.NUMBER_THOUSANDS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 407
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
                self.match(NumberParser.NUMBER_THOUSANDS)
                self.state = 412
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                if la_ == 1:
                    self.state = 409
                    self.hundreds_format()
                    pass

                elif la_ == 2:
                    self.state = 410
                    self.tens_format()
                    pass

                elif la_ == 3:
                    self.state = 411
                    self.units_format()
                    pass


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 414
                self.match(NumberParser.NUMBER_THOUSANDS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 415
                self.prefix_thousands()

                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 416
                    self.match(NumberParser.T__0)


                self.state = 419
                self.match(NumberParser.T__4)
                self.state = 420
                _la = self._input.LA(1)
                if not(_la==NumberParser.EOF or _la==NumberParser.T__0):
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


        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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
        self.enterRule(localctx, 22, self.RULE_hundreds_format)
        self._la = 0 # Token type
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS))) != 0):
                    self.state = 424
                    self.prefix_hundreds()


                self.state = 427
                self.match(NumberParser.WORD_NUMBER_HUNDREDS)
                self.state = 429
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
                if la_ == 1:
                    self.state = 428
                    self.match(NumberParser.CONJUNCTION)


                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS))) != 0):
                    self.state = 431
                    self.suffix_hundreds()


                self.state = 435
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
                if la_ == 1:
                    self.state = 434
                    self.match(NumberParser.CONJUNCTION)


                self.state = 438
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
                if la_ == 1:
                    self.state = 437
                    self.fractional_format()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.spl_hundreds()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.spl_hundreds_1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 442
                self.spl_hundreds_2()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 443
                self.spl_hundreds_3()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 444
                self.spl_hundreds_4()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 445
                self.match(NumberParser.NUMBER_HUNDREDS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 446
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 447
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 448
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 449
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 451
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 452
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 453
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
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

        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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
        self.enterRule(localctx, 24, self.RULE_tens_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_TENS]:
                self.state = 456
                self.match(NumberParser.WORD_NUMBER_TENS)
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 457
                    self.units_format()


                pass
            elif token in [NumberParser.NUMBER_TENS]:
                self.state = 460
                self.match(NumberParser.NUMBER_TENS)
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 461
                    self.units_format()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.state = 466
                self.match(NumberParser.CONJUNCTION)


            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 469
                self.fractional_format()


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

        def fractional_format(self):
            return self.getTypedRuleContext(NumberParser.Fractional_formatContext,0)


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
        self.enterRule(localctx, 26, self.RULE_units_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 473
                self.match(NumberParser.CONJUNCTION)


            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                self.state = 476
                self.fractional_format()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fractional_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_FRACTIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_FRACTIONS, 0)

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

        def units_format(self):
            return self.getTypedRuleContext(NumberParser.Units_formatContext,0)


        def getRuleIndex(self):
            return NumberParser.RULE_fractional_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFractional_format" ):
                listener.enterFractional_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFractional_format" ):
                listener.exitFractional_format(self)




    def fractional_format(self):

        localctx = NumberParser.Fractional_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fractional_format)
        self._la = 0 # Token type
        try:
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(NumberParser.WORD_NUMBER_FRACTIONS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 480
                    self.match(NumberParser.T__0)


                self.state = 483
                _la = self._input.LA(1)
                if not(_la==NumberParser.T__5 or _la==NumberParser.T__6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 485
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
                if la_ == 1:
                    self.state = 484
                    self.match(NumberParser.T__0)


                self.state = 490
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 487
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 492
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 493
                    self.match(NumberParser.T__0)


                self.state = 496
                _la = self._input.LA(1)
                if not(_la==NumberParser.T__5 or _la==NumberParser.T__6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 497
                    self.match(NumberParser.T__0)


                self.state = 508
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_TENS]:
                    self.state = 500
                    self.match(NumberParser.WORD_NUMBER_TENS)
                    self.state = 502
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                        self.state = 501
                        self.units_format()


                    pass
                elif token in [NumberParser.NUMBER_TENS]:
                    self.state = 504
                    self.match(NumberParser.NUMBER_TENS)
                    self.state = 506
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                        self.state = 505
                        self.units_format()


                    pass
                else:
                    raise NoViableAltException(self)

                pass


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
        self.enterRule(localctx, 30, self.RULE_prefix_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                self.state = 512
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 513
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 514
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 515
                self.thousands_format()
                pass

            elif la_ == 5:
                self.state = 516
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
        self.enterRule(localctx, 32, self.RULE_suffix_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 519
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 520
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 521
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 522
                self.thousands_format()
                pass

            elif la_ == 5:
                self.state = 523
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
        self.enterRule(localctx, 34, self.RULE_prefix_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.state = 526
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 527
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 528
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 529
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
        self.enterRule(localctx, 36, self.RULE_suffix_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.state = 532
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 533
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 534
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 535
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
        self.enterRule(localctx, 38, self.RULE_prefix_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 538
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 539
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 540
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
        self.enterRule(localctx, 40, self.RULE_suffix_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.state = 543
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 544
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 545
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
        self.enterRule(localctx, 42, self.RULE_prefix_hundreds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_UNITS, NumberParser.NUMBER_UNITS]:
                self.state = 548
                self.units_format()
                pass
            elif token in [NumberParser.WORD_NUMBER_TENS, NumberParser.NUMBER_TENS]:
                self.state = 549
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
        self.enterRule(localctx, 44, self.RULE_suffix_hundreds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_UNITS, NumberParser.NUMBER_UNITS]:
                self.state = 552
                self.units_format()
                pass
            elif token in [NumberParser.WORD_NUMBER_TENS, NumberParser.NUMBER_TENS]:
                self.state = 553
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
        self.enterRule(localctx, 46, self.RULE_spl_tens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(NumberParser.T__2)
            self.state = 557
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
            if la_ == 1:
                self.state = 558
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
        self.enterRule(localctx, 48, self.RULE_spl_hundreds)
        self._la = 0 # Token type
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.match(NumberParser.T__2)
                self.state = 562
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 564
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
                if la_ == 1:
                    self.state = 563
                    self.match(NumberParser.T__0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(NumberParser.T__2)
                self.state = 567
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
        self.enterRule(localctx, 50, self.RULE_spl_hundreds_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.spl_tens()
            self.state = 571
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
        self.enterRule(localctx, 52, self.RULE_spl_hundreds_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 574
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
        self.enterRule(localctx, 54, self.RULE_spl_hundreds_3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 577
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 578
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
        self.enterRule(localctx, 56, self.RULE_spl_hundreds_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.spl_tens()
            self.state = 581
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
        self.enterRule(localctx, 58, self.RULE_spl_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(NumberParser.T__2)
            self.state = 584
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
        self.enterRule(localctx, 60, self.RULE_spl_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(NumberParser.T__2)
            self.state = 587
            self.match(NumberParser.WORD_NUMBER_LAKHS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_millionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_MILLIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_MILLIONS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_millions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_millions" ):
                listener.enterSpl_millions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_millions" ):
                listener.exitSpl_millions(self)




    def spl_millions(self):

        localctx = NumberParser.Spl_millionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_spl_millions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(NumberParser.T__2)
            self.state = 590
            self.match(NumberParser.WORD_NUMBER_MILLIONS)
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
        self.enterRule(localctx, 64, self.RULE_spl_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(NumberParser.T__2)
            self.state = 593
            self.match(NumberParser.WORD_NUMBER_CRORES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spl_billionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_NUMBER_BILLIONS(self):
            return self.getToken(NumberParser.WORD_NUMBER_BILLIONS, 0)

        def getRuleIndex(self):
            return NumberParser.RULE_spl_billions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpl_billions" ):
                listener.enterSpl_billions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpl_billions" ):
                listener.exitSpl_billions(self)




    def spl_billions(self):

        localctx = NumberParser.Spl_billionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_spl_billions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(NumberParser.T__2)
            self.state = 596
            self.match(NumberParser.WORD_NUMBER_BILLIONS)
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
        self.enterRule(localctx, 68, self.RULE_spl_epilogue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(NumberParser.T__7)
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
        self.enterRule(localctx, 70, self.RULE_spl_discard)
        self._la = 0 # Token type
        try:
            self.state = 622
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.match(NumberParser.T__2)
                self.state = 604
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NumberParser.T__0:
                    self.state = 601
                    self.match(NumberParser.T__0)
                    self.state = 606
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 607
                self.match(NumberParser.WORD)
                pass
            elif token in [NumberParser.T__0, NumberParser.T__8, NumberParser.T__9, NumberParser.T__10, NumberParser.T__11, NumberParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NumberParser.T__0:
                    self.state = 608
                    self.match(NumberParser.T__0)
                    self.state = 613
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 614
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.T__8) | (1 << NumberParser.T__9) | (1 << NumberParser.T__10) | (1 << NumberParser.T__11) | (1 << NumberParser.T__12))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NumberParser.T__0:
                    self.state = 615
                    self.match(NumberParser.T__0)
                    self.state = 620
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 621
                self.match(NumberParser.T__2)
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

        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

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
        self.enterRule(localctx, 72, self.RULE_prefix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 625
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 624
                        self.match(NumberParser.T__0)


                    self.state = 627
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 629
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
                    if la_ == 1:
                        self.state = 628
                        self.match(NumberParser.T__0)

             
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

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

        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(NumberParser.CONJUNCTION)
            else:
                return self.getToken(NumberParser.CONJUNCTION, i)

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
        self.enterRule(localctx, 74, self.RULE_suffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.T__0) | (1 << NumberParser.CONJUNCTION) | (1 << NumberParser.WORD))) != 0):
                self.state = 637
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 636
                    self.match(NumberParser.T__0)


                self.state = 639
                _la = self._input.LA(1)
                if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 641
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
                if la_ == 1:
                    self.state = 640
                    self.match(NumberParser.T__0)


                self.state = 647
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





