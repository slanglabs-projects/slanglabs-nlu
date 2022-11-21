from abc import abstractmethod
from typing import Dict
import regex

REGEX_SEPARATOR = ' | '


class AbstractSpecialEntities:

    def regexes(self):
        return self._regexes

    def entity2entitytypes(self):
        return {}

    def case_sensitive(self):
        return False

    def _is_overlap(self, s1, s2):
        return s1[0] <= s2[0] <= s1[1] or s1[0] <= s2[1] <= s1[1]

    def _is_not_overlap(self, spans, span):
        overlap = False
        s2 = span
        for s1 in spans:
            overlap1 = self._is_overlap(s1, s2)
            overlap2 = self._is_overlap(s2, s1)
            if overlap1 or overlap2:
                overlap = True
        return not overlap

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

    def _use_regex(self, start_index2token_index: Dict,
                   end_index2token_index: Dict, start_char_index: int,
                   end_char_index: int) -> bool:
        return start_char_index in start_index2token_index and end_char_index in end_index2token_index  # noqa

    def _get_previous_spans(self, matching_regexes):
        return [i.char_span() for i in matching_regexes]

    def find_in_text(self, text):
        matching_regexes = []
        start_index2token_index, end_index2token_index = self.char_index2token_index(text)  # noqa
        spans = self._get_previous_spans(matching_regexes)
        for regex_pattern in self.regexes():
            found_patterns = regex.finditer(regex_pattern, text, concurrent=True)      # noqa
            for found_pattern in found_patterns:
                total_span = found_pattern.span()
                start_char_index = total_span[0]
                end_char_index = total_span[1] - 1
                use_regex = self._use_regex(start_index2token_index, end_index2token_index, start_char_index, end_char_index)  # noqa
                if use_regex and self._is_not_overlap(spans, total_span):
                    spans.append(total_span)
                    start_token_index = start_index2token_index[start_char_index]  # noqa
                    end_token_index = end_index2token_index[end_char_index]
                    if all(i is not None for i in [start_token_index, end_token_index]):  # noqa
                        use, normalized_value = self.normalize(found_pattern)
                        special_entity_regex_match = SpecialEntityRegexMatch(
                            entitytype=self.name(),
                            start_token_index=start_token_index,
                            end_token_index=end_token_index,
                            start_char_index=start_char_index,
                            end_char_index=end_char_index,
                            use=use,
                            normalized_value=normalized_value,
                        )
                        matching_regexes.append(special_entity_regex_match)
        return matching_regexes

    @abstractmethod
    def normalize(self, found_pattern):
        raise NotImplementedError


class SpecialEntityRegexMatch():
    def __init__(self, entitytype: str, start_token_index: int,
                 end_token_index: int, start_char_index: int,
                 end_char_index: int, use: bool, normalized_value: str):
        self._entitytype = entitytype
        self._start_token_index = start_token_index
        self._end_token_index = end_token_index
        self._start_char_index = start_char_index
        self._end_char_index = end_char_index
        self._use = use
        self._normalized_value = normalized_value

    def start_char_index(self):
        return self._start_char_index

    def end_char_index(self):
        return self._end_char_index

    def start_token_index(self):
        return self._start_token_index

    def end_token_index(self):
        return self._end_token_index

    def token_span(self):
        return (self._start_token_index, self._end_token_index)

    def char_span(self):
        return (self._start_char_index, self._end_char_index)

    def entitytype(self):
        return self._entitytype

    def use(self):
        return self._use

    def normalized_value(self):
        return self._normalized_value
