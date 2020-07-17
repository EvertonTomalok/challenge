# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_mount_df 1'] = [
    6,
    9,
    12
]

snapshots['test_normalize_score[701] 1'] = 700

snapshots['test_normalize_score[831] 1'] = 800

snapshots['test_normalize_score[988] 1'] = 900

snapshots['test_get_rate[650-6] 1'] = 0.064

snapshots['test_get_rate[701-12] 1'] = 0.061

snapshots['test_get_rate[831-9] 1'] = 0.05

snapshots['test_get_rate[988-6] 1'] = 0.039

snapshots['test_normalize_score[600] 1'] = 600

snapshots['test_normalize_score[679] 1'] = 600

snapshots['test_normalize_score[1000] 1'] = 900
