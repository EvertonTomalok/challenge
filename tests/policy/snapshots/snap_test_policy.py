# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_age_policy_approve 1'] = 1

snapshots['test_age_policy_approve 2'] = None

snapshots['test_age_policy_deny 1'] = 0

snapshots['test_age_policy_deny 2'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'refused_policy': 'age',
    'result': 'refused',
    'status': 'completed',
    'terms': None
}

snapshots['test_score_policy_approve 1'] = 1

snapshots['test_score_policy_approve 2'] = None

snapshots['test_score_policy_deny 1'] = 0

snapshots['test_score_policy_deny 2'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'metadata': {
        'score': 131
    },
    'refused_policy': 'score',
    'result': 'refused',
    'status': 'completed',
    'terms': None
}

snapshots['test_commitment_approve 1'] = 1

snapshots['test_commitment_approve 2'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': 1000,
    'metadata': {
        'commitment': 0.9,
        'score': 900
    },
    'refused_policy': None,
    'result': 'approved',
    'status': 'completed',
    'terms': 9
}

snapshots['test_commitment_deny 1'] = 0

snapshots['test_commitment_deny 2'] = {
    '_id': 'a3289e62-c171-11ea-81ba-0242c0a88005',
    'amount': None,
    'metadata': {
        'commitment': 0.9,
        'score': 600
    },
    'refused_policy': 'commitment',
    'result': 'refused',
    'status': 'completed',
    'terms': None
}
