# coding:utf8
# http://dongweiming.github.io/python-state.html


# state 模式 状态模式
# 可以在调用时修改其内部属性，看起来像改变了类的状态


class NetworkCardState:
    ''' 基类 '''
    def send(self):
        raise NotImplementedError

    def receive(self):
        raise NotImplementedError


class Online(NetworkCardState):
    ''' 在线 '''
    def send(self):
        print 'sending ...data ...'

    def receive(self):
        print 'receiving data...'


class Offline(NetworkCardState):
    ''' 离线 '''
    def send(self):
        print 'cannot send .. offline'

    def receive(self):
        print ' cannot receive ....offline'


class NetworkCard:
    
    def __init__(self):
        self.online = Online()
        self.offline = Offline()
        # 修改内部属性currentState, 默认是离线，直接传入类
        self.current_state = self.offline
        
    def start_connection(self):
        # 改变状态成在线
        self.current_state = self.online

    def stop_connection(self):
        self.current_state = self.offline

    def send(self):
        # 去掉用这个可变的属性的方法，达到看起来是操作了类的属性的改变
        self.current_state.send()

    def receive(self):
        self.current_state.receive()


def main():
    my_network_card = NetworkCard()
    print 'without connection: '
    my_network_card.send()
    my_network_card.receive()
    print 'starting conneciton '
    my_network_card.start_connection()
    my_network_card.send()
    my_network_card.receive()


if __name__ == '__main__':
    main()
# without connection:
# cannot send .. offline
#  cannot receive ....offline
# starting conneciton
# sending ...data ...
# receiving data...
