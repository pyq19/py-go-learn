# coding:utf8
# https://ruslanspivak.com/lsbasi-part4/

INTEGER, MUL, DIV, EOF = 'INTEGER', 'MUL', 'DIV', 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        pass # TODO
