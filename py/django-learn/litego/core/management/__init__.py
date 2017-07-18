import sys, os
from importlib import import_module


def execute_from_command_line(argv=None):
    print(argv)
    utility = ManagementUtility(argv)
    utility.execute()


class ManagementUtility(object):
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.settings_exception = None
        print(self.prog_name) # main.py

    def execute(self):
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = 'help'
        print(subcommand)

        # ...

        module = import_module(f'litego.core.management.commands.{subcommand}')
        command = module.Command()
        command.execute()
