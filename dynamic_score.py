#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 4:18 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : dynamic.py
# @Description:
import sys
import pygame
import pygame.freetype

pygame.init()
size = width, height = 640, 480  # 设置窗口的大小
# print(pygame.display.Info())
screen = pygame.display.set_mode(size)  # 将窗口显示到屏幕上
# print(pygame.display.Info())        # 在set_mode前后调用是有区别的
pygame.display.set_caption("Pygame文字绘制")
# color=(0,0,0)     # 设置刷新的颜色
black = 0, 0, 0
GOLD = 255, 251, 0
pos = [230, 160]
# 引入字体类型
f1 = pygame.freetype.Font(r"/Users/dongqiudi/PycharmProjects/DanmakuGame/font/BOBOHEI-2.otf", 36)
bgImg = pygame.image.load('/Users/dongqiudi/PycharmProjects/DanmakuGame/image/backgroud.jpg')
fps = 300
fclock = pygame.time.Clock()

score = 0
while True:
    # clock.tick(60)         # 每秒执行60次
    # 检查事件
    screen.blit(bgImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果单机关闭窗口，则退出
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    f1.render_to(screen, pos, f"得分： {score}", fgcolor=GOLD, size=50)

    # text = f1.render(f"得分： {score}", True, (255, 251, 0))
    # screen.blit(text,(50, 100))
    score += 1
    fclock.tick(fps)
    pygame.display.update()  # 更新全部显示


# pygame.quit()
