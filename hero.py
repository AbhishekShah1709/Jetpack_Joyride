import time
from os import system, name 
import sys
import os

class Person():
    def __init__(self,matrix,x_co,y_co,lives,score,time,is_filled,initial_time,flag,boos_x,boos_y,transform):
        self.__shape = [[ "\\" ,'0', "/"], ["|" , " " , "|"], ["/" , " ", "\\"]]
        self.__shape1 = [[ "0" ," ", "\\"], ["|" , "=" , "|"], ["/" , "\\", "/"]]
        self.__shape2 = [[ "0" ,"0", "0"], ["|" , "|" , "|"], ["/" , "/", "/"]]
        
        self.__shape3 = [[ "-" ,"\\", " "], ["o" , " " , ")"], ["-" , "-", ")"]]
        self.__shape4 = [[ "^" ,'^', "~"], [" " , " " , ">"], ["v" , "v", "~"]]
        self.__shape5 = [[ "^" ,'^', "~"], [" " , " " , ">"], ["v" , "v", "~"]]
        self.__shape6 = [[ "|" ,'\\', "~"], [" " , " " , ">"], ["|" , "/", "~"]]
        self.__shape7 = [[ "^" ,'^', "~"], [" " , " " , ">"], ["v" , "v", "~"]]
        self.__shape8 = [[ "^" ,'^', "~"], [" " , " " , ">"], ["v" , "v", "~"]]
        self.__shape9 = [[ " " ,' ', "/"], ["c" , "~" , " "], [" " , " ", "\\"]]


        self.__lives = lives
        self.__init_time = initial_time
        self.__time = time
        self.__score = score
        self.__flag = flag
        self.__transform = transform
        self.__is_filled = is_filled
        self.__matrix = matrix
        self.__x = x_co
        self.__y = y_co
        self.__boos_x = boos_x
        self.__boos_y = boos_y
 
 
#    def draw_hero(self,st_co):
#        if self.__flag==0:
#            for i in range(-1,2):
#                for j in range(-1,2):
#                    self.__matrix[self.__y+i][self.__x+j+st_co] = self.__shape[i+1][j+1]
#        elif self.__flag==1:
#            for i in range(-1,2):
#                for j in range(-1,2):
#                    self.__matrix[self.__y+i][self.__x+j+st_co] = self.__shape1[i+1][j+1]
   

    def draw_hero(self,st_co,prev1,prev2,prev3,prev4,prev5,prev6):
        if self.__transform==1:
            for i in range(-1,2):
                for j in range(-19,-16):
                    self.__matrix[prev6+i][self.__x+j+st_co] = self.__shape9[i+1][j+19]
                for j in range(-16,-13):
                    self.__matrix[prev5+i][self.__x+j+st_co] = self.__shape8[i+1][j+16]
                for j in range(-13,-10):
                    self.__matrix[prev4+i][self.__x+j+st_co] = self.__shape7[i+1][j+13]
                for j in range(-10,-7):
                    self.__matrix[prev3+i][self.__x+j+st_co] = self.__shape6[i+1][j+10]
                for j in range(-7,-4):
                    self.__matrix[prev2+i][self.__x+j+st_co] = self.__shape5[i+1][j+7]
                for j in range(-4,-1):
                    self.__matrix[prev1+i][self.__x+j+st_co] = self.__shape4[i+1][j+4]
                for j in range(-1,2):
                    self.__matrix[self.__y+i][self.__x+j+st_co] = self.__shape3[i+1][j+1]
        else:
            if self.__flag==0:
                for i in range(-1,2):
                    for j in range(-1,2):
                        self.__matrix[self.__y+i][self.__x+j+st_co] = self.__shape[i+1][j+1]
            elif self.__flag==1:
                for i in range(-1,2):
                    for j in range(-1,2):
                        self.__matrix[self.__y+i][self.__x+j+st_co] = self.__shape1[i+1][j+1]

    def draw_villain(self,st_co,prev_y):
        file = open("dragon2","r")
        content = file.readlines()
        vil_mat = []

        for line in content:
            vil_temp = []
            for char in line:
                vil_temp.append(char)
            vil_mat.append(vil_temp)

        if prev_y <= 16:
            for i in range(0,19):
                for j in range(0,62):
                    self.__matrix[prev_y+i-1][2118+j] = vil_mat[i][j]
                    if vil_mat[i][j] != " ":
                        self.__is_filled[prev_y+i-1][2118+j] = 10
        else:
            for i in range(0,19):
                for j in range(0,62):
                    self.__matrix[15+i][2118+j] = vil_mat[i][j] 
                    if vil_mat[i][j] != " ":
                        self.__is_filled[15+i][2118+j] = 10

