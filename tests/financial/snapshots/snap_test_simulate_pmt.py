# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_pmt_calculate 1'] = 380.28266841167584

snapshots['test_pmt_available 1'] = 1

snapshots['test_pmt_available 2'] = 286.85597559800516

snapshots['test_pmt_available 3'] = 12

snapshots['test_pmt_available 4'] = 'Loan is available'

snapshots['test_pmt_not_available 1'] = 0

snapshots['test_pmt_not_available 2'] = 'Loan is not available'
