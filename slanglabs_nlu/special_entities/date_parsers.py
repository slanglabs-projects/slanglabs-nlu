from slanglabs_nlu.special_entities.date_parsing.slangdateparser import DateExtractionListener  # noqa
from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from slanglabs_nlu.special_entities.date_parsing.DateLexer import DateLexer     # noqa
from slanglabs_nlu.special_entities.date_parsing.DateParser import DateParser     # noqa
from slanglabs_nlu.special_entities.abstract_special_entities import SpecialEntityRegexMatch  # noqa
from abc import ABC

class AbstractDateParser(ABC):

    def entity2entitytypes(self):
        return {}

    def case_sensitive(self):
        return False

    def char_index2token_index(self, text):
        start_index2token_index = {}
        end_index2token_index = {}
        token_i = 0
        start_index2token_index[0] = 0
        for chari, char in enumerate(text):
            if char == ' ':
                start_index2token_index[chari + 1] = token_i + 1
                end_index2token_index[chari - 1] = token_i
                token_i += 1
        end_index2token_index[chari] = token_i
        return start_index2token_index, end_index2token_index

    def find_in_text(self, text):
        matches = []
        start_index2token_index, end_index2token_index = self.char_index2token_index(text)    # noqa
        lexer = DateLexer(InputStream(text))
        parser = DateParser(CommonTokenStream(lexer))
        listener = DateExtractionListener(
            lexer,
            include_time=self._include_time,
            bias_to_future=self._bias_to_future,
        )
        try:
            self.walker.walk(listener, parser.utterance())
            for result in listener.results:
                start_char_index = result[1][0]
                end_char_index = result[1][1]
                normalised_value = result[0]
                start_token_index = start_index2token_index[start_char_index]  # noqa
                end_token_index = end_index2token_index[end_char_index]
                special_entity_regex_match = SpecialEntityRegexMatch(
                            entitytype=self.name(),
                            start_token_index=start_token_index,
                            end_token_index=end_token_index,
                            start_char_index=0,
                            end_char_index=0,
                            use=True,
                            normalized_value=normalised_value,
                        )
                matches.append(special_entity_regex_match)
        except Exception:
            pass
        return matches


class DateParserPast(AbstractDateParser):

    def __init__(self):
        self._include_time = False
        self._bias_to_future = False
        self.walker = ParseTreeWalker()

    def name(self):
        return 'std.dateparser.past'


class DateParserFuture(AbstractDateParser):

    def __init__(self):
        self._include_time = False
        self._bias_to_future = True
        self.walker = ParseTreeWalker()

    def name(self):
        return 'std.dateparser.future'
