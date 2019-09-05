# -*- coding: utf-8 -*-
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_logging"
    label = "shuup_logging"
    provides = {
        "admin_module": [
            "shuup_logging.admin:LogsModule",
        ]
    }

    def ready(self):
        from django.conf import settings
        if settings.SHUUP_LOGGING_ENABLE_BASIC_LOGGING:
            import shuup_logging.signal_handlers  # noqa: F401
