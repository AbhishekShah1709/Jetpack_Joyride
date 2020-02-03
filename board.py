from colorama import Fore,Back,Style

class Board():
    def __init__(self, rows, columns, tot_columns,is_filled):
        self.__rows = rows
        self.__columns = columns
        self.__matrix = []
        self.__tot_columns = tot_columns
        self.__is_filled=is_filled 

    
    def make_board(self, is_filled):
        for i in range(int(self.__rows)):
            row = []
            for j in range(int(self.__tot_columns)):
                row.append(" ")
            self.__matrix.append(row)

    def print_board(self,st_co):
        for i in range(int(self.__rows)):
            for j in range(st_co, st_co+int(self.__columns)):
                print(Back.BLACK,end='')
                if int(self.__is_filled[i][j])==1 or int(self.__is_filled[i][j])==2 or int(self.__is_filled[i][j])==3 or int(self.__is_filled[i][j])==6 or int(self.__is_filled[i][j])==10 :
                    print(Fore.RED,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==4:
                    print(Fore.YELLOW,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==7:
                    print(Fore.BLUE,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==9:
                    print(Fore.GREEN,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==0:
                    print(Fore.CYAN,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==11:
                    print(Fore.WHITE,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==12:
                    print(Fore.WHITE,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                elif int(self.__is_filled[i][j])==13:
                    print(Fore.RED,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
                else:
                    print(Fore.RED,end='')
                    print(Style.BRIGHT,end='')
                    print(self.__matrix[i][j],end='')
            if i!=(self.__rows-1):
                print()

    def get_matrix(self):
        return self.__matrix
