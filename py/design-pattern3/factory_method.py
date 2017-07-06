# coding:utf8
# https://github.com/faif/python-patterns/blob/master/creational/factory_method.py


class GreekGetter(object):
    ''' A simple localizer a la gettext '''
    def __init__(self):
        self.trans = dict(dog='dog1', cat='cat1')

    def get(self, msgid):
        ''' we'll punt if we don't have a translation '''
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    ''' simply echoes the msg ids '''
    def get(self, msgid):
        return str(msgid)


def get_localizer(language='English'):
    ''' the factory method '''
    languages= dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


if __name__ == '__main__':
    e, g = get_localizer(language='English'), get_localizer(language='Greek')

    for msgid in 'dog parrot cat bear'.split():
        print(e.get(msgid), g.get(msgid))

# dog dog1
# parrot parrot
# cat cat1
# bear bear
