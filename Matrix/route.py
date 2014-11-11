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
    route_list_x = []
    route_y = []
    route_list_y = []
    route_depth = []
    route_list_depth = []
    steps = []
    matrix = []
    matrix_x = 0
    matrix_y = 0

    # the only information the constructor needs are the dimensions of the
    # matrix
    def __init__(self, x, y):
        self.matrix_x = x
        self.matrix_y = y

    # if either the begin points of x or y are larger than the end points we
    # switch them (going from a to b is the same as going from b to a in
    # this problem.
    def switch_coordinates(self):
        if self.x_0 > self.x_1:
            temp = self.x_0
            self.x_0 = self.x_1
            self.x_1 = temp
            temp = self.y_0
            self.y_0 = self.y_1
            self.y_1 = temp
            
    def start_routes(self, scheme, matrix, results):
        random_order = random.sample(range(len(scheme)), len(scheme))
        self.route_list_x = []
        self.route_list_y = []
        self.route_list_depth = []
        matrix_inst = matrix
        self.matrix = matrix_inst.get_matrix()

        for i in range(len(scheme)):
            route_number = random_order[i]
            route = scheme[route_number]
            start_number = route[0]
            finish_number = route[1]
            start_coordinates = results[int(start_number)]
            finish_coordinates = results[int(finish_number)]
            x_0 = start_coordinates[0]
            y_0 = start_coordinates[1]
            x_1 = finish_coordinates[0]
            y_1 = finish_coordinates[1]
            route_append = self.createRoute(int(x_0), int(x_1),
                                                 int(y_0), int(y_1), route)
            if (route_append):
                self.route_list_x.append(self.route_x)
                self.route_list_y.append(self.route_y)
                self.route_list_depth.append(self.route_depth)
            else:
                route_list.append("schijt")
                return False

    # a method that creates a route (for now in 2D only)
    def createRoute(self, x_0, x_1, y_0, y_1, route):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1

        self.x_dist = self.x_1 - self.x_0
        self.y_dist = self.y_1 - self.y_0
        total_dist = self.x_dist + self.y_dist
        
        self.x_0_original = self.x_0
        self.y_0_original = self.y_0
        self.route_x = []
        self.route_y = []
        self.route_depth = []
        self.steps = []
        attempt = 0
        attempt_serious = 0
        left_added = 0;
        up_added = 0;
        # We first try to draw a route which goes from a to b in as few steps
        # as possible in 2D. For now we only take into account crossing logical
        # gates a route should not cross.
        if self.x_dist >= 0:
            for i in range (self.x_dist):
                self.steps.append(0)
        else:
            for i in range (abs(self.x_dist)):
                self.steps.append(2)
                
        if self.y_dist >= 0:
            for j in range (self.y_dist):
                self.steps.append(1)
        else:
            for j in range (abs(self.y_dist)):
                self.steps.append(3)

        route = False

        for i in range(5):
            if random.random() < .05 and left_added < 4:
                self.steps.append(0)
                self.steps.append(2)
                left_added += 1
            if random.random() < .05 and up_added < 4:
                self.steps.append(1)
                self.steps.append(3)
                up_added += 1

            if random.random() < .05 and left_added > 0:
                self.steps.remove(0)
                self.steps.remove(2)
                left_added -= 1
            if random.random() < .05 and up_added > 0:
                self.steps.remove(1)
                self.steps.remove(3)
                up_added -= 1

        random.shuffle(self.steps)

        # while no route has been established: loop
        while (not route and attempt_serious < 100):
            
            cont = True
            # self.steps tells the route to go right or down (at first) or left
            # or up (after no legal route can be made with just down and right)
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
                # if a route encounters a logical gate the right/down steps are
                # shuffled in an attempt to reach the correct logical gate in as
                # few steps as possible
                else:
                    attempt += 1
                    random.shuffle(self.steps)
                    route = False
                    self.route_x = []
                    self.route_y = []
                    self.x_0 = self.x_0_original
                    self.y_0 = self.y_0_original
                    break

            # nonetheless, if after 100 attempts still no correct route is found
            # we include a step going left or up and try reaching the goal again
            if (attempt == 1000):
                attempt = 0
                attempt_serious += 1
                random_hor_add = random.random()
                random_hor_rem = random.random()
                random_vert_add = random.random()
                random_vert_rem = random.random()
                if (random_hor_add > .5 and left_added < 4):
                    self.steps.append(2)
                    self.steps.append(0)
                    left_added += 1
                elif up_added < 4:
                    self.steps.append(3)
                    self.steps.append(1)
                    up_added += 1
                    
                if (random_hor_rem > .5 and left_added > 0):
                    self.steps.remove(2)
                    self.steps.remove(0)
                    left_added -= 1
                elif (random_vert_rem > .5 and up_added > 0):
                      self.steps.remove(3)
                      self.steps.remove(1)
                      up_added -= 1

                random.shuffle(self.steps)
                route = False
                self.route_x = []
                self.route_y = []
                self.x_0 = self.x_0_original
                self.y_0 = self.y_0_original


        # create an array of the depth of the route, so far only zeroes
        for i in range(len(self.steps) - 1):
            self.route_depth.append(0)

        return self.steps

    # the methods for actually moving around
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
        
