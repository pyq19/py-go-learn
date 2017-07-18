import os
import sys


if __name__ == '__main__':
    from litego.core.management import execute_from_command_line
    print('current file abspath ->', os.path.abspath(__file__))

    execute_from_command_line(sys.argv)
