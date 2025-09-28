# 这是贪吃蛇的源代码。
# 运行前请先安装pygame库，命令行运行pip install pygame。
# 文件夹内的Button.py是自定义的按钮类，请不要修改,同时它也要和snake.py放在同一目录下。
# 运行时会在当前目录生成data.pkl文件，为游戏的配置文件(请勿删除)。
# 作者：氢気氚 | qinch，邮箱：BlueRectS@outlook.com
# 版本：v1.1.1
# 最后编辑时间：2025年09月27日 23:23:16

import pygame
import sys
import random
import Button
import pickle

MUTOS_B = False
BJPZ_B = True
SSCD_B = False
TouchMode = False
Guideline = False
try:
    with open('data.pkl', 'rb') as f:
        MUTOS_B = pickle.load(f)
        BJPZ_B = pickle.load(f)
        SSCD_B = pickle.load(f)
        TouchMode = pickle.load(f)
        Guideline = pickle.load(f)
except FileNotFoundError:
    with open('data.pkl', 'wb') as f:
        pickle.dump(MUTOS_B,f)
        pickle.dump(BJPZ_B,f)
        pickle.dump(SSCD_B,f)
        pickle.dump(TouchMode,f)
        pickle.dump(Guideline, f)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("贪吃蛇-v1.1.1")
screen_rect = screen.get_rect()
direction = 'R'
N_direction = 'R'
snake_h = [40, 10]
snake_b = [[40, 10], [50, 10], [60, 10]]
food = [300, 400]
MainViewColor = (0,153,204)
AColor = (32, 158, 133)
UColor = (194, 70, 48)

game = 'M'
title_text = "贪吃蛇"
sc = 0
font = pygame.font.SysFont("SimHei", 40)
Title = font.render(title_text, True, (255,255,255))
Score = font.render(f"得分:{sc}", True, (255,255,255))
Score_rect = Score.get_rect()
Play = Button.Button("开始",0,0, font_size=40)
Play_R = Play.get_rect()
Play_R.topleft = screen_rect.width/2-Play_R.width/2, 200
Settings = Button.Button("设置", 0,0,font_size=40)
Settings_R = Settings.get_rect()
Settings_R.topleft = screen_rect.width/2-Settings_R.width/2, 250
Exit = Button.Button("退出", 0,0, font_size=40)
Exit_R = Exit.get_rect()
Exit_R.topleft = screen_rect.width/2-Exit_R.width/2, 300
Title_rect = Title.get_rect()

