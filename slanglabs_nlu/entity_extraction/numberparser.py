# Copyright (c) 2017-2022 Slang Labs Private Limited. All rights reserved.

from slanglabs_nlu.entity_extraction.generated.NumberListener import NumberListener
from slanglabs_nlu.entity_extraction.generated.NumberParser import NumberParser

UNIT = 1
TEN = UNIT * 10
HUNDRED = TEN * 10
THOUSAND = HUNDRED * 10
LAKH = THOUSAND * 100
CRORE = LAKH * 100


FRACTIONS_MAP = {
    'half': '0.5',
    'quarter': '0.25',
    'three fourth': '0.75',
    'three fourths': '0.75',
}

NUMBERS_MAP = {
    'oh': 0,
    'not': 0,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninty': 90,
    'hundred': HUNDRED,
    'hundreds': HUNDRED,
    'thousand': THOUSAND,
    'thousands': THOUSAND,
    'lakh': LAKH,
    'lakhs': LAKH,
    'crore': CRORE,
    'crores': CRORE,
}


def norm(c):
    if isinstance(c, list):
        return [norm(elem) for elem in c]
    return str(c).lower().strip()


def parse_units(ctx):
    units = 0

    if ctx.WORD_NUMBER_UNITS():
        units = NUMBERS_MAP[norm(ctx.WORD_NUMBER_UNITS())]
    elif ctx.NUMBER_UNITS():
        units = float(norm(ctx.NUMBER_UNITS()))

    return units


def parse_tens(ctx):
    tens = 0

    if ctx.WORD_NUMBER_TENS():
        tens = NUMBERS_MAP[norm(ctx.WORD_NUMBER_TENS())]
    elif ctx.NUMBER_TENS():
        tens = float(norm(ctx.NUMBER_TENS()))

    return tens


def parse_hundreds(ctx, prefix=1, suffix=0):
    if ctx.WORD_NUMBER_HUNDREDS():
        return float(
            prefix * NUMBERS_MAP[norm(ctx.WORD_NUMBER_HUNDREDS())]
            + suffix
        )

    if ctx.NUMBER_HUNDREDS():
        return float(norm(ctx.NUMBER_HUNDREDS()))

    hundreds = tens = units = 0
    children = [norm(c) for c in ctx.getChildren()]
    for i in range(3):
        idx = -1
        if ctx.WORD_NUMBER_UNITS(i):
            tmp = norm(ctx.WORD_NUMBER_UNITS(i))
            if tmp in children:
                idx = children.index(tmp)
            if idx == 0:
                hundreds = NUMBERS_MAP[tmp]
            elif idx == 1:
                tens = NUMBERS_MAP[tmp]
            elif idx == 2:
                units = NUMBERS_MAP[tmp]

        idx = -1
        if ctx.NUMBER_UNITS(i):
            tmp = norm(ctx.NUMBER_UNITS(i))
            if tmp in children:
                idx = children.index(tmp)
            if idx == 0:
                hundreds = float(tmp)
            elif idx == 1:
                tens = float(tmp)
            elif idx == 2:
                units = float(tmp)

    return hundreds * 100 + tens + units


def parse_thousands(ctx, prefix=1, suffix=0):
    if ctx.WORD_NUMBER_THOUSANDS():
        return float(
            prefix * NUMBERS_MAP[norm(ctx.WORD_NUMBER_THOUSANDS())]
            + suffix
        )

    if ctx.NUMBER_THOUSANDS():
        try:
            return float(norm(ctx.NUMBER_THOUSANDS()))
        except ValueError:
            return float(norm(ctx.NUMBER_THOUSANDS()))

    upper = lower = 0
    children = [norm(c) for c in ctx.getChildren()]
    for i in range(2):
        idx = -1
        if ctx.WORD_NUMBER_TENS(i):
            tmp = norm(ctx.WORD_NUMBER_TENS(i))
            if tmp in children:
                idx = children.index(tmp)
            if idx == 0:
                upper = NUMBERS_MAP[tmp]
            elif idx == 1:
                lower = NUMBERS_MAP[tmp]

        idx = -1
        if ctx.NUMBER_TENS(i):
            tmp = norm(ctx.NUMBER_TENS(i))
            if tmp in children:
                idx = children.index(tmp)
            if idx == 0:
                upper = float(tmp)
            if idx == 1:
                lower = float(tmp)

    return upper * 100 + lower


def parse_lakhs(ctx, prefix=1, suffix=0):
    if ctx.WORD_NUMBER_LAKHS():
        return float(
            prefix * NUMBERS_MAP[norm(ctx.WORD_NUMBER_LAKHS())]
            + suffix
        )

    if ctx.NUMBER_LAKHS():
        try:
            return float(norm(ctx.NUMBER_LAKHS()))
        except ValueError:
            return float(norm(ctx.NUMBER_LAKHS()))

    return 0


