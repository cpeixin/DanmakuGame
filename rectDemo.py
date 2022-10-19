#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/17 9:33 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : rectDemo.py
# @Description:

import pygame
import sys

pygame.init()

size = width, height = 600, 600

bg = (255, 255, 255)  # RGB 白色

# 创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("Python Demo")

clock = pygame.time.Clock()



r_people = 0
b_people = 0


total_width = 350
r_left = 80
r_top = 20
r_width = (r_people / (r_people + b_people + 1)) * total_width
r_height = 20

b_left = r_left + r_width
b_top = 20
b_width = (b_people / (r_people + b_people + 1)) * total_width
b_height = 20

rect1 = pygame.Rect(r_left, r_top, r_width, r_height)
rect2 = pygame.Rect(b_left, b_top, b_width, b_height)

f = pygame.font.Font('/Users/dongqiudi/PycharmProjects/DanmakuGame/font/simsun.ttc', 10)
l_text = f.render("中国队：{people}".format(people=r_people), True, (255, 0, 0), None)
l_textRect = l_text.get_rect()
if r_people == 0:
    l_textRect.center = (r_left, r_top + r_height + 10)
else:
    l_textRect.center = ((r_left + r_width) / 2, r_top + r_height + 10)

r_text = f.render("法国队：{people}".format(people=b_people), True, (200, 0, 0), None)
r_textRect = r_text.get_rect()
if b_people == 0:
    r_textRect.center = (b_left, r_top + r_height + 10)
else:
    r_textRect.center = (r_left + r_width + b_width / 2, r_top + r_height + 10)

title_text = f.render("总支持人数： ", True, (200, 0, 0), None)
title_textRect = title_text.get_rect()
title_textRect.center = (40, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)

    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)
    # pygame.draw.rect(screen, (0, 0, 255), rect1.fit(rect2))
    screen.blit(l_text, l_textRect)
    screen.blit(r_text, r_textRect)
    screen.blit(title_text, title_textRect)
    pygame.display.flip()

    clock.tick(10)
