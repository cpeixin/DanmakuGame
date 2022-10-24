#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 8:24 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : demo_1.py
# @Description:


#导入所需的模块
import sys
import pygame
# 使用pygame之前必须初始化
pygame.init()
# 设置主屏窗口
screen = pygame.display.set_mode((1920,1080))
# 设置窗口的标题，即游戏名称
pygame.display.set_caption('为主队扛大旗')

# 设置背景图
bgImg = pygame.image.load('/Users/cpeixin/PycharmProjects/DanmakuGame/image/backgroud.jpg')

screen.blit(bgImg,(0,0))

#创建时钟对象（控制游戏的FPS）
clock = pygame.time.Clock()
r_left, r_top, r_width, r_height = 20,20,20,20
b_left, b_top, b_width, b_height = 120,120,120,120
rect1 = pygame.Rect(r_left, r_top, r_width, r_height)
rect2 = pygame.Rect(b_left, b_top, b_width, b_height)
l_people = 50
r_people = 60
f = pygame.font.Font('/Users/cpeixin/PycharmProjects/DanmakuGame/font/simsun.ttc', 10)
l_text = f.render("中国队：{people}".format(people=l_people), True, (255, 250, 250), None)
l_textRect = l_text.get_rect()
if l_people == 0:
    l_textRect.center = (r_left, r_top + r_height + 10)
else:
    l_textRect.center = ((r_left + r_width) / 2, r_top + r_height + 10)

r_text = f.render("法国队：{people}".format(people=r_people), True, (255, 250, 250), None)
r_textRect = r_text.get_rect()
if r_people == 0:
    r_textRect.center = (b_left, r_top + r_height + 10)
else:
    r_textRect.center = (r_left + r_width + b_width / 2, r_top + r_height + 10)

title_text = f.render("总支持人数： ", True, (200, 0, 0), None)
title_textRect = title_text.get_rect()
title_textRect.center = (40, 30)
##------------------##

pygame.draw.rect(screen, (255, 0, 0), rect1)
pygame.draw.rect(screen, (0, 255, 0), rect2)
# pygame.draw.rect(screen, (0, 0, 255), rect1.fit(rect2))
screen.blit(l_text, l_textRect)
screen.blit(r_text, r_textRect)
screen.blit(title_text, title_textRect)


# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:

    #通过时钟对象，指定循环频率，每秒循环60次
    clock.tick(60)

    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()



    pygame.display.flip() #更新屏幕内容
