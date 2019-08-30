# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup.admin.shop_provider import get_shop
from shuup.core.models._product_shops import ShopProductLogEntry

from shuup_logging.views import BaseLogListView


class ShopProductLogListView(BaseLogListView):
    model = ShopProductLogEntry
    target_search_field = "target__product__translations__name"

    def get_queryset(self):
        shop = get_shop(self.request)
        return self.model.objects.filter(target__shop=shop).order_by("-created_on")
