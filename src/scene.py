import queue
import random
import pygame
import numpy as np
from src.person import Person

# w_start = 27
# w_end = 1454
# w_num = 45
# h_start = 2
# h_end = 790
# h_num = 15
# font_size = 10
#
# font_h_ = 20

# 左侧显示玩家范围
w_left_start = 27
w_left_end = 800
h_left_start = 200
h_left_end = 1080

# 右侧显示玩家范围
w_right_start = 1000
w_right_end = 1900
h_right_start = 200
h_right_end = 1080

# 玩家 左右空间位置步长
w_num = 35
h_num = 20

# 字体设置
font_size = 10
font_h_ = 20


class Scene:
    def __init__(self, screen):
        self.screen = screen
        # 加载需要用的图片
        self.prepare_pic()
        self.init_pos()
        self.ava_ids = list(range(1, self.num + 1))
        self.left_ava_ids = list(range(1, self.left_num + 1))
        self.right_ava_ids = list(range(1, self.right_num + 1))

        self.people = {}
        # 玩家字典 散列表 实现快速的找到用户
        self.left_people = {}
        self.right_people = {}
        # 玩家队列 实现足球场内的用户数恒定，并且 先进先出，维护最近评论的用户
        self.left_people_queue = queue.Queue(len(self.left_ava_ids))
        self.right_people_queue = queue.Queue(len(self.right_ava_ids))
        # 全局变量 记录左右阵营支持的人数
        self.left_total_people = 0
        self.right_total_people = 0
        self.font = pygame.font.Font("/Users/dongqiudi/PycharmProjects/DanmakuGame/font/BOBOHEI-2.otf", font_size)

    def prepare_pic(self):
        # self.map = pygame.image.load("pic/map.jpg").convert()
        self.map = pygame.image.load("/Users/dongqiudi/PycharmProjects/DanmakuGame/image/backgroud.jpg").convert()
        self.r_cell = pygame.image.load("/Users/dongqiudi/PycharmProjects/DanmakuGame/pic/red_cell.png").convert_alpha()
        self.y_cell = pygame.image.load(
            "/Users/dongqiudi/PycharmProjects/DanmakuGame/pic/yello_cell.png").convert_alpha()
        self.b_cell = pygame.image.load(
            "/Users/dongqiudi/PycharmProjects/DanmakuGame/pic/blue_cell.png").convert_alpha()
        self.g_cell = pygame.image.load(
            "/Users/dongqiudi/PycharmProjects/DanmakuGame/pic/green_cell.png").convert_alpha()
        self.cell = {"r": self.r_cell, "y": self.y_cell, "b": self.b_cell, "g": self.g_cell}

    def init_pos(self, ):
        # 用于在线性空间中以均匀步长生成数字序列
        w_left_pos = list(np.linspace(w_left_start, w_left_end, num=w_num, endpoint=True))
        h_left_pos = list(np.linspace(h_left_start, h_left_end, num=h_num, endpoint=True))

        w_right_pos = list(np.linspace(w_right_start, w_right_end, num=w_num, endpoint=True))
        h_right_pos = list(np.linspace(h_right_start, h_right_end, num=h_num, endpoint=True))
        num = 0
        # 位置列表
        self.left_pos = {}
        self.right_pos = {}
        left_num = 0
        for i, h in enumerate(h_left_pos):
            for j, w in enumerate(w_left_pos):
                # 当横坐标为奇数时，则纵坐标为偶数
                # 当横坐标为偶数时，则纵坐标为奇数
                if (i % 2 == 0) != (j % 2 == 0):
                    left_num += 1
                    self.left_pos[left_num] = (int(w), int(h))
        self.left_num = left_num

        right_num = 0
        for i, h in enumerate(h_right_pos):
            for j, w in enumerate(w_right_pos):
                # 当横坐标为奇数时，则纵坐标为偶数
                # 当横坐标为偶数时，则纵坐标为奇数
                if (i % 2 == 0) != (j % 2 == 0):
                    right_num += 1
                    self.right_pos[right_num] = (int(w), int(h))
        self.right_num = right_num
        self.num = right_num + left_num

    def if_have_ids(self, ava_ids):
        return len(ava_ids) > 0

    def create_person(self, name, location):
        global id
        if name in self.left_people and location == "left":
            return
        if name in self.right_people and location == "right":
            return
        # if name in self.people or (not self.if_have_ids()):
        #     return


        # 此处逻辑 如果位置满了，只展示最新评论的玩家，这样可以刺激大家刷评论
        if location == "left":
            if self.if_have_ids(self.left_ava_ids):
                id = random.choice(self.left_ava_ids)
                self.left_ava_ids.remove(id)
            else:
                leave_user = self.left_people_queue.get()
                leave_person = self.left_people[leave_user]
                self.left_people.pop(leave_user)
                id = leave_person.id
            person = Person(id, name, self.font)
            self.left_people[name] = person
            self.left_people_queue.put(name)
            self.render_person(self.left_people[name], location)
            self.left_total_people += 1
        if location == "right":
            # id = random.choice(self.right_ava_ids)
            # self.right_ava_ids.remove(id)
            # person = Person(id, name, self.font)
            # self.people[name] = person
            # self.render_person(self.people[name], location)

            if self.if_have_ids(self.right_ava_ids):
                id = random.choice(self.right_ava_ids)
                self.right_ava_ids.remove(id)
            else:
                leave_user = self.right_people_queue.get()
                leave_person = self.right_people[leave_user]
                self.right_people.pop(leave_user)
                id = leave_person.id
            person = Person(id, name, self.font)
            self.right_people[name] = person
            self.right_people_queue.put(name)
            self.render_person(self.right_people[name], location)
            self.right_total_people += 1

    def delete_person(self, name):
        self.ava_ids.append(self.people[name].id)
        self.people.pop(name)

    def change_answer(self, name, answer):
        if name not in self.people:
            return
        if answer in ['a', 'A']:
            self.people[name].change_answer('r')
        if answer in ['b', 'B']:
            self.people[name].change_answer('y')
        if answer in ['c', 'C']:
            self.people[name].change_answer('b')
        if answer in ['d', 'D']:
            self.people[name].change_answer('g')
        self.render_person(self.people[name], "left")

    def render_scene(self):
        self.render_map()
        for name in self.people:
            self.render_person(self.people[name], "left")

    def render_map(self):
        self.screen.blit(self.map, (0, 0))

    # 指定玩家位置
    def render_person(self, person, location):
        # 改变玩家的颜色
        self.render_cell(person.id, person.color)
        # 根据person.id，取pos中相应的坐标位移
        # self.screen.blit(person.name, (self.pos[person.id][0], self.pos[person.id][1] + 30))
        if location == "left":
            self.screen.blit(person.name, (self.left_pos[person.id][0], self.left_pos[person.id][1]))
        if location == "right":
            self.screen.blit(person.name, (self.right_pos[person.id][0], self.right_pos[person.id][1]))

    def render_cell(self, id, color=None):
        if color:
            if not isinstance(id, list):
                id = [id]
            for i in id:
                self.screen.blit(self.cell[color], self.pos[i])

    def render_debug(self):
        for id in self.pos:
            color = random.choice(["r", "y", "b", "g"])
            self.render_cell(self.screen, id, color)


