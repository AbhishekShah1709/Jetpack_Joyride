from os import system, name 
from colorama import Fore,Back,Style
import os
import curses
import signal
import random
import time
from board import Board
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from hero import Person 
from features import Features  
from obstacles import Obstacle_Vertical,Obstacle_Diagonal45,Obstacle_Diagonal135,Obstacle_Horizontal,Obstacle_Booster,Obstacle_Magnet
from scenery import Scenery
import sys
import math

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows) - 2

x = 22
y = 11

last_y1=0
last_y2=0
last_y3=0
last_y4=0
last_y5=0
last_y6=0
last_y7=0
last_y8=0

itr=0
hero_lives = 5
hero_score = 0
initial_time= time.time() 

is_filled = []
store_booster_xcoo = []
booster_ycood = []
temp_row = []

temp_fr_x = {}
temp_fr_y = {}
temp_dr_x = {}
temp_dr_y = {}
temp_start = {}
fr_x = {}
fr_y = {}
dr_x = {}
dr_y = {}

start = {}
booster_coo = {}
booster_cood = {}
coins_listx = {}
coins_listy = {}
clouds_x = {}
clouds_y = {}

st_co = 0
last_used_time = 0
booster_on = 0
last_speed_booster_used=0
magnet_x = {}
magnet_y = {}
dragon_lives = 10
x_dragon = 2175
dr_bullets=0

shoot = 0
hit_flag=0
magnet_flag = {}
magnet_flag[0] = 0
magnet_flag[1] = 0
magnet_flag[2] = 0
magnet_flag[3] = 0
last_w_time = time.time()
last_w_y= 11
transform=0
transform_flag=0

for i in range(int(rows)):
    temp_row = []
    for j in range(3000):
        temp_row.append("0 ")
    is_filled.append(temp_row)

for i in range(int(rows)):
    temp_row = []
    for j in range(3000):
        temp_row.append("0 ")
    store_booster_xcoo.append(temp_row)

for i in range(int(rows)):
    temp_row = []
    for j in range(3000):
        temp_row.append("0 ")
    booster_ycood.append(temp_row)

d = 100

for i in range(7):
    r = random.randint(int(d),200+int(d))
    booster_coo[i] = r
    d = d+250
for i in range(7):
    r = random.randint(1,1000)
    booster_cood[i] = ((r%(int(rows)-15))+11)

d = 200

for i in range(4):
    r = random.randint(d,d+200)
    magnet_x[i] = r
    d = d+400
for i in range(4):
    r = random.randint(1,1000)
    magnet_y[i] = r

d = 50

for i in range(37):
    r = random.randint(d,d+50)
    coins_listx[i] = r
    d = d+50
for i in range(37):
    r = random.randint(1,1000)
    coins_listy[i] = r

d = 75

for i in range(28):
    r = random.randint(d,d+75)
    clouds_x[i] = r
    d = d+75
for i in range(28):
    r = random.randint(1,1000)
    clouds_y[i] = r

flag=0
fire_flag=0

m = Board(rows, columns, 3000, is_filled)
m.make_board(is_filled)
mat = m.get_matrix()

for i in range(1,14):
    fill = 0
    a = random.randint(11,int(rows)-5)
    b = random.randint(60,1978)
    o = Obstacle_Vertical(mat,is_filled,a,b)

    if int(is_filled[a-2][b])==0:
        fill = fill+1
    if int(is_filled[a-1][b])==0:
        fill = fill+1
    if int(is_filled[a][b])==0:
        fill = fill+1
    if int(is_filled[a+1][b])==0:
        fill = fill+1
    if int(is_filled[a+2][b])==0:
        fill = fill+1
    
    if int(fill) == 5:
        o.draw_beam()
        is_filled[a-2][b]=1
        is_filled[a-1][b]=1
        is_filled[a][b]=1
        is_filled[a+1][b]=1
        is_filled[a+2][b]=1

