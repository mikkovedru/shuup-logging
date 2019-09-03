# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup.core.models._products import ProductLogEntry
from shuup_logging.views import BaseLogListView


class ProductLogListView(BaseLogListView):
    model = ProductLogEntry
    target_search_field = "target__translations__name"
