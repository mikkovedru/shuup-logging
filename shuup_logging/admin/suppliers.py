# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup.admin.shop_provider import get_shop
from shuup.core.models._suppliers import SupplierLogEntry
from shuup_logging.views import BaseLogListView


class SupplierLogListView(BaseLogListView):
    model = SupplierLogEntry
    target_search_field = "target__name"

    def get_queryset(self):
        shop = get_shop(self.request)
        return self.model.objects.filter(target__shops=shop).order_by("-created_on")
