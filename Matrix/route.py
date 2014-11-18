import random
import csv
from GridMatrix import GridMatrix
import sys

class Route:

    x_0 = 0
    x_0_original = 0
    y_0 = 0
    y_0_original = 0
    current_depth = 0
    x_1 = 0
    y_1 = 0
    x_dist = 0
    y_dist = 0
    results = []
    route_x = []
    route_list_x = []
    route_y = []
    route_list_y = []
    route_depth = []
    route_list_depth = []
    scheme = []
    steps = []
    matrix = []
    matrix_x = 0
    matrix_y = 0
    matrix_inst = GridMatrix(0, 0)
    list_matrices = []
    list_matrix_inst = []
    amount_steps = 0

    # the only information the constructor needs are the dimensions of the
    # matrix
    def __init__(self, x, y):
        self.matrix_x = x
        self.matrix_y = y
        self.matrix_inst = GridMatrix(x, y)
        self.list_matrix_inst.append(self.matrix_inst)
        self.matrix_inst.read_coordinates('grid_1.txt')
        self.results = self.matrix_inst.get_results()

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


    def read_routes(self, scheme):
        with open(scheme) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.scheme.append(row)

    def start_routes(self):
        random_order = random.sample(range(len(self.scheme)), len(self.scheme))
        self.route_list_x = []
        self.route_list_y = []
        self.route_list_depth = []
        # we make a list of matrices with an entry for each seperate layer
        self.matrix = self.matrix_inst.get_matrix()
        self.list_matrices.append(self.matrix_inst.get_matrix())

        for i in range(len(self.scheme)):
            route_number = random_order[i]
            route = self.scheme[route_number]
            start_number = route[0]
            finish_number = route[1]
            print self.results
            print finish_number
            start_coordinates = self.results[int(start_number)]
            finish_coordinates = self.results[int(finish_number)]
            x_0 = start_coordinates[0]
            y_0 = start_coordinates[1]
            x_1 = finish_coordinates[0]
            y_1 = finish_coordinates[1]
            route_append = self.createRoute(int(x_0), int(x_1),
                                                 int(y_0), int(y_1), route, route_number)
            if (route_append):
                self.route_list_x.append(self.route_x)
                self.route_list_y.append(self.route_y)
                self.route_list_depth.append(self.route_depth)
            else:
                route_list.append("schijt")
                return False

    # a method that creates a route (for now in 2D only)
    def createRoute(self, x_0, x_1, y_0, y_1, route, route_number):
        print route
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1

        self.matrix = self.list_matrices[0]

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

##        for i in range(5):
##            if random.random() < .05 and left_added < 4:
##                self.steps.append(0)
##                self.steps.append(2)
##                left_added += 1
##            if random.random() < .05 and up_added < 4:
##                self.steps.append(1)
##                self.steps.append(3)
##                up_added += 1
##
##            if random.random() < .05 and left_added > 0:
##                self.steps.remove(0)
##                self.steps.remove(2)
##                left_added -= 1
##            if random.random() < .05 and up_added > 0:
##                self.steps.remove(1)
##                self.steps.remove(3)
##                up_added -= 1

        random.shuffle(self.steps)
        self.current_depth = 0
        
        # while no route has been established: loop
        while (not route and attempt_serious < 100):
            cont = True
            # self.steps tells the route to go right or down (at first) or left
            # or up (after no legal route can be made with just down and right)
            i = 0
            not_last = True
            for i in range(len(self.steps)):
                if i + 1 == len(self.steps):
                    not_last = False
                step = self.steps[i]
                i += 1
                if (cont and step == 0):
                    cont = self.go_right(not_last)
                    route = True
                elif (cont and step == 1):
                    cont = self.go_down(not_last)
                    route = True
                elif (cont and step == 2):
                    cont = self.go_left(not_last)
                    route = True
                elif (cont and step == 3):
                    cont = self.go_up(not_last)
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
            if (attempt == 100):
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


        ## check for crossings and go deep
        j = 0
        self.current_depth = 0
        while j < len(self.steps) - 1:
            step = self.steps[j]
            free = self.check_free(step, j)
            # if a line can't go anywhere, it has to go back to try again
            if not free:
                go_back = self.go_back(step, j)
                if not go_back:
                    self.current_depth += 1
                    j = 0
                else:
                    j = go_back
            else:
                self.route_depth.append(self.current_depth)
                j += 1

        self.draw_route(self.route_x, self.route_y, self.route_depth, route_number)
        
##        for layer in self.list_matrices:
##            self.create_route(self.route_x, self.route_y, self.route_depth, route_number)

