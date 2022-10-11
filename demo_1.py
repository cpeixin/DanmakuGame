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
bgImg = pygame.image.load('/Users/dongqiudi/PycharmProjects/DamakuGame/image/backgroud.jpg')

screen.blit(bgImg,(0,0))

#创建时钟对象（控制游戏的FPS）
clock = pygame.time.Clock()


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
