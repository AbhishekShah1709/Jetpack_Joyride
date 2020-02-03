import time
from os import system

class Features():
    def __init__(self,matrix,is_filled):
        self.__matrix = matrix
        self.__is_filled = is_filled
        self.__shape = [["|"], ["|"], ["|"], ["|"], ["|"]]
        self.__shape1 = [["/"], ["/"], ["/"], ["/"], ["/"]]
        self.__shape2 = [["\\"], ["\\"], ["\\"], ["\\"], ["\\"]]
        self.__shape3 = [[">"], ["-"], [">"]]
        self.__shape4 = [["-"], ["-"], ["-"], ["-"], ["-"]]
        self.__shape5 = [["=", "=", "\\"], [" ", "|", "|"], ["=", "=", "/"]]
        self.__shape6 = [[" ", "_", " "], ["|", " ", "|"], ["|", " ", "|"]]
        self.__shape7 = [["<"], ["-"], ["<"]]

    def draw_coins(self,x_coo,y_coo):
        ind = 0
        for i in range(1,13):
            if int(self.__is_filled[x_coo][y_coo+i]) == 0 or int(self.__is_filled[x_coo][y_coo+i]) == 4 or int(self.__is_filled[x_coo][y_coo+i]) == 5: 
                ind = i
            else:
                break

        if ind-3 > 4:
            for i in range(1,ind-3):
                if int(self.__is_filled[x_coo][y_coo+i]) == 5:
                    self.__matrix[x_coo][y_coo+i] = " "
                    self.__is_filled[x_coo][y_coo+i]=5
                else:
                    self.__matrix[x_coo][y_coo+i] = "$"
                    self.__is_filled[x_coo][y_coo+i]=4

#    def draw_booster(self,x_coo,y_coo):
#        for i in range(-1,2):
#            for j in range(-1,2):
#                self.__matrix[y_coo+i][x_coo+j] = self.__shape5[i+1][j+1]
#
#    def draw_magnet(self, x_coo, y_coo):
#        for i in range(-1,2):
#            for j in range(-1,2):
#                self.__matrix[y_coo+i][x_coo+j] = self.__shape6[i+1][j+1]

    def draw_bullet(self, x_coo, y_coo,st_co,booster_on):
        if x_coo==y_coo and y_coo==st_co and st_co==-1:
            return -1,-1,-1
        elif x_coo+st_co+4 > 2900:
            return -1,-1,-1
        
        for i in range(-1,2):
            self.__matrix[y_coo-1][x_coo+st_co+i+3] = self.__shape3[i+1][0]

        if x_coo + st_co >= 2050:
            if int(booster_on) == 0:
                return x_coo+1,y_coo,st_co+2
            elif int(booster_on) == 1:
                return x_coo+1,y_coo,st_co+3

        else:
            if int(booster_on) == 0:
                return x_coo,y_coo,st_co+2
            elif int(booster_on) == 1:
                return x_coo,y_coo,st_co+3

    def draw_bullet_dragon(self, x_coo, y_coo):
        if x_coo==-1:
            return -1, -1

        if y_coo <= 20:
            for i in range(-1,2):
                self.__matrix[y_coo][x_coo+i-3] = self.__shape7[i+1][0]
                self.__matrix[y_coo+12][x_coo+i-3] = self.__shape7[i+1][0]
                self.__is_filled[y_coo][x_coo+i-3] = 13
                self.__is_filled[y_coo+12][x_coo+i-3] = 13
            return x_coo-3, y_coo
        else:
            for i in range(-1,2):
                self.__matrix[20][x_coo+i-3] = self.__shape7[i+1][0]
                self.__matrix[32][x_coo+i-3] = self.__shape7[i+1][0]
                self.__is_filled[20][x_coo+i-3] = 13
                self.__is_filled[32][x_coo+i-3] = 13
            return x_coo-3, 20 

    def clear_bullet(self, x_coo, y_coo, st_co):
        for i in range(-1,2):
            self.__matrix[y_coo-1][x_coo+st_co+i+3] = " "
            self.__is_filled[y_coo-1][x_coo+st_co+i+3]=0

    def clear_dragon_bullet(self, x_coo, y_coo):
        for i in range(-1,2):
            if y_coo <= 20:
                self.__matrix[y_coo][x_coo+i-3] = " "
                self.__matrix[y_coo+12][x_coo+i-3] = " "
#                print("got")
#                time.sleep(0.2)
            else:
                self.__matrix[20][x_coo+i-3] = " "
                self.__matrix[32][x_coo+i-3] = " "
