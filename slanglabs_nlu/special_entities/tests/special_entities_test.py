import unittest

from collections import defaultdict
from slanglabs_nlu.special_entities.special_entities import SpecialEntities


def defaultdict_to_dict(d, sort_list=True):
    if isinstance(d, (defaultdict, dict)):
        d = {k: defaultdict_to_dict(v, sort_list) for k, v in d.items()}
    if isinstance(d, list) and sort_list is True:
        d = sorted(d)
    return d


class SpecialEntitiesTest(unittest.TestCase):
    def setUp(self):
        self.special_entity = SpecialEntities()

    def test_integer(self):
        special_entity = self.special_entity.find_in_text('dummy 12 dummy')
        token2types = defaultdict_to_dict(special_entity.token2types())
        chunks = defaultdict_to_dict(special_entity.chunks())
        token2special_entity = defaultdict_to_dict(special_entity.token2special_entity())  # noqa
        self.assertEqual(token2types, {1: ['std.date', 'std.date.future', 'std.date.past', 'std.float', 'std.integer', 'std.time']})  # noqa
        self.assertEqual(
            chunks,
            {1: {'std.date': range(1, 2), 'std.date.future': range(1, 2), 'std.date.past': range(1, 2), 'std.time': range(1, 2), 'std.float': range(1, 2), 'std.integer': range(1, 2)}}  # noqa
        )
        self.assertEqual(
            list(token2special_entity[1].keys()),
            ['std.date', 'std.date.future', 'std.date.past', 'std.time', 'std.float', 'std.integer']  # noqa
        )

    def test_date(self):
        special_entity = self.special_entity.find_in_text('dummy 12th October dummy')  # noqa
        token2types = defaultdict_to_dict(special_entity.token2types())
        chunks = defaultdict_to_dict(special_entity.chunks())
        self.assertEqual(
            token2types,
            {1: ['std.date', 'std.date.future', 'std.date.past'], 2: ['std.date', 'std.date.future', 'std.date.past']}  # noqa
        )
        self.assertEqual(
            chunks,
            {1: {'std.date': range(1, 3), 'std.date.future': range(1, 3), 'std.date.past': range(1, 3)}}  # noqa
        )

    def test_time(self):
        special_entity = self.special_entity.find_in_text('dummy 12:00 pm dummy')  # noqa
        token2types = defaultdict_to_dict(special_entity.token2types())
        chunks = defaultdict_to_dict(special_entity.chunks())
        self.assertEqual(
            token2types,
            {1: ['std.time'], 2: ['std.time']}
        )
        self.assertEqual(
            chunks,
            {1: {'std.time': range(1, 3)}}
        )


if __name__ == '__main__':
    unittest.main()
