class Obstacle_Vertical():
    def __init__(self,matrix,is_filled,x_coo,y_coo):
        self._matrix = matrix
        self._is_filled = is_filled
        self._shape = [["|"], ["|"], ["|"], ["|"], ["|"]]
        self._shape1 = [["/"], ["/"], ["/"], ["/"], ["/"]]
        self._shape2 = [["\\"], ["\\"], ["\\"], ["\\"], ["\\"]]
#        self.__shape3 = [[">"], ["-"], [">"]]
        self._shape4 = [["-"], ["-"], ["-"], ["-"], ["-"]]
        self._shape5 = [["=", "=", "\\"], [" ", "|", "|"], ["=", "=", "/"]]
        self._shape6 = [[" ", "_", " "], ["|", " ", "|"], ["|", " ", "|"]]
#        self.__shape7 = [["<"], ["-"], ["<"]]
        self._x_coo = x_coo
        self._y_coo = y_coo

    def draw_beam(self):
        for i in range(-2,3):
            self._matrix[self._x_coo+i][self._y_coo] = self._shape[i+2][0]
   
class Obstacle_Diagonal45(Obstacle_Vertical):
    def __init__(self,matrix,is_filled,x_coo,y_coo):
        Obstacle_Vertical.__init__(self,matrix,is_filled,x_coo,y_coo)

    def draw_beam(self):
        for i in range(-2,3):
            self._matrix[self._x_coo+i][self._y_coo-i] = self._shape1[i+2][0]
                
class Obstacle_Diagonal135(Obstacle_Vertical):
    def __init__(self,matrix,is_filled,x_coo,y_coo):
        Obstacle_Vertical.__init__(self,matrix,is_filled,x_coo,y_coo)
    
    def draw_beam(self):
        for i in range(-2,3):
            self._matrix[self._x_coo+i][self._y_coo+i] = self._shape2[i+2][0]

class Obstacle_Horizontal(Obstacle_Vertical):
    def __init__(self,matrix,is_filled,x_coo,y_coo):
        Obstacle_Vertical.__init__(self,matrix,is_filled,x_coo,y_coo)
    
    def draw_beam(self):
        for i in range(-2,3):
            self._matrix[self._x_coo][self._y_coo+i] = self._shape4[i+2][0]

class Obstacle_Magnet(Obstacle_Vertical):
    def __init__(self,matrix,is_filled,x_coo,y_coo):
        Obstacle_Vertical.__init__(self,matrix,is_filled,x_coo,y_coo)

    def draw_beam(self):
        for i in range(-1,2):
            for j in range(-1,2):
                self._matrix[self._x_coo+i][self._y_coo+j] = self._shape6[i+1][j+1]

class Obstacle_Booster(Obstacle_Vertical):
    def __init__(self,matrix,is_filled,x_coo,y_coo):
        Obstacle_Vertical.__init__(self,matrix,is_filled,x_coo,y_coo)
    
    def draw_beam(self):
        for i in range(-1,2):
            for j in range(-1,2):
                self._matrix[self._x_coo+i][self._y_coo+j] = self._shape5[i+1][j+1]
