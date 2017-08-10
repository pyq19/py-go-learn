# coding:utf8
# https://github.com/gennad/Design-Patterns-in-Python/blob/master/adapter.py


class Command(object):
    def run(self):
        # return 'default command'
        raise NotImplementedError


class NewCommand(Command):
    def run(self):
        return 'new command'


class Executer(object):
    def __init__(self, command):
        self.command = command

    def exc(self):
        return self.command.run()


executer = Executer(NewCommand())
print executer.exc()
# new command


# --------------


class UppercasingFile(object):
    def __init__(self, *a, **k):
        self.f = file(*a, **k)

    def write(self, data):
        self.f.write(data.upper())

    def __getattr__(self, name):
        return getattr(self.f, name)
