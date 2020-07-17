# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_get 1'] = 200

snapshots['test_get 2'] = b'<h1>Challenge!</h1>'

snapshots['test_loan_error_first_check 1'] = 400

snapshots['test_loan_error_first_check 2'] = {
    'errors': [
        {
            'cpf': 'Field is Required.'
        },
        {
            'birthdate': 'Field is Required.'
        },
        {
            'amount': 'Field is Required.'
        },
        {
            'income': 'Field is Required.'
        },
        {
            'terms': 'Field is Required.'
        }
    ]
}

snapshots['test_loan_saving 1'] = 200

snapshots['test_loan_saving 2'] = True

snapshots['test_loan_saving_error_model 1'] = 400

snapshots['test_loan_saving_error_model 2'] = {
    'errors': [
        {
            'terms': 'The terms not in [6, 9, 12]'
        }
    ]
}

snapshots['test_loan_no_api_key_provided 1'] = 401

snapshots['test_loan_no_api_key_provided 2'] = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>401 Unauthorized</title>
<h1>Unauthorized</h1>
<p>Forbidden access</p>
'''

snapshots['test_health 1'] = 200

snapshots['test_health 2'] = b"I'm fine!"
