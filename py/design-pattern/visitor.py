# coding:utf8
# http://dongweiming.github.io/python-visitor.html


# 轮子，引擎，车身 都定义好了不需要变动
class Wheel:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        # 每个visitor 是同样的，但其中的方法不同，比如visitWheel
        # 然后传入了self
        visitor.visitWheel(self)


class Engine:
    def accept(self, visitor):
        visitor.visitEngine(self)


class Body:
    def accept(self, visitor):
        visitor.visitBody(self)


class Car:
    def __init__(self):
        self.engine = Engine()
        self.body = Body()
        self.wheels = [Wheel('front left'), Wheel('front right'),
                       Wheel('back left'), Wheel('back right')]

    def accept(self, visitor):
        visitor.visitCar(self)
        self.engine.accept(visitor)
        self.body.accept(visitor)
        for wheel in self.wheels:
            wheel.accept(visitor)

# 访问者，每次修改都在这里
class PrintVisitor:
    def visitWheel(self, wheel):
        print 'visiting ..', wheel.name + ' wheel'
    def visitEngine(self, wheel):
        print 'visiting .. engine'
    def visitBody(self, body):
        print 'visiting .. body'
    def visitCar(self, car):
        print 'visiting .. car'


if __name__ == '__main__':
    car = Car()
    visitor = PrintVisitor()
    car.accept(visitor)

# visiting .. car
# visiting .. engine
# visiting .. body
# visiting .. front left wheel
# visiting .. front right wheel
# visiting .. back left wheel
# visiting .. back right wheel
