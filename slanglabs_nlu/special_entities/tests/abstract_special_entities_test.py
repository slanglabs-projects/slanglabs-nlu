import unittest

from slanglabs_nlu.special_entities.abstract_special_entities import (
    SpecialEntityRegexMatch
)


class SpecialEntityRegexMatchTest(unittest.TestCase):
    def test_special_entity_regex_match(self):
        match = SpecialEntityRegexMatch(
            entitytype='entitytype',
            start_token_index=2,
            end_token_index=5,
            start_char_index=3,
            end_char_index=10,
            use=True,
            normalized_value='normalized_value',
        )
        self.assertEqual(match.entitytype(), 'entitytype')
        self.assertEqual(match.normalized_value(), 'normalized_value')
        self.assertEqual(match.start_token_index(), 2)
        self.assertEqual(match.end_token_index(), 5)
        self.assertEqual(match.start_char_index(), 3)
        self.assertEqual(match.end_char_index(), 10)
        self.assertTrue(match.use())


if __name__ == '__main__':
    unittest.main()