#    def clearhero(self,st_co,x_coo,y_coo):
#        for i in range(-1,2):
#            for j in range(-1,2):
#                self.__matrix[self.__y+i][self.__x+j+st_co] = " "


    def clearhero(self,st_co,x_coo,y_coo,prev1,prev2,prev3,prev4,prev5,prev6):
        if self.__transform==1:
            for i in range(-1,2):
                for j in range(-19,-16):
                    self.__matrix[prev6+i][self.__x+j+st_co] = " "
                for j in range(-16,-13):
                    self.__matrix[prev5+i][self.__x+j+st_co] = " "
                for j in range(-13,-10):
                    self.__matrix[prev4+i][self.__x+j+st_co] = " "
                for j in range(-10,-7):
                    self.__matrix[prev3+i][self.__x+j+st_co] = " "
                for j in range(-7,-4):
                    self.__matrix[prev2+i][self.__x+j+st_co] = " "
                for j in range(-4,-1):
                    self.__matrix[prev1+i][self.__x+j+st_co] = " "
                for j in range(-1,2):
                    self.__matrix[self.__y+i][self.__x+j+st_co] = " "
        else: 
            for i in range(-1,2):
                for j in range(-1,2):
                    self.__matrix[self.__y+i][self.__x+j+st_co] = " "

    def clearvillain(self,prev_y):
        if prev_y <= 16:
            for i in range(0,19):
                for j in range(0,62):
                    self.__matrix[prev_y+i-1][2118+j] = " "
                    self.__is_filled[prev_y+i-1][2118+j] = 0
        else:
            for i in range(0,19):
                for j in range(0,62):
                    self.__matrix[15+i][2118+j] = " "
                    self.__is_filled[15+i][2118+j] = 0

    def dragon_hero_collision(self, x_coo, y_coo):
        if self.__flag == 1:
            return 0
        else:
            if self.__matrix[y_coo][x_coo] != " " and x_coo>=2000:
                self.reducelive()
                return 1
            if self.__matrix[y_coo][x_coo-1] != " " and x_coo>=2000:
                self.reducelive()
                return 1
            if self.__matrix[y_coo][x_coo+1] != " " and x_coo>=2000:
                self.reducelive()
                return 1
            if self.__matrix[y_coo+12][x_coo] != " " and x_coo>=2000: 
                self.reducelive()
                return 1
            if self.__matrix[y_coo+12][x_coo-1] != " " and x_coo>=2000: 
                self.reducelive()
                return 1
            if self.__matrix[y_coo+12][x_coo+1] != " " and x_coo>=2000: 
                self.reducelive()
                return 1
            return 0

    def addscore(self,points):
        self.__score = self.__score + points

    def getscore(self):
        return self.__score
    
    def draw_scoreboard(self,st_co,dragon_lives):
        print("LIVES: ",self.__lives,end = '\t \t')
        print("SCORE: ",self.__score,end = '\t \t')
        print("TIME_REM: ",int(320 + self.__init_time - self.__time ),end = '\t \t')
        print("BOSS_LIVES: ",dragon_lives)