for i in range(1,14):
    fill = 0
    a = random.randint(11,int(rows)-5)
    b = random.randint(60,1978)
    o1 = Obstacle_Diagonal45(mat,is_filled,a,b)
    
    if int(is_filled[a-2][b+2])==0:
        fill = fill+1
    if int(is_filled[a-1][b+1])==0:
        fill = fill+1
    if int(is_filled[a][b])==0:
        fill = fill+1
    if int(is_filled[a+1][b-1])==0:
        fill = fill+1
    if int(is_filled[a+2][b-2])==0:
        fill = fill+1
       
    if fill == 5:
        o1.draw_beam()
        is_filled[a-2][b+2]=2
        is_filled[a-1][b+1]=2
        is_filled[a][b]=2
        is_filled[a+1][b-1]=2
        is_filled[a+2][b-2]=2

for i in range(1,14):
    fill = 0
    a = random.randint(11,int(rows)-5)
    b = random.randint(60,1978)
    o2 = Obstacle_Diagonal135(mat,is_filled,a,b)
    
    if int(is_filled[a-2][b-2])==0:
        fill = fill+1
    if int(is_filled[a-1][b-1])==0:
        fill = fill+1
    if int(is_filled[a][b])==0:
        fill = fill+1
    if int(is_filled[a+1][b+1])==0:
        fill = fill+1
    if int(is_filled[a+2][b+2])==0:
        fill = fill+1
       
    if fill == 5:
        o2.draw_beam()
        is_filled[a-2][b-2]=3
        is_filled[a-1][b-1]=3
        is_filled[a][b]=3
        is_filled[a+1][b+1]=3
        is_filled[a+2][b+2]=3

for i in range(1,14):
    fill = 0
    a = random.randint(11,int(rows)-5)
    b = random.randint(60,1978)
    o6 = Obstacle_Horizontal(mat,is_filled,a,b)
    
    if int(is_filled[a][b-2])==0:
        fill = fill+1
    if int(is_filled[a][b-1])==0:
        fill = fill+1
    if int(is_filled[a][b])==0:
        fill = fill+1
    if int(is_filled[a][b+1])==0:
        fill = fill+1
    if int(is_filled[a][b+2])==0:
        fill = fill+1
       
    if fill == 5:
        o6.draw_beam()
        is_filled[a][b-2]=6
        is_filled[a][b-1]=6
        is_filled[a][b]=6
        is_filled[a][b+1]=6
        is_filled[a][b+2]=6

system('clear')
while True:
    print('\033[0;0H',end='')
