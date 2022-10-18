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
            # 总人数
            count = 0
            l_people = 0
            r_people = 0
            while not queue.empty() and count < max_comment:
                # ('bbbbbrent', 'd')
                # ('bbbbbrent', '加入游戏')
                chat = queue.get()
                count += 1
                if chat[1] == "中国必胜":
                    l_people+=1
                    self.scene.create_person(chat[0], location="left")
                elif chat[1] == "法国必胜":
                    r_people+=1
                    self.scene.create_person(chat[0], location="right")
                elif chat[1] == "平":
                    self.scene.create_person(chat[0], location="middle")
                elif chat[1] in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
                    self.scene.change_answer(chat[0], chat[1])
                else:
                    return

                ##-------bar--------##

                total_width = 350

                l_people = 0
                r_people = 0

                r_left = 80
                r_top = 20
                r_width = (r_people / (l_people + r_people + 1)) * total_width
                r_height = 20

                b_left = r_left + r_width
                b_top = 20
                b_width = (r_people / (l_people + r_people + 1)) * total_width
                b_height = 20

                rect1 = pygame.Rect(r_left, r_top, r_width, r_height)
                rect2 = pygame.Rect(b_left, b_top, b_width, b_height)

                f = pygame.font.Font('/Users/dongqiudi/PycharmProjects/DanmakuGame/font/simsun.ttc', 10)
                l_text = f.render("中国队：{people}".format(people=l_people), True, (255, 0, 0), None)
                l_textRect = l_text.get_rect()
                if l_people == 0:
                    l_textRect.center = (r_left, r_top + r_height + 10)
                else:
                    l_textRect.center = ((r_left + r_width) / 2, r_top + r_height + 10)

                r_text = f.render("法国队：{people}".format(people=r_people), True, (200, 0, 0), None)
                r_textRect = r_text.get_rect()
                if r_people == 0:
                    r_textRect.center = (b_left, r_top + r_height + 10)
                else:
                    r_textRect.center = (r_left + r_width + b_width / 2, r_top + r_height + 10)

                title_text = f.render("总支持人数： ", True, (200, 0, 0), None)
                title_textRect = title_text.get_rect()
                title_textRect.center = (40, 30)

                ##------------------##


                pygame.draw.rect(self.screen, (255, 0, 0),
                                 (10 + count * 4, 20, 40 - count * 4, 8))

            # display
            pygame.display.update()


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    game = Game(width, height)
    # queue.put(("brent", "中国必胜"))
    # queue.put(("shaqpkuls", "中国必胜"))
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
    # queue.put(("King大智", "中国必胜"))
    # queue.put(("无声", "中国必胜"))
    # queue.put(("torres9", "中国必胜"))
    # queue.put(("参了个星", "中国必胜"))
    # queue.put(("红魔吉格斯", "中国必胜"))
    # queue.put(("老孫", "中国必胜"))
    # queue.put(("arsenalwin", "中国必胜"))
    # queue.put(("修炼爱情的心酸", "中国必胜"))
    # queue.put(("苏锦up", "中国必胜"))
    # queue.put(("瓜瓜", "中国必胜"))
    # queue.put(("雷科巴", "中国必胜"))
    # queue.put(("魔兽世界", "中国必胜"))
    # queue.put(("巴蒂", "中国必胜"))
    # queue.put(("两耳失聪", "中国必胜"))
    # queue.put(("小耳总", "中国必胜"))
    # queue.put(("伊藤诚", "中国必胜"))
    # queue.put(("DORT-NIEPAN", "中国必胜"))
    # queue.put(("天津", "中国必胜"))
    # queue.put(("太妃糖", "中国必胜"))
    # queue.put(("南开", "中国必胜"))
    # queue.put(("兵工厂", "中国必胜"))
    # queue.put(("908930685", "中国必胜"))
    # queue.put(("小德", "中国必胜"))
    # queue.put(("巴西", "中国必胜"))
    # queue.put(("格子", "中国必胜"))
    # queue.put(("老村长", "中国必胜"))
    # queue.put(("低产射手", "中国必胜"))
    # queue.put(("lvchenglong", "中国必胜"))
    # queue.put(("猫粮", "中国必胜"))
    # queue.put(("中国", "中国必胜"))
    # queue.put(("红魔曼联", "中国必胜"))
    # queue.put(("cjou", "中国必胜"))
    # queue.put(("阿根廷", "中国必胜"))
    # queue.put(("FIFA", "中国必胜"))
    # queue.put(("失去蝶的花", "中国必胜"))
    # queue.put(("药厂10号", "中国必胜"))
    # queue.put(("spearsong", "中国必胜"))
    # queue.put(("vitalize1992", "中国必胜"))
    # queue.put(("潜龙在渊__腾必九天", "中国必胜"))
    # queue.put(("inter镜", "中国必胜"))
    # queue.put(("丶且听风吟_", "中国必胜"))
    # queue.put(("雪花", "中国必胜"))
    # queue.put(("KOP", "中国必胜"))
    # queue.put(("11141066", "中国必胜"))
    # queue.put(("qwe", "中国必胜"))
    # queue.put(("电话12", "中国必胜"))
    # queue.put(("设计ssd", "中国必胜"))
    # queue.put(("shdh123", "中国必胜"))
    # queue.put(("bluepoint", "中国必胜"))
    # queue.put(("Cloud", "中国必胜"))
    # queue.put(("JeLeVeux-", "中国必胜"))
    # queue.put(("S7", "中国必胜"))
    # queue.put(("Suarez7", "中国必胜"))
    # queue.put(("传奇", "中国必胜"))
    # queue.put(("GlenJohnson", "中国必胜"))
    # queue.put(("LuisSuarez", "中国必胜"))
    # queue.put(("Sturridge15", "中国必胜"))
    # queue.put(("LiverpoolFC_待改名", "中国必胜"))
    # queue.put(("T9", "中国必胜"))
    # queue.put(("C7", "中国必胜"))
    # queue.put(("MartinSkrtel", "中国必胜"))
    # queue.put(("Suso_待改名", "中国必胜"))
    # queue.put(("Smile", "中国必胜"))
    # queue.put(("SAS", "中国必胜"))
    # queue.put(("DanielAgger", "中国必胜"))
    # queue.put(("Gerrard8", "中国必胜"))
    # queue.put(("G8", "中国必胜"))
    # queue.put(("LucasLeiva", "中国必胜"))
    # queue.put(("杰队", "中国必胜"))
    # queue.put(("我就是那只泼猴啊", "中国必胜"))
    # queue.put(("Sakho17", "中国必胜"))
    # queue.put(("YNWA", "中国必胜"))
    # queue.put(("Allen", "中国必胜"))
    # queue.put(("科诺普良卡", "中国必胜"))
    # queue.put(("红黑之心", "中国必胜"))
    # queue.put(("科诺普尔扬卡", "中国必胜"))
    # queue.put(("安菲尔德", "中国必胜"))
    # queue.put(("Anfield", "中国必胜"))
    # queue.put(("每个人都在等待-", "中国必胜"))
    # queue.put(("球盲", "中国必胜"))
    # queue.put(("Carragher", "中国必胜"))
    # queue.put(("卡拉格", "中国必胜"))

    queue.put(("1", "中国必胜"))
    queue.put(("2", "中国必胜"))
    queue.put(("3", "中国必胜"))
    queue.put(("4", "中国必胜"))
    queue.put(("5", "中国必胜"))
    queue.put(("6", "中国必胜"))
    queue.put(("7", "中国必胜"))
    queue.put(("8", "中国必胜"))
    queue.put(("9", "中国必胜"))
    queue.put(("10", "中国必胜"))
    queue.put(("11", "中国必胜"))
    queue.put(("12", "中国必胜"))
    queue.put(("13", "中国必胜"))
    queue.put(("14", "中国必胜"))
    queue.put(("15", "中国必胜"))
    queue.put(("16", "中国必胜"))
    queue.put(("17", "中国必胜"))
    queue.put(("18", "中国必胜"))
    queue.put(("19", "中国必胜"))
    queue.put(("20", "中国必胜"))
    queue.put(("21", "中国必胜"))
    queue.put(("22", "中国必胜"))
    queue.put(("23", "中国必胜"))
    queue.put(("24", "中国必胜"))
    queue.put(("25", "中国必胜"))
    queue.put(("26", "中国必胜"))
    queue.put(("27", "中国必胜"))
    queue.put(("28", "中国必胜"))
    queue.put(("29", "中国必胜"))
    queue.put(("30", "中国必胜"))
    queue.put(("31", "中国必胜"))
    queue.put(("32", "中国必胜"))
    queue.put(("33", "中国必胜"))
    queue.put(("34", "中国必胜"))
    queue.put(("35", "中国必胜"))
    queue.put(("36", "中国必胜"))
    queue.put(("37", "中国必胜"))
    queue.put(("38", "中国必胜"))
    queue.put(("39", "中国必胜"))
    queue.put(("40", "中国必胜"))
    queue.put(("41", "中国必胜"))
    queue.put(("42", "中国必胜"))
    queue.put(("43", "中国必胜"))
    queue.put(("44", "中国必胜"))
    queue.put(("45", "中国必胜"))
    queue.put(("46", "中国必胜"))
    queue.put(("47", "中国必胜"))
    queue.put(("48", "中国必胜"))
    queue.put(("49", "中国必胜"))
    queue.put(("50", "中国必胜"))
    queue.put(("51", "中国必胜"))
    queue.put(("52", "中国必胜"))
    queue.put(("53", "中国必胜"))
    queue.put(("54", "中国必胜"))
    queue.put(("55", "中国必胜"))
    queue.put(("56", "中国必胜"))
    queue.put(("57", "中国必胜"))
    queue.put(("58", "中国必胜"))
    queue.put(("59", "中国必胜"))
    queue.put(("60", "中国必胜"))
    queue.put(("61", "中国必胜"))
    queue.put(("62", "中国必胜"))
    queue.put(("63", "中国必胜"))
    queue.put(("64", "中国必胜"))
    queue.put(("65", "中国必胜"))
    queue.put(("66", "中国必胜"))
    queue.put(("67", "中国必胜"))
    queue.put(("68", "中国必胜"))
    queue.put(("69", "中国必胜"))
    queue.put(("70", "中国必胜"))
    queue.put(("71", "中国必胜"))
    queue.put(("72", "中国必胜"))
    queue.put(("73", "中国必胜"))
    queue.put(("74", "中国必胜"))
    queue.put(("75", "中国必胜"))
    queue.put(("76", "中国必胜"))
    queue.put(("77", "中国必胜"))
    queue.put(("78", "中国必胜"))
    queue.put(("79", "中国必胜"))
    queue.put(("80", "中国必胜"))
    queue.put(("81", "中国必胜"))
    queue.put(("82", "中国必胜"))
    queue.put(("83", "中国必胜"))
    queue.put(("84", "中国必胜"))
    queue.put(("85", "中国必胜"))
    queue.put(("86", "中国必胜"))
    queue.put(("87", "中国必胜"))
    queue.put(("88", "中国必胜"))
    queue.put(("89", "中国必胜"))
    queue.put(("90", "中国必胜"))
    queue.put(("91", "中国必胜"))
    queue.put(("92", "中国必胜"))
    queue.put(("93", "中国必胜"))
    queue.put(("94", "中国必胜"))
    queue.put(("95", "中国必胜"))
    queue.put(("96", "中国必胜"))
    queue.put(("97", "中国必胜"))
    queue.put(("98", "中国必胜"))
    queue.put(("99", "中国必胜"))
    queue.put(("100", "中国必胜"))
    queue.put(("101", "中国必胜"))
    queue.put(("102", "中国必胜"))
    queue.put(("103", "中国必胜"))
    queue.put(("104", "中国必胜"))
    queue.put(("105", "中国必胜"))
    queue.put(("106", "中国必胜"))
    queue.put(("107", "中国必胜"))
    queue.put(("108", "中国必胜"))
    queue.put(("109", "中国必胜"))
    queue.put(("110", "中国必胜"))
    queue.put(("111", "中国必胜"))
    queue.put(("112", "中国必胜"))
    queue.put(("113", "中国必胜"))
    queue.put(("114", "中国必胜"))
    queue.put(("115", "中国必胜"))
    queue.put(("116", "中国必胜"))
    queue.put(("117", "中国必胜"))
    queue.put(("118", "中国必胜"))
    queue.put(("119", "中国必胜"))
    queue.put(("120", "中国必胜"))
    queue.put(("121", "中国必胜"))
    queue.put(("122", "中国必胜"))
    queue.put(("123", "中国必胜"))
    queue.put(("124", "中国必胜"))
    queue.put(("125", "中国必胜"))
    queue.put(("126", "中国必胜"))
    queue.put(("127", "中国必胜"))
    queue.put(("128", "中国必胜"))
    queue.put(("129", "中国必胜"))
    queue.put(("130", "中国必胜"))
    queue.put(("131", "中国必胜"))
    queue.put(("132", "中国必胜"))
    queue.put(("133", "中国必胜"))
    queue.put(("134", "中国必胜"))
    queue.put(("135", "中国必胜"))
    queue.put(("136", "中国必胜"))
    queue.put(("137", "中国必胜"))
    queue.put(("138", "中国必胜"))
    queue.put(("139", "中国必胜"))
    queue.put(("140", "中国必胜"))
    queue.put(("141", "中国必胜"))
    queue.put(("142", "中国必胜"))
    queue.put(("143", "中国必胜"))
    queue.put(("144", "中国必胜"))
    queue.put(("145", "中国必胜"))
    queue.put(("146", "中国必胜"))
    queue.put(("147", "中国必胜"))
    queue.put(("148", "中国必胜"))
    queue.put(("149", "中国必胜"))
    queue.put(("150", "中国必胜"))
    queue.put(("151", "中国必胜"))
    queue.put(("152", "中国必胜"))
    queue.put(("153", "中国必胜"))
    queue.put(("154", "中国必胜"))
    queue.put(("155", "中国必胜"))
    queue.put(("156", "中国必胜"))
    queue.put(("157", "中国必胜"))
    queue.put(("158", "中国必胜"))
    queue.put(("159", "中国必胜"))
    queue.put(("160", "中国必胜"))
    queue.put(("161", "中国必胜"))
    queue.put(("162", "中国必胜"))
    queue.put(("163", "中国必胜"))
    queue.put(("164", "中国必胜"))
    queue.put(("165", "中国必胜"))
    queue.put(("166", "中国必胜"))
    queue.put(("167", "中国必胜"))
    queue.put(("168", "中国必胜"))
    queue.put(("169", "中国必胜"))
    queue.put(("170", "中国必胜"))
    queue.put(("171", "中国必胜"))
    queue.put(("172", "中国必胜"))
    queue.put(("173", "中国必胜"))
    queue.put(("174", "中国必胜"))
    queue.put(("175", "中国必胜"))
    queue.put(("176", "中国必胜"))
    queue.put(("177", "中国必胜"))
    queue.put(("178", "中国必胜"))
    queue.put(("179", "中国必胜"))
    queue.put(("180", "中国必胜"))
    queue.put(("181", "中国必胜"))
    queue.put(("182", "中国必胜"))
    queue.put(("183", "中国必胜"))
    queue.put(("184", "中国必胜"))
    queue.put(("185", "中国必胜"))
    queue.put(("186", "中国必胜"))
    queue.put(("187", "中国必胜"))
    queue.put(("188", "中国必胜"))
    queue.put(("189", "中国必胜"))
    queue.put(("190", "中国必胜"))
    queue.put(("191", "中国必胜"))
    queue.put(("192", "中国必胜"))
    queue.put(("193", "中国必胜"))
    queue.put(("194", "中国必胜"))
    queue.put(("195", "中国必胜"))
    queue.put(("196", "中国必胜"))
    queue.put(("197", "中国必胜"))
    queue.put(("198", "中国必胜"))
    queue.put(("199", "中国必胜"))
    queue.put(("200", "中国必胜"))
    queue.put(("201", "中国必胜"))
    queue.put(("202", "中国必胜"))
    queue.put(("203", "中国必胜"))
    queue.put(("204", "中国必胜"))
    queue.put(("205", "中国必胜"))
    queue.put(("206", "中国必胜"))
    queue.put(("207", "中国必胜"))
    queue.put(("208", "中国必胜"))
    queue.put(("209", "中国必胜"))
    queue.put(("210", "中国必胜"))
    queue.put(("211", "中国必胜"))
    queue.put(("212", "中国必胜"))
    queue.put(("213", "中国必胜"))
    queue.put(("214", "中国必胜"))
    queue.put(("215", "中国必胜"))
    queue.put(("216", "中国必胜"))
    queue.put(("217", "中国必胜"))
    queue.put(("218", "中国必胜"))
    queue.put(("219", "中国必胜"))
    queue.put(("220", "中国必胜"))
    queue.put(("221", "中国必胜"))
    queue.put(("222", "中国必胜"))
    queue.put(("223", "中国必胜"))
    queue.put(("224", "中国必胜"))
    queue.put(("225", "中国必胜"))
    queue.put(("226", "中国必胜"))
    queue.put(("227", "中国必胜"))
    queue.put(("228", "中国必胜"))
    queue.put(("229", "中国必胜"))
    queue.put(("230", "中国必胜"))
    queue.put(("231", "中国必胜"))
    queue.put(("232", "中国必胜"))
    queue.put(("233", "中国必胜"))
    queue.put(("234", "中国必胜"))
    queue.put(("235", "中国必胜"))
    queue.put(("236", "中国必胜"))
    queue.put(("237", "中国必胜"))
    queue.put(("238", "中国必胜"))
    queue.put(("239", "中国必胜"))
    queue.put(("240", "中国必胜"))
    queue.put(("241", "中国必胜"))
    queue.put(("242", "中国必胜"))
    queue.put(("243", "中国必胜"))
    queue.put(("244", "中国必胜"))
    queue.put(("245", "中国必胜"))
    queue.put(("246", "中国必胜"))
    queue.put(("247", "中国必胜"))
    queue.put(("248", "中国必胜"))
    queue.put(("249", "中国必胜"))
    queue.put(("250", "中国必胜"))
    queue.put(("251", "中国必胜"))
    queue.put(("252", "中国必胜"))
    queue.put(("253", "中国必胜"))
    queue.put(("254", "中国必胜"))
    queue.put(("255", "中国必胜"))
    queue.put(("256", "中国必胜"))
    queue.put(("257", "中国必胜"))
    queue.put(("258", "中国必胜"))
    queue.put(("259", "中国必胜"))
    queue.put(("260", "中国必胜"))
    queue.put(("261", "中国必胜"))
    queue.put(("262", "中国必胜"))
    queue.put(("263", "中国必胜"))
    queue.put(("264", "中国必胜"))
    queue.put(("265", "中国必胜"))
    queue.put(("266", "中国必胜"))
    queue.put(("267", "中国必胜"))
    queue.put(("268", "中国必胜"))
    queue.put(("269", "中国必胜"))
    queue.put(("270", "中国必胜"))
    queue.put(("271", "中国必胜"))
    queue.put(("272", "中国必胜"))
    queue.put(("273", "中国必胜"))
    queue.put(("274", "中国必胜"))
    queue.put(("275", "中国必胜"))
    queue.put(("276", "中国必胜"))
    queue.put(("277", "中国必胜"))
    queue.put(("278", "中国必胜"))
    queue.put(("279", "中国必胜"))
    queue.put(("280", "中国必胜"))
    queue.put(("281", "中国必胜"))
    queue.put(("282", "中国必胜"))
    queue.put(("283", "中国必胜"))
    queue.put(("284", "中国必胜"))
    queue.put(("285", "中国必胜"))
    queue.put(("286", "中国必胜"))
    queue.put(("287", "中国必胜"))
    queue.put(("288", "中国必胜"))
    queue.put(("289", "中国必胜"))
    queue.put(("290", "中国必胜"))
    queue.put(("291", "中国必胜"))
    queue.put(("292", "中国必胜"))
    queue.put(("293", "中国必胜"))
    queue.put(("294", "中国必胜"))
    queue.put(("295", "中国必胜"))
    queue.put(("296", "中国必胜"))
    queue.put(("297", "中国必胜"))
    queue.put(("298", "中国必胜"))
    queue.put(("299", "中国必胜"))
    queue.put(("300", "中国必胜"))
    queue.put(("301", "中国必胜"))
    queue.put(("302", "中国必胜"))
    queue.put(("303", "中国必胜"))
    queue.put(("304", "中国必胜"))
    queue.put(("305", "中国必胜"))
    queue.put(("306", "中国必胜"))
    queue.put(("307", "中国必胜"))
    queue.put(("308", "中国必胜"))
    queue.put(("309", "中国必胜"))
    queue.put(("310", "中国必胜"))
    queue.put(("311", "中国必胜"))
    queue.put(("312", "中国必胜"))
    queue.put(("313", "中国必胜"))
    queue.put(("314", "中国必胜"))
    queue.put(("315", "中国必胜"))
    queue.put(("316", "中国必胜"))
    queue.put(("317", "中国必胜"))
    queue.put(("318", "中国必胜"))
    queue.put(("319", "中国必胜"))
    queue.put(("320", "中国必胜"))
    queue.put(("321", "中国必胜"))
    queue.put(("322", "中国必胜"))
    queue.put(("323", "中国必胜"))
    queue.put(("324", "中国必胜"))
    queue.put(("325", "中国必胜"))
    queue.put(("326", "中国必胜"))
    queue.put(("327", "中国必胜"))
    queue.put(("328", "中国必胜"))
    queue.put(("329", "中国必胜"))
    queue.put(("330", "中国必胜"))
    queue.put(("331", "中国必胜"))
    queue.put(("332", "中国必胜"))
    queue.put(("333", "中国必胜"))
    queue.put(("334", "中国必胜"))
    queue.put(("335", "中国必胜"))
    queue.put(("336", "中国必胜"))
    queue.put(("337", "中国必胜"))
    queue.put(("338", "中国必胜"))
    queue.put(("339", "中国必胜"))
    queue.put(("340", "中国必胜"))
    queue.put(("341", "中国必胜"))
    queue.put(("342", "中国必胜"))
    queue.put(("343", "中国必胜"))
    queue.put(("344", "中国必胜"))
    queue.put(("345", "中国必胜"))
    queue.put(("346", "中国必胜"))
    queue.put(("347", "中国必胜"))
    queue.put(("348", "中国必胜"))
    queue.put(("349", "中国必胜"))
    queue.put(("350", "中国必胜"))
    queue.put(("351", "中国必胜"))
    queue.put(("352", "中国必胜"))
    queue.put(("353", "中国必胜"))
    queue.put(("354", "中国必胜"))
    queue.put(("355", "中国必胜"))
    queue.put(("356", "中国必胜"))
    queue.put(("357", "中国必胜"))
    queue.put(("358", "中国必胜"))
    queue.put(("359", "中国必胜"))

    queue.put(("法国———shaqpkuls", "法国必胜"))
    queue.put(("法国———王彭彭_Mr", "法国必胜"))
    queue.put(("法国———流离半世的苍白", "法国必胜"))
    queue.put(("法国———呱呱罗", "法国必胜"))
    queue.put(("法国———木林森", "法国必胜"))
    queue.put(("法国———一世红黑", "法国必胜"))
    queue.put(("法国———davidzhang11", "法国必胜"))
    queue.put(("法国———boy", "法国必胜"))
    queue.put(("法国———球迷18414666", "法国必胜"))
    queue.put(("法国———aspuk", "法国必胜"))
    queue.put(("法国———球迷18414698", "法国必胜"))
    queue.put(("法国———LYZRiot", "法国必胜"))
    queue.put(("法国———fisher", "法国必胜"))
    queue.put(("法国———庞大王王王王王", "法国必胜"))
    queue.put(("法国———boyfromfy", "法国必胜"))
    queue.put(("法国———永远的十号", "法国必胜"))
    queue.put(("法国———周品尧Leo", "法国必胜"))
    queue.put(("法国———niufei", "法国必胜"))
    queue.put(("法国———King大智", "法国必胜"))
    queue.put(("法国———无声", "法国必胜"))
    queue.put(("法国———torres9", "法国必胜"))
    queue.put(("法国———参了个星", "法国必胜"))
    queue.put(("法国———红魔吉格斯", "法国必胜"))
    queue.put(("法国———老孫", "法国必胜"))
    queue.put(("法国———arsenalwin", "法国必胜"))
    queue.put(("法国———修炼爱情的心酸", "法国必胜"))
    queue.put(("法国———苏锦up", "法国必胜"))
    queue.put(("法国———瓜瓜", "法国必胜"))
    queue.put(("法国———雷科巴", "法国必胜"))
    queue.put(("法国———魔兽世界", "法国必胜"))
    queue.put(("法国———巴蒂", "法国必胜"))
    queue.put(("法国———两耳失聪", "法国必胜"))
    queue.put(("法国———小耳总", "法国必胜"))
    queue.put(("法国———伊藤诚", "法国必胜"))
    queue.put(("法国———DORT-NIEPAN", "法国必胜"))
    queue.put(("法国———天津", "法国必胜"))
    queue.put(("法国———太妃糖", "法国必胜"))
    queue.put(("法国———南开", "法国必胜"))
    queue.put(("法国———兵工厂", "法国必胜"))
    queue.put(("法国———908930685", "法国必胜"))
    queue.put(("法国———小德", "法国必胜"))
    queue.put(("法国———巴西", "法国必胜"))
    queue.put(("法国———格子", "法国必胜"))
    queue.put(("法国———老村长", "法国必胜"))
    queue.put(("法国———低产射手", "法国必胜"))
    queue.put(("法国———lvchenglong", "法国必胜"))
    queue.put(("法国———猫粮", "法国必胜"))
    queue.put(("法国———中国", "法国必胜"))
    queue.put(("法国———红魔曼联", "法国必胜"))
    queue.put(("法国———cjou", "法国必胜"))
    queue.put(("法国———阿根廷", "法国必胜"))
    queue.put(("法国———FIFA", "法国必胜"))
    queue.put(("法国———失去蝶的花", "法国必胜"))
    queue.put(("法国———药厂10号", "法国必胜"))
    queue.put(("法国———spearsong", "法国必胜"))
    queue.put(("法国———vitalize1992", "法国必胜"))
    queue.put(("法国———潜龙在渊__腾必九天", "法国必胜"))
    queue.put(("法国———inter镜", "法国必胜"))
    queue.put(("法国———丶且听风吟_", "法国必胜"))
    queue.put(("法国———雪花", "法国必胜"))
    queue.put(("法国———KOP", "法国必胜"))
    queue.put(("法国———11141066", "法国必胜"))
    queue.put(("法国———qwe", "法国必胜"))
    queue.put(("法国———电话12", "法国必胜"))
    queue.put(("法国———设计ssd", "法国必胜"))
    queue.put(("法国———shdh123", "法国必胜"))
    queue.put(("法国———bluepoint", "法国必胜"))
    queue.put(("法国———Cloud", "法国必胜"))
    queue.put(("法国———JeLeVeux-", "法国必胜"))
    queue.put(("法国———S7", "法国必胜"))
    queue.put(("法国———Suarez7", "法国必胜"))
    queue.put(("法国———传奇", "法国必胜"))
    queue.put(("法国———GlenJohnson", "法国必胜"))
    queue.put(("法国———LuisSuarez", "法国必胜"))
    queue.put(("法国———Sturridge15", "法国必胜"))
    queue.put(("法国———LiverpoolFC_待改名", "法国必胜"))
    queue.put(("法国———T9", "法国必胜"))
    queue.put(("法国———C7", "法国必胜"))
    queue.put(("法国———MartinSkrtel", "法国必胜"))
    queue.put(("法国———Suso_待改名", "法国必胜"))
    queue.put(("法国———Smile", "法国必胜"))
    queue.put(("法国———SAS", "法国必胜"))
    queue.put(("法国———DanielAgger", "法国必胜"))
    queue.put(("法国———Gerrard8", "法国必胜"))
    queue.put(("法国———G8", "法国必胜"))
    queue.put(("法国———LucasLeiva", "法国必胜"))
    queue.put(("法国———杰队", "法国必胜"))
    queue.put(("法国———我就是那只泼猴啊", "法国必胜"))
    queue.put(("法国———Sakho17", "法国必胜"))
    queue.put(("法国———YNWA", "法国必胜"))
    queue.put(("法国———Allen", "法国必胜"))
    queue.put(("法国———科诺普良卡", "法国必胜"))
    queue.put(("法国———红黑之心", "法国必胜"))
    queue.put(("法国———科诺普尔扬卡", "法国必胜"))
    queue.put(("法国———安菲尔德", "法国必胜"))
    queue.put(("法国———Anfield", "法国必胜"))
    queue.put(("法国———每个人都在等待-", "法国必胜"))
    queue.put(("法国———球盲", "法国必胜"))
    queue.put(("法国———Carragher", "法国必胜"))
    queue.put(("法国———卡拉格", "法国必胜"))

    # queue.put(("shaqpkuls", "法国必胜"))
    # queue.put(("王彭彭_Mr", "法国必胜"))
    # queue.put(("流离半世的苍白", "法国必胜"))
    # queue.put(("呱呱罗", "法国必胜"))
    # queue.put(("木林森", "法国必胜"))
    # queue.put(("一世红黑", "法国必胜"))
    # queue.put(("davidzhang11", "法国必胜"))
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
    # queue.put(("魔兽世界", "法国必胜"))
    # queue.put(("巴蒂", "法国必胜"))
    # queue.put(("两耳失聪", "法国必胜"))
    # queue.put(("小耳总", "法国必胜"))
    # queue.put(("伊藤诚", "法国必胜"))
    # queue.put(("DORT-NIEPAN", "法国必胜"))
    # queue.put(("天津", "法国必胜"))
    # queue.put(("太妃糖", "法国必胜"))
    # queue.put(("南开", "法国必胜"))
    # queue.put(("兵工厂", "法国必胜"))
    # queue.put(("908930685", "法国必胜"))
    # queue.put(("小德", "法国必胜"))
    # queue.put(("巴西", "法国必胜"))
    # queue.put(("格子", "法国必胜"))
    # queue.put(("老村长", "法国必胜"))
    # queue.put(("低产射手", "法国必胜"))
    # queue.put(("lvchenglong", "法国必胜"))
    # queue.put(("猫粮", "法国必胜"))
    # queue.put(("中国", "法国必胜"))
    # queue.put(("红魔曼联", "法国必胜"))
    # queue.put(("cjou", "法国必胜"))
    # queue.put(("阿根廷", "法国必胜"))
    # queue.put(("FIFA", "法国必胜"))
    # queue.put(("失去蝶的花", "法国必胜"))
    # queue.put(("药厂10号", "法国必胜"))
    # queue.put(("spearsong", "法国必胜"))
    # queue.put(("vitalize1992", "法国必胜"))
    # queue.put(("潜龙在渊__腾必九天", "法国必胜"))
    # queue.put(("inter镜", "法国必胜"))
    # queue.put(("丶且听风吟_", "法国必胜"))
    # queue.put(("雪花", "法国必胜"))
    # queue.put(("KOP", "法国必胜"))
    # queue.put(("11141066", "法国必胜"))
    # queue.put(("qwe", "法国必胜"))
    # queue.put(("电话12", "法国必胜"))
    # queue.put(("设计ssd", "法国必胜"))
    # queue.put(("shdh123", "法国必胜"))
    # queue.put(("bluepoint", "法国必胜"))
    # queue.put(("Cloud", "法国必胜"))
    # queue.put(("JeLeVeux-", "法国必胜"))
    # queue.put(("S7", "法国必胜"))
    # queue.put(("Suarez7", "法国必胜"))
    # queue.put(("传奇", "法国必胜"))
    # queue.put(("GlenJohnson", "法国必胜"))
    # queue.put(("LuisSuarez", "法国必胜"))
    # queue.put(("Sturridge15", "法国必胜"))
    # queue.put(("LiverpoolFC_待改名", "法国必胜"))
    # queue.put(("T9", "法国必胜"))
    # queue.put(("C7", "法国必胜"))
    # queue.put(("MartinSkrtel", "法国必胜"))
    # queue.put(("Suso_待改名", "法国必胜"))
    # queue.put(("Smile", "法国必胜"))
    # queue.put(("SAS", "法国必胜"))
    # queue.put(("DanielAgger", "法国必胜"))
    # queue.put(("Gerrard8", "法国必胜"))
    # queue.put(("G8", "法国必胜"))
    # queue.put(("LucasLeiva", "法国必胜"))
    # queue.put(("杰队", "法国必胜"))
    # queue.put(("我就是那只泼猴啊", "法国必胜"))
    # queue.put(("Sakho17", "法国必胜"))
    # queue.put(("YNWA", "法国必胜"))
    # queue.put(("Allen", "法国必胜"))
    # queue.put(("科诺普良卡", "法国必胜"))
    # queue.put(("红黑之心", "法国必胜"))
    # queue.put(("科诺普尔扬卡", "法国必胜"))
    # queue.put(("安菲尔德", "法国必胜"))
    # queue.put(("Anfield", "法国必胜"))
    # queue.put(("每个人都在等待-", "法国必胜"))
    # queue.put(("球盲", "法国必胜"))
    # queue.put(("Carragher", "法国必胜"))
    # queue.put(("卡拉格", "法国必胜"))

    game.run(queue)