def parse_crores(ctx, prefix=1, suffix=0):
    if ctx.WORD_NUMBER_CRORES():
        return float(
            prefix * NUMBERS_MAP[norm(ctx.WORD_NUMBER_CRORES())]
            + suffix
        )

    if ctx.NUMBER_CRORES():
        return float(norm(ctx.NUMBER_CRORES()))

    return 0


def parse_fraction(ctx):
    if ctx.WORD_NUMBER_FRACTIONS():
        return float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

    return 0


def magnitude(val):
    magnitudes = [CRORE, LAKH, THOUSAND, HUNDRED, TEN, UNIT]
    val = float(val)
    for m in magnitudes:
        div = int(val / m)
        if div > 0:
            return div, m
    return 1, UNIT


class NumberExtractionListener(NumberListener):
    def __init__(self, lexer):
        self.lexer = lexer
        self.results = []
        self.crores = self.lakhs = self.thousands = 0
        self.hundreds = self.tens = self.units = 0
        self.spl_crores = self.spl_lakhs = self.spl_thousands = 0
        self.spl_hundreds = self.spl_tens = self.spl_units = 0
        self.prefix = 0
        self.prefixes = []
        self.suffixes = []
        self.result = 0

    def reset(self):
        self.results = []
        self.reset_numbers()

    def reset_numbers(self):
        self.crores = self.lakhs = self.thousands = 0
        self.hundreds = self.tens = self.units = 0
        self.spl_crores = self.spl_lakhs = self.spl_thousands = 0
        self.spl_hundreds = self.spl_tens = self.spl_units = 0

    def handle_enter_prefix(self):
        self.reset_numbers()

    def handle_enter_suffix(self):
        self.reset_numbers()

    def handle_exit_prefix(self):
        tmp = (self.crores + self.lakhs + self.thousands
               + self.hundreds + self.tens + self.units)
        self.prefixes[-1] += tmp
        self.reset_numbers()

    def handle_exit_suffix(self):
        tmp = (self.crores + self.lakhs + self.thousands
               + self.hundreds + self.tens + self.units)
        self.suffixes[-1] += tmp
        self.reset_numbers()

    def enterNumbers_utterance(self, ctx: NumberParser.Numbers_utteranceContext):  # noqa
        self.reset()

    def enterRanges_utterance(self, ctx: NumberParser.Ranges_utteranceContext):  # noqa
        self.reset()

    def exitRange_pattern(self, ctx: NumberParser.Range_patternContext):
        if len(self.results) != 2:
            return

        first = self.results[0][0]
        second = self.results[1][0]

        if first > second:
            return

        fdiv, fmag = magnitude(first)
        sdiv, smag = magnitude(second)

        if fdiv > sdiv:
            return

        smag2 = magnitude(sdiv)[1]
        if fmag == smag2 or fmag == smag2/10:
            self.results[0] = fdiv * fmag * smag, self.results[0][1]

    def enterNumber_pattern(self, ctx: NumberParser.Number_patternContext):
        self.reset_numbers()

    def exitNumber_pattern(self, ctx: NumberParser.Number_patternContext):
        # print('c:{} l:{} t:{} h:{} t:{} u:{}'.format(
        #     self.crores,
        #     self.lakhs,
        #     self.thousands,
        #     self.hundreds,
        #     self.tens,
        #     self.units,
        # ))

        tmp = (self.crores + self.lakhs + self.thousands
               + self.hundreds + self.tens + self.units)

        if isinstance(tmp, float) and tmp.is_integer():  # noqa
            tmp = int(tmp)

        istream = self.lexer.inputStream
        text = istream.getText(0, istream.size)
        start = ctx.start.start
        stop = ctx.stop.stop
        while text[start] == ' ':
            start += 1
        while text[stop] == ' ':
            stop -= 1

        if stop >= start:
            self.results.append((tmp, (start, stop)))

    def enterCrores_format(self, ctx: NumberParser.Crores_formatContext):
        self.prefixes.append(0)
        self.suffixes.append(0)

    def exitCrores_format(self, ctx: NumberParser.Crores_formatContext):
        prefix = self.prefixes.pop()
        prefix = max(1, prefix)

        suffix = self.suffixes.pop()

        fraction = 0
        if ctx.WORD_NUMBER_FRACTIONS():
            fraction = float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

        self.crores = parse_crores(ctx, prefix, suffix) + fraction
        if self.crores == 0 and self.spl_crores != 0:
            self.crores = prefix * self.spl_crores + suffix + fraction

    def enterPrefix_crores(self, ctx: NumberParser.Prefix_croresContext):
        self.handle_enter_prefix()

    def exitPrefix_crores(self, ctx: NumberParser.Prefix_croresContext):
        self.handle_exit_prefix()

    def enterSuffix_crores(self, ctx: NumberParser.Suffix_croresContext):
        self.handle_enter_suffix()

    def exitSuffix_crores(self, ctx: NumberParser.Suffix_croresContext):
        self.handle_exit_suffix()

    def enterLakhs_format(self, ctx: NumberParser.Lakhs_formatContext):
        self.prefixes.append(0)
        self.suffixes.append(0)

    def exitLakhs_format(self, ctx: NumberParser.Lakhs_formatContext):
        prefix = self.prefixes.pop()
        prefix = max(1, prefix)
        suffix = self.suffixes.pop()

        fraction = 0
        if ctx.WORD_NUMBER_FRACTIONS():
            fraction = float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

        self.lakhs = parse_lakhs(ctx, prefix, suffix) + fraction
        if self.lakhs == 0 and self.spl_lakhs != 0:
            self.lakhs = prefix * self.spl_lakhs + suffix + fraction

    def enterPrefix_lakhs(self, ctx: NumberParser.Prefix_lakhsContext):
        self.handle_enter_prefix()

    def exitPrefix_lakhs(self, ctx: NumberParser.Prefix_lakhsContext):
        self.handle_exit_prefix()

    def enterSuffix_lakhs(self, ctx: NumberParser.Suffix_lakhsContext):
        self.handle_enter_suffix()

    def exitSuffix_lakhs(self, ctx: NumberParser.Suffix_lakhsContext):
        self.handle_exit_suffix()

    def enterThousands_format(self, ctx: NumberParser.Thousands_formatContext):
        self.prefixes.append(0)
        self.suffixes.append(0)

    def exitThousands_format(self, ctx: NumberParser.Thousands_formatContext):
        prefix = self.prefixes.pop()
        prefix = max(1, prefix)
        suffix = self.suffixes.pop()

        fraction = 0
        if ctx.WORD_NUMBER_FRACTIONS():
            fraction = float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

        self.thousands = parse_thousands(ctx, prefix, suffix) + fraction
        if self.thousands == 0 and self.spl_thousands != 0:
            self.thousands = prefix * self.spl_thousands + suffix + fraction

    def enterPrefix_thousands(self, ctx: NumberParser.Prefix_thousandsContext):
        self.handle_enter_prefix()

    def exitPrefix_thousands(self, ctx: NumberParser.Prefix_thousandsContext):
        self.handle_exit_prefix()

    def enterSuffix_thousands(self, ctx: NumberParser.Suffix_thousandsContext):
        self.handle_enter_suffix()

    def exitSuffix_thousands(self, ctx: NumberParser.Suffix_thousandsContext):
        self.handle_exit_suffix()

    def enterHundreds_format(self, ctx: NumberParser.Hundreds_formatContext):
        self.prefixes.append(0)
        self.suffixes.append(0)

    def exitHundreds_format(self, ctx: NumberParser.Hundreds_formatContext):
        prefix = self.prefixes.pop()
        prefix = max(1, prefix)
        suffix = self.suffixes.pop()

        fraction = 0
        if ctx.WORD_NUMBER_FRACTIONS():
            fraction = float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

        if ctx.WORD_NUMBER_HUNDREDS():
            self.hundreds = prefix * NUMBERS_MAP[
                norm(ctx.WORD_NUMBER_HUNDREDS())
            ] + suffix + fraction

        elif ctx.NUMBER_HUNDREDS():
            self.hundreds = float(norm(ctx.NUMBER_HUNDREDS()))
        elif self.spl_hundreds != 0:
            self.hundreds = prefix * self.spl_hundreds + fraction
        else:
            units = tens = hundreds = 0
            if ctx.WORD_NUMBER_UNITS(0):
                hundreds = NUMBERS_MAP[norm(ctx.WORD_NUMBER_UNITS(0))]
            elif ctx.NUMBER_UNITS(0):
                hundreds = float(norm(ctx.NUMBER_UNITS(0)))

            if ctx.WORD_NUMBER_TENS():
                tens = NUMBERS_MAP[norm(ctx.WORD_NUMBER_TENS())]
            elif ctx.NUMBER_TENS():
                tens = float(norm(ctx.NUMBER_TENS()))
            else:
                children = [norm(c) for c in ctx.getChildren()]
                for i in range(3):
                    idx = -1
                    if ctx.WORD_NUMBER_UNITS(i):
                        tmp = norm(ctx.WORD_NUMBER_UNITS(i))
                        if tmp in children:
                            idx = children.index(tmp)
                        if idx == 0:
                            hundreds = NUMBERS_MAP[tmp]
                        elif idx == 1:
                            tens = NUMBERS_MAP[tmp]
                        elif idx == 2:
                            units = NUMBERS_MAP[tmp]

                    idx = -1
                    if ctx.NUMBER_UNITS(i):
                        tmp = norm(ctx.NUMBER_UNITS(i))
                        if tmp in children:
                            idx = children.index(tmp)
                        if idx == 0:
                            hundreds = float(tmp)
                        elif idx == 1:
                            tens = float(tmp)
                        elif idx == 2:
                            units = float(tmp)

            if hundreds > 0 or tens > 0 or units > 0:
                self.hundreds = hundreds * 100 + tens + units + fraction

    def enterPrefix_hundreds(self, ctx: NumberParser.Prefix_hundredsContext):
        self.handle_enter_prefix()

    def exitPrefix_hundreds(self, ctx: NumberParser.Prefix_hundredsContext):
        self.handle_exit_prefix()

    def enterSuffix_hundreds(self, ctx: NumberParser.Suffix_hundredsContext):
        self.handle_enter_suffix()

    def exitSuffix_hundreds(self, ctx: NumberParser.Suffix_hundredsContext):
        self.handle_exit_suffix()

    def enterTens_format(self, ctx: NumberParser.Tens_formatContext):
        self.prefixes.append(0)
        self.suffixes.append(0)

    def exitTens_format(self, ctx: NumberParser.Tens_formatContext):
        self.prefixes.pop()
        self.suffixes.pop()

        fraction = 0
        if ctx.WORD_NUMBER_FRACTIONS():
            fraction = float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

        self.tens = parse_tens(ctx) + fraction

    def enterUnits_format(self, ctx: NumberParser.Units_formatContext):
        self.prefixes.append(0)
        self.suffixes.append(0)

    def exitUnits_format(self, ctx: NumberParser.Units_formatContext):
        self.prefixes.pop()
        self.suffixes.pop()

        fraction = 0
        if ctx.WORD_NUMBER_FRACTIONS():
            fraction = float(FRACTIONS_MAP[norm(ctx.WORD_NUMBER_FRACTIONS())])

        self.units = parse_units(ctx) + fraction

    def exitSpl_crores(self, ctx: NumberParser.Spl_croresContext):
        self.spl_crores = 20000000

    def exitSpl_lakhs(self, ctx: NumberParser.Spl_lakhsContext):
        self.spl_lakhs = 200000

    def exitSpl_thousands(self, ctx: NumberParser.Spl_thousandsContext):
        self.spl_thousands = 2000

    def exitSpl_hundreds(self, ctx: NumberParser.Spl_hundredsContext):
        tens = parse_tens(ctx)
        self.spl_hundreds = 200 + tens

    def exitSpl_hundreds_1(self, ctx: NumberParser.Spl_hundreds_1Context):
        tens = self.spl_tens
        units = parse_units(ctx)
        self.hundreds = tens * 10 + units

    def exitSpl_hundreds_2(self, ctx: NumberParser.Spl_hundreds_2Context):
        hundreds = parse_units(ctx)
        self.hundreds = hundreds * 100 + self.spl_tens

    def exitSpl_hundreds_3(self, ctx: NumberParser.Spl_hundreds_3Context):
        units = 2
        tens = 0
        hundreds = 0

        if ctx.WORD_NUMBER_UNITS(1):
            tens = NUMBERS_MAP[norm(ctx.WORD_NUMBER_UNITS(1))]
        elif ctx.NUMBER_UNITS(1):
            tens = float(norm(ctx.NUMBER_UNITS(1)))

        if ctx.WORD_NUMBER_UNITS(0):
            hundreds = NUMBERS_MAP[norm(ctx.WORD_NUMBER_UNITS(0))]
        elif ctx.NUMBER_UNITS(0):
            hundreds = float(norm(ctx.NUMBER_UNITS(0)))

        self.hundreds = hundreds * 100 + tens * 10 + units

    def exitSpl_hundreds_4(self, ctx: NumberParser.Spl_hundreds_4Context):
        units = 2
        tens = self.spl_tens
        self.hundreds = tens * 10 + units

    def exitSpl_tens(self, ctx: NumberParser.Spl_tensContext):
        units = parse_units(ctx)
        self.spl_tens = 20 + units

    def exitSpl_epilogue(self, ctx: NumberParser.Spl_epilogueContext):
        self.spl_units = 2
