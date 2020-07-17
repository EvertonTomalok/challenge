# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_normalize_cpf 1'] = '12345678900'

snapshots['test_transform_cpf[12345678900] 1'] = '123.456.789-00'

snapshots['test_transform_cpf[98765432111] 1'] = '987.654.321-11'

snapshots['test_transform_cpf[98076543244] 1'] = '980.765.432-44'

snapshots['test_check_and_return_amount_float 1'] = 1000.0

snapshots['test_check_and_return_term_int 1'] = 6
