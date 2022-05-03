# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u023b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\7\2\u00a8")
        buf.write("\n\2\f\2\16\2\u00ab\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\38\58\u018b\n8\39\39\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\3=\3=\3=\3=\5=\u019e\n=\3=\3=\3>\3>\7>\u01a4")
        buf.write("\n>\f>\16>\u01a7\13>\3>\5>\u01aa\n>\3?\3?\3?\3?\7?\u01b0")
        buf.write("\n?\f?\16?\u01b3\13?\3?\5?\u01b6\n?\3@\3@\3@\7@\u01bb")
        buf.write("\n@\f@\16@\u01be\13@\3@\5@\u01c1\n@\3A\3A\3A\3A\7A\u01c7")
        buf.write("\nA\fA\16A\u01ca\13A\3A\5A\u01cd\nA\3B\3B\3B\3B\3B\3B")
        buf.write("\5B\u01d5\nB\3B\3B\3B\5B\u01da\nB\3B\3B\3C\3C\5C\u01e0")
        buf.write("\nC\3D\3D\7D\u01e4\nD\fD\16D\u01e7\13D\3E\3E\3E\5E\u01ec")
        buf.write("\nE\3E\3E\5E\u01f0\nE\3F\3F\7F\u01f4\nF\fF\16F\u01f7\13")
        buf.write("F\3G\3G\6G\u01fb\nG\rG\16G\u01fc\3H\6H\u0200\nH\rH\16")
        buf.write("H\u0201\3H\3H\3I\3I\3I\3J\3J\7J\u020b\nJ\fJ\16J\u020e")
        buf.write("\13J\3J\3J\3J\3K\3K\3L\3L\3M\3M\3M\3M\3M\5M\u021c\nM\3")
        buf.write("N\3N\3N\3O\3O\7O\u0223\nO\fO\16O\u0226\13O\3O\5O\u0229")
        buf.write("\nO\3O\3O\3P\3P\7P\u022f\nP\fP\16P\u0232\13P\3P\3P\3P")
        buf.write("\3Q\3Q\3Q\5Q\u023a\nQ\3\u00a9\2R\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w\2y:{\2}\2\177\2")
        buf.write("\u0081\2\u0083;\u0085\2\u0087\2\u0089\2\u008b<\u008d=")
        buf.write("\u008f>\u0091?\u0093@\u0095\2\u0097\2\u0099\2\u009b\2")
        buf.write("\u009dA\u009fB\u00a1\2\3\2\27\4\2ZZzz\4\2DDdd\3\2\63;")
        buf.write("\4\2\62;aa\3\2\62;\4\2\63;CH\5\2\62;CHaa\4\2\62;CH\3\2")
        buf.write("\639\4\2\629aa\3\2\629\4\2\62\63aa\3\2\62\63\4\2GGgg\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\7\2\n\f\16")
        buf.write("\17$$))^^\t\2))^^ddhhppttvv\6\3\n\f\16\17))^^\3\2^^\2")
        buf.write("\u024a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2y\3\2\2\2\2\u0083\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a3\3\2\2\2\5\u00b1")
        buf.write("\3\2\2\2\7\u00b7\3\2\2\2\t\u00c0\3\2\2\2\13\u00c3\3\2")
        buf.write("\2\2\r\u00ca\3\2\2\2\17\u00cf\3\2\2\2\21\u00d7\3\2\2\2")
        buf.write("\23\u00dc\3\2\2\2\25\u00e2\3\2\2\2\27\u00e8\3\2\2\2\31")
        buf.write("\u00eb\3\2\2\2\33\u00ef\3\2\2\2\35\u00f5\3\2\2\2\37\u00fd")
        buf.write("\3\2\2\2!\u0104\3\2\2\2#\u010b\3\2\2\2%\u0110\3\2\2\2")
        buf.write("\'\u0116\3\2\2\2)\u011a\3\2\2\2+\u011e\3\2\2\2-\u012a")
        buf.write("\3\2\2\2/\u0135\3\2\2\2\61\u0139\3\2\2\2\63\u013c\3\2")
        buf.write("\2\2\65\u0141\3\2\2\2\67\u0143\3\2\2\29\u0145\3\2\2\2")
        buf.write(";\u0147\3\2\2\2=\u0149\3\2\2\2?\u014b\3\2\2\2A\u014d\3")
        buf.write("\2\2\2C\u0150\3\2\2\2E\u0153\3\2\2\2G\u0156\3\2\2\2I\u0158")
        buf.write("\3\2\2\2K\u015b\3\2\2\2M\u015d\3\2\2\2O\u015f\3\2\2\2")
        buf.write("Q\u0162\3\2\2\2S\u0165\3\2\2\2U\u0169\3\2\2\2W\u016c\3")
        buf.write("\2\2\2Y\u016f\3\2\2\2[\u0171\3\2\2\2]\u0173\3\2\2\2_\u0175")
        buf.write("\3\2\2\2a\u0177\3\2\2\2c\u0179\3\2\2\2e\u017c\3\2\2\2")
        buf.write("g\u017e\3\2\2\2i\u0180\3\2\2\2k\u0182\3\2\2\2m\u0184\3")
        buf.write("\2\2\2o\u018a\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2u\u0192")
        buf.write("\3\2\2\2w\u0195\3\2\2\2y\u019d\3\2\2\2{\u01a1\3\2\2\2")
        buf.write("}\u01ab\3\2\2\2\177\u01b7\3\2\2\2\u0081\u01c2\3\2\2\2")
        buf.write("\u0083\u01d9\3\2\2\2\u0085\u01df\3\2\2\2\u0087\u01e1\3")
        buf.write("\2\2\2\u0089\u01e8\3\2\2\2\u008b\u01f1\3\2\2\2\u008d\u01f8")
        buf.write("\3\2\2\2\u008f\u01ff\3\2\2\2\u0091\u0205\3\2\2\2\u0093")
        buf.write("\u0208\3\2\2\2\u0095\u0212\3\2\2\2\u0097\u0214\3\2\2\2")
        buf.write("\u0099\u021b\3\2\2\2\u009b\u021d\3\2\2\2\u009d\u0220\3")
        buf.write("\2\2\2\u009f\u022c\3\2\2\2\u00a1\u0239\3\2\2\2\u00a3\u00a4")
        buf.write("\7%\2\2\u00a4\u00a5\7%\2\2\u00a5\u00a9\3\2\2\2\u00a6\u00a8")
        buf.write("\13\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ac\3\2\2\2")
        buf.write("\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7%\2\2\u00ad\u00ae\7")
        buf.write("%\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\b\2\2\2\u00b0\4")
        buf.write("\3\2\2\2\u00b1\u00b2\7D\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7m\2\2\u00b6\6")
        buf.write("\3\2\2\2\u00b7\u00b8\7E\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7g\2\2\u00bf\b")
        buf.write("\3\2\2\2\u00c0\u00c1\7K\2\2\u00c1\u00c2\7h\2\2\u00c2\n")
        buf.write("\3\2\2\2\u00c3\u00c4\7G\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6")
        buf.write("\7u\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\f\3\2\2\2\u00ca\u00cb\7G\2\2\u00cb\u00cc")
        buf.write("\7n\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\16")
        buf.write("\3\2\2\2\u00cf\u00d0\7H\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7e\2\2\u00d5\u00d6\7j\2\2\u00d6\20\3\2\2\2\u00d7\u00d8")
        buf.write("\7V\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\22\3\2\2\2\u00dc\u00dd\7H\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\24\3\2\2\2\u00e2\u00e3\7C\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7{\2\2\u00e7\26\3\2\2\2\u00e8\u00e9\7K\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\30\3\2\2\2\u00eb\u00ec\7K\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7v\2\2\u00ee\32\3\2\2\2\u00ef\u00f0")
        buf.write("\7H\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7v\2\2\u00f4\34\3\2\2\2\u00f5\u00f6")
        buf.write("\7D\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\36\3\2\2\2\u00fd\u00fe\7U\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7i\2\2\u0103 \3\2\2\2\u0104\u0105")
        buf.write("\7T\2\2\u0105\u0106\7g\2\2\u0106\u0107\7v\2\2\u0107\u0108")
        buf.write("\7w\2\2\u0108\u0109\7t\2\2\u0109\u010a\7p\2\2\u010a\"")
        buf.write("\3\2\2\2\u010b\u010c\7P\2\2\u010c\u010d\7w\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7n\2\2\u010f$\3\2\2\2\u0110\u0111")
        buf.write("\7E\2\2\u0111\u0112\7n\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7u\2\2\u0114\u0115\7u\2\2\u0115&\3\2\2\2\u0116\u0117")
        buf.write("\7X\2\2\u0117\u0118\7c\2\2\u0118\u0119\7n\2\2\u0119(\3")
        buf.write("\2\2\2\u011a\u011b\7X\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d*\3\2\2\2\u011e\u011f\7E\2\2\u011f\u0120")
        buf.write("\7q\2\2\u0120\u0121\7p\2\2\u0121\u0122\7u\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123\u0124\7t\2\2\u0124\u0125\7w\2\2\u0125\u0126")
        buf.write("\7e\2\2\u0126\u0127\7v\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129,\3\2\2\2\u012a\u012b\7F\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7u\2\2\u012d\u012e\7v\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7w\2\2\u0130\u0131\7e\2\2\u0131\u0132")
        buf.write("\7v\2\2\u0132\u0133\7q\2\2\u0133\u0134\7t\2\2\u0134.\3")
        buf.write("\2\2\2\u0135\u0136\7P\2\2\u0136\u0137\7g\2\2\u0137\u0138")
        buf.write("\7y\2\2\u0138\60\3\2\2\2\u0139\u013a\7D\2\2\u013a\u013b")
        buf.write("\7{\2\2\u013b\62\3\2\2\2\u013c\u013d\7U\2\2\u013d\u013e")
        buf.write("\7g\2\2\u013e\u013f\7n\2\2\u013f\u0140\7h\2\2\u0140\64")
        buf.write("\3\2\2\2\u0141\u0142\7-\2\2\u0142\66\3\2\2\2\u0143\u0144")
        buf.write("\7/\2\2\u01448\3\2\2\2\u0145\u0146\7,\2\2\u0146:\3\2\2")
        buf.write("\2\u0147\u0148\7\61\2\2\u0148<\3\2\2\2\u0149\u014a\7\'")
        buf.write("\2\2\u014a>\3\2\2\2\u014b\u014c\7#\2\2\u014c@\3\2\2\2")
        buf.write("\u014d\u014e\7(\2\2\u014e\u014f\7(\2\2\u014fB\3\2\2\2")
        buf.write("\u0150\u0151\7~\2\2\u0151\u0152\7~\2\2\u0152D\3\2\2\2")
        buf.write("\u0153\u0154\7?\2\2\u0154\u0155\7?\2\2\u0155F\3\2\2\2")
        buf.write("\u0156\u0157\7?\2\2\u0157H\3\2\2\2\u0158\u0159\7#\2\2")
        buf.write("\u0159\u015a\7?\2\2\u015aJ\3\2\2\2\u015b\u015c\7@\2\2")
        buf.write("\u015cL\3\2\2\2\u015d\u015e\7>\2\2\u015eN\3\2\2\2\u015f")
        buf.write("\u0160\7@\2\2\u0160\u0161\7?\2\2\u0161P\3\2\2\2\u0162")
        buf.write("\u0163\7>\2\2\u0163\u0164\7?\2\2\u0164R\3\2\2\2\u0165")
        buf.write("\u0166\7?\2\2\u0166\u0167\7?\2\2\u0167\u0168\7\60\2\2")
        buf.write("\u0168T\3\2\2\2\u0169\u016a\7-\2\2\u016a\u016b\7\60\2")
        buf.write("\2\u016bV\3\2\2\2\u016c\u016d\7<\2\2\u016d\u016e\7<\2")
        buf.write("\2\u016eX\3\2\2\2\u016f\u0170\7*\2\2\u0170Z\3\2\2\2\u0171")
        buf.write("\u0172\7+\2\2\u0172\\\3\2\2\2\u0173\u0174\7]\2\2\u0174")
        buf.write("^\3\2\2\2\u0175\u0176\7_\2\2\u0176`\3\2\2\2\u0177\u0178")
        buf.write("\7\60\2\2\u0178b\3\2\2\2\u0179\u017a\7\60\2\2\u017a\u017b")
        buf.write("\7\60\2\2\u017bd\3\2\2\2\u017c\u017d\7.\2\2\u017df\3\2")
        buf.write("\2\2\u017e\u017f\7<\2\2\u017fh\3\2\2\2\u0180\u0181\7=")
        buf.write("\2\2\u0181j\3\2\2\2\u0182\u0183\7}\2\2\u0183l\3\2\2\2")
        buf.write("\u0184\u0185\7\177\2\2\u0185n\3\2\2\2\u0186\u018b\5q9")
        buf.write("\2\u0187\u018b\5s:\2\u0188\u018b\5u;\2\u0189\u018b\5w")
        buf.write("<\2\u018a\u0186\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018bp\3\2\2\2\u018c\u018d")
        buf.write("\7\62\2\2\u018dr\3\2\2\2\u018e\u018f\7\62\2\2\u018f\u0190")
        buf.write("\t\2\2\2\u0190\u0191\7\62\2\2\u0191t\3\2\2\2\u0192\u0193")
        buf.write("\7\62\2\2\u0193\u0194\7\62\2\2\u0194v\3\2\2\2\u0195\u0196")
        buf.write("\7\62\2\2\u0196\u0197\t\3\2\2\u0197\u0198\7\62\2\2\u0198")
        buf.write("x\3\2\2\2\u0199\u019e\5{>\2\u019a\u019e\5}?\2\u019b\u019e")
        buf.write("\5\177@\2\u019c\u019e\5\u0081A\2\u019d\u0199\3\2\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u01a0\b=\3\2\u01a0z\3\2\2\2")
        buf.write("\u01a1\u01a9\t\4\2\2\u01a2\u01a4\t\5\2\2\u01a3\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("\u01aa\t\6\2\2\u01a9\u01a5\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aa|\3\2\2\2\u01ab\u01ac\7\62\2\2\u01ac\u01ad\t\2\2")
        buf.write("\2\u01ad\u01b5\t\7\2\2\u01ae\u01b0\t\b\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b6\t\t\2\2\u01b5\u01b1\3\2\2\2\u01b5\u01b6\3")
        buf.write("\2\2\2\u01b6~\3\2\2\2\u01b7\u01b8\7\62\2\2\u01b8\u01c0")
        buf.write("\t\n\2\2\u01b9\u01bb\t\13\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\t")
        buf.write("\f\2\2\u01c0\u01bc\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u0080")
        buf.write("\3\2\2\2\u01c2\u01c3\7\62\2\2\u01c3\u01c4\t\3\2\2\u01c4")
        buf.write("\u01cc\7\63\2\2\u01c5\u01c7\t\r\2\2\u01c6\u01c5\3\2\2")
        buf.write("\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("\u01cd\t\16\2\2\u01cc\u01c8\3\2\2\2\u01cc\u01cd\3\2\2")
        buf.write("\2\u01cd\u0082\3\2\2\2\u01ce\u01d4\5\u0085C\2\u01cf\u01d0")
        buf.write("\5\u0087D\2\u01d0\u01d1\5\u0089E\2\u01d1\u01d5\3\2\2\2")
        buf.write("\u01d2\u01d5\5\u0087D\2\u01d3\u01d5\5\u0089E\2\u01d4\u01cf")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5")
        buf.write("\u01da\3\2\2\2\u01d6\u01d7\5\u0087D\2\u01d7\u01d8\5\u0089")
        buf.write("E\2\u01d8\u01da\3\2\2\2\u01d9\u01ce\3\2\2\2\u01d9\u01d6")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\bB\4\2\u01dc")
        buf.write("\u0084\3\2\2\2\u01dd\u01e0\5q9\2\u01de\u01e0\5{>\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0\u0086\3\2\2\2")
        buf.write("\u01e1\u01e5\5a\61\2\u01e2\u01e4\t\6\2\2\u01e3\u01e2\3")
        buf.write("\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u0088\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8")
        buf.write("\u01eb\t\17\2\2\u01e9\u01ec\5\65\33\2\u01ea\u01ec\5\67")
        buf.write("\34\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01eb\u01ec")
        buf.write("\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01f0\5q9\2\u01ee\u01f0")
        buf.write("\5{>\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u008a")
        buf.write("\3\2\2\2\u01f1\u01f5\t\20\2\2\u01f2\u01f4\t\21\2\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u008c\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f8\u01fa\7&\2\2\u01f9\u01fb\t\21\2\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u008e\3\2\2\2\u01fe\u0200\t\22\2")
        buf.write("\2\u01ff\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0204\bH\2\2\u0204\u0090\3\2\2\2\u0205\u0206\13\2\2\2")
        buf.write("\u0206\u0207\bI\5\2\u0207\u0092\3\2\2\2\u0208\u020c\5")
        buf.write("\u0095K\2\u0209\u020b\5\u0099M\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u020f\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210\5")
        buf.write("\u0095K\2\u0210\u0211\bJ\6\2\u0211\u0094\3\2\2\2\u0212")
        buf.write("\u0213\7$\2\2\u0213\u0096\3\2\2\2\u0214\u0215\7)\2\2\u0215")
        buf.write("\u0098\3\2\2\2\u0216\u021c\n\23\2\2\u0217\u0218\5\u0097")
        buf.write("L\2\u0218\u0219\5\u0095K\2\u0219\u021c\3\2\2\2\u021a\u021c")
        buf.write("\5\u009bN\2\u021b\u0216\3\2\2\2\u021b\u0217\3\2\2\2\u021b")
        buf.write("\u021a\3\2\2\2\u021c\u009a\3\2\2\2\u021d\u021e\7^\2\2")
        buf.write("\u021e\u021f\t\24\2\2\u021f\u009c\3\2\2\2\u0220\u0224")
        buf.write("\5\u0095K\2\u0221\u0223\5\u0099M\2\u0222\u0221\3\2\2\2")
        buf.write("\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3")
        buf.write("\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0229")
        buf.write("\t\25\2\2\u0228\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a")
        buf.write("\u022b\bO\7\2\u022b\u009e\3\2\2\2\u022c\u0230\5\u0095")
        buf.write("K\2\u022d\u022f\5\u0099M\2\u022e\u022d\3\2\2\2\u022f\u0232")
        buf.write("\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0233\3\2\2\2\u0232\u0230\3\2\2\2\u0233\u0234\5\u00a1")
        buf.write("Q\2\u0234\u0235\bP\b\2\u0235\u00a0\3\2\2\2\u0236\u0237")
        buf.write("\7^\2\2\u0237\u023a\n\24\2\2\u0238\u023a\n\26\2\2\u0239")
        buf.write("\u0236\3\2\2\2\u0239\u0238\3\2\2\2\u023a\u00a2\3\2\2\2")
        buf.write("\35\2\u00a9\u018a\u019d\u01a5\u01a9\u01b1\u01b5\u01bc")
        buf.write("\u01c0\u01c8\u01cc\u01d4\u01d9\u01df\u01e5\u01eb\u01ef")
        buf.write("\u01f5\u01fc\u0201\u020c\u021b\u0224\u0228\u0230\u0239")
        buf.write("\t\b\2\2\3=\2\3B\3\3I\4\3J\5\3O\6\3P\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    CONSTRUCTOR = 21
    DESTRUCTOR = 22
    NEW = 23
    BY = 24
    SELF = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AND = 32
    OR = 33
    EQUAL = 34
    ASSIGN = 35
    NEQ = 36
    GT = 37
    LT = 38
    GTE = 39
    LTE = 40
    EQUALSTR = 41
    ADDSTR = 42
    DOUBLECOLON = 43
    LP = 44
    RP = 45
    LSB = 46
    RSB = 47
    DOT = 48
    DOUBLEDOT = 49
    COMMA = 50
    COLON = 51
    SEMICOLON = 52
    LCB = 53
    RCB = 54
    ZEROINT = 55
    NONZEROINT = 56
    FLOATLIT = 57
    ID = 58
    DOLLARID = 59
    WS = 60
    ERROR_TOKEN = 61
    STRINGLIT = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'>'", "'<'", "'>='", "'<='", "'==.'", "'+.'", 
            "'::'", "'('", "')'", "'['", "']'", "'.'", "'..'", "','", "':'", 
            "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NEQ", "GT", "LT", "GTE", "LTE", 
            "EQUALSTR", "ADDSTR", "DOUBLECOLON", "LP", "RP", "LSB", "RSB", 
            "DOT", "DOUBLEDOT", "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", 
            "ZEROINT", "NONZEROINT", "FLOATLIT", "ID", "DOLLARID", "WS", 
            "ERROR_TOKEN", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "ASSIGN", "NEQ", "GT", "LT", "GTE", "LTE", "EQUALSTR", 
                  "ADDSTR", "DOUBLECOLON", "LP", "RP", "LSB", "RSB", "DOT", 
                  "DOUBLEDOT", "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", 
                  "ZEROINT", "ZDEC", "ZHEX", "ZOCT", "ZBIN", "NONZEROINT", 
                  "NDEC", "NHEX", "NOCT", "NBIN", "FLOATLIT", "INTPART", 
                  "DECPART", "EXPART", "ID", "DOLLARID", "WS", "ERROR_TOKEN", 
                  "STRINGLIT", "DQUOTE", "SQUOTE", "STRCONTENT", "ESCSEQ", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ILGESC" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.NONZEROINT_action 
            actions[64] = self.FLOATLIT_action 
            actions[71] = self.ERROR_TOKEN_action 
            actions[72] = self.STRINGLIT_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NONZEROINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    string2=str(self.text)
                    self.text=string2.replace("_","")
                
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    string2=str(self.text)
                    self.text=string2.replace("_","")
                
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise ErrorToken(self.text)
            	
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		string = str(self.text)
            		self.text = string[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


