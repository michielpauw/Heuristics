import random

class Route:

    x_0 = 0
    x_0_original = 0
    y_0 = 0
    y_0_original = 0
    x_1 = 0
    y_1 = 0
    x_dist = 0
    y_dist = 0
    route_x = []
    route_y = []
    steps = []
    matrix = []
    matrix_x = 0
    matrix_y = 0

    def __init__(self, x, y):
        self.matrix_x = x
        self.matrix_y = y

    
    def switch_coordinates(self):
        if self.x_0 > self.x_1:
            temp = self.x_0
            self.x_0 = self.x_1
            self.x_1 = temp

        if self.y_0 > self.y_1:
            temp = self.y_0
            self.y_0 = self.y_1
            self.y_1 = temp
            
    def import_matrix(self, matrix_in):
        self.matrix = matrix_in

    def createRoute(self, x_0, x_1, y_0, y_1, route):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_dist = abs(x_1 - x_0)
        self.y_dist = abs(y_1 -y_0)
        total_dist = self.x_dist + self.y_dist
        self.switch_coordinates()
        self.x_0_original = self.x_0
        self.y_0_original = self.y_0
        self.route_x = []
        self.route_y = []
        self.steps = []
        attempt = 0
        left_added = 0;
        up_added = 0;
        for i in range (self.x_dist):
            self.steps.append(0)
        for j in range (self.y_dist):
            self.steps.append(1)
        
        route = False
        
        while (not route):
            cont = True
            for step in self.steps:
                if (cont and step == 0):
                    cont = self.go_right()
                    route = True
                elif (cont and step == 1):
                    cont = self.go_down()
                    route = True
                elif (cont and step == 2):
                    cont = self.go_left()
                    route = True
                elif (cont and step == 3):
                    cont = self.go_up()
                    route = True
                else:
                    attempt += 1
                    random.shuffle(self.steps)
                    route = False
                    self.route_x = []
                    self.route_y = []
                    self.x_0 = self.x_0_original
                    self.y_0 = self.y_0_original
                    break

            if (attempt == 100):
                attempt = 0
                random_hor_add = random.random()
                random_hor_rem = random.random()
                random_vert_add = random.random()
                random_vert_rem = random.random()
                if (random_hor_add > .5):
                    self.steps.append(2)
                    self.steps.append(0)
                    left_added += 1
                else:
                    self.steps.append(3)
                    self.steps.append(1)
                    up_added += 1
##                elif (random_hor_rem > .5 and left_added > 0):
##                    self.steps.remove(2)
##                    self.steps.remove(0)
##                    left_added -= 1
##                
##                elif (random_vert_rem > .5 and up_added > 0):
##                      self.steps.remove(3)
##                      self.steps.remove(1)
##                      up_added -= 1

                random.shuffle(self.steps)
                route = False
                self.route_x = []
                self.route_y = []
                self.x_0 = self.x_0_original
                self.y_0 = self.y_0_original

        return self.steps
        
    def go_right(self):
        self.x_0 += 1
        if (self.x_0 == self.matrix_x):
            return False
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        self.route_x.append(self.x_0)
        self.route_y.append(self.y_0)
        return True

    def go_left(self):
        self.x_0 -= 1
        if (self.x_0 == 0):
            return False
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        self.route_x.append(self.x_0)
        self.route_y.append(self.y_0)
        return True

    def go_down(self):
        self.y_0 += 1
        if (self.y_0 == self.matrix_y):
            return False
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        self.route_y.append(self.y_0)
        self.route_x.append(self.x_0)
        return True

    def go_up(self):
        self.y_0 -= 1
        if (self.y_0 == 0):
            return False
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        self.route_y.append(self.y_0)
        self.route_x.append(self.x_0)
        return True
        
