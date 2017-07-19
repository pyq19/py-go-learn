from threading import local


_urlconfs = local()


def set_urlconf(urlconf_name):
    ''' set the URLconf for the current thread (overriding the default one in settings.)
        if urlconf_name is None, revert back to the default. '''
    if urlconf_name:
        _urlconfs.value = urlconf_name
    else:
        if hasattr(_urlconfs, 'value'):
            del _urlconfs.value