if __name__ == '__main__':
    w_left_start = 27
    w_left_end = 800
    h_left_start = 200
    h_left_end = 1080

    w_num = 35
    h_num = 20

    font_size = 10
    font_h_ = 20

    # # 用于在线性空间中以均匀步长生成数字序列
    # w_pos = list(np.linspace(w_left_start, w_left_end, num=w_num, endpoint=True))
    # print(w_pos)
    # # [27.0, 59.43181818181818, 91.86363636363636, 124.29545454545453, 156.72727272727272, 189.1590909090909, 221.59090909090907, 254.02272727272725, 286.45454545454544, 318.8863636363636, 351.3181818181818, 383.75, 416.18181818181813, 448.6136363636363, 481.0454545454545, 513.4772727272727, 545.9090909090909, 578.340909090909, 610.7727272727273, 643.2045454545454, 675.6363636363636, 708.0681818181818, 740.5, 772.9318181818181, 805.3636363636363, 837.7954545454545, 870.2272727272726, 902.6590909090909, 935.090909090909, 967.5227272727273, 999.9545454545454, 1032.3863636363635, 1064.8181818181818, 1097.25, 1129.681818181818, 1162.1136363636363, 1194.5454545454545, 1226.9772727272727, 1259.4090909090908, 1291.840909090909, 1324.2727272727273, 1356.7045454545453, 1389.1363636363635, 1421.5681818181818, 1454.0]
    # h_pos = list(np.linspace(h_left_start, h_left_end, num=h_num, endpoint=True))
    # print(h_pos)
    # # [2.0, 58.285714285714285, 114.57142857142857, 170.85714285714286, 227.14285714285714, 283.42857142857144, 339.7142857142857, 396.0, 452.2857142857143, 508.57142857142856, 564.8571428571429, 621.1428571428571, 677.4285714285714, 733.7142857142857, 790.0]
    # pos = {}
    # num = 0
    # for i, h in enumerate(h_pos):
    #     for j, w in enumerate(w_pos):
    #         # 当横坐标为奇数时，则纵坐标为偶数
    #         # 当横坐标为偶数时，则纵坐标为奇数
    #         if (i % 4 == 0) != (j % 4 == 0):
    #             num += 1
    #             pos[num] = (int(w), int(h))
    # num = num

    # print(pos)

    class Item:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    left_people_dict = {}
    left_people_queue = queue.Queue(5)
    left_people_queue.put("jack")
    left_people_dict['jack'] = Item(1, "jack")
    left_people_queue.put("judu")
    left_people_dict['judu'] = Item(2, "judu")
    left_people_queue.put("hudy")
    left_people_dict['hudy'] = Item(3, "hudy")

    print(left_people_queue.queue)
    print(left_people_dict)

    user = left_people_queue.get()
    print(user)
    leave_person = left_people_dict[user]
    print(leave_person)
    print(left_people_dict)
    print(left_people_queue.queue)



    for i in range(1,360):
        print(i)
