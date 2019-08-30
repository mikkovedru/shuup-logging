# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.dispatch import receiver
from shuup.admin.signals import object_saved
from shuup.core.models import Product, ShopProduct, Supplier
from shuup.utils.analog import LogEntryKind
from shuup.utils.models import get_data_dict

SHUUP_LOGGING_ADMIN_SAVE_LOG_IDENTIFIER = "shuup_logging_admin_save"


@receiver(object_saved, dispatch_uid="shuup-logging-product-updated")
def product_post_save(sender, object, request, **kwargs):
    if isinstance(object, Product):
        # TODO: check if extra has changed from last log entry
        object.add_log_entry(
            "Product saved at admin",
            user=request.user,
            identifier=SHUUP_LOGGING_ADMIN_SAVE_LOG_IDENTIFIER,
            kind=LogEntryKind.EDIT,
            extra=get_data_dict(object, force_text_for_value=True)
        )


@receiver(object_saved, dispatch_uid="shuup-logging-shop-product-updated")
def shop_product_post_save(sender, object, request, **kwargs):
    if isinstance(object, ShopProduct):
        # TODO: check if extra has changed from last log entry
        object.add_log_entry(
            "Shop product saved at admin",
            user=request.user,
            identifier=SHUUP_LOGGING_ADMIN_SAVE_LOG_IDENTIFIER,
            kind=LogEntryKind.EDIT,
            extra=get_data_dict(object, force_text_for_value=True)
        )


@receiver(object_saved, dispatch_uid="shuup-logging-supplier-updated")
def supplier_post_save(sender, object, request, **kwargs):
    if isinstance(object, Supplier):
        # TODO: check if extra has changed from last log entry
        object.add_log_entry(
            "Supplier saved at admin",
            user=request.user,
            identifier=SHUUP_LOGGING_ADMIN_SAVE_LOG_IDENTIFIER,
            kind=LogEntryKind.EDIT,
            extra=get_data_dict(object, force_text_for_value=True)
        )
