# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_insert_client 1'] = {
    '_id': 'uuid-1234',
    'amount': '3000',
    'birthdate': '1992-08-15',
    'cpf': '12345678900',
    'income': '12000',
    'name': 'Everton Tomalok',
    'terms': 6
}

snapshots['test_insert_loan 1'] = 1

snapshots['test_insert_loan 2'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'refused_policy': None,
    'result': None,
    'status': 'processing',
    'terms': None
}

snapshots['test_insert_loan 3'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'refused_policy': None,
    'result': None,
    'status': 'processing',
    'terms': None
}

snapshots['test_start_process 1'] = {
    '_id': 'uuid_1234',
    'amount': '3000',
    'birthdate': '1992-08-15',
    'cpf': '12345678900',
    'income': '12000',
    'name': 'Everton Tomalok',
    'terms': 6
}

snapshots['test_start_process 2'] = {
    '_id': 'uuid_1234',
    'amount': None,
    'refused_policy': None,
    'result': None,
    'status': 'processing',
    'terms': None
}

snapshots['test_set_loan_refused_by_age 1'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'refused_policy': 'age',
    'result': 'refused',
    'status': 'completed',
    'terms': None
}

snapshots['test_set_loan_refused_by_score 1'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'metadata': {
        'score': 300
    },
    'refused_policy': 'score',
    'result': 'refused',
    'status': 'completed',
    'terms': None
}

snapshots['test_set_loan_accept 1'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': 4000.0,
    'metadata': {
        'commitment': 0.3,
        'score': 954
    },
    'refused_policy': None,
    'result': 'approved',
    'status': 'completed',
    'terms': 9
}

snapshots['test_set_loan_refused_by_pmt 1'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'metadata': {
        'commitment': 0.3,
        'score': 954
    },
    'refused_policy': 'commitment',
    'result': 'refused',
    'status': 'completed',
    'terms': None
}

snapshots['test_set_loan_task_error 1'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'metadata': {
        'err': {
            'description': 'Raising an error',
            'type': "<class 'ValueError'>"
        }
    },
    'refused_policy': None,
    'result': None,
    'status': 'processing',
    'terms': None
}

snapshots['test_delete_loan_and_cliente 1'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'refused_policy': None,
    'result': None,
    'status': 'processing',
    'terms': None
}

snapshots['test_delete_loan_and_cliente 2'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': 1900.0,
    'birthdate': '1992-08-15',
    'cpf': '12345678901',
    'income': 900.0,
    'name': 'João',
    'terms': 6
}

snapshots['test_delete_loan_and_cliente 3'] = None

snapshots['test_delete_loan_and_cliente 4'] = None
