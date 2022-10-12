import multiprocessing
import sys

import pygame
from src.scene import Scene

# width = 1542
# height = 865

width = 1920
height = 1080

max_comment = 1000


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

    def run(self, queue):
        self.scene.render_scene()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            count = 0
            while not queue.empty() and count < max_comment:
                # ('bbbbbrent', 'd')
                # ('bbbbbrent', '加入游戏')
                chat = queue.get()
                count += 1
                if chat[1] == "中国必胜":
                    self.scene.create_person(chat[0], location="left")
                if chat[1] == "法国必胜":
                    self.scene.create_person(chat[0], location="right")
                if chat[1] == "平":
                    self.scene.create_person(chat[0], location="middle")
                if chat[1] in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
                    self.scene.change_answer(chat[0], chat[1])

            # display
            pygame.display.update()


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    game = Game(width, height)
    queue.put(("brent", "中国必胜"))
    queue.put(("shaqpkuls", "中国必胜"))
    queue.put(("王彭彭_Mr", "中国必胜"))
    queue.put(("流离半世的苍白", "中国必胜"))
    queue.put(("呱呱罗", "中国必胜"))
    queue.put(("木林森", "中国必胜"))
    queue.put(("一世红黑", "中国必胜"))
    queue.put(("davidzhang11", "中国必胜"))
    queue.put(("boy", "中国必胜"))
    queue.put(("球迷18414666", "中国必胜"))
    queue.put(("aspuk", "中国必胜"))
    queue.put(("球迷18414698", "中国必胜"))
    queue.put(("LYZRiot", "中国必胜"))
    queue.put(("fisher", "中国必胜"))
    queue.put(("庞大王王王王王", "中国必胜"))
    queue.put(("boyfromfy", "中国必胜"))
    queue.put(("永远的十号", "中国必胜"))
    queue.put(("周品尧Leo", "中国必胜"))
    queue.put(("niufei", "中国必胜"))
    queue.put(("King大智", "中国必胜"))
    queue.put(("无声", "中国必胜"))
    queue.put(("torres9", "中国必胜"))
    queue.put(("参了个星", "中国必胜"))
    queue.put(("红魔吉格斯", "中国必胜"))
    queue.put(("老孫", "中国必胜"))
    queue.put(("arsenalwin", "中国必胜"))
    queue.put(("修炼爱情的心酸", "中国必胜"))
    queue.put(("苏锦up", "中国必胜"))
    queue.put(("瓜瓜", "中国必胜"))
    queue.put(("雷科巴", "中国必胜"))
    queue.put(("魔兽世界", "中国必胜"))
    queue.put(("巴蒂", "中国必胜"))
    queue.put(("两耳失聪", "中国必胜"))
    queue.put(("小耳总", "中国必胜"))
    queue.put(("伊藤诚", "中国必胜"))
    queue.put(("DORT-NIEPAN", "中国必胜"))
    queue.put(("天津", "中国必胜"))
    queue.put(("太妃糖", "中国必胜"))
    queue.put(("南开", "中国必胜"))
    queue.put(("兵工厂", "中国必胜"))
    queue.put(("908930685", "中国必胜"))
    queue.put(("小德", "中国必胜"))
    queue.put(("巴西", "中国必胜"))
    queue.put(("格子", "中国必胜"))
    queue.put(("老村长", "中国必胜"))
    queue.put(("低产射手", "中国必胜"))
    queue.put(("lvchenglong", "中国必胜"))
    queue.put(("猫粮", "中国必胜"))
    queue.put(("中国", "中国必胜"))
    queue.put(("红魔曼联", "中国必胜"))
    queue.put(("cjou", "中国必胜"))
    queue.put(("阿根廷", "中国必胜"))
    queue.put(("FIFA", "中国必胜"))
    queue.put(("失去蝶的花", "中国必胜"))
    queue.put(("药厂10号", "中国必胜"))
    queue.put(("spearsong", "中国必胜"))
    queue.put(("vitalize1992", "中国必胜"))
    queue.put(("潜龙在渊__腾必九天", "中国必胜"))
    queue.put(("inter镜", "中国必胜"))
    queue.put(("丶且听风吟_", "中国必胜"))
    queue.put(("雪花", "中国必胜"))
    queue.put(("KOP", "中国必胜"))
    queue.put(("11141066", "中国必胜"))
    queue.put(("qwe", "中国必胜"))
    queue.put(("电话12", "中国必胜"))
    queue.put(("设计ssd", "中国必胜"))
    queue.put(("shdh123", "中国必胜"))
    queue.put(("bluepoint", "中国必胜"))
    queue.put(("Cloud", "中国必胜"))
    queue.put(("JeLeVeux-", "中国必胜"))
    queue.put(("S7", "中国必胜"))
    queue.put(("Suarez7", "中国必胜"))
    queue.put(("传奇", "中国必胜"))
    queue.put(("GlenJohnson", "中国必胜"))
    queue.put(("LuisSuarez", "中国必胜"))
    queue.put(("Sturridge15", "中国必胜"))
    queue.put(("LiverpoolFC_待改名", "中国必胜"))
    queue.put(("T9", "中国必胜"))
    queue.put(("C7", "中国必胜"))
    queue.put(("MartinSkrtel", "中国必胜"))
    queue.put(("Suso_待改名", "中国必胜"))
    queue.put(("Smile", "中国必胜"))
    queue.put(("SAS", "中国必胜"))
    queue.put(("DanielAgger", "中国必胜"))
    queue.put(("Gerrard8", "中国必胜"))
    queue.put(("G8", "中国必胜"))
    queue.put(("LucasLeiva", "中国必胜"))
    queue.put(("杰队", "中国必胜"))
    queue.put(("我就是那只泼猴啊", "中国必胜"))
    queue.put(("Sakho17", "中国必胜"))
    queue.put(("YNWA", "中国必胜"))
    queue.put(("Allen", "中国必胜"))
    queue.put(("科诺普良卡", "中国必胜"))
    queue.put(("红黑之心", "中国必胜"))
    queue.put(("科诺普尔扬卡", "中国必胜"))
    queue.put(("安菲尔德", "中国必胜"))
    queue.put(("Anfield", "中国必胜"))
    queue.put(("每个人都在等待-", "中国必胜"))
    queue.put(("球盲", "中国必胜"))
    queue.put(("Carragher", "中国必胜"))
    queue.put(("卡拉格", "中国必胜"))
    game.run(queue)
