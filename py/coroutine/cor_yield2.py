# coding:utf8
# https://my.oschina.net/u/877348/blog/184058

# 异步逻辑..
# 同步逻辑见 cor_yield3.py

import random


class Player(object):
    ''' 玩家实体类 '''
    def __init__(self, entity_id):
        super(Player, self).__init__()
        # 玩家标识
        self.entity_id = entity_id

    def on_fuben_end(self, mail_box):
        score = random.randint(1, 10)
        print('on_fuben_end player %d score %d' % (self.entity_id, score))
        # 向副本管理进程发送自己的id 和战斗信息
        mail_box.on_eval_fuben_score(self.entity_id, score)


class FubenStub(object):
    ''' 副本管理类 '''
    def __init__(self, players):
        super(FubenStub, self).__init__()
        self.players = players

    def eval_fuben_score(self):
        self.player_relay_cnt = 0
        self.total_score = 0

        # 通知每个注册的玩家，副本已经结束，索取战斗信息
        for player in self.players:
            player.on_fuben_end(self)

    def on_eval_fuben_score(self, entity_id, score):
        # 收到其中一个玩家的战斗信息
        print('on_eval_fuben_score player %d score %d' % (entity_id, score))
        self.player_relay_cnt += 1
        self.total_score += score

        # 当收集完所有玩家的信息后，打印评分
        if len(self.players) == self.player_relay_cnt:
            print('the fuben total_score is %d' % self.total_score)


if __name__ == '__main__':
    # 模拟创建玩家实体
    players = [Player(i) for i in xrange(3)]

    # 副本开始时，每个玩家将自己的mail_box 注册到副本管理进程
    fs = FubenStub(players)

    # 副本进行中
    # ...

    # 副本结束，开始评分
    fs.eval_fuben_score()
