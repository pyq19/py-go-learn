# coding:utf8
# https://github.com/faif/python-patterns/blob/master/creational/borg.py


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print(f'rm1: {rm1}')
    print(f'rm2: {rm2}')

    rm2.state = 'Zombie'

    print(f'rm1: {rm1}')
    print(f'rm2: {rm2}')

    print(f'rm1 id: {id(rm1)}')
    print(f'rm2 id: {id(rm2)}')

    rm3 = YourBorg()


    print(f'rm1: {rm1}')
    print(f'rm2: {rm2}')
    print(f'rm3: {rm3}')

# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 4321733320
# rm2 id: 4321733432
# rm1: Init
# rm2: Init
# rm3: Init