#    system('tput reset')

    if time.time() - last_used_time >=10:
        flag=0

    p = Person(mat,x,y,hero_lives,hero_score,time.time(),is_filled,initial_time,flag,store_booster_xcoo,booster_ycood,transform)
    s = Scenery(mat,is_filled)
    recent_x = p.get_x()
    recent_y = p.get_y()

    for i in range(28):
        s.draw_clouds(clouds_x[i],((clouds_y[i])%4)+2)
    
    s.draw_ground(rows-1,2900)

    if st_co < 2080:
        p.draw_hero(st_co,last_y2,last_y3,last_y4,last_y5,last_y6,last_y7)
        p.draw_villain(st_co,last_y8)

    if hit_flag == 1:
        for i in range(dr_bullets):
            o5.clear_dragon_bullet(dr_x[i]+3, dr_y[i])
        dr_bullets = 0

    if st_co + x >= 2022:
        if shoot%15 == 0:
            o5 = Features(mat,is_filled)
            dr_x[dr_bullets], dr_y[dr_bullets] = o5.draw_bullet_dragon(2110,last_y8)
            dr_bullets = dr_bullets+1
            o5.clear_dragon_bullet(2110,last_y8)
    
    hit_flag=0

    if st_co+x >= 2022:
        for i in range(dr_bullets):
            hit = p.dragon_hero_collision(dr_x[i],dr_y[i])
            dr_x[i], dr_y[i] = o5.draw_bullet_dragon(dr_x[i], dr_y[i])
            
            if hit == 1:
                p.clearhero(st_co,recent_x,recent_y,last_y2,last_y3,last_y4,last_y5,last_y6,last_y7)
                hit_flag=1
                transform=0
                time.sleep(1.5)
                st_co = st_co - 20

    if fire_flag>=0:
        for i in range(0,itr):
            temp_fr_x[i] = fr_x[i]
            temp_fr_y[i] = fr_y[i]
            temp_start[i] = start[i]
            fr_x[i], fr_y[i], start[i] = o4.draw_bullet(fr_x[i],fr_y[i],start[i],booster_on)
            did_collide = o4.bullet_collision(temp_fr_x[i], temp_fr_y[i], temp_start[i])

            if x+st_co >= 2010:
                did_collide_dragon, dragon_lives = o4.bullet_collision_dragon(temp_fr_x[i], temp_fr_y[i], temp_start[i], dragon_lives)
                if did_collide_dragon == 1:
                    fr_x[i]=-1
                    fr_y[i]=-1
                    start[i]=-1
                    fire_flag = fire_flag-1
                    p.addscore(15)
                    hero_score = p.getscore()
    
                if dragon_lives == 0:
                    for i in range(int(rows)):
                        for j in range(2117,2179):
                            if int(is_filled[i][j]) == 10:
                                mat[i][j] = " "
    
                    system('clear')
                    print("CONGRATULATIONS!!!")
                    print("YOU WON THE GAME!!!")
                    quit()

            if did_collide == 1:  
                fr_x[i]=-1
                fr_y[i]=-1
                start[i]=-1
                fire_flag = fire_flag-1
                p.addscore(5)
                hero_score = p.getscore()

 
    
    for i in range(37):
        o3 = Features(mat,is_filled)
        o3.draw_coins((coins_listy[i]%(int(rows)-15))+11,coins_listx[i])

    for i in range(1,8):
        cnt = 0
        a = int(booster_coo[i-1])
        b = int((booster_cood[i-1]))
        o7 = Obstacle_Booster(mat,is_filled,b,a)
        
        for i in range(-1,2):
            for j in range(-1,2):
                if int(is_filled[b+i][a+j]) == 0 or int(is_filled[b+i][a+j]) == 7:
                    cnt = cnt+1
    
        if int(cnt) == 9:
            o7.draw_beam()
            for i in range(-1,2):
                for j in range(-1,2):
                    is_filled[b+i][a+j] = 7
                    store_booster_xcoo[b+i][a+j] = int(a)
                    booster_ycood[b+i][a+j] = int(b)

    for i in range(1,5):
        cnt = 0
        a = int(magnet_x[i-1])
        b = int((magnet_y[i-1]%(int(rows)-15))+11)
        o8 = Obstacle_Magnet(mat, is_filled,b,a)

        for i in range(-1,2):
            for j in range(-1,2):
                if int(is_filled[b+i][a+j]) == 0 or int(is_filled[b+i][a+j]) == 9:
                    cnt = cnt+1

        if int(cnt) == 9:
            o8.draw_beam()
            for i in range(-1,2):
                for j in range(-1,2):
                    is_filled[b+i][a+j] = 9

    m.print_board(st_co)
    p.draw_scoreboard(st_co,dragon_lives)
    if p.getlive() == 0:
        system('clear')
        print("GAME OVER!!!")
        print("BETTER LUCK NEXT TIME!!!")
        quit()


    for i in range(0,itr):
        o4.clear_bullet(temp_fr_x[i], temp_fr_y[i], temp_start[i])

    for i in range(0,dr_bullets):
        o5.clear_dragon_bullet(dr_x[i]+3 , dr_y[i])

    p.clearvillain(last_y8)
    p.clearhero(st_co,recent_x,recent_y,last_y2,last_y3,last_y4,last_y5,last_y6,last_y7)

    def alarmhandler(signum, frame):
        raise AlarmException
    
    def user_input(timeout=0.1):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        c = time.time()
        try:
            text = getChar()()
            signal.alarm(0)
            elps = time.time() - c
            wt = 0.1-elps
#            sys.stdout = open(os.devnull, 'w')
#            curses.noecho()
#            disable = keyboardDisable()
#            disable.start()
            time.sleep(wt)
