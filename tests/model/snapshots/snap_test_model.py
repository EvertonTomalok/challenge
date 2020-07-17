# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_parse_and_validate 1'] = {
    'amount': '4000',
    'birthdate': '1992-08-15',
    'cpf': '12345678900',
    'income': '12000',
    'name': 'Everton Tomalok',
    'terms': 6
}

snapshots['test_client 1'] = {
    'amount': '4000',
    'birthdate': '1992-08-15',
    'cpf': '12345678900',
    'income': '12000',
    'name': 'Everton Tomalok',
    'terms': 6
}

snapshots['test_client_data_error 1'] = {
    'data_received': {
        'birthdate': '1992-08-15',
        'income': 12000,
        'name': 'Everton Tomalok',
        'terms': 6
    },
    'fields_with_error': [
        {
            'cpf': 'This field is required.'
        },
        {
            'amount': 'This field is required.'
        }
    ]
}

snapshots['test_client_data_min_max_value_error 1'] = {
    'data_received': {
        'amount': 6000,
        'birthdate': '1992-08-15',
        'cpf': '12345678900',
        'income': 12000,
        'name': 'Everton Tomalok',
        'terms': 3
    },
    'fields_with_error': [
        {
            'amount': 'The amount must to be between 1000.00 - 4000.00'
        },
        {
            'terms': 'The terms not in [6, 9, 12]'
        }
    ]
}

snapshots['test_loan_initialize 1'] = {
    '_id': 'uuid-1234',
    'amount': None,
    'refused_policy': None,
    'result': None,
    'status': 'processing',
    'terms': None
}

snapshots['test_loan_no_uuid 1'] = {
    'data_received': {
        'terms': 6
    },
    'fields_with_error': [
        {
            '_id': 'This field is required.'
        }
    ]
}

snapshots['test_loan_error_amount_and_terms 1'] = {
    'data_received': {
        '_id': 'uuid-5678',
        'amount': 10000,
        'terms': 15
    },
    'fields_with_error': [
        {
            'amount': 'Decimal value should be less than or equal to 4000.'
        },
        {
            'terms': 'Int value should be less than or equal to 12.'
        }
    ]
}
