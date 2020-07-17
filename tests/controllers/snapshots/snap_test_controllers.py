# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_url 1'] = {
    'test': 123
}

snapshots['test_get_score[12345678900] 1'] = 131

snapshots['test_get_score[12345678912] 1'] = 694

snapshots['test_get_commitment[12345678900] 1'] = 0.9

snapshots['test_get_commitment[12345678912] 1'] = 0.8444218515250481
