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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u0213\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\5\2F\n\2\3\2\7\2I\n")
        buf.write("\2\f\2\16\2L\13\2\3\2\3\2\7\2P\n\2\f\2\16\2S\13\2\3\2")
        buf.write("\3\2\7\2W\n\2\f\2\16\2Z\13\2\5\2\\\n\2\3\2\5\2_\n\2\5")
        buf.write("\2a\n\2\3\2\7\2d\n\2\f\2\16\2g\13\2\3\2\3\2\7\2k\n\2\f")
        buf.write("\2\16\2n\13\2\6\2p\n\2\r\2\16\2q\3\2\5\2u\n\2\3\2\7\2")
        buf.write("x\n\2\f\2\16\2{\13\2\3\2\3\2\7\2\177\n\2\f\2\16\2\u0082")
        buf.write("\13\2\5\2\u0084\n\2\3\2\5\2\u0087\n\2\7\2\u0089\n\2\f")
        buf.write("\2\16\2\u008c\13\2\3\2\7\2\u008f\n\2\f\2\16\2\u0092\13")
        buf.write("\2\3\2\5\2\u0095\n\2\3\3\3\3\7\3\u0099\n\3\f\3\16\3\u009c")
        buf.write("\13\3\3\3\3\3\7\3\u00a0\n\3\f\3\16\3\u00a3\13\3\7\3\u00a5")
        buf.write("\n\3\f\3\16\3\u00a8\13\3\3\4\5\4\u00ab\n\4\3\4\3\4\3\4")
        buf.write("\5\4\u00b0\n\4\3\4\3\4\5\4\u00b4\n\4\5\4\u00b6\n\4\3\4")
        buf.write("\5\4\u00b9\n\4\5\4\u00bb\n\4\3\4\5\4\u00be\n\4\3\4\3\4")
        buf.write("\5\4\u00c2\n\4\6\4\u00c4\n\4\r\4\16\4\u00c5\3\4\3\4\3")
        buf.write("\4\5\4\u00cb\n\4\3\4\3\4\5\4\u00cf\n\4\5\4\u00d1\n\4\3")
        buf.write("\4\5\4\u00d4\n\4\5\4\u00d6\n\4\7\4\u00d8\n\4\f\4\16\4")
        buf.write("\u00db\13\4\3\4\5\4\u00de\n\4\3\5\5\5\u00e1\n\5\3\5\3")
        buf.write("\5\5\5\u00e5\n\5\3\5\3\5\3\5\3\5\3\5\5\5\u00ec\n\5\3\5")
        buf.write("\3\5\5\5\u00f0\n\5\3\5\3\5\3\5\3\5\3\5\5\5\u00f7\n\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u00fe\n\5\3\5\3\5\5\5\u0102\n\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5\u0108\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u0111\n\6\3\7\5\7\u0114\n\7\3\7\3\7\5\7\u0118")
        buf.write("\n\7\6\7\u011a\n\7\r\7\16\7\u011b\3\b\5\b\u011f\n\b\3")
        buf.write("\b\3\b\5\b\u0123\n\b\3\b\5\b\u0126\n\b\3\b\5\b\u0129\n")
        buf.write("\b\3\b\5\b\u012c\n\b\3\b\5\b\u012f\n\b\3\b\5\b\u0132\n")
        buf.write("\b\3\t\5\t\u0135\n\t\3\t\3\t\5\t\u0139\n\t\3\t\5\t\u013c")
        buf.write("\n\t\3\t\5\t\u013f\n\t\3\t\5\t\u0142\n\t\3\t\5\t\u0145")
        buf.write("\n\t\3\t\5\t\u0148\n\t\3\n\5\n\u014b\n\n\3\n\3\n\5\n\u014f")
        buf.write("\n\n\3\n\5\n\u0152\n\n\3\n\5\n\u0155\n\n\3\n\5\n\u0158")
        buf.write("\n\n\3\n\5\n\u015b\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u0164\n\n\3\n\5\n\u0167\n\n\3\13\5\13\u016a\n\13\3\13")
        buf.write("\3\13\5\13\u016e\n\13\3\13\5\13\u0171\n\13\3\13\5\13\u0174")
        buf.write("\n\13\3\13\5\13\u0177\n\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0187")
        buf.write("\n\13\3\f\3\f\5\f\u018b\n\f\3\f\3\f\5\f\u018f\n\f\5\f")
        buf.write("\u0191\n\f\3\f\5\f\u0194\n\f\3\f\5\f\u0197\n\f\3\r\3\r")
        buf.write("\5\r\u019b\n\r\3\r\5\r\u019e\n\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u01a5\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u01ac")
        buf.write("\n\17\3\20\3\20\3\20\3\20\5\20\u01b2\n\20\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u01b8\n\21\3\22\3\22\3\22\5\22\u01bd\n\22")
        buf.write("\3\23\3\23\3\23\5\23\u01c2\n\23\3\24\3\24\5\24\u01c6\n")
        buf.write("\24\3\25\3\25\5\25\u01ca\n\25\3\26\3\26\3\26\5\26\u01cf")
        buf.write("\n\26\3\27\3\27\3\27\5\27\u01d4\n\27\3\27\3\27\5\27\u01d8")
        buf.write("\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \7 \u01f4\n \f \16 \u01f7\13 \3 ")
        buf.write("\3 \3!\5!\u01fc\n!\3!\3!\5!\u0200\n!\7!\u0202\n!\f!\16")
        buf.write("!\u0205\13!\3\"\5\"\u0208\n\"\3\"\3\"\5\"\u020c\n\"\7")
        buf.write("\"\u020e\n\"\f\"\16\"\u0211\13\"\3\"\2\2#\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("B\2\5\4\2\17\17\31\31\4\2\t\t\22\22\4\2\n\n\23\23\2\u0277")
        buf.write("\2E\3\2\2\2\4\u0096\3\2\2\2\6\u00aa\3\2\2\2\b\u0107\3")
        buf.write("\2\2\2\n\u0110\3\2\2\2\f\u0119\3\2\2\2\16\u0131\3\2\2")
        buf.write("\2\20\u0147\3\2\2\2\22\u0166\3\2\2\2\24\u0186\3\2\2\2")
        buf.write("\26\u0190\3\2\2\2\30\u0198\3\2\2\2\32\u01a4\3\2\2\2\34")
        buf.write("\u01ab\3\2\2\2\36\u01b1\3\2\2\2 \u01b7\3\2\2\2\"\u01bc")
        buf.write("\3\2\2\2$\u01c1\3\2\2\2&\u01c5\3\2\2\2(\u01c9\3\2\2\2")
        buf.write("*\u01cb\3\2\2\2,\u01d7\3\2\2\2.\u01d9\3\2\2\2\60\u01dc")
        buf.write("\3\2\2\2\62\u01df\3\2\2\2\64\u01e3\3\2\2\2\66\u01e6\3")
        buf.write("\2\2\28\u01e9\3\2\2\2:\u01ec\3\2\2\2<\u01ef\3\2\2\2>\u01f1")
        buf.write("\3\2\2\2@\u0203\3\2\2\2B\u020f\3\2\2\2DF\5@!\2ED\3\2\2")
        buf.write("\2EF\3\2\2\2FJ\3\2\2\2GI\5\4\3\2HG\3\2\2\2IL\3\2\2\2J")
        buf.write("H\3\2\2\2JK\3\2\2\2K`\3\2\2\2LJ\3\2\2\2M[\5\n\6\2NP\7")
        buf.write("\3\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2")
        buf.write("\2SQ\3\2\2\2TX\t\2\2\2UW\7\3\2\2VU\3\2\2\2WZ\3\2\2\2X")
        buf.write("V\3\2\2\2XY\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2[Q\3\2\2\2[\\")
        buf.write("\3\2\2\2\\^\3\2\2\2]_\5> \2^]\3\2\2\2^_\3\2\2\2_a\3\2")
        buf.write("\2\2`M\3\2\2\2`a\3\2\2\2a\u008a\3\2\2\2bd\7\3\2\2cb\3")
        buf.write("\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2")
        buf.write("\2hl\t\2\2\2ik\7\3\2\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2l")
        buf.write("m\3\2\2\2mp\3\2\2\2nl\3\2\2\2oe\3\2\2\2pq\3\2\2\2qo\3")
        buf.write("\2\2\2qr\3\2\2\2rt\3\2\2\2su\5\n\6\2ts\3\2\2\2tu\3\2\2")
        buf.write("\2u\u0083\3\2\2\2vx\7\3\2\2wv\3\2\2\2x{\3\2\2\2yw\3\2")
        buf.write("\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2\2\2|\u0080\t\2\2\2}\177")
        buf.write("\7\3\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2")
        buf.write("\u0083y\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2")
        buf.write("\2\u0085\u0087\5> \2\u0086\u0085\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\u0089\3\2\2\2\u0088o\3\2\2\2\u0089\u008c")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u0090\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008f\5\4\3\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0090\u0091\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0093\u0095\5B\"\2\u0094\u0093\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\3\3\2\2\2\u0096\u00a6\5> \2\u0097")
        buf.write("\u0099\7\3\2\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u00a1\t\2\2\2\u009e\u00a0")
        buf.write("\7\3\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a5\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u009a\3\2\2\2\u00a5\u00a8\3")
        buf.write("\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\5")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\5@!\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ba\3\2\2\2\u00ac")
        buf.write("\u00bb\5\b\5\2\u00ad\u00b5\5\n\6\2\u00ae\u00b0\7\3\2\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b3\7\31\2\2\u00b2\u00b4\7\3\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2")
        buf.write("\u00b5\u00af\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3")
        buf.write("\2\2\2\u00b7\u00b9\5> \2\u00b8\u00b7\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00ac\3\2\2\2\u00ba")
        buf.write("\u00ad\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00d9\3\2\2\2")
        buf.write("\u00bc\u00be\7\3\2\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\7\31\2\2\u00c0")
        buf.write("\u00c2\7\3\2\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c4\3\2\2\2\u00c3\u00bd\3\2\2\2\u00c4\u00c5\3")
        buf.write("\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00d5")
        buf.write("\3\2\2\2\u00c7\u00d6\5\b\5\2\u00c8\u00d0\5\n\6\2\u00c9")
        buf.write("\u00cb\7\3\2\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00ce\7\31\2\2\u00cd\u00cf")
        buf.write("\7\3\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00ca\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d3\3\2\2\2\u00d2\u00d4\5> \2\u00d3\u00d2\3\2")
        buf.write("\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00c7")
        buf.write("\3\2\2\2\u00d5\u00c8\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00c3\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00de\5B\"\2\u00dd\u00dc\3\2\2\2\u00dd\u00de")
        buf.write("\3\2\2\2\u00de\7\3\2\2\2\u00df\u00e1\7\3\2\2\u00e0\u00df")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e4\7\4\2\2\u00e3\u00e5\7\3\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\5")
        buf.write("\n\6\2\u00e7\u00e8\7\17\2\2\u00e8\u00e9\5\n\6\2\u00e9")
        buf.write("\u0108\3\2\2\2\u00ea\u00ec\7\3\2\2\u00eb\u00ea\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\7")
        buf.write("\4\2\2\u00ee\u00f0\7\3\2\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\5\n\6\2\u00f2")
        buf.write("\u00f3\7\5\2\2\u00f3\u00f4\5\n\6\2\u00f4\u0108\3\2\2\2")
        buf.write("\u00f5\u00f7\7\3\2\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\5\n\6\2\u00f9\u00fa")
        buf.write("\7\5\2\2\u00fa\u00fb\5\n\6\2\u00fb\u0108\3\2\2\2\u00fc")
        buf.write("\u00fe\7\3\2\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u00ff\3\2\2\2\u00ff\u0101\7\6\2\2\u0100\u0102\7")
        buf.write("\3\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103\u0104\5\n\6\2\u0104\u0105\7\17\2\2\u0105")
        buf.write("\u0106\5\n\6\2\u0106\u0108\3\2\2\2\u0107\u00e0\3\2\2\2")
        buf.write("\u0107\u00eb\3\2\2\2\u0107\u00f6\3\2\2\2\u0107\u00fd\3")
        buf.write("\2\2\2\u0108\t\3\2\2\2\u0109\u0111\5\16\b\2\u010a\u0111")
        buf.write("\5\20\t\2\u010b\u0111\5\22\n\2\u010c\u0111\5\24\13\2\u010d")
        buf.write("\u0111\5\26\f\2\u010e\u0111\5\30\r\2\u010f\u0111\5\f\7")
        buf.write("\2\u0110\u0109\3\2\2\2\u0110\u010a\3\2\2\2\u0110\u010b")
        buf.write("\3\2\2\2\u0110\u010c\3\2\2\2\u0110\u010d\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\13\3\2\2\2\u0112")
        buf.write("\u0114\7\3\2\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115\u0117\t\3\2\2\u0116\u0118\7")
        buf.write("\3\2\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a")
        buf.write("\3\2\2\2\u0119\u0113\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\r\3\2\2\2\u011d")
        buf.write("\u011f\5\32\16\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2")
        buf.write("\2\u011f\u0122\3\2\2\2\u0120\u0123\7\16\2\2\u0121\u0123")
        buf.write("\5:\36\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0125\3\2\2\2\u0124\u0126\7\17\2\2\u0125\u0124\3\2\2")
        buf.write("\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0129")
        buf.write("\5\34\17\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012b\3\2\2\2\u012a\u012c\7\17\2\2\u012b\u012a\3\2\2")
        buf.write("\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012f")
        buf.write("\7\b\2\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u0132\7\27\2\2\u0131\u011e\3\2\2")
        buf.write("\2\u0131\u0130\3\2\2\2\u0132\17\3\2\2\2\u0133\u0135\5")
        buf.write("\36\20\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0138\3\2\2\2\u0136\u0139\7\r\2\2\u0137\u0139\58\35\2")
        buf.write("\u0138\u0136\3\2\2\2\u0138\u0137\3\2\2\2\u0139\u013b\3")
        buf.write("\2\2\2\u013a\u013c\7\17\2\2\u013b\u013a\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013f\5 \21\2")
        buf.write("\u013e\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3")
        buf.write("\2\2\2\u0140\u0142\7\17\2\2\u0141\u0140\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0145\7\b\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0148\3")
        buf.write("\2\2\2\u0146\u0148\7\26\2\2\u0147\u0134\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148\21\3\2\2\2\u0149\u014b\5\"\22\2\u014a")
        buf.write("\u0149\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014e\3\2\2\2")
        buf.write("\u014c\u014f\7\f\2\2\u014d\u014f\5\66\34\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0151\3\2\2\2\u0150")
        buf.write("\u0152\7\17\2\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2")
        buf.write("\2\u0152\u0154\3\2\2\2\u0153\u0155\5$\23\2\u0154\u0153")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0158\7\17\2\2\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2")
        buf.write("\2\u0158\u015a\3\2\2\2\u0159\u015b\7\b\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0167\3\2\2\2\u015c")
        buf.write("\u0167\7\25\2\2\u015d\u015e\t\4\2\2\u015e\u0167\t\4\2")
        buf.write("\2\u015f\u0163\7\25\2\2\u0160\u0164\5\24\13\2\u0161\u0164")
        buf.write("\5\26\f\2\u0162\u0164\5\30\r\2\u0163\u0160\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0167\7\25\2\2\u0166\u014a\3\2\2\2\u0166\u015c")
        buf.write("\3\2\2\2\u0166\u015d\3\2\2\2\u0166\u015f\3\2\2\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\23\3\2\2\2\u0168\u016a\5&\24\2\u0169")
        buf.write("\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016d\7\13\2\2\u016c\u016e\7\17\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f")
        buf.write("\u0171\5(\25\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0173\3\2\2\2\u0172\u0174\7\17\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175")
        buf.write("\u0177\7\b\2\2\u0176\u0175\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u0187\3\2\2\2\u0178\u0187\5,\27\2\u0179\u0187\5")
        buf.write(".\30\2\u017a\u0187\5\60\31\2\u017b\u0187\5\62\32\2\u017c")
        buf.write("\u0187\5\64\33\2\u017d\u0187\7\24\2\2\u017e\u017f\t\3")
        buf.write("\2\2\u017f\u0180\t\3\2\2\u0180\u0187\t\3\2\2\u0181\u0182")
        buf.write("\t\3\2\2\u0182\u0187\t\4\2\2\u0183\u0184\t\3\2\2\u0184")
        buf.write("\u0185\t\4\2\2\u0185\u0187\t\3\2\2\u0186\u0169\3\2\2\2")
        buf.write("\u0186\u0178\3\2\2\2\u0186\u0179\3\2\2\2\u0186\u017a\3")
        buf.write("\2\2\2\u0186\u017b\3\2\2\2\u0186\u017c\3\2\2\2\u0186\u017d")
        buf.write("\3\2\2\2\u0186\u017e\3\2\2\2\u0186\u0181\3\2\2\2\u0186")
        buf.write("\u0183\3\2\2\2\u0187\25\3\2\2\2\u0188\u018a\7\n\2\2\u0189")
        buf.write("\u018b\5\30\r\2\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2")
        buf.write("\2\u018b\u0191\3\2\2\2\u018c\u018e\7\23\2\2\u018d\u018f")
        buf.write("\5\30\r\2\u018e\u018d\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u0191\3\2\2\2\u0190\u0188\3\2\2\2\u0190\u018c\3\2\2\2")
        buf.write("\u0191\u0193\3\2\2\2\u0192\u0194\7\17\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195")
        buf.write("\u0197\7\b\2\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\27\3\2\2\2\u0198\u019a\t\3\2\2\u0199\u019b\7\17")
        buf.write("\2\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u019e\7\b\2\2\u019d\u019c\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\31\3\2\2\2\u019f\u01a5\5\30\r\2\u01a0")
        buf.write("\u01a5\5\26\f\2\u01a1\u01a5\5\24\13\2\u01a2\u01a5\5\22")
        buf.write("\n\2\u01a3\u01a5\5\20\t\2\u01a4\u019f\3\2\2\2\u01a4\u01a0")
        buf.write("\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\33\3\2\2\2\u01a6\u01ac\5\30\r\2\u01a7")
        buf.write("\u01ac\5\26\f\2\u01a8\u01ac\5\24\13\2\u01a9\u01ac\5\22")
        buf.write("\n\2\u01aa\u01ac\5\20\t\2\u01ab\u01a6\3\2\2\2\u01ab\u01a7")
        buf.write("\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\35\3\2\2\2\u01ad\u01b2\5\30\r\2\u01ae")
        buf.write("\u01b2\5\26\f\2\u01af\u01b2\5\24\13\2\u01b0\u01b2\5\22")
        buf.write("\n\2\u01b1\u01ad\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2\37\3\2\2\2\u01b3\u01b8")
        buf.write("\5\30\r\2\u01b4\u01b8\5\26\f\2\u01b5\u01b8\5\24\13\2\u01b6")
        buf.write("\u01b8\5\22\n\2\u01b7\u01b3\3\2\2\2\u01b7\u01b4\3\2\2")
        buf.write("\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8!\3\2")
        buf.write("\2\2\u01b9\u01bd\5\30\r\2\u01ba\u01bd\5\26\f\2\u01bb\u01bd")
        buf.write("\5\24\13\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd#\3\2\2\2\u01be\u01c2\5\30\r\2\u01bf")
        buf.write("\u01c2\5\26\f\2\u01c0\u01c2\5\24\13\2\u01c1\u01be\3\2")
        buf.write("\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2%\3")
        buf.write("\2\2\2\u01c3\u01c6\5\30\r\2\u01c4\u01c6\5\26\f\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\'\3\2\2\2\u01c7")
        buf.write("\u01ca\5\30\r\2\u01c8\u01ca\5\26\f\2\u01c9\u01c7\3\2\2")
        buf.write("\2\u01c9\u01c8\3\2\2\2\u01ca)\3\2\2\2\u01cb\u01cc\7\5")
        buf.write("\2\2\u01cc\u01ce\t\3\2\2\u01cd\u01cf\7\3\2\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf+\3\2\2\2\u01d0\u01d1")
        buf.write("\7\5\2\2\u01d1\u01d3\t\4\2\2\u01d2\u01d4\7\3\2\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d8\3\2\2\2")
        buf.write("\u01d5\u01d6\7\5\2\2\u01d6\u01d8\7\13\2\2\u01d7\u01d0")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8-\3\2\2\2\u01d9\u01da")
        buf.write("\5*\26\2\u01da\u01db\t\3\2\2\u01db/\3\2\2\2\u01dc\u01dd")
        buf.write("\t\3\2\2\u01dd\u01de\5*\26\2\u01de\61\3\2\2\2\u01df\u01e0")
        buf.write("\t\3\2\2\u01e0\u01e1\t\3\2\2\u01e1\u01e2\5<\37\2\u01e2")
        buf.write("\63\3\2\2\2\u01e3\u01e4\5*\26\2\u01e4\u01e5\5<\37\2\u01e5")
        buf.write("\65\3\2\2\2\u01e6\u01e7\7\5\2\2\u01e7\u01e8\7\f\2\2\u01e8")
        buf.write("\67\3\2\2\2\u01e9\u01ea\7\5\2\2\u01ea\u01eb\7\r\2\2\u01eb")
        buf.write("9\3\2\2\2\u01ec\u01ed\7\5\2\2\u01ed\u01ee\7\16\2\2\u01ee")
        buf.write(";\3\2\2\2\u01ef\u01f0\7\7\2\2\u01f0=\3\2\2\2\u01f1\u01f5")
        buf.write("\7\5\2\2\u01f2\u01f4\7\3\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f9\7")
        buf.write("\31\2\2\u01f9?\3\2\2\2\u01fa\u01fc\7\3\2\2\u01fb\u01fa")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u01ff\t\2\2\2\u01fe\u0200\7\3\2\2\u01ff\u01fe\3\2\2\2")
        buf.write("\u01ff\u0200\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u01fb\3")
        buf.write("\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204A\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0208")
        buf.write("\7\3\2\2\u0207\u0206\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u020b\t\2\2\2\u020a\u020c\7\3\2\2")
        buf.write("\u020b\u020a\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020e\3")
        buf.write("\2\2\2\u020d\u0207\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210C\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2hEJQX[^`elqty\u0080\u0083\u0086\u008a\u0090\u0094")
        buf.write("\u009a\u00a1\u00a6\u00aa\u00af\u00b3\u00b5\u00b8\u00ba")
        buf.write("\u00bd\u00c1\u00c5\u00ca\u00ce\u00d0\u00d3\u00d5\u00d9")
        buf.write("\u00dd\u00e0\u00e4\u00eb\u00ef\u00f6\u00fd\u0101\u0107")
        buf.write("\u0110\u0113\u0117\u011b\u011e\u0122\u0125\u0128\u012b")
        buf.write("\u012e\u0131\u0134\u0138\u013b\u013e\u0141\u0144\u0147")
        buf.write("\u014a\u014e\u0151\u0154\u0157\u015a\u0163\u0166\u0169")
        buf.write("\u016d\u0170\u0173\u0176\u0186\u018a\u018e\u0190\u0193")
        buf.write("\u0196\u019a\u019d\u01a4\u01ab\u01b1\u01b7\u01bc\u01c1")
        buf.write("\u01c5\u01c9\u01ce\u01d3\u01d7\u01f5\u01fb\u01ff\u0203")
        buf.write("\u0207\u020b\u020f")
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
                      "CONJUNCTION", "ART", "PUNCT", "NUMBER_UNITS", "NUMBER_TENS", 
                      "NUMBER_HUNDREDS", "NUMBER_THOUSANDS", "NUMBER_LAKHS", 
                      "NUMBER_CRORES", "WHITESPACE", "WORD", "NUMBER" ]

    RULE_numbers_utterance = 0
    RULE_discards = 1
    RULE_ranges_utterance = 2
    RULE_range_pattern = 3
    RULE_number_pattern = 4
    RULE_literal_format = 5
    RULE_crores_format = 6
    RULE_lakhs_format = 7
    RULE_thousands_format = 8
    RULE_hundreds_format = 9
    RULE_tens_format = 10
    RULE_units_format = 11
    RULE_prefix_crores = 12
    RULE_suffix_crores = 13
    RULE_prefix_lakhs = 14
    RULE_suffix_lakhs = 15
    RULE_prefix_thousands = 16
    RULE_suffix_thousands = 17
    RULE_prefix_hundreds = 18
    RULE_suffix_hundreds = 19
    RULE_spl_tens = 20
    RULE_spl_hundreds = 21
    RULE_spl_hundreds_1 = 22
    RULE_spl_hundreds_2 = 23
    RULE_spl_hundreds_3 = 24
    RULE_spl_hundreds_4 = 25
    RULE_spl_thousands = 26
    RULE_spl_lakhs = 27
    RULE_spl_crores = 28
    RULE_spl_epilogue = 29
    RULE_spl_discard = 30
    RULE_prefix = 31
    RULE_suffix = 32

    ruleNames =  [ "numbers_utterance", "discards", "ranges_utterance", 
                   "range_pattern", "number_pattern", "literal_format", 
                   "crores_format", "lakhs_format", "thousands_format", 
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
    PUNCT=15
    NUMBER_UNITS=16
    NUMBER_TENS=17
    NUMBER_HUNDREDS=18
    NUMBER_THOUSANDS=19
    NUMBER_LAKHS=20
    NUMBER_CRORES=21
    WHITESPACE=22
    WORD=23
    NUMBER=24

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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 66
                self.prefix()


            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.discards() 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 75
                self.number_pattern()
                self.state = 89
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==NumberParser.T__0:
                        self.state = 76
                        self.match(NumberParser.T__0)
                        self.state = 81
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 82
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 86
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 83
                            self.match(NumberParser.T__0) 
                        self.state = 88
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)



                self.state = 92
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 91
                    self.spl_discard()




            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 99
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==NumberParser.T__0:
                                self.state = 96
                                self.match(NumberParser.T__0)
                                self.state = 101
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 102
                            _la = self._input.LA(1)
                            if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 106
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt==1:
                                    self.state = 103
                                    self.match(NumberParser.T__0) 
                                self.state = 108
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)


                        else:
                            raise NoViableAltException(self)
                        self.state = 111 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        self.state = 113
                        self.number_pattern()


                    self.state = 129
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 119
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==NumberParser.T__0:
                            self.state = 116
                            self.match(NumberParser.T__0)
                            self.state = 121
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 122
                        _la = self._input.LA(1)
                        if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 123
                                self.match(NumberParser.T__0) 
                            self.state = 128
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)



                    self.state = 132
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        self.state = 131
                        self.spl_discard()

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NumberParser.T__2:
                self.state = 139
                self.discards()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 145
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
            self.state = 148
            self.spl_discard()
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==NumberParser.T__0:
                        self.state = 149
                        self.match(NumberParser.T__0)
                        self.state = 154
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 155
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 159
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 156
                            self.match(NumberParser.T__0) 
                        self.state = 161
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
             
                self.state = 166
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
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 167
                self.prefix()


            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 170
                self.range_pattern()

            elif la_ == 2:
                self.state = 171
                self.number_pattern()
                self.state = 179
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 172
                        self.match(NumberParser.T__0)


                    self.state = 175
                    self.match(NumberParser.WORD)
                    self.state = 177
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        self.state = 176
                        self.match(NumberParser.T__0)




                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__2:
                    self.state = 181
                    self.spl_discard()




            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 187
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==NumberParser.T__0:
                                self.state = 186
                                self.match(NumberParser.T__0)


                            self.state = 189
                            self.match(NumberParser.WORD)
                            self.state = 191
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                            if la_ == 1:
                                self.state = 190
                                self.match(NumberParser.T__0)



                        else:
                            raise NoViableAltException(self)
                        self.state = 195 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                    self.state = 211
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 197
                        self.range_pattern()
                        pass

                    elif la_ == 2:
                        self.state = 198
                        self.number_pattern()
                        self.state = 206
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                        if la_ == 1:
                            self.state = 200
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==NumberParser.T__0:
                                self.state = 199
                                self.match(NumberParser.T__0)


                            self.state = 202
                            self.match(NumberParser.WORD)
                            self.state = 204
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                            if la_ == 1:
                                self.state = 203
                                self.match(NumberParser.T__0)




                        self.state = 209
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==NumberParser.T__2:
                            self.state = 208
                            self.spl_discard()


                        pass

             
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 218
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
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 221
                    self.match(NumberParser.T__0)


                self.state = 224
                self.match(NumberParser.T__1)
                self.state = 226
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 225
                    self.match(NumberParser.T__0)


                self.state = 228
                self.number_pattern()
                self.state = 229
                self.match(NumberParser.CONJUNCTION)
                self.state = 230
                self.number_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 232
                    self.match(NumberParser.T__0)


                self.state = 235
                self.match(NumberParser.T__1)
                self.state = 237
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 236
                    self.match(NumberParser.T__0)


                self.state = 239
                self.number_pattern()
                self.state = 240
                self.match(NumberParser.T__2)
                self.state = 241
                self.number_pattern()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 243
                    self.match(NumberParser.T__0)


                self.state = 246
                self.number_pattern()
                self.state = 247
                self.match(NumberParser.T__2)
                self.state = 248
                self.number_pattern()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 250
                    self.match(NumberParser.T__0)


                self.state = 253
                self.match(NumberParser.T__3)
                self.state = 255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 254
                    self.match(NumberParser.T__0)


                self.state = 257
                self.number_pattern()
                self.state = 258
                self.match(NumberParser.CONJUNCTION)
                self.state = 259
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
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 263
                self.crores_format()
                pass

            elif la_ == 2:
                self.state = 264
                self.lakhs_format()
                pass

            elif la_ == 3:
                self.state = 265
                self.thousands_format()
                pass

            elif la_ == 4:
                self.state = 266
                self.hundreds_format()
                pass

            elif la_ == 5:
                self.state = 267
                self.tens_format()
                pass

            elif la_ == 6:
                self.state = 268
                self.units_format()
                pass

            elif la_ == 7:
                self.state = 269
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
            self.state = 279 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 272
                        self.match(NumberParser.T__0)


                    self.state = 275
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 276
                        self.match(NumberParser.T__0)



                else:
                    raise NoViableAltException(self)
                self.state = 281 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_crores_format)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_LAKHS, NumberParser.WORD_NUMBER_CRORES, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS, NumberParser.NUMBER_LAKHS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 283
                    self.prefix_crores()


                self.state = 288
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_CRORES]:
                    self.state = 286
                    self.match(NumberParser.WORD_NUMBER_CRORES)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 287
                    self.spl_crores()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 291
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 290
                    self.match(NumberParser.CONJUNCTION)


                self.state = 294
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 293
                    self.suffix_crores()


                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 296
                    self.match(NumberParser.CONJUNCTION)


                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_FRACTIONS:
                    self.state = 299
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass
            elif token in [NumberParser.NUMBER_CRORES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
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
        self.enterRule(localctx, 14, self.RULE_lakhs_format)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.T__2, NumberParser.WORD_NUMBER_UNITS, NumberParser.WORD_NUMBER_TENS, NumberParser.WORD_NUMBER_HUNDREDS, NumberParser.WORD_NUMBER_THOUSANDS, NumberParser.WORD_NUMBER_LAKHS, NumberParser.NUMBER_UNITS, NumberParser.NUMBER_TENS, NumberParser.NUMBER_HUNDREDS, NumberParser.NUMBER_THOUSANDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 305
                    self.prefix_lakhs()


                self.state = 310
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_LAKHS]:
                    self.state = 308
                    self.match(NumberParser.WORD_NUMBER_LAKHS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 309
                    self.spl_lakhs()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 313
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 312
                    self.match(NumberParser.CONJUNCTION)


                self.state = 316
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 315
                    self.suffix_lakhs()


                self.state = 319
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 318
                    self.match(NumberParser.CONJUNCTION)


                self.state = 322
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 321
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass
            elif token in [NumberParser.NUMBER_LAKHS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
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
        self.enterRule(localctx, 16, self.RULE_thousands_format)
        self._la = 0 # Token type
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 327
                    self.prefix_thousands()


                self.state = 332
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NumberParser.WORD_NUMBER_THOUSANDS]:
                    self.state = 330
                    self.match(NumberParser.WORD_NUMBER_THOUSANDS)
                    pass
                elif token in [NumberParser.T__2]:
                    self.state = 331
                    self.spl_thousands()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 335
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 334
                    self.match(NumberParser.CONJUNCTION)


                self.state = 338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 337
                    self.suffix_thousands()


                self.state = 341
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 340
                    self.match(NumberParser.CONJUNCTION)


                self.state = 344
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                if la_ == 1:
                    self.state = 343
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(NumberParser.NUMBER_THOUSANDS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 348
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.match(NumberParser.NUMBER_THOUSANDS)
                self.state = 353
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                if la_ == 1:
                    self.state = 350
                    self.hundreds_format()
                    pass

                elif la_ == 2:
                    self.state = 351
                    self.tens_format()
                    pass

                elif la_ == 3:
                    self.state = 352
                    self.units_format()
                    pass


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
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
        self.enterRule(localctx, 18, self.RULE_hundreds_format)
        self._la = 0 # Token type
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS))) != 0):
                    self.state = 358
                    self.prefix_hundreds()


                self.state = 361
                self.match(NumberParser.WORD_NUMBER_HUNDREDS)
                self.state = 363
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
                if la_ == 1:
                    self.state = 362
                    self.match(NumberParser.CONJUNCTION)


                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.WORD_NUMBER_UNITS) | (1 << NumberParser.WORD_NUMBER_TENS) | (1 << NumberParser.NUMBER_UNITS) | (1 << NumberParser.NUMBER_TENS))) != 0):
                    self.state = 365
                    self.suffix_hundreds()


                self.state = 369
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                if la_ == 1:
                    self.state = 368
                    self.match(NumberParser.CONJUNCTION)


                self.state = 372
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                if la_ == 1:
                    self.state = 371
                    self.match(NumberParser.WORD_NUMBER_FRACTIONS)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.spl_hundreds()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.spl_hundreds_1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
                self.spl_hundreds_2()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 377
                self.spl_hundreds_3()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 378
                self.spl_hundreds_4()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 379
                self.match(NumberParser.NUMBER_HUNDREDS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 380
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 382
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 383
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 384
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 385
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 386
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 387
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
        self.enterRule(localctx, 20, self.RULE_tens_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_TENS]:
                self.state = 390
                self.match(NumberParser.WORD_NUMBER_TENS)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 391
                    self.units_format()


                pass
            elif token in [NumberParser.NUMBER_TENS]:
                self.state = 394
                self.match(NumberParser.NUMBER_TENS)
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS:
                    self.state = 395
                    self.units_format()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.state = 400
                self.match(NumberParser.CONJUNCTION)


            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.state = 403
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
        self.enterRule(localctx, 22, self.RULE_units_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 407
                self.match(NumberParser.CONJUNCTION)


            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 410
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
        self.enterRule(localctx, 24, self.RULE_prefix_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 413
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 414
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 415
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 416
                self.thousands_format()
                pass

            elif la_ == 5:
                self.state = 417
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
        self.enterRule(localctx, 26, self.RULE_suffix_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.state = 420
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 421
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 422
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 423
                self.thousands_format()
                pass

            elif la_ == 5:
                self.state = 424
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
        self.enterRule(localctx, 28, self.RULE_prefix_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.state = 427
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 428
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 429
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 430
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
        self.enterRule(localctx, 30, self.RULE_suffix_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.state = 433
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 434
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 435
                self.hundreds_format()
                pass

            elif la_ == 4:
                self.state = 436
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
        self.enterRule(localctx, 32, self.RULE_prefix_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 439
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 440
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 441
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
        self.enterRule(localctx, 34, self.RULE_suffix_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 444
                self.units_format()
                pass

            elif la_ == 2:
                self.state = 445
                self.tens_format()
                pass

            elif la_ == 3:
                self.state = 446
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
        self.enterRule(localctx, 36, self.RULE_prefix_hundreds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_UNITS, NumberParser.NUMBER_UNITS]:
                self.state = 449
                self.units_format()
                pass
            elif token in [NumberParser.WORD_NUMBER_TENS, NumberParser.NUMBER_TENS]:
                self.state = 450
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
        self.enterRule(localctx, 38, self.RULE_suffix_hundreds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NumberParser.WORD_NUMBER_UNITS, NumberParser.NUMBER_UNITS]:
                self.state = 453
                self.units_format()
                pass
            elif token in [NumberParser.WORD_NUMBER_TENS, NumberParser.NUMBER_TENS]:
                self.state = 454
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
        self.enterRule(localctx, 40, self.RULE_spl_tens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(NumberParser.T__2)
            self.state = 458
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 459
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
        self.enterRule(localctx, 42, self.RULE_spl_hundreds)
        self._la = 0 # Token type
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(NumberParser.T__2)
                self.state = 463
                _la = self._input.LA(1)
                if not(_la==NumberParser.WORD_NUMBER_TENS or _la==NumberParser.NUMBER_TENS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 465
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
                if la_ == 1:
                    self.state = 464
                    self.match(NumberParser.T__0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.match(NumberParser.T__2)
                self.state = 468
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
        self.enterRule(localctx, 44, self.RULE_spl_hundreds_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.spl_tens()
            self.state = 472
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
        self.enterRule(localctx, 46, self.RULE_spl_hundreds_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 475
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
        self.enterRule(localctx, 48, self.RULE_spl_hundreds_3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 478
            _la = self._input.LA(1)
            if not(_la==NumberParser.WORD_NUMBER_UNITS or _la==NumberParser.NUMBER_UNITS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 479
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
        self.enterRule(localctx, 50, self.RULE_spl_hundreds_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.spl_tens()
            self.state = 482
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
        self.enterRule(localctx, 52, self.RULE_spl_thousands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(NumberParser.T__2)
            self.state = 485
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
        self.enterRule(localctx, 54, self.RULE_spl_lakhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(NumberParser.T__2)
            self.state = 488
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
        self.enterRule(localctx, 56, self.RULE_spl_crores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(NumberParser.T__2)
            self.state = 491
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
        self.enterRule(localctx, 58, self.RULE_spl_epilogue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
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
        self.enterRule(localctx, 60, self.RULE_spl_discard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(NumberParser.T__2)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NumberParser.T__0:
                self.state = 496
                self.match(NumberParser.T__0)
                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 502
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
        self.enterRule(localctx, 62, self.RULE_prefix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,98,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 505
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==NumberParser.T__0:
                        self.state = 504
                        self.match(NumberParser.T__0)


                    self.state = 507
                    _la = self._input.LA(1)
                    if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 509
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
                    if la_ == 1:
                        self.state = 508
                        self.match(NumberParser.T__0)

             
                self.state = 515
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,98,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_suffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NumberParser.T__0) | (1 << NumberParser.CONJUNCTION) | (1 << NumberParser.WORD))) != 0):
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NumberParser.T__0:
                    self.state = 516
                    self.match(NumberParser.T__0)


                self.state = 519
                _la = self._input.LA(1)
                if not(_la==NumberParser.CONJUNCTION or _la==NumberParser.WORD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 521
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
                if la_ == 1:
                    self.state = 520
                    self.match(NumberParser.T__0)


                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





