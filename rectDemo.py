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

total_width = 300

r_people = 0
b_people = 0


r_left = 20
r_top = 20
r_width = (r_people / (r_people + b_people + 1)) * total_width
r_height = 20

b_left = r_left+r_width
b_top = 20
b_width = (b_people / (r_people + b_people + 1)) * total_width
b_height = 20
               # left, top, width, height
rect1 = pygame.Rect(r_left, r_top, r_width, r_height)
# rect2 = pygame.Rect(50, 50, 200, 200)
rect2 = pygame.Rect(b_left, b_top, b_width, b_height)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)

    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)
    # pygame.draw.rect(screen, (0, 0, 255), rect1.fit(rect2))

    pygame.display.flip()

    clock.tick(10)
