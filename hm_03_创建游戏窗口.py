# coding=gbk

import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
# set_mode初始化游戏窗口，返回结果为surface
# resolution参数必须是列表
# flags参数指定屏幕的附加选项（如是否全屏），默认不需要传递
# depth参数表示颜色的位数，默认自动匹配。
screen = pygame.display.set_mode((480, 700))

# 游戏循环
while True:
    pass

pygame.quit()