#            curses.echo()
#            disable.stop()
#            sys.stdout = sys.__stdout__
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    
    char = user_input()
    
    cur_x = recent_x
    cur_y = recent_y

    x = cur_x
    y = cur_y

    if char != 'w':
        tt = time.time()
        diff = tt-last_w_time
        fin_pos = math.ceil(4*diff*diff)

        if magnet_flag[0] == 1 or magnet_flag[1] == 1 or magnet_flag[2] == 1 or magnet_flag[3] == 1:
            if y < int(rows)-2:
                y = y+1
        else:
            if last_w_y+fin_pos <= int(rows)-3:
                y = last_w_y+fin_pos
            else:
                y = int(rows)-3
    
    if char == 'd':
        if x+st_co < 2060:
            if x < int(columns)-2:
                x = x+1
    
    elif char == 'a':
        if int(booster_on) == 1:
            if x > 3:
                x = x-3
            if x == 3:
                x = x-2
        else:
            if x > 2:
                x = x-2
            elif x == 2:
                x = x-1
    
    elif char == 'w':
        last_w_time = time.time()
        if magnet_flag[0] == 1 or magnet_flag[1] == 1 or magnet_flag[2] == 1 or magnet_flag[3] == 1:
            if y > 12:
               y = y-2
        else:
            if y > 11:
                y = y-1

        last_w_y = y
    
    elif char == 's':
        if magnet_flag[0] == 1 or magnet_flag[1] == 1 or magnet_flag[2] == 1 or magnet_flag[3] == 1:
            if y < int(rows)-4:
                y = y+2
        else:
            if y < int(rows)-3:
                y = y+1
        
    elif char == 'f':
        o4 = Features(mat,is_filled)
        fr_x[itr], fr_y[itr], start[itr] = o4.draw_bullet(recent_x,recent_y,st_co,booster_on)
        fire_flag=fire_flag+1
        itr = itr+1
        o4.clear_bullet(recent_x,recent_y,st_co)
        
    elif char == 'q':
        system('clear')
        quit()
    
    elif char == 't':
        if transform_flag==0: 
            transform=1
            transform_flag=1
    
    elif time.time() - last_used_time >=70:
        if char == ' ':
            last_used_time = time.time()
            flag=1
    

    for i in range(0,4):
        if magnet_x[i] >= st_co and magnet_x[i] <= st_co + int(columns):
            magnet_flag[i]=1
            if x+st_co < magnet_x[i] and y < (((magnet_y[i])%(int(rows)-15))+11):
                x = x+1
                y = y+1
            elif x+st_co < magnet_x[i] and y > (((magnet_y[i])%(int(rows)-15))+11):
                x = x+1
                y = y-2
            elif x+st_co > magnet_x[i] and y < (((magnet_y[i])%(int(rows)-15))+11):
                if booster_on == 1:
                    x = x-4
                else:
                    x = x-3
                y = y+1
            elif x+st_co > magnet_x[i] and y > (((magnet_y[i])%(int(rows)-15))+11):
                if booster_on == 1:
                    x = x-4
                else:
                    x = x-3
                y = y-2
        else:
            magnet_flag[i]=0

    if magnet_flag[0] == 1 or magnet_flag[1] == 1 or magnet_flag[2] == 1 or magnet_flag[3] == 1:
        last_w_y = y
        last_w_time = time.time()

    if flag == 0:
        val = p.collision(st_co, x, y)
    
        if val >= 1:
            p.reducelive()
            transform=0
            time.sleep(1.5)
            st_co = st_co - 20

    elif flag == 1:
        p.fake_collision(st_co, x, y)

    hero_lives = p.getlive()
    points = p.gettingcoins(st_co, x, y)
    p.addscore(points)
    hero_score = p.getscore()

    if time.time()-last_speed_booster_used>=10:
        booster_on = p.collected_booster(st_co, x, y)
        if int(booster_on) == 1:
            last_speed_booster_used = time.time()
   
    last_y8 = last_y7
    last_y7 = last_y6
    last_y6 = last_y5
    last_y5 = last_y4
    last_y4 = last_y3
    last_y3 = last_y2
    last_y2 = last_y1
    last_y1 = y

    shoot = shoot+1

    if st_co<2049:
        if st_co + x > 2060:
            x = x-1
        if int(booster_on) == 0:
            st_co = st_co+1
        else:
            st_co = st_co+2

    if 320 + initial_time - time.time() <= 0:
        system('clear')
        print("TIME IS OVER!!!")
        print("BETTER LUCK NEXT TIME!!!")
        quit()
