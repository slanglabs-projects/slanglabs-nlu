# Generated from ../grammars/Number.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NumberParser import NumberParser
else:
    from NumberParser import NumberParser

# This class defines a complete listener for a parse tree produced by NumberParser.
class NumberListener(ParseTreeListener):

    # Enter a parse tree produced by NumberParser#numbers_utterance.
    def enterNumbers_utterance(self, ctx:NumberParser.Numbers_utteranceContext):
        pass

    # Exit a parse tree produced by NumberParser#numbers_utterance.
    def exitNumbers_utterance(self, ctx:NumberParser.Numbers_utteranceContext):
        pass


    # Enter a parse tree produced by NumberParser#ranges_utterance.
    def enterRanges_utterance(self, ctx:NumberParser.Ranges_utteranceContext):
        pass

    # Exit a parse tree produced by NumberParser#ranges_utterance.
    def exitRanges_utterance(self, ctx:NumberParser.Ranges_utteranceContext):
        pass


    # Enter a parse tree produced by NumberParser#range_pattern.
    def enterRange_pattern(self, ctx:NumberParser.Range_patternContext):
        pass

    # Exit a parse tree produced by NumberParser#range_pattern.
    def exitRange_pattern(self, ctx:NumberParser.Range_patternContext):
        pass


    # Enter a parse tree produced by NumberParser#number_pattern.
    def enterNumber_pattern(self, ctx:NumberParser.Number_patternContext):
        pass

    # Exit a parse tree produced by NumberParser#number_pattern.
    def exitNumber_pattern(self, ctx:NumberParser.Number_patternContext):
        pass


    # Enter a parse tree produced by NumberParser#crores_format.
    def enterCrores_format(self, ctx:NumberParser.Crores_formatContext):
        pass

    # Exit a parse tree produced by NumberParser#crores_format.
    def exitCrores_format(self, ctx:NumberParser.Crores_formatContext):
        pass


    # Enter a parse tree produced by NumberParser#lakhs_format.
    def enterLakhs_format(self, ctx:NumberParser.Lakhs_formatContext):
        pass

    # Exit a parse tree produced by NumberParser#lakhs_format.
    def exitLakhs_format(self, ctx:NumberParser.Lakhs_formatContext):
        pass


    # Enter a parse tree produced by NumberParser#thousands_format.
    def enterThousands_format(self, ctx:NumberParser.Thousands_formatContext):
        pass

    # Exit a parse tree produced by NumberParser#thousands_format.
    def exitThousands_format(self, ctx:NumberParser.Thousands_formatContext):
        pass


    # Enter a parse tree produced by NumberParser#hundreds_format.
    def enterHundreds_format(self, ctx:NumberParser.Hundreds_formatContext):
        pass

    # Exit a parse tree produced by NumberParser#hundreds_format.
    def exitHundreds_format(self, ctx:NumberParser.Hundreds_formatContext):
        pass


    # Enter a parse tree produced by NumberParser#tens_format.
    def enterTens_format(self, ctx:NumberParser.Tens_formatContext):
        pass

    # Exit a parse tree produced by NumberParser#tens_format.
    def exitTens_format(self, ctx:NumberParser.Tens_formatContext):
        pass


    # Enter a parse tree produced by NumberParser#units_format.
    def enterUnits_format(self, ctx:NumberParser.Units_formatContext):
        pass

    # Exit a parse tree produced by NumberParser#units_format.
    def exitUnits_format(self, ctx:NumberParser.Units_formatContext):
        pass


    # Enter a parse tree produced by NumberParser#prefix_crores.
    def enterPrefix_crores(self, ctx:NumberParser.Prefix_croresContext):
        pass

    # Exit a parse tree produced by NumberParser#prefix_crores.
    def exitPrefix_crores(self, ctx:NumberParser.Prefix_croresContext):
        pass


    # Enter a parse tree produced by NumberParser#suffix_crores.
    def enterSuffix_crores(self, ctx:NumberParser.Suffix_croresContext):
        pass

    # Exit a parse tree produced by NumberParser#suffix_crores.
    def exitSuffix_crores(self, ctx:NumberParser.Suffix_croresContext):
        pass


    # Enter a parse tree produced by NumberParser#prefix_lakhs.
    def enterPrefix_lakhs(self, ctx:NumberParser.Prefix_lakhsContext):
        pass

    # Exit a parse tree produced by NumberParser#prefix_lakhs.
    def exitPrefix_lakhs(self, ctx:NumberParser.Prefix_lakhsContext):
        pass


    # Enter a parse tree produced by NumberParser#suffix_lakhs.
    def enterSuffix_lakhs(self, ctx:NumberParser.Suffix_lakhsContext):
        pass

    # Exit a parse tree produced by NumberParser#suffix_lakhs.
    def exitSuffix_lakhs(self, ctx:NumberParser.Suffix_lakhsContext):
        pass


    # Enter a parse tree produced by NumberParser#prefix_thousands.
    def enterPrefix_thousands(self, ctx:NumberParser.Prefix_thousandsContext):
        pass

    # Exit a parse tree produced by NumberParser#prefix_thousands.
    def exitPrefix_thousands(self, ctx:NumberParser.Prefix_thousandsContext):
        pass


    # Enter a parse tree produced by NumberParser#suffix_thousands.
    def enterSuffix_thousands(self, ctx:NumberParser.Suffix_thousandsContext):
        pass

    # Exit a parse tree produced by NumberParser#suffix_thousands.
    def exitSuffix_thousands(self, ctx:NumberParser.Suffix_thousandsContext):
        pass


    # Enter a parse tree produced by NumberParser#prefix_hundreds.
    def enterPrefix_hundreds(self, ctx:NumberParser.Prefix_hundredsContext):
        pass

    # Exit a parse tree produced by NumberParser#prefix_hundreds.
    def exitPrefix_hundreds(self, ctx:NumberParser.Prefix_hundredsContext):
        pass


    # Enter a parse tree produced by NumberParser#suffix_hundreds.
    def enterSuffix_hundreds(self, ctx:NumberParser.Suffix_hundredsContext):
        pass

    # Exit a parse tree produced by NumberParser#suffix_hundreds.
    def exitSuffix_hundreds(self, ctx:NumberParser.Suffix_hundredsContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_tens.
    def enterSpl_tens(self, ctx:NumberParser.Spl_tensContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_tens.
    def exitSpl_tens(self, ctx:NumberParser.Spl_tensContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_hundreds.
    def enterSpl_hundreds(self, ctx:NumberParser.Spl_hundredsContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_hundreds.
    def exitSpl_hundreds(self, ctx:NumberParser.Spl_hundredsContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_hundreds_1.
    def enterSpl_hundreds_1(self, ctx:NumberParser.Spl_hundreds_1Context):
        pass

    # Exit a parse tree produced by NumberParser#spl_hundreds_1.
    def exitSpl_hundreds_1(self, ctx:NumberParser.Spl_hundreds_1Context):
        pass


    # Enter a parse tree produced by NumberParser#spl_hundreds_2.
    def enterSpl_hundreds_2(self, ctx:NumberParser.Spl_hundreds_2Context):
        pass

    # Exit a parse tree produced by NumberParser#spl_hundreds_2.
    def exitSpl_hundreds_2(self, ctx:NumberParser.Spl_hundreds_2Context):
        pass


    # Enter a parse tree produced by NumberParser#spl_hundreds_3.
    def enterSpl_hundreds_3(self, ctx:NumberParser.Spl_hundreds_3Context):
        pass

    # Exit a parse tree produced by NumberParser#spl_hundreds_3.
    def exitSpl_hundreds_3(self, ctx:NumberParser.Spl_hundreds_3Context):
        pass


    # Enter a parse tree produced by NumberParser#spl_hundreds_4.
    def enterSpl_hundreds_4(self, ctx:NumberParser.Spl_hundreds_4Context):
        pass

    # Exit a parse tree produced by NumberParser#spl_hundreds_4.
    def exitSpl_hundreds_4(self, ctx:NumberParser.Spl_hundreds_4Context):
        pass


    # Enter a parse tree produced by NumberParser#spl_thousands.
    def enterSpl_thousands(self, ctx:NumberParser.Spl_thousandsContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_thousands.
    def exitSpl_thousands(self, ctx:NumberParser.Spl_thousandsContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_lakhs.
    def enterSpl_lakhs(self, ctx:NumberParser.Spl_lakhsContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_lakhs.
    def exitSpl_lakhs(self, ctx:NumberParser.Spl_lakhsContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_crores.
    def enterSpl_crores(self, ctx:NumberParser.Spl_croresContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_crores.
    def exitSpl_crores(self, ctx:NumberParser.Spl_croresContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_epilogue.
    def enterSpl_epilogue(self, ctx:NumberParser.Spl_epilogueContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_epilogue.
    def exitSpl_epilogue(self, ctx:NumberParser.Spl_epilogueContext):
        pass


    # Enter a parse tree produced by NumberParser#spl_discard.
    def enterSpl_discard(self, ctx:NumberParser.Spl_discardContext):
        pass

    # Exit a parse tree produced by NumberParser#spl_discard.
    def exitSpl_discard(self, ctx:NumberParser.Spl_discardContext):
        pass


    # Enter a parse tree produced by NumberParser#prefix.
    def enterPrefix(self, ctx:NumberParser.PrefixContext):
        pass

    # Exit a parse tree produced by NumberParser#prefix.
    def exitPrefix(self, ctx:NumberParser.PrefixContext):
        pass


    # Enter a parse tree produced by NumberParser#suffix.
    def enterSuffix(self, ctx:NumberParser.SuffixContext):
        pass

    # Exit a parse tree produced by NumberParser#suffix.
    def exitSuffix(self, ctx:NumberParser.SuffixContext):
        pass



del NumberParser