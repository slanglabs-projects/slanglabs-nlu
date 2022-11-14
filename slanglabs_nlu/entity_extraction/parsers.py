from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from slanglabs_nlu.entity_extraction.generated.DateLexer import DateLexer
from slanglabs_nlu.entity_extraction.generated.DateListener import DateListener  # noqa
from slanglabs_nlu.entity_extraction.generated.DateParser import DateParser
from slanglabs_nlu.entity_extraction.dateparser import DateExtractionListener

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