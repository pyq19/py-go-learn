# coding:utf8
# https://github.com/faif/python-patterns/blob/master/structural/bridge.py


class DrawingAPI_1(object):
    ''' ConcreteImplementor 1/2 '''
    def draw_circle(self, x, y, radius):
        print(f'API_1.circle at {x}, {y} radius {radius}')


class DrawingAPI_2(object):
    ''' ConcreteImplementor 2/2 '''
    def draw_circle(self, x, y, radius):
        print(f'API_2.circle at {x} {y} radius {radius}')


class CircleShape(object):
    ''' refined abstraction '''
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        ''' low-level i.e. Implementation specific '''
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        ''' high-level i.e. Abstraction specific '''
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI_1()),
        CircleShape(5, 7, 11, DrawingAPI_2()),
    )

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()

# API_1.circle at 1, 2 radius 7.5
# API_2.circle at 5 7 radius 27.5
