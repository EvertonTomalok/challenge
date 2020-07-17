# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['test_parse_str_to_date[15/08/1992] 1'] = GenericRepr('datetime.date(1992, 8, 15)')

snapshots['test_parse_str_to_date[1992-08-15] 1'] = GenericRepr('datetime.date(1992, 8, 15)')

snapshots['test_parse_str_to_date[1992/08/15] 1'] = GenericRepr('datetime.date(1992, 8, 15)')

snapshots['test_parse_str_to_date_date_obj 1'] = GenericRepr('datetime.date(1992, 8, 15)')

snapshots['test_get_age[1992-08-15] 1'] = 27

snapshots['test_get_age[2005-08-15] 1'] = 14

snapshots['test_get_age[2010-08-15] 1'] = 9

snapshots['test_is_older[1992-08-15] 1'] = True

snapshots['test_is_older[2005-08-15] 1'] = False

snapshots['test_is_older[2010-08-15] 1'] = False
