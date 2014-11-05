import random

class route:

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
    
    def __init__(self, x_0, x_1, y_0, y_1):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_0_original = x_0
        self.y_0_original = y_0
        self.x_dist = abs(x_1 - x_0)
        self.y_dist = abs(y_1 -y_0)
        self.switch_coordinates()
        self.route_x = [self.x_0]
        self.route_y = [self.y_0]
        for i in range (self.x_dist):
            self.steps.append(0)
        for j in range (self.y_dist):
            self.steps.append(1)

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

    def createRoute(self):
        route = False
        
        while (route == False):
            cont = True
            for step in self.steps:
                if (cont and step == 0):
                    cont = self.go_right()
                    route = True
                elif (cont and step == 1):
                    cont = self.go_down()
                    route = True
                else:
                    random.shuffle(self.steps)
                    route = False
                    self.route_x = [self.x_0_original]
                    self.route_y = [self.y_0_original]
                    self.x_0 = self.x_0_original
                    self.y_0 = self.y_0_original
                    break
                
        return self.steps
        
    def go_right(self):
        self.x_0 += 1
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry == -1:
            return False
        self.route_x.append(self.x_0)
        self.route_y.append(self.y_0)
        return True

    def go_down(self):
        self.y_0 += 1
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry == -1:
            return False
        self.route_y.append(self.y_0)
        self.route_x.append(self.x_0)
        return True
        
