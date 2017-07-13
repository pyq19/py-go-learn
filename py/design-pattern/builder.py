# coding:utf8
# http://dongweiming.github.io/python-builder.html


# Builder 模式


import abc

class Vehicle(object):
    
    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

    # 不同的车子类型，齿轮，车门数，座位数都不尽相同
    def view(self):
        print(
            'this vehicle is a ' +
            self.type + 
            ' with ' + 
            str(self.wheels) + 
            ' wheels ' + 
            str(self.doors) + 
            ' doors and ' +
            str(self.seats) + 
            ' seats ')

# 把制造齿轮，车门，座位的工序抽象出来，用不同的制造部门去做
class VehicleBuilder(object):
    
    __metadata__ = abc.ABCMeta
    # 装饰器定义抽象方法（只能用在metaclass 为abc.ABCMeta 或其子类的class 中)
    # 这里也可以pass 或raise 基类未实现的异常
    @abc.abstractmethod
    def make_wheels(self):
        raise

    @abc.abstractmethod
    def make_doors(self):
        raise

    @abc.abstractmethod
    def make_seats(self):
        raise


# 架设要制造汽车和单车，每个都要继承这个VehicleBuilder 基类，
# 但是齿轮，车门，座位都是不同的

class CarBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle('Car')

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 3

    def make_seats(self):
        self.vehicle.seats = 5


class BikeBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle('Bike')

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2


# 制造的Director

class VehicleManufacturer(object):
    
    def __init__(self):
        self.builder = None

    def create(self):
        assert not self.builder is None, 'No defined builder...'
        self.builder.make_wheels()
        self.builder.make_doors()
        self.builder.make_seats()
        return self.builder.vehicle


if __name__ == '__main__':
    manufacturer = VehicleManufacturer()
    # 重要的是这样的调用方式，每次修改builder 方法传入不同的要求，
    # 然后在create 里制造，整个过程在VehicleManufacturer 完成
    manufacturer.builder = CarBuilder()
    car = manufacturer.create()
    car.view()

    manufacturer.builder = BikeBuilder()
    bike = manufacturer.create()
    bike.view()

# this vehicle is a Car with 4 wheels 3 doors and 5 seats
# this vehicle is a Bike with 2 wheels 0 doors and 2 seats
