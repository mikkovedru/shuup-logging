# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse

from shuup.notify.models.script import ScriptLogEntry
from shuup_logging.views import BaseLogListView


class NotificationLogListView(BaseLogListView):
    model = ScriptLogEntry
    target_search_field = "target__name"
    hide_extra_changed = True

    def format_target(self, instance, *args, **kwargs):
        if instance.target:
            return '<a href=%s target="_blank">%s</a>' % (
                reverse("shuup_admin:notify.script.edit", kwargs={"pk": instance.target.pk}), instance.target
            )
        return "-"