#                print("got1")
#                time.sleep(0.2)


    def bullet_collision_dragon(self, x_coo, y_coo, st_co, dragon_lives):
        val1 = self.__is_filled[y_coo-1][x_coo+st_co+4]
        val2 = self.__is_filled[y_coo-1][x_coo+st_co+3]
        val3 = self.__is_filled[y_coo-1][x_coo+st_co+2]

        if int(val1) == 10 or int(val2) == 10 or int(val3) == 10:
            dragon_lives = dragon_lives - 1
            return 1, dragon_lives
        return 0, dragon_lives


    def bullet_collision(self, x_coo, y_coo ,st_co):
        val1 = self.__is_filled[y_coo-1][x_coo+st_co+4]
        val2 = self.__is_filled[y_coo-1][x_coo+st_co+3]
        val3 = self.__is_filled[y_coo-1][x_coo+st_co+2]
        if int(val1) == 1:
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+4]=="|":
                    self.__matrix[y_coo-1-t][x_coo+st_co+4]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+4]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+4]=="|":
                    self.__matrix[y_coo-1+t][x_coo+st_co+4]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+4]=0
                else:
                    break
            return 1
        elif int(val2) == 1:
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+3]=="|":
                    self.__matrix[y_coo-1-t][x_coo+st_co+3]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+3]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+3]=="|":
                    self.__matrix[y_coo-1+t][x_coo+st_co+3]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+3]=0
                else:
                    break
            return 1   
        elif int(val3) == 1:
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+2]=="|":
                    self.__matrix[y_coo-1-t][x_coo+st_co+2]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+2]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+2]=="|":
                    self.__matrix[y_coo-1+t][x_coo+st_co+2]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+2]=0
                else:
                    break
            return 1

        elif int(val1) == 2:
#            print("hiii2")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+4+t]=="/":
                    self.__matrix[y_coo-1-t][x_coo+st_co+4+t]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+4+t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+4-t]=="/":
                    self.__matrix[y_coo-1+t][x_coo+st_co+4-t]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+4-t]=0
                else:
                    break
            return 1
        
        elif int(val2) == 2:
#            print("hiii2")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+3+t]=="/":
                    self.__matrix[y_coo-1-t][x_coo+st_co+3+t]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+3+t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+3-t]=="/":
                    self.__matrix[y_coo-1+t][x_coo+st_co+3-t]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+3-t]=0
                else:
                    break
            return 1
        
        elif int(val3) == 2:
#            print("hiii2")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+3+t]=="/":
                    self.__matrix[y_coo-1-t][x_coo+st_co+3+t]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+3+t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+3-t]=="/":
                    self.__matrix[y_coo-1+t][x_coo+st_co+3-t]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+3-t]=0
                else:
                    break
            return 1

        elif int(val1) == 3:
#            print("hiii3")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+4-t]=="\\":
                    self.__matrix[y_coo-1-t][x_coo+st_co+4-t]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+4-t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+4+t]=="\\":
                    self.__matrix[y_coo-1+t][x_coo+st_co+4+t]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+4+t]=0
                else:
                    break
            return 1
        
        elif int(val2) == 3:
#            print("hiii3")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+3-t]=="\\":
                    self.__matrix[y_coo-1-t][x_coo+st_co+3-t]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+3-t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+3+t]=="\\":
                    self.__matrix[y_coo-1+t][x_coo+st_co+3+t]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+3+t]=0
                else:
                    break
            return 1        
        
        elif int(val3) == 3:
#            print("hiii3")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1-t][x_coo+st_co+2-t]=="\\":
                    self.__matrix[y_coo-1-t][x_coo+st_co+2-t]=""
                    self.__is_filled[y_coo-1-t][x_coo+st_co+2-t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1+t][x_coo+st_co+2+t]=="\\":
                    self.__matrix[y_coo-1+t][x_coo+st_co+2+t]=""
                    self.__is_filled[y_coo-1+t][x_coo+st_co+2+t]=0
                else:
                    break
            return 1

        elif int(val1) == 6:
#            print("hiii3")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1][x_coo+st_co+4-t]=="-":
                    self.__matrix[y_coo-1][x_coo+st_co+4-t]=""
                    self.__is_filled[y_coo-1][x_coo+st_co+4-t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1][x_coo+st_co+4+t]=="-":
                    self.__matrix[y_coo-1][x_coo+st_co+4+t]=""
                    self.__is_filled[y_coo-1][x_coo+st_co+4+t]=0
                else:
                    break
            return 1
        
        elif int(val2) == 6:
#            print("hiii3")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1][x_coo+st_co+3-t]=="-":
                    self.__matrix[y_coo-1][x_coo+st_co+3-t]=""
                    self.__is_filled[y_coo-1][x_coo+st_co+3-t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1][x_coo+st_co+3+t]=="-":
                    self.__matrix[y_coo-1][x_coo+st_co+3+t]=""
                    self.__is_filled[y_coo-1][x_coo+st_co+3+t]=0
                else:
                    break
            return 1        
        
        elif int(val3) == 6:
#            print("hiii3")
#            time.sleep(1)
            for t in range(1,6):
                if self.__matrix[y_coo-1][x_coo+st_co+2-t]=="-":
                    self.__matrix[y_coo-1][x_coo+st_co+2-t]=""
                    self.__is_filled[y_coo-1][x_coo+st_co+2-t]=0
                else:
                    break
            for t in range(1,6):
                if self.__matrix[y_coo-1][x_coo+st_co+2+t]=="-":
                    self.__matrix[y_coo-1][x_coo+st_co+2+t]=""
                    self.__is_filled[y_coo-1][x_coo+st_co+2+t]=0
                else:
                    break
            return 1