MUTOS = Button.Button("原地掉头", 0,0, font_size=40)
MUTOS_R = MUTOS.get_rect()
MUTOS_R.topleft = screen_rect.width/2-MUTOS_R.width/2, 200
BJPZ = Button.Button("边界碰撞", 0,0, font_size=40)
BJPZ_R = BJPZ.get_rect()
BJPZ_R.topleft = screen_rect.width/2-BJPZ_R.width/2, 250
SSCD = Button.Button("蛇身重叠", 0,0, font_size=40)
SSCD_R = SSCD.get_rect()
SSCD_R.topleft = screen_rect.width/2-SSCD_R.width/2, 300
Touch = Button.Button("触控模式", 0,0, font_size=40)
Touch_R = Touch.get_rect()
Touch.rect.topleft = screen_rect.width/2-Touch_R.width/2, 350
GuiLinesS = Button.Button("开启辅助线", 0,0, font_size=40)
GuiLinesS_R = GuiLinesS.get_rect()
GuiLinesS.rect.topleft = screen_rect.width/2-GuiLinesS_R.width/2, 400
Back = Button.Button("返回", 0,0, font_size=40)
Back_R = Back.get_rect()
Back_R.topleft = screen_rect.width/2-Back_R.width/2, 450
REST = Button.Button("主菜单", 0,0, font_size=40)
REST_R = REST.get_rect()
REST_R.topleft = screen_rect.width/2-REST_R.width/2, 350
TouchEsc = Button.Button("菜单", 0, 0, font_size=40)
TouchEsc_R = TouchEsc.get_rect()
TouchW = Button.Button(" W ", 40, 440, font_size=52)
TouchW.TouchInterval = 0
TouchW.hover = True
TouchW_R = TouchW.get_rect()
TouchA = Button.Button(" A ", 40-TouchW_R.width+TouchW_R.width/2, TouchW_R.y+TouchW_R.height, font_size=52)
TouchA.TouchInterval = 0
TouchA.hover = True
TouchA_R = TouchA.get_rect()
TouchD = Button.Button(" D ", 40+TouchW_R.width-TouchW_R.width/2, TouchW_R.y+TouchW_R.height, font_size=52)
TouchD.TouchInterval = 0
TouchD.hover = True
TouchD_R = TouchD.get_rect()
TouchS = Button.Button(" S ", 40, TouchD_R.y+TouchD_R.height, font_size=52)
TouchS.TouchInterval = 0
TouchS.hover = True
TouchS_R = TouchS.get_rect()
Clock = pygame.time.Clock()
Play.draw(screen)
Settings.draw(screen)
Exit.draw(screen)
MUTOS.draw(screen)
BJPZ.draw(screen)
SSCD.draw(screen)
Back.draw(screen)
REST.draw(screen)
Touch.draw(screen)
TouchEsc.draw(screen)
TouchW.draw(screen)
TouchA.draw(screen)
TouchD.draw(screen)
TouchS.draw(screen)
GuiLinesS.draw(screen)
E = ""
while True:
    
    if game == 'M':
        Clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or Exit.get_button_state():
                pygame.quit()
                sys.exit()
            if Play.get_button_state():
                game = 'P'
            if Settings.get_button_state():
                game = 'S'
        Title = font.render(title_text, True, (255,255,255))
        sc = 0
        title_text = "贪吃蛇"
        screen.blit(Title, (screen_rect.width/2-Title_rect.width/2,100))
        Play = Button.Button("开始",0,0, font_size=40)
        Play_R = Play.get_rect()
        Play_R.topleft = screen_rect.width/2-Play_R.width/2, 200
        screen.fill(MainViewColor)
        Title = font.render(title_text, True, (255,255,255))
        title_text = "暂停"
        screen.blit(Title, (screen_rect.width/2-Title_rect.width/2,100))
        Exit = Button.Button("退出", 0,0, font_size=40)
        Exit_R = Exit.get_rect()
        Exit_R.topleft = screen_rect.width/2-Exit_R.width/2, 300
        Play.draw(screen)
        Settings.draw(screen)
        Exit.draw(screen)
        pygame.display.update()
    if game == 'E':
        Clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Play.get_button_state():
                game = 'P'
            if Settings.get_button_state():
                game = 'S'
                E = "ES"
            if Exit.get_button_state():
                game = 'M'
                snake_h = [40, 10]
                snake_b = [[40, 10], [50, 10], [60, 10]]
                food = [300, 400]
                direction = 'R'
                E = ""
        Play = Button.Button("继续",0,0, font_size=40)
        Play_R = Play.get_rect()
        Play_R.topleft = screen_rect.width/2-Play_R.width/2, 200
        screen.fill(MainViewColor)
        Title = font.render(title_text, True, (255,255,255))
        title_text = "暂停"
        screen.blit(Title, (screen_rect.width/2-Title_rect.width/2,100))
        Exit = Button.Button("主菜单", 0,0, font_size=40)
        Exit_R = Exit.get_rect()
        Exit_R.topleft = screen_rect.width/2-Exit_R.width/2, 300
        Play.draw(screen)
        Settings.draw(screen)
        Exit.draw(screen)
        pygame.display.update()
        
    if game == 'S':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Back.get_button_state():
                if E == "ES":
                    game = "E"
                else:
                    game = 'M'
                    E = ""
            if MUTOS.get_button_state():
                MUTOS_B = not MUTOS_B
                with open('data.pkl', 'wb') as f:
                    pickle.dump(MUTOS_B,f)
                    pickle.dump(BJPZ_B,f)
                    pickle.dump(SSCD_B, f)
                    pickle.dump(TouchMode, f)
                    pickle.dump(Guideline, f)
            if BJPZ.get_button_state():
                BJPZ_B = not BJPZ_B
                with open('data.pkl', 'wb') as f:
                    pickle.dump(MUTOS_B,f)
                    pickle.dump(BJPZ_B,f)
                    pickle.dump(SSCD_B, f)
                    pickle.dump(TouchMode, f)
                    pickle.dump(Guideline, f)
            if SSCD.get_button_state():
                SSCD_B = not SSCD_B
                with open('data.pkl', 'wb') as f:
                    pickle.dump(MUTOS_B,f)
                    pickle.dump(BJPZ_B,f)
                    pickle.dump(SSCD_B, f)
                    pickle.dump(TouchMode, f)
                    pickle.dump(Guideline, f)
            if Touch.get_button_state():
                TouchMode = not TouchMode
                with open('data.pkl', 'wb') as f:
                    pickle.dump(MUTOS_B,f)
                    pickle.dump(BJPZ_B,f)
                    pickle.dump(SSCD_B, f)
                    pickle.dump(TouchMode, f)
                    pickle.dump(Guideline, f)
            if GuiLinesS.get_button_state():
                Guideline = not Guideline
                with open('data.pkl', 'wb') as f:
                    pickle.dump(MUTOS_B,f)
                    pickle.dump(BJPZ_B,f)
                    pickle.dump(SSCD_B, f)
                    pickle.dump(TouchMode, f)
                    pickle.dump(Guideline, f)
        Title = font.render(title_text, True, (255,255,255))
        title_text = "设置"
        screen.fill(MainViewColor)
        screen.blit(Title, (screen_rect.width/2-Title_rect.width/2,100))
        if MUTOS_B:
            MUTOS.draw(screen, AColor)
        else:
            MUTOS.draw(screen, UColor)
        if BJPZ_B:
            BJPZ.draw(screen, AColor)
        else:
            BJPZ.draw(screen, UColor)
        if SSCD_B:
            SSCD.draw(screen, AColor)
        else:
            SSCD.draw(screen, UColor)
        if TouchMode:
            Touch.draw(screen, AColor)
        else:
            Touch.draw(screen, UColor)
        if Guideline:
            GuiLinesS.draw(screen, AColor)
        else:
            GuiLinesS.draw(screen, UColor)
        Back.draw(screen)
        pygame.display.update()
    if game == 'P':
        Clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = 'E'
                if MUTOS_B:
                    if event.key == pygame.K_RIGHT:
                        direction = 'R'
                    if event.key == pygame.K_LEFT:
                        direction = 'L'
                    if event.key == pygame.K_UP:
                        direction = 'U'
                    if event.key == pygame.K_DOWN:
                        direction = 'D'
                else:
                    if event.key == pygame.K_RIGHT and direction != 'L':
                        direction = 'R'
                    if event.key == pygame.K_LEFT and direction != 'R':
                        direction = 'L'
                    if event.key == pygame.K_UP and direction != 'D':
                        direction = 'U'
                    if event.key == pygame.K_DOWN and direction != 'U':
                        direction = 'D'
        if TouchMode:
            if TouchEsc.get_button_state():
                game = 'E'
            if MUTOS_B:
                if TouchD.get_button_state():
                    direction = 'R'
                if TouchA.get_button_state():
                    direction = 'L'
                if TouchW.get_button_state():
                    direction = 'U'
                if TouchS.get_button_state():
                    direction = 'D'
            else:
                if TouchD.get_button_state() and direction != 'L':
                    direction = 'R'
                if TouchA.get_button_state() and direction != 'R':
                    direction = 'L'
                if TouchW.get_button_state() and direction != 'D':
                    direction = 'U'
                if TouchS.get_button_state() and direction != 'U':
                    direction = 'D'
        if direction == 'R':
            snake_h[0] += 10
        if direction == 'L':
            snake_h[0] -= 10
        if direction == 'U':
            snake_h[1] -= 10
        if direction == 'D':
            snake_h[1] += 10
        if snake_h in snake_b[2:]:
            game = 'D'
        if snake_h == food:
            fx = random.randint(0, 800)
            fy = random.randint(0, 600)
            fx, fy = str(fx), str(fy)
            fx, fy = fx[:-1] + '0', fy[:-1] + '0'
            fx, fy = int(fx), int(fy)
            print(fx, fy)
            food = [fx, fy]
            sc += 1
        else:
            snake_b.pop()
        snake_b.insert(0, [snake_h[0], snake_h[1]])
        if snake_h[0] > 800 or snake_h[0] < 0 or snake_h[1] < 0 or snake_h[1] > 600:
            if BJPZ_B:
                game = 'D'
        screen.fill((13,62,77))
        Score = font.render(f"得分:{sc}", True, (255,255,255))
        screen.blit(Score, (0, 40))
        if TouchMode:
            TouchW.draw(screen)
            TouchS.draw(screen)
            TouchD.draw(screen)
            TouchA.draw(screen)
            TouchEsc.draw(screen)
        if Guideline:
            for i in range(0, 801, 10):
                pygame.draw.rect(screen, (24, 70, 84), pygame.Rect(i, snake_h[1], 10, 10))
            for i in range(0, 601, 10):
                pygame.draw.rect(screen, (24, 70, 84), pygame.Rect(snake_h[0], i, 10, 10))
        pygame.draw.rect(screen, (218,118,91), pygame.Rect(food[0], food[1], 10, 10))
        for pos in snake_b:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.display.update()
    
    if game == 'D':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if REST.get_button_state():
                game = 'M'
                snake_h = [40, 10]
                snake_b = [[40, 10], [50, 10], [60, 10]]
                food = [300, 400]
                direction = 'R'
                E = ""
        Title = font.render(title_text, True, (255,0,0))
        title_text = "你寄了"
        Score = font.render(f"得分:{sc}", True, (255,255,255))
        screen.fill(MainViewColor)
        screen.blit(Title, (screen_rect.width/2-Title_rect.width/2,100))
        screen.blit(Score, (screen_rect.width/2-Score_rect.width/2, 150))
        REST.draw(screen)
        pygame.display.update()