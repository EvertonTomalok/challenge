# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_parse_loan_form 1'] = {
    'amount': '1000.50',
    'birthdate': '15/08/1992',
    'cpf': '12345678900',
    'income': '12000.00',
    'name': 'Everton Tomalok',
    'terms': '6'
}

snapshots['test_parse_loan_form_incomplete 1'] = {
    'amount': None,
    'birthdate': None,
    'cpf': '12345678900',
    'income': '12000.00',
    'name': 'Everton Tomalok',
    'terms': '6'
}

snapshots['test_check_loan_fields 1'] = [
]

snapshots['test_check_loan_fields_all_fields_invalid 1'] = [
    {
        'name': 'Invalid Format'
    },
    {
        'cpf': 'Invalid Format'
    },
    {
        'birthdate': 'Invalid Format'
    },
    {
        'amount': 'Invalid Format'
    },
    {
        'terms': 'Invalid Format'
    },
    {
        'income': 'Invalid Format'
    }
]

snapshots['test_check_loan_fields_missing_fields 1'] = [
    {
        'cpf': 'Field is Required.'
    },
    {
        'birthdate': 'Field is Required.'
    },
    {
        'amount': 'Field is Required.'
    }
]

snapshots['test_is_api_key_valid 1'] = True
