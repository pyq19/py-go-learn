

class ResolverMatch(object):
    def __init__(self, func, args, kwargs, url_name=None, app_name=None, namespaces=None):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.url_name = url_name

        # if a URLRegexResolver doesn't have a namespace or app_name,
        # it passes in an empty value.
        self.app_names = [x for x in app_names if x] if app_names else []
        self.app_name = ':'.join(self.app_names)
        self.namespaces = [x for x in namespaces if x] if namespaces else []
        self.namespace = ':'.join(self.namespaces)

    def __getitem__(self, index):
        return (self.func, self.args, self.kwargs)[index]


# TODO @lru_cache.lru_cache(maxsize=None)
def get_resolver(urlconf=None):
    if urlconf is None:
        from litego.conf import settings
        urlconf = settings.ROOT_URLCONF
    return RegexURLResolver(r'^/', urlconf)


class LocaleRegexProvider(object):
    def __init__(self, regex):
        self._regex = regex
        self._regex_dict = {}

    def describe(self):
        pass

    def _check_pattern_startswith_slash(self):
        pass


class RegexURLResolver(LocaleRegexProvider):
    def __init__(self, regex, urlconf_name, default_kwargs=None, app_name=None, namespace=None):
        pass

    def resolve(self, path):
        # path = force_text(path)
        match = self.regex.search(path)
        if match:
            # ...
            return ResolverMatch(
                # sub_match.func,
                # sub_match.args,
            )
