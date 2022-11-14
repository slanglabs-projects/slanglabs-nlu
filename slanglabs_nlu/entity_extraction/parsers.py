# Copyright (c) 2017-2022 Slang Labs Private Limited. All rights reserved.

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from slanglabs_nlu.entity_extraction.dateparser import DateExtractionListener
from slanglabs_nlu.entity_extraction.generated.DateLexer import DateLexer
from slanglabs_nlu.entity_extraction.generated.DateListener import DateListener
from slanglabs_nlu.entity_extraction.generated.DateParser import DateParser


def parse_dates(val, include_time=False, bias_to_future=True):
    try:
        lexer = DateLexer(InputStream(val.lower()))
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

if __name__ == "__main__":
    val = 'train tickets for 15th departure and next month 10th return'
    print(parse_dates(val))