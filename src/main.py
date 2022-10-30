import multiprocessing
import sys
import time

import pygame
from src.scene import Scene

# width = 1542
# height = 865

width = 1920
height = 1050

max_comment = 1000
left_people = 0
right_people = 0
fclock = pygame.time.Clock()
GOLD = 255, 251, 0


class Game:
    def __init__(self, width=width, height=height):
        self.w = width
        self.h = height
        self.screen = self.get_screen()
        self.scene = Scene(self.screen)

    def get_screen(self, ):
        pygame.init()
        screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('世界杯')
        return screen

    def show_score(self, ):
        GOLD = 255, 251, 0
        global left_people
        global right_people
        # f = pygame.font.Font('/Users/cpeixin/PycharmProjects/DanmakuGame/font/simsun.ttc', 10)
        f = pygame.font.Font('/Users/cpeixin/PycharmProjects/DanmakuGame/font/simsun.ttc', 10)
        # l_text = f.render("中国队：{people}".format(people=left_total_people), True, (255, 255, 255), None)
        # l_textRect = l_text.get_rect()
        # if left_total_people == 0:
        #     l_textRect.center = (r_left, r_top + r_height + 10)
        # else:
        #     l_textRect.center = ((r_left + r_width) / 2, r_top + r_height + 10)
        # l_textRect.center = (50, 100)
        # l_f1rect = f.render_to(self.screen, [50,100], "中国队：{people}".format(people=left_total_people), fgcolor=GOLD, size=20)
        l_f1rect = f.render("中国队：{people}".format(people=left_people), True, (255, 255, 255))

        # r_text = f.render("法国队：{people}".format(people=right_total_people), True, (255, 255, 255), None)
        # r_textRect = r_text.get_rect()
        # # if right_total_people == 0:
        # #     r_textRect.center = (b_left, r_top + r_height + 10)
        # # else:
        # #     r_textRect.center = (r_left + r_width + b_width / 2, r_top + r_height + 10)
        # r_textRect.center = (150, 100)
        # r_f1rect = f.render_to(self.screen, [300,100], "法国队：{people}".format(people=right_total_people), fgcolor=GOLD, size=20)
        r_f1rect = f.render("法国队：{people}".format(people=right_people), True, (255, 255, 255))

        # title_text = f.render("总支持人数： ", True, (255, 255, 255), None)
        # title_textRect = title_text.get_rect()
        # title_textRect.center = (40, 30)
        # 背景填色
        # self.screen.blit(l_text, l_textRect)
        # self.screen.blit(r_text, r_textRect)
        # self.screen.blit(title_text, title_textRect)
        self.screen.blit(l_f1rect, (50, 100))
        self.screen.blit(r_f1rect, (200, 100))

    def run(self, queue):
        self.scene.render_scene()  # 原始位置
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            count = 0

            # self.show_score()

            while not queue.empty() and count < max_comment:
                chat = queue.get()
                count += 1
                if chat[1] == "皇家马德里必胜":
                    self.scene.create_person(chat[0], location="left")
                    global left_people
                    left_people += 1
                elif chat[1] == "郝罗纳必胜":
                    self.scene.create_person(chat[0], location="right")
                    global right_people
                    right_people += 1
                elif chat[1] == "平":
                    self.scene.create_person(chat[0], location="middle")
                elif chat[1] in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
                    self.scene.change_answer(chat[0], chat[1])
                pygame.display.update()
            pygame.display.update()


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    game = Game(width, height)
    queue.put(("brent", "中国必胜"))
    queue.put(("shaqpkuls", "中国必胜"))
    # queue.put(("王彭彭_Mr", "中国必胜"))
    # queue.put(("流离半世的苍白", "中国必胜"))
    # queue.put(("呱呱罗", "中国必胜"))
    # queue.put(("木林森", "中国必胜"))
    # queue.put(("一世红黑", "中国必胜"))
    # queue.put(("davidzhang11", "中国必胜"))
    # queue.put(("boy", "中国必胜"))
    # queue.put(("球迷18414666", "中国必胜"))
    # queue.put(("aspuk", "中国必胜"))
    # queue.put(("球迷18414698", "中国必胜"))
    # queue.put(("LYZRiot", "中国必胜"))
    # queue.put(("fisher", "中国必胜"))
    # queue.put(("庞大王王王王王", "中国必胜"))
    # queue.put(("boyfromfy", "中国必胜"))
    # queue.put(("永远的十号", "中国必胜"))
    # queue.put(("周品尧Leo", "中国必胜"))
    # queue.put(("niufei", "中国必胜"))

    queue.put(("shaqpkuls", "法国必胜"))
    queue.put(("王彭彭_Mr", "法国必胜"))
    queue.put(("流离半世的苍白", "法国必胜"))
    queue.put(("呱呱罗", "法国必胜"))
    queue.put(("木林森", "法国必胜"))
    queue.put(("一世红黑", "法国必胜"))
    queue.put(("davidzhang11", "法国必胜"))
    # queue.put(("boy", "法国必胜"))
    # queue.put(("球迷18414666", "法国必胜"))
    # queue.put(("aspuk", "法国必胜"))
    # queue.put(("球迷18414698", "法国必胜"))
    # queue.put(("LYZRiot", "法国必胜"))
    # queue.put(("fisher", "法国必胜"))
    # queue.put(("庞大王王王王王", "法国必胜"))
    # queue.put(("boyfromfy", "法国必胜"))
    # queue.put(("永远的十号", "法国必胜"))
    # queue.put(("周品尧Leo", "法国必胜"))
    # queue.put(("niufei", "法国必胜"))
    # queue.put(("King大智", "法国必胜"))
    # queue.put(("无声", "法国必胜"))
    # queue.put(("torres9", "法国必胜"))
    # queue.put(("参了个星", "法国必胜"))
    # queue.put(("红魔吉格斯", "法国必胜"))
    # queue.put(("老孫", "法国必胜"))
    # queue.put(("arsenalwin", "法国必胜"))
    # queue.put(("修炼爱情的心酸", "法国必胜"))
    # queue.put(("苏锦up", "法国必胜"))
    # queue.put(("瓜瓜", "法国必胜"))
    # queue.put(("雷科巴", "法国必胜"))

    game.run(queue)