#        self.__matrix[1][st_co+0] = 'L'
#        self.__matrix[1][st_co+1] = 'I'
#        self.__matrix[1][st_co+2] = 'V'
#        self.__matrix[1][st_co+3] = 'E'
#        self.__matrix[1][st_co+4] = 'S'
#        self.__matrix[1][st_co+5] = ':'
#        self.__matrix[1][st_co+7] = self.__lives
#        self.__matrix[1][st_co+8] = ' '
#        self.__matrix[1][st_co+9] = ' '
#        self.__matrix[1][st_co+10] = 'S'
#        self.__matrix[1][st_co+11] = 'C'
#        self.__matrix[1][st_co+12] = 'O'
#        self.__matrix[1][st_co+13] = 'R'
#        self.__matrix[1][st_co+14] = 'E'
#        self.__matrix[1][st_co+15] = ':'
#        self.__matrix[1][st_co+16] = self.__score
#        self.__matrix[1][st_co+17] = ' ' 
#        self.__matrix[1][st_co+18] = ' ' 
#        self.__matrix[1][st_co+19] = 'T'
#        self.__matrix[1][st_co+20] = 'I'
#        self.__matrix[1][st_co+21] = 'M'
#        self.__matrix[1][st_co+22] = 'E'
#        self.__matrix[1][st_co+23] = '_'
#        self.__matrix[1][st_co+24] = 'R'
#        self.__matrix[1][st_co+25] = 'E'
#        self.__matrix[1][st_co+26] = 'M'
#        self.__matrix[1][st_co+27] = ':'
#        self.__matrix[1][st_co+28] = int(320 + self.__init_time - self.__time )
#        self.__matrix[1][st_co+29] = ' '
#        self.__matrix[1][st_co+30] = ' '
#        self.__matrix[1][st_co+31] = 'B'
#        self.__matrix[1][st_co+32] = 'O'
#        self.__matrix[1][st_co+33] = 'S'
#        self.__matrix[1][st_co+34] = 'S'
#        self.__matrix[1][st_co+35] = '_'
#        self.__matrix[1][st_co+36] = 'L'
#        self.__matrix[1][st_co+37] = 'I'
#        self.__matrix[1][st_co+38] = 'V'
#        self.__matrix[1][st_co+39] = 'E'
#        self.__matrix[1][st_co+40] = 'S'
#        self.__matrix[1][st_co+41] = ':'
#        self.__matrix[1][st_co+42] = dragon_lives

    def clear_scoreboard(self,__matrix,st_co):
        self.__matrix[1][st_co+0] = ' '
        self.__matrix[1][st_co+1] = ' '
        self.__matrix[1][st_co+2] = ' '
        self.__matrix[1][st_co+3] = ' '
        self.__matrix[1][st_co+4] = ' '
        self.__matrix[1][st_co+5] = ' '
        self.__matrix[1][st_co+7] = ' ' 
        self.__matrix[1][st_co+8] = ' '
        self.__matrix[1][st_co+9] = ' '
        self.__matrix[1][st_co+10] = ' '
        self.__matrix[1][st_co+11] = ' '
        self.__matrix[1][st_co+12] = ' '
        self.__matrix[1][st_co+13] = ' '
        self.__matrix[1][st_co+14] = ' ' 
        self.__matrix[1][st_co+15] = ' '
        self.__matrix[1][st_co+16] = ' '
        self.__matrix[1][st_co+17] = ' '
        self.__matrix[1][st_co+18] = ' '
        self.__matrix[1][st_co+19] = ' '
        self.__matrix[1][st_co+20] = ' '
        self.__matrix[1][st_co+21] = ' '
        self.__matrix[1][st_co+22] = ' '
        self.__matrix[1][st_co+23] = ' '
        self.__matrix[1][st_co+24] = ' ' 
        self.__matrix[1][st_co+25] = ' '
        self.__matrix[1][st_co+26] = ' '
        self.__matrix[1][st_co+27] = ' '
        self.__matrix[1][st_co+28] = ' '
        self.__matrix[1][st_co+29] = ' '
        self.__matrix[1][st_co+30] = ' '
        self.__matrix[1][st_co+31] = ' '
        self.__matrix[1][st_co+32] = ' '
        self.__matrix[1][st_co+33] = ' '
        self.__matrix[1][st_co+34] = ' '
        self.__matrix[1][st_co+35] = ' '
        self.__matrix[1][st_co+36] = ' '
        self.__matrix[1][st_co+37] = ' '
        self.__matrix[1][st_co+38] = ' '
        self.__matrix[1][st_co+39] = ' '
        self.__matrix[1][st_co+40] = ' '
        self.__matrix[1][st_co+41] = ' '
        self.__matrix[1][st_co+42] = ' '
        self.__matrix[1][st_co+43] = ' ' 

    def collision(self,st_co,cur_x,cur_y):
        cnt=0
        for i in range(-1,2):
            for j in range(-1,2):
                value = self.__is_filled[cur_y+i][cur_x+j+st_co]
                if int(value) == 1:
                    cnt = cnt+1
                    self.__matrix[cur_y+i][cur_x+j+st_co]="|"
                    return cnt
                elif int(value) == 2:
                    cnt = cnt+1
                    self.__matrix[cur_y+i][cur_x+j+st_co]="/"
                    return cnt
                elif int(value) == 3:
                    cnt = cnt+1
                    self.__matrix[cur_y+i][cur_x+j+st_co]="\\"
                    return cnt
                elif int(value) == 6:
                    cnt = cnt+1
                    self.__matrix[cur_y+i][cur_x+j+st_co]="-"
                    return cnt

        return cnt

    def fake_collision(self,st_co,cur_x,cur_y):
        for i in range(-1,2):
            for j in range(-1,2):
                value = self.__is_filled[cur_y+i][cur_x+j+st_co]
                if int(value) == 1:
                    for t in range(1,6):
                        if self.__matrix[cur_y+i+t][cur_x+j+st_co]=="|":
                            self.__matrix[cur_y+i+t][cur_x+j+st_co]=""
                        else:
                            break

                    for t in range(1,6):
                        if self.__matrix[cur_y+i-t][cur_x+j+st_co]=="|":
                            self.__matrix[cur_y+i-t][cur_x+j+st_co]=""
                        else:
                            break
                    return

                elif int(value) == 2:
                    for t in range(1,6):
                        if self.__matrix[cur_y+i-t][cur_x+j+st_co+t]=="/":
                            self.__matrix[cur_y+i-t][cur_x+j+st_co+t]=""
                        else:
                            break

                    for t in range(1,6):
                        if self.__matrix[cur_y+i+t][cur_x+j+st_co-t]=="/":
                            self.__matrix[cur_y+i+t][cur_x+j+st_co-t]=""
                        else:
                            break
                    return

                elif int(value) == 3:
                    for t in range(1,6):
                        if self.__matrix[cur_y+i-t][cur_x+j+st_co-t]=="\\":
                            self.__matrix[cur_y+i-t][cur_x+j+st_co-t]=""
                        else:
                            break

                    for t in range(1,6):
                        if self.__matrix[cur_y+i+t][cur_x+j+st_co+t]=="\\":
                            self.__matrix[cur_y+i+t][cur_x+j+st_co+t]=""
                        else:
                            break
                    return
                
                elif int(value) == 6:
                    for t in range(1,6):
                        if self.__matrix[cur_y+i][cur_x+j+st_co+t]=="-":
                            self.__matrix[cur_y+i][cur_x+j+st_co+t]=""
                        else:
                            break

                    for t in range(1,6):
                        if self.__matrix[cur_y+i][cur_x+j+st_co-t]=="-":
                            self.__matrix[cur_y+i][cur_x+j+st_co-t]=""
                        else:
                            break
                    return

    def gettingcoins(self, st_co, cur_x, cur_y):
        cnt1=0
        for i in range(-1,2):
            for j in range(-1,2):
                val_coin = self.__is_filled[cur_y+i][cur_x+j+st_co]
                if int(val_coin) == 4:
                    cnt1 = cnt1+1
                    self.__is_filled[cur_y+i][cur_x+j+st_co]=5
                    self.__matrix[cur_y+i][cur_x+j+st_co]=""

        return cnt1
    
    def collected_booster(self, st_co, cur_x, cur_y):
        for i in range(-1,2):
            for j in range(-1,2):
                booster_flag = self.__is_filled[cur_y+i][cur_x+j+st_co]
                if int(booster_flag) == 7:
                    x = self.__boos_x[cur_y+i][cur_x+j+st_co]
                    y = self.__boos_y[cur_y+i][cur_x+j+st_co]
                    for r in range(-1,2):
                        for c in range(-1,2):
                            self.__is_filled[y+r][x+c]=8
                            self.__matrix[y+r][x+c]=""
                    return 1
        return 0

    def reducelive(self):
        self.__lives = self.__lives-1

    def getlive(self):
        return self.__lives

    def get_matrix(self):
        return self.__matrix

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def livesboard(self,lives,dragon_lives,finish_time):
        if dragon_lives == 0:
            system('clear')
            print("Congratulations!!")
            print("You won the game!!")
            quit()
        elif finish_time == 1:
            system('clear')
            print("Time is finished!!")
            print("Better luck next time!!")
            quit()
        elif lives > 1:
            system('clear')
            print("Play carefully next time!!")
            print("You have", lives, "more lives to go")
        elif lives == 1:
            system('clear')
            print("Play carefully next time!!")
            print("You have", lives, "more live to go")
        elif lives == 0:
            system('clear')
            print("GAME OVER!!")
            print("Better luck next time!!")
            quit()
