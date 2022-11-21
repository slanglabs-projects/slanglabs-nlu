# Copyright (c) 2017-2021 Slang Labs Private Limited. All rights reserved.

import re
from collections import defaultdict
from typing import Dict, List

from slang.brahman.assistant_version import AssistantVersion
from slang.brahman.protocol import SlangRequest
from slang.vedvyasa import VEDVYASA_VERSION
from slang.vedvyasa.datatypes.vedvyasa_infer_request import VedVyasaInferRequest  # noqa


def safe_divide(num, den):
    if den == 0:
        return 0
    else:
        return float(num) / den


def normalize_fn(value, total):
    return safe_divide(value, total)


def defaultdict_to_dict(d, sort_list=True):
    if isinstance(d, (defaultdict, dict)):
        d = {k: defaultdict_to_dict(v, sort_list) for k, v in d.items()}
    if isinstance(d, list) and sort_list is True:
        d = sorted(d)
    return d


def normalize_str(string):
    string = re.sub(r'[!"#$*,\/;<=>?[\]^_`{|}~]+', '', string)  # noqa  Remove special characters
    string = re.sub(r'[()]', ' ', string)
    return string.strip().lower()


class VedVyasaServiceError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def ctx_entities2entities(ctx_entities, top=True, is_list=False):
    entities = {}
    if is_list is True and isinstance(ctx_entities, Dict) and ctx_entities['is_composite'] is False:  # noqa
        return ctx_entities['str_val']
    for entity_name, entity_value in ctx_entities.items():
        if isinstance(entity_value, List):
            entities[entity_name] = [ctx_entities2entities(e, top=False, is_list=True) for e in entity_value]  # noqa
        elif isinstance(entity_value, Dict):
            children = {}
            if entity_value.get('is_composite', True) is False:
                entities.update({entity_value['key']: entity_value['str_val']})
                continue
            for item_value in entity_value.values():
                if item_value['is_composite'] is False:
                    key = item_value['key']
                    value = item_value['str_val']
                    if top is True:
                        children[key] = value
                        entities.update({entity_name: children})
                    else:
                        entities[key] = value
                elif item_value['is_composite'] is True:
                    v = ctx_entities2entities(item_value['composite_values'], top=False)  # noqa
                    entities.update({item_value['key']: v})
        elif top is True and not isinstance(entity_value, (List, Dict)):
            entities[entity_name] = entity_value
    return entities


def slang2vedvyasarequest(slang_request: SlangRequest, assistant_version: AssistantVersion, query_str: str) -> VedVyasaInferRequest:  # noqa
    if slang_request.is_context_empty() is True:
        context_intent_name = ''
        context_intent_status = 0
        context_resolved_entities = {}
        context_entities_to_fill = []
        is_strict_intent_mode = False
        is_strict_entity_mode = False
    else:
        context_intent_name = slang_request.context_intent_name()
        context_intent_status = slang_request.intent_status()
        context_resolved_entities = slang_request.context_resolved_entities()
        context_entities_to_fill = slang_request.context_entities_to_resolve()
        is_strict_intent_mode = slang_request.is_strict_intent_mode()
        is_strict_entity_mode = slang_request.is_strict_entity_mode()
    return VedVyasaInferRequest.create(
        app_id=slang_request.app_id(),
        request_id=slang_request.request_id(),
        assistant_version=assistant_version,
        text=query_str,
        context_intent_name=context_intent_name,
        context_intent_status=context_intent_status,
        context_resolved_entities=context_resolved_entities,
        context_entities_to_fill=context_entities_to_fill,
        is_strict_intent_mode=is_strict_intent_mode,
        is_strict_entity_mode=is_strict_entity_mode,
    )


def action2url(endpoint: str, action: str, paras: Dict) -> str:
    paras.update({'version': VEDVYASA_VERSION.strip('/')})
    APP_URI_FORMAT_STR = '{version}/applications/{app_id}/'
    ASSISTANT_URI_FORMAT_STR = '{version}/assistants/{app_id}/'
    ENV_PARA_FORMAT_STR = 'env={env}'
    ASSISTANT_VERSION_PARA_FORMAT_STR = 'assistant_version={assistant_version}'
    actions = {
        'infer': APP_URI_FORMAT_STR + 'text2intent?' + ENV_PARA_FORMAT_STR,
        'train': APP_URI_FORMAT_STR + '?' + ENV_PARA_FORMAT_STR,
        'delete': APP_URI_FORMAT_STR + '?' + ENV_PARA_FORMAT_STR,
        'assistant_infer': ASSISTANT_URI_FORMAT_STR + 'text2intent?' + ENV_PARA_FORMAT_STR,   # noqa
        'assistant_train': ASSISTANT_URI_FORMAT_STR + '?' + ENV_PARA_FORMAT_STR + '&' + ASSISTANT_VERSION_PARA_FORMAT_STR,  # noqa
        'assistant_delete': ASSISTANT_URI_FORMAT_STR + '?' + ENV_PARA_FORMAT_STR + '&' + ASSISTANT_VERSION_PARA_FORMAT_STR,  # noqa
    }
    url = endpoint.strip('/') + '/' + actions[action].strip('/').format(**paras)  # noqa
    return url
