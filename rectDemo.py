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

rect1 = pygame.Rect(0, 0, 100, 50)
rect2 = pygame.Rect(50, 50, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)

    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)
    pygame.draw.rect(screen, (0, 0, 255), rect1.fit(rect2))

    pygame.display.flip()

    clock.tick(10)
