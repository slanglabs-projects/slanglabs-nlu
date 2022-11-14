# Generated from ../grammars/Date.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DateParser import DateParser
else:
    from DateParser import DateParser

# This class defines a complete listener for a parse tree produced by DateParser.
class DateListener(ParseTreeListener):

    # Enter a parse tree produced by DateParser#utterance.
    def enterUtterance(self, ctx:DateParser.UtteranceContext):
        pass

    # Exit a parse tree produced by DateParser#utterance.
    def exitUtterance(self, ctx:DateParser.UtteranceContext):
        pass


    # Enter a parse tree produced by DateParser#date_pattern.
    def enterDate_pattern(self, ctx:DateParser.Date_patternContext):
        pass

    # Exit a parse tree produced by DateParser#date_pattern.
    def exitDate_pattern(self, ctx:DateParser.Date_patternContext):
        pass


    # Enter a parse tree produced by DateParser#literal_form.
    def enterLiteral_form(self, ctx:DateParser.Literal_formContext):
        pass

    # Exit a parse tree produced by DateParser#literal_form.
    def exitLiteral_form(self, ctx:DateParser.Literal_formContext):
        pass


    # Enter a parse tree produced by DateParser#relative_form.
    def enterRelative_form(self, ctx:DateParser.Relative_formContext):
        pass

    # Exit a parse tree produced by DateParser#relative_form.
    def exitRelative_form(self, ctx:DateParser.Relative_formContext):
        pass


    # Enter a parse tree produced by DateParser#year_form.
    def enterYear_form(self, ctx:DateParser.Year_formContext):
        pass

    # Exit a parse tree produced by DateParser#year_form.
    def exitYear_form(self, ctx:DateParser.Year_formContext):
        pass


    # Enter a parse tree produced by DateParser#year.
    def enterYear(self, ctx:DateParser.YearContext):
        pass

    # Exit a parse tree produced by DateParser#year.
    def exitYear(self, ctx:DateParser.YearContext):
        pass


    # Enter a parse tree produced by DateParser#relative_year.
    def enterRelative_year(self, ctx:DateParser.Relative_yearContext):
        pass

    # Exit a parse tree produced by DateParser#relative_year.
    def exitRelative_year(self, ctx:DateParser.Relative_yearContext):
        pass


    # Enter a parse tree produced by DateParser#month_form.
    def enterMonth_form(self, ctx:DateParser.Month_formContext):
        pass

    # Exit a parse tree produced by DateParser#month_form.
    def exitMonth_form(self, ctx:DateParser.Month_formContext):
        pass


    # Enter a parse tree produced by DateParser#month.
    def enterMonth(self, ctx:DateParser.MonthContext):
        pass

    # Exit a parse tree produced by DateParser#month.
    def exitMonth(self, ctx:DateParser.MonthContext):
        pass


    # Enter a parse tree produced by DateParser#relative_month.
    def enterRelative_month(self, ctx:DateParser.Relative_monthContext):
        pass

    # Exit a parse tree produced by DateParser#relative_month.
    def exitRelative_month(self, ctx:DateParser.Relative_monthContext):
        pass


    # Enter a parse tree produced by DateParser#literal_month.
    def enterLiteral_month(self, ctx:DateParser.Literal_monthContext):
        pass

    # Exit a parse tree produced by DateParser#literal_month.
    def exitLiteral_month(self, ctx:DateParser.Literal_monthContext):
        pass


    # Enter a parse tree produced by DateParser#double_ordinal_month.
    def enterDouble_ordinal_month(self, ctx:DateParser.Double_ordinal_monthContext):
        pass

    # Exit a parse tree produced by DateParser#double_ordinal_month.
    def exitDouble_ordinal_month(self, ctx:DateParser.Double_ordinal_monthContext):
        pass


    # Enter a parse tree produced by DateParser#week_form.
    def enterWeek_form(self, ctx:DateParser.Week_formContext):
        pass

    # Exit a parse tree produced by DateParser#week_form.
    def exitWeek_form(self, ctx:DateParser.Week_formContext):
        pass


    # Enter a parse tree produced by DateParser#week.
    def enterWeek(self, ctx:DateParser.WeekContext):
        pass

    # Exit a parse tree produced by DateParser#week.
    def exitWeek(self, ctx:DateParser.WeekContext):
        pass


    # Enter a parse tree produced by DateParser#relative_week.
    def enterRelative_week(self, ctx:DateParser.Relative_weekContext):
        pass

    # Exit a parse tree produced by DateParser#relative_week.
    def exitRelative_week(self, ctx:DateParser.Relative_weekContext):
        pass


    # Enter a parse tree produced by DateParser#day_form.
    def enterDay_form(self, ctx:DateParser.Day_formContext):
        pass

    # Exit a parse tree produced by DateParser#day_form.
    def exitDay_form(self, ctx:DateParser.Day_formContext):
        pass


    # Enter a parse tree produced by DateParser#day.
    def enterDay(self, ctx:DateParser.DayContext):
        pass

    # Exit a parse tree produced by DateParser#day.
    def exitDay(self, ctx:DateParser.DayContext):
        pass


    # Enter a parse tree produced by DateParser#relative_day.
    def enterRelative_day(self, ctx:DateParser.Relative_dayContext):
        pass

    # Exit a parse tree produced by DateParser#relative_day.
    def exitRelative_day(self, ctx:DateParser.Relative_dayContext):
        pass


    # Enter a parse tree produced by DateParser#time.
    def enterTime(self, ctx:DateParser.TimeContext):
        pass

    # Exit a parse tree produced by DateParser#time.
    def exitTime(self, ctx:DateParser.TimeContext):
        pass


    # Enter a parse tree produced by DateParser#tod.
    def enterTod(self, ctx:DateParser.TodContext):
        pass

    # Exit a parse tree produced by DateParser#tod.
    def exitTod(self, ctx:DateParser.TodContext):
        pass


    # Enter a parse tree produced by DateParser#prefix.
    def enterPrefix(self, ctx:DateParser.PrefixContext):
        pass

    # Exit a parse tree produced by DateParser#prefix.
    def exitPrefix(self, ctx:DateParser.PrefixContext):
        pass


    # Enter a parse tree produced by DateParser#suffix.
    def enterSuffix(self, ctx:DateParser.SuffixContext):
        pass

    # Exit a parse tree produced by DateParser#suffix.
    def exitSuffix(self, ctx:DateParser.SuffixContext):
        pass



del DateParser