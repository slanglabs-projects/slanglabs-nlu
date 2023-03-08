# Copyright (c) 2017-2022 Slang Labs Private Limited. All rights reserved.

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from slanglabs_nlu.entity_extraction.dateparser import DateExtractionListener
from slanglabs_nlu.entity_extraction.generated.DateLexer import DateLexer
from slanglabs_nlu.entity_extraction.generated.DateParser import DateParser

from slanglabs_nlu.entity_extraction.numberparser import NumberExtractionListener
from slanglabs_nlu.entity_extraction.generated.NumberLexer import NumberLexer
from slanglabs_nlu.entity_extraction.generated.NumberParser import NumberParser


def parse_dates(inputstr, include_time=False, bias_to_future=True):
    try:
        lexer = DateLexer(InputStream(inputstr.lower()))
        lexer.removeErrorListeners()
        parser = DateParser(CommonTokenStream(lexer))
        parser.removeErrorListeners()
        listener = DateExtractionListener(
            lexer,
            include_time=include_time,
            bias_to_future=bias_to_future
        )
        walker = ParseTreeWalker()
        walker.walk(listener, parser.utterance())
        return listener.results
    except Exception as e:
        print(str(e))
        return []


def _parse(inputstr, with_ranges=False):
    try:
        lexer = NumberLexer(InputStream(inputstr.lower()))
        parser = NumberParser(CommonTokenStream(lexer))
        listener = NumberExtractionListener(lexer)
        walker = ParseTreeWalker()
        walker.walk(
            listener,
            parser.ranges_utterance() if with_ranges
            else parser.numbers_utterance()
        )
        return listener.results
    except Exception as e:
        print('Exception: {}!'.format(str(e)))
        return []


def parse_numbers(inputstr):
    return _parse(inputstr)


def parse_numbers_with_ranges(inputstr):
    return _parse(inputstr, with_ranges=True)


if __name__ == "__main__":
    # s = 'train tickets for 15th departure and next month 10th return'
    # print(parse_dates(s))
    s = 'so happy to give away twenty thousand to the winner'
    print(parse_numbers(s))
