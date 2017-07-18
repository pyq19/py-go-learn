class BaseCommand(object):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        pass

    def run_from_argv(self, argv):
        pass

    def execute(self, *args, **options):
        output = self.handle(*args, **options)
        if output:
            pass
        return output

    def handle(self, *args, **options):
        raise NotImplementedError('subclasses of BaseCommand must provide a handle() method')
