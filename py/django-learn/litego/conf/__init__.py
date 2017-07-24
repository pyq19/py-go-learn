import os
import importlib


ENVIRONMENT_VARIABLE = 'DJANGO_SETTINGS_MODULE'


class LazySettings(object):
    def _setup(self, name=None):
        settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        if not settings_module:
            raise Exception # TODO ImproperlyConfigured
        self._wrapped = Settings(settings_module)


class Settings(object):
    def __init__(self, settings_module):
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(global_settings, setting))
        self.SETTINGS_MODULE = settings_module
        # mod = importlib.import_module(self.SETTINGS_MODULE)
        # tuple_settings = (
        #     'INSTALLED_APPS',
        #     'TEMPLATE_DIRS',
        #     'LOCALE_PATHS',
        # )
        # self._explicit_settings = set()
        # for setting in dir(mod):
        #     if setting.isupper():
        #         setting_value = getattr(mod, setting)
        #         if (setting in tuple_settings and 



settings = LazySettings()