##        print route_number 
##        matrix_val = self.matrix_inst.get_matrix()
##        # print the matrix as strings, so it's easy to read
##        for column in matrix_val:
##            for row in column:
##                sys.stdout.write("%03d " % (row))
##                sys.stdout.write(" ")
##                sys.stdout.flush()
##            print
##
##        print
        
        return self.steps

    # the methods for actually moving around
    def go_right(self, not_last):
        self.x_0 += 1
        if (self.x_0 == self.matrix_x):
            return False
        self.matrix = self.list_matrices[self.current_depth]
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        if not_last:
            self.route_x.append(self.x_0)
            self.route_y.append(self.y_0)
        return True

    def go_left(self, not_last):
        self.x_0 -= 1
        if (self.x_0 == 0):
            return False
        self.matrix = self.list_matrices[self.current_depth]
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        if not_last:
            self.route_x.append(self.x_0)
            self.route_y.append(self.y_0)
        return True

    def go_down(self, not_last):
        self.y_0 += 1
        if (self.y_0 == self.matrix_y):
            return False
        self.matrix = self.list_matrices[self.current_depth]
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        if not_last:
            self.route_x.append(self.x_0)
            self.route_y.append(self.y_0)
        return True

    def go_up(self, not_last):
        self.y_0 -= 1
        if (self.y_0 == 0):
            return False
        self.matrix = self.list_matrices[self.current_depth]
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False
        if not_last:
            self.route_x.append(self.x_0)
            self.route_y.append(self.y_0)
        return True

    def check_free(self, step, step_no):
        y_check = self.route_y[step_no]
        x_check = self.route_x[step_no]
##        if step == 0:
##            x_check = self.route_x[step_no] + 1
##            y_check = self.route_y[step_no]
##        elif step == 1:
##            y_check = self.route_y[step_no + 1]
##            x_check = self.route_x[step_no + 1]
##        elif step == 2:
##            x_check = self.route_x[step_no] - 1
##            y_check = self.route_y[step_no]
##        else:
##            y_check = self.route_y[step_no] - 1
##            x_check = self.route_x[step_no]

        self.matrix = self.list_matrices[self.current_depth]
        list_temp = self.matrix[y_check]
        matrix_entry = list_temp[x_check]
        
        # check step ahead, if not free move deeper
        if matrix_entry > 0:
            return self.try_layer(x_check, y_check, self.current_depth)
        else:
            return True

    def try_layer(self, x_check, y_check, depth):
        tried_up = False
        try_both = True
        random_deep = random.random
        while try_both:
            new_depth = depth
            if self.current_depth == 0 or tried_up or random.random > .9:
                 new_depth = depth + 1
                 try_both = False
            else:
                new_depth = depth - 1
                tried_up = True
            if len(self.list_matrices) > new_depth:
                self.matrix = self.list_matrices[new_depth]
                print "oude matrix"
                print x_check
                print y_check
                print self.matrix
            else:
                self.matrix_inst = GridMatrix(self.matrix_x, self.matrix_y)
                self.list_matrix_inst.append(self.matrix_inst)
                self.matrix_inst.read_coordinates('grid_1.txt')
                self.matrix = self.matrix_inst.get_matrix()
                print "nieuwe matrix"
                print self.matrix
                self.list_matrices.append(self.matrix)

            list_temp = self.matrix[y_check]
            matrix_entry = list_temp[x_check]
            # return if you can go up (or down)
            if matrix_entry == 0:
                self.current_depth = new_depth
                return True
                                   
        return False
    
    def go_back(self, step, step_no):
        move = False
        for step in range(step_no):
            i = step + 1
            step_now = step_no - i
            if step_now == 0:
                return False
            x = self.route_x[step_now]
            y = self.route_y[step_now]
            depth = self.current_depth
            move = self.try_layer(x, y, depth)
            if move:
                return step_now
        if not move:
            return False
            
    # create a route in the matrix, overwriting previously established routes
    # for now
    def draw_route(self, route_x, route_y, route_depth, value):
        if (len(route_x) != len(route_y)):
            return False

        length = len(route_y)
##        print route_x
##        print route_y
##        print route_depth
        for i in range(length):
            route_depth = self.route_depth[i]
            current_matrix = self.list_matrices[route_depth]
            self.list_matrices.pop(route_depth)
            b = route_y[i]
            a = route_x[i]
            list_temp = current_matrix[b]
            current_matrix.pop(b)
            list_temp.pop(a)
            list_temp.insert(a, value + 1)
            current_matrix.insert(b, list_temp)
            self.list_matrices.insert(route_depth, current_matrix)

    def draw_matrices(self):
##        for i in range(len(self.route_list_y)):
##            self.draw_route(self.route_list_x[i], self.route_list_y[i], self.route_list_depth[i], i)

        for i in range(len(self.list_matrices)):
            for column in self.list_matrices[i]:
                for row in column:
                    sys.stdout.write("%03d " % (row))
                    sys.stdout.write(" ")
                    sys.stdout.flush()
                print
            print
