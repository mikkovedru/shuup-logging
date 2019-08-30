# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import six
from django.utils.translation import ugettext_lazy as _
from shuup.admin.base import AdminModule, MenuEntry
from shuup.admin.menu import LOG_MENU_CATEGORY

PRODUCT_LOG_URL_NAME = "shuup_logging.product_log"
SHOP_PRODUCT_LOG_URL_NAME = "shuup_logging.shop_product_log"
SUPPLIER_LOG_URL_NAME = "shuup_logging.supplier_log"

MENU_ENTRIES_URL_NAME_TO_TITLE = {
    PRODUCT_LOG_URL_NAME: _("Product Logs"),
    SHOP_PRODUCT_LOG_URL_NAME: _("Shop Product Logs"),
    SUPPLIER_LOG_URL_NAME: _("Supplier Logs"),
}


class LogsModule(AdminModule):
    name = _("Logs")
    breadcrumbs_menu_entry = MenuEntry(name, url="shuup_admin:shuup_logging.product_log")

    def get_urls(self):
        from shuup.admin.urls import admin_url
        return [
            admin_url(
                "^product_logs",
                "shuup_logging.admin.products.ProductLogListView",
                name=PRODUCT_LOG_URL_NAME
            ),
            admin_url(
                "^shop_product_logs",
                "shuup_logging.admin.shop_products.ShopProductLogListView",
                name=SHOP_PRODUCT_LOG_URL_NAME
            ),
            admin_url(
                "^supplier_logs",
                "shuup_logging.admin.suppliers.SupplierLogListView",
                name=SUPPLIER_LOG_URL_NAME
            ),
        ]

    def get_menu_entries(self, request):
        from shuup.admin.utils.permissions import get_missing_permissions
        missing_permissions = get_missing_permissions(
            request.user,
            MENU_ENTRIES_URL_NAME_TO_TITLE.keys()
        )
        menu_entries = []
        for url_name, title in six.iteritems(MENU_ENTRIES_URL_NAME_TO_TITLE):
            if url_name not in missing_permissions:
                menu_entries.append(
                    MenuEntry(
                        text=title,
                        icon="fa fa-archive",
                        url="shuup_admin:%s" % url_name,
                        category=LOG_MENU_CATEGORY,
                        ordering=1
                    )
                )
        return menu_entries
