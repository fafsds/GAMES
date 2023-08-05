#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
import pygame,os,wx
from random import randint
from sys import exit
from pygame.locals import *
pygame.init()

def main():
 #获取屏幕大小
 app=wx.App()
 WHFRAMES=wx.DisplaySize()
 WIDTH=int(WHFRAMES[0]*0.7)
 HEIGHT=int(WHFRAMES[1]*0.8)
 Timers = 0 #游戏定时器
 TimersSec = 0 #秒
 tim_psd = 0
 #获取屏幕大小
 screen=pygame.display.set_mode((WIDTH,HEIGHT),0,32)
 caption=pygame.display.set_caption("超级马里奥")
 screen.fill([255,255,255])
 mariofont = pygame.font.Font('fonts/poster.ttf',22)
 mario_name = mariofont.render("MARIO",True,(84,65,190),None)
 #Game_world = mariofont.render("WORLD",True,(84,65,190),None)
 Game_moneyX = mariofont.render("X",True,(255,255,128),None)
 Game_time = mariofont.render("TIME",True,(84,65,190),None)

 money_ic5 = pygame.image.load('images/PTModelSprite_ID21675.png')
 money_ic5 = pygame.transform.scale(money_ic5, (25, 25))
 money_ic6 = pygame.image.load('images/PTModelSprite_ID21676.png')
 money_ic6 = pygame.transform.scale(money_ic6, (10, 25))
 money_ic7 = pygame.image.load('images/PTModelSprite_ID21677.png')
 money_ic7 = pygame.transform.scale(money_ic7, (25, 25))
 money_ic8 = pygame.image.load('images/PTModelSprite_ID21678.png')
 money_ic8 = pygame.transform.scale(money_ic8, (25, 25))
 money_timers = 0 #图片轮播定时器
 
 Game_world = pygame.image.load('images/PTModelSprite_ID2478.png')

 background = pygame.image.load('images/PTModelSprite_ID35342.png').convert_alpha()
 background = pygame.transform.scale(background, (WIDTH, HEIGHT))

 Roads = pygame.image.load('images/PTModelSprite_ID3790.png').convert_alpha()
 Roads2 = pygame.image.load('images/PTModelSprite_ID4224.png').convert_alpha()
 
 hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
 x,y = 15,HEIGHT-200
 inp_flag = -2 #(stop:-1 left drection ,-2 right drection) ,(walk:1 right drection ,2 left drection)
 times,times2 = 0,0 #人物动作定时器
 move_values,jump_values,jump_values2,jump_values3 = 12,0,0,0 #一步移动的距离 和 跳跃的值1,2
 jump_adder,jump_max_point = 0,50 #跳跃累加器 用来累加按键的长短 然后判断跳跃的高度,跳跃的初始值最高点 
 jump_flag = 0
 bg_w_1,bg_w_2 = 0,WIDTH-2 #两张壁纸 一前一后循环拖动的变量

 #播放背景
 
 #播放背景



 #游戏信息数据定义
 score = 0
 money = 0
 world = 11
 time = 400
 Gdata = [score,money,world,time]
 #游戏信息数据定义

 #初始化函数
 def game_initializaion(score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd):#数据初始化
 #游戏初始化数据
 inp_flag = -2 #(stop:-1 left drection ,-2 right drection) ,(walk:1 right drection ,2 left drection)
 x,y = 15,HEIGHT-200 #马里奥坐标
 times,times2 = 0,0 #人物动作定时器
 move_values,jump_values,jump_values2,jump_values3 = 12,0,0,0 #一步移动的距离 和 跳跃的值1,2
 jump_adder,jump_max_point = 0,50 #跳跃累加器 用来累加按键的长短 然后判断跳跃的高度,跳跃的初始值最高点
 jump_flag = 0
 tim_psd = 0
 bg_w_1,bg_w_2 = 0,WIDTH-2 #两张壁纸 一前一后循环拖动的变量
 Timers = 0 #游戏定时器
 score = 0 #开始分数
 money = 0 #开始金钱
 world = 11 #世界关卡第一关1-1 = 11
 time = 400 #游戏总时间
 TimersSec = 0 #游戏里的秒
 Gdata = [score,money,world,time]
 #游戏初始化数据
 return score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd
 #初始化函数

 score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd = \
 game_initializaion(score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd)#数据初始化主调函数

 clock = pygame.time.Clock()
 pygame.key.set_repeat(55)
 pygame.display.flip()

 def WalkAction(times,times2,inp_flag,hero):
 #walk action
 if y < HEIGHT -200: #如果在空中 为跳跃图片
 if inp_flag == 1: #right
 hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
 if inp_flag == 2: #left
 hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
 hero = pygame.transform.flip(hero, True, False)
 else:
 if inp_flag == 1: #right
 times += 2
 if times < 20:
  hero = pygame.image.load('images/PTModelSprite_ID34256.png').convert_alpha()
 elif times < 20:
  hero = pygame.image.load('images/PTModelSprite_ID34257..png').convert_alpha()
 elif times < 40:
  hero = pygame.image.load('images/PTModelSprite_ID34258.png').convert_alpha() 
 elif times < 60:
  hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
 elif times < 80:
  hero = pygame.image.load('images/PTModelSprite_ID34260.png').convert_alpha()
 elif times < 100:
  hero = pygame.image.load('images/PTModelSprite_ID34261.png').convert_alpha() 
 elif times < 120:
  hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
 elif times < 140:
  times = 0
 if inp_flag == 2: #left 
 times2 += 2
 if times2 < 20:
  hero = pygame.image.load('images/PTModelSprite_ID34256.png').convert_alpha()
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 20:
  hero = pygame.image.load('images/PTModelSprite_ID34257..png').convert_alpha()
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 40:
  hero = pygame.image.load('images/PTModelSprite_ID34258.png').convert_alpha() 
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 60:
  hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 80:
  hero = pygame.image.load('images/PTModelSprite_ID34260.png').convert_alpha()
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 100:
  hero = pygame.image.load('images/PTModelSprite_ID34261.png').convert_alpha() 
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 120:
  hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
  hero = pygame.transform.flip(hero, True, False)
 elif times2 < 140:
  times2 = 0
 elif inp_flag == -1:
 hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
 hero = pygame.transform.flip(hero, True, False) 
 times2 = 0
 elif inp_flag == -2:
 hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
 times2 = 0

 return times,times2,inp_flag,hero


 def HeroHeightIs(): #判断角色是否为地面y轴
 if y >= HEIGHT-200:
 return False
 else: #这是在控制的状况
 return True 


 def Reset_max_point(jump_max_point): #在地面重设默认跳跃的最高点(还原)
 if y >= (HEIGHT-200):
 jump_max_point = 50 #默认最高点是 50 
 return jump_max_point



 def jump_leftScreenBgnotMove(x): 
 if x<(WIDTH/4):
 if jump_max_point == 50 :
  if inp_flag == 1:
  x+=(2.7)
  if inp_flag == 2:
  x-=(2.7)
 elif jump_max_point == 100 :
  if inp_flag == 1:
  x+=(0.27)
  if inp_flag == 2:
  x-=(0.27)
 return x

 def Screen_MoneyIc(screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers) : #绘制第二项 金钱图标

 money_timers += 1
 if money_timers < 15 :
 screen.blit(money_ic5,(WIDTH*0.24,25)) #绘制第二项 金钱图标1
 elif money_timers < 40 :
 screen.blit(money_ic6,(WIDTH*0.24+7.5,25)) #绘制第二项 金钱图标2
 elif money_timers < 55 :
 screen.blit(money_ic7,(WIDTH*0.24,25)) #绘制第二项 金钱图标3
 elif money_timers < 80 :
 screen.blit(money_ic8,(WIDTH*0.24,25)) #绘制第二项 金钱图标4
 else:
 money_timers = 0
 return screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers


 def Game_Timers(TimersSec,Gdata,time_passed,tim_psd) : #游戏定时器

 tim_psd += time_passed
 if tim_psd >= 1000 : #为1秒的时候
 TimersSec += 1 
 tim_psd = 0
 Gdata[3] = 400 - TimersSec #游戏所剩时间
 
 return TimersSec,Gdata,time_passed,tim_psd


 while True: 
 
 #事件检测 
 for event in pygame.event.get(): 
 if event.type == pygame.QUIT: 
 exit()

 if event.type == KEYDOWN:
 keys=pygame.key.get_pressed()
 if keys[pygame.K_a]:
  if event.key == K_w and inp_flag == 0:
  if y <= HEIGHT-200: #看y坐标 必须在起点
  jump_flag = 3 #按了上 和 向前
  if y >= HEIGHT-200:#如果角色在平地才走动 后退 左
  #if bg_w_1==0:
  #x-=5
  x-=(move_values+3.5)
  inp_flag = 2
  
 if keys[pygame.K_d]:
  if event.key == K_w and inp_flag == 0:
  if y <= HEIGHT-200: #看y坐标 必须在起点
  jump_flag = 2 #按了上 和 向前
  if y >= HEIGHT-200:#如果角色在平地才走动 前景 右
  if x<(WIDTH/4): #角色还在屏幕左边 可移动
  x+=(move_values+3.5)
  inp_flag = 1
  
 if keys[pygame.K_w]: #jump
  jump_flag = 1 #仅仅是按了跳跃
  jump_adder += 1 #跳跃累加器
  if event.key == pygame.K_d and (jump_flag == 1):
  if y == HEIGHT-200: #看y坐标 必须在起点
  jump_flag = 2 #按了上 和 向前
  if event.key == pygame.K_a and (jump_flag == 1):
  if y == HEIGHT-200: #看y坐标 必须在起点
  jump_flag = 3 #按了上 和 向后

 if keys[pygame.K_p]: #重启
  score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,\
  jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd = \
  game_initializaion(score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,\
  move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,\
  bg_w_2,tim_psd)
  

 if event.type == KEYUP:
 if keys[pygame.K_a]:
  inp_flag = -1
 if keys[pygame.K_d]:
  inp_flag = -2
 if keys[pygame.K_w]:
  if jump_adder < 4 : #如果松开按键没有达到jump_adder跳跃累加器的值 (那么就他们置零)
  jump_adder = 0

 ##在地面时 重设默认跳跃的最高点(还原)
 jump_max_point = Reset_max_point(jump_max_point)

 #jump action 1
 if jump_flag == 1: #只有跳跃
 #让其他方式跳跃值为 0
 jump_values2 = 0
 jump_values3 = 0
 #------
 #持续按键跳跃的结构
 if jump_adder >=4 :
 jump_max_point = 100 #第二次跳跃最大值
 jump_adder = 0
 #------
 jump_values+=1.25
 if jump_values <= jump_max_point:
 y -= 5

 x = jump_leftScreenBgnotMove(x)

 if jump_max_point == 100:#跳跃的高度不同 y坐标的速度也要慢点
  y += 1.5
  x = jump_leftScreenBgnotMove(x)

 elif jump_values <= jump_max_point+8:
 pass
 elif jump_values <=jump_max_point*2+8:
 if HeroHeightIs(): #如果角色在控制 就继续加y轴的值 1
  y += 5
  
  x = jump_leftScreenBgnotMove(x)

  if jump_max_point == 100:#跳跃的高度不同 y坐标的速度也要慢点
  y -= 1.5
  x = jump_leftScreenBgnotMove(x)

 else:
 y = HEIGHT-200
 jump_flag = 0
 jump_values = 0

 
 #wall detection
 if x<=0:
 x=0
 if x+hero.get_width()>WIDTH:
 x=WIDTH-hero.get_width()
 

 #角色的动作 函数 
 times,times2,inp_flag,hero = WalkAction(times,times2,inp_flag,hero)

 #1 .bg move---blit
 screen.blit(background,(bg_w_2,0))
 screen.blit(background,(bg_w_1,0))

 #绘制信息
 
 screen.blit(mario_name,(WIDTH*0.03,3))#绘制第一项 名字

 screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers = \
 Screen_MoneyIc(screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers) #绘制第二项 金钱图标

 screen.blit(Game_moneyX,(WIDTH*0.28,24))#绘制第二项 x
 screen.blit(Game_world,(WIDTH*0.5-Game_world.get_width()/2,3))#绘制第三项 世界地图
 screen.blit(Game_time,(WIDTH*0.84,3))#绘制第四项 游戏时间

 for DATAi in range(4):
 Game_data = mariofont.render("%s"% Gdata[DATAi],True,(255,255,128),None) #综合绘制: 分数 金币 关卡 游戏时间
 if DATAi != 2:
 screen.blit(Game_data,(WIDTH*(0.03+DATAi*0.27),24))
 elif DATAi == 2:
 Game_data = mariofont.render("%s-%s"% (Gdata[DATAi]/10,Gdata[DATAi]%10),True,(255,255,128),None) #综合绘制: 分数 金币 关卡 游戏时间
 screen.blit(Game_data,(WIDTH*0.5-Game_data.get_width()/2,15))
 
 #绘制信息

 #2 .bg move--panel
 #if inp_flag == 2: #往左走 壁纸向右拖动
 # bg_w_1+=move_values/4
 # bg_w_2+=move_values/4
 if inp_flag == 1 and x>=(WIDTH/4):#往右走 壁纸向左拖动
 bg_w_1-=(move_values/4-0.5)
 bg_w_2-=(move_values/4-0.5)

 if bg_w_1>=0:
 bg_w_1,bg_w_2 = 0,WIDTH-2
 if bg_w_1<-WIDTH:
 bg_w_1,bg_w_2 = 0,WIDTH-2

 screen.blit(hero,(x,y))
 pygame.time.delay(2) #毫秒

 time_passed = clock.tick()
 TimersSec,Gdata,time_passed,tim_psd = Game_Timers(TimersSec,Gdata,time_passed,tim_psd) #游戏定时
 
 pygame.display.update()
 
if __name__ == '__main__':
 main()
