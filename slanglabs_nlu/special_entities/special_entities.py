from collections import defaultdict

from slanglabs_nlu.special_entities.date_entity import DateEntity, DateEntityFuture, DateEntityPast  # noqa
from slanglabs_nlu.special_entities.time_entity import TimeEntity
from slanglabs_nlu.special_entities.money_composite_entity import MoneyCompositeEntity  # noqa
from slanglabs_nlu.special_entities.number_entity import NumberEntity, IntegerNumberEntity  # noqa
from slanglabs_nlu.special_entities.weight_entity import WeightEntityKilogram, WeightEntityMilligram  # noqa
from slanglabs_nlu.special_entities.volume_entity import VolumeEntityLitre, VolumeEntityMillilitre  # noqa
from slanglabs_nlu.special_entities.weight_composite_entity import WeightCompositeEntity  # noqa
from slanglabs_nlu.special_entities.volume_composite_entity import VolumeCompositeEntity  # noqa
from slanglabs_nlu.special_entities.date_parsers import DateParserFuture, DateParserPast  # noqa


special_entities_list = [
    'std.date',
    'std.date.future',
    'std.date.past',
    'std.time',
    'std.duration',
    'std.money',
    'std.weight',
    'std.weight.kilogram',
    'std.weight.milligram',
    'std.volume',
    'std.volume.litre',
    'std.volume.millilitre',
    'std.integer',
    'std.float',
    'std.dateparser.past',
    'std.dateparser.future'
]

special_entities_classes = [
    DateEntity(),
    DateEntityFuture(),
    DateEntityPast(),
    TimeEntity(),
    MoneyCompositeEntity(),
    WeightCompositeEntity(),
    WeightEntityKilogram(),
    WeightEntityMilligram(),
    VolumeCompositeEntity(),
    VolumeEntityLitre(),
    VolumeEntityMillilitre(),
    NumberEntity(),
    IntegerNumberEntity(),
]

special_entitytype2classes_mappings = {
    'std.date': DateEntity(),
    'std.date.future': DateEntityFuture(),
    'std.date.past': DateEntityPast(),
    'std.time': TimeEntity(),
    'std.duration': TimeEntity(),
    'std.money': MoneyCompositeEntity(),
    'std.weight': WeightCompositeEntity(),
    'std.weight.kilogram': WeightEntityKilogram(),
    'std.weight.milligram': WeightEntityMilligram(),
    'std.volume': VolumeCompositeEntity(),
    'std.volume.litre': VolumeEntityLitre,
    'std.volume.millilitre': VolumeEntityMillilitre(),
    'std.integer': IntegerNumberEntity(),
    'std.float': NumberEntity(),
    'std.dateparser.future': DateParserFuture(),
    'std.dateparser.past': DateParserPast()
}


class SpecialEntities():
    def __init__(self):
        self._token2types = defaultdict(lambda: [])
        self._chunks = defaultdict(lambda: defaultdict(lambda: []))  # noqa
        self._token2special_entity = defaultdict(lambda: defaultdict(lambda: []))  # noqa
        self._entity2entitytypes = {}

    def find_in_text(self, text, special_entitytypes=[]):
        matching_regexes_list = []
        if special_entitytypes:
            required_special_entities_classes = [special_entitytype2classes_mappings[special_entitytype] for special_entitytype in special_entitytypes]   # noqa
        else:
            required_special_entities_classes = special_entities_classes
        for special_entity in required_special_entities_classes:
            if not special_entity.case_sensitive():
                matching_regexes_list.extend(special_entity.find_in_text(text.lower()))  # noqa
            else:
                matching_regexes_list.extend(special_entity.find_in_text(text))  # noqa
            self._entity2entitytypes.update(special_entity.entity2entitytypes())  # noqa
        token2length = defaultdict(lambda: 0)
        for match in matching_regexes_list:
            start_token_index = match.start_token_index()
            end_token_index = match.end_token_index()
            regex_length = end_token_index + 1 - start_token_index
            if token2length[start_token_index] == 0:
                token2length[start_token_index] = regex_length
            elif token2length[start_token_index] < regex_length:
                token2length[start_token_index] = regex_length
        for match in matching_regexes_list:
            start_token_index = match.start_token_index()
            end_token_index = match.end_token_index()
            regex_length = end_token_index + 1 - start_token_index
            if regex_length == token2length[start_token_index] and match.use():
                for tokeni in range(start_token_index, end_token_index + 1):
                    self._token2types[tokeni].append(match.entitytype())
                self._token2special_entity[start_token_index][match.entitytype()] = match  # noqa
                self._chunks[start_token_index][match.entitytype()] = range(start_token_index, end_token_index + 1)  # noqa
        return self

    def entity2entitytypes(self):
        return self._entity2entitytypes

    def token2types(self):
        return self._token2types

    def chunks(self):
        return self._chunks

    def token2special_entity(self):
        return self._token2special_entity
