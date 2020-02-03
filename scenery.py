class Scenery():
    def __init__(self, matrix ,is_filled):
        self.__matrix = matrix
        self.__is_filled= is_filled

    def draw_clouds(self, x, y):
        file = open("cloud","r")
        content = file.readlines()
        cloud_mat = []

        for line in content:
            cloud_temp = []
            for char in line:
                cloud_temp.append(char)
            cloud_mat.append(cloud_temp)

        for i in range(6):
            for j in range(30):
                self.__matrix[y+i][x+j] = cloud_mat[i][j]
                if cloud_mat[i][j] != " ":
                        self.__is_filled[y+i][x+j] = 11

    def draw_ground(self, x, cols):
        for i in range(cols):
            self.__matrix[x][i] = "-"
            self.__is_filled[x][i] = 12
