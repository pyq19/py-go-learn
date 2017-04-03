# 3

# 不明白

class Proxy:
    def __init__(self, obj):
        self.obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
    # Call original __setattr__
        else:
            setattr(self._obj, name, value)
