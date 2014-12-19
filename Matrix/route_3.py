from GridMatrix import GridMatrix
import csv
import random
import sys

# This class implements the Removing Intersections algorithm. It was
# written very last-minute, so we haven't had time to improve it as
# much as we like.

class route_3:
    
    grid = []
    list_matrices = []
    matrix_width = 0
    matrix_height = 0
    matrix = []
    intersection_list = []
    intersection_list_ordered = []
    route_list_x = []
    route_list_y = []
    route_list_z = []
    steps = []
    scheme = []
    random_order = []
    intersection_point_amount = 0
    intersection_in_route = []
    list_step_list = []
    intersection_amount = 0
    gate_coordinates = []
    times_tried = 0
    tried_previous = []
    tried_previous_original = []
    z_warning = []
    z_warning_original = []
    x_warning = []
    x_warning_original = []
    y_warning = []
    y_warning_original = []
    attempt_serious = 0
    list_step_list_original = []
    least_intersections = 1000
    best_step_list = []
    best_intersection_list = []
    best_intersection_list_ordered = []
    try_further = 0
    
    
    
	# get the dimensions of the matrix and fill in the gates, setup other
    # necessary variables
    def __init__(self, x, y, grid):
        self.grid = grid
        self.list_matrices = []
        self.matrix_width = x
        self.matrix_height = y
        self.matrix_inst = GridMatrix(x, y)
        self.read_coordinates(grid)
        self.results = self.matrix_inst.get_results()
        self.setup_intersection_list()
        self.best_step_list = []
        self.best_intersection_list = []
        self.best_intersection_list_ordered = []
        self.least_intersections = 1000
        
        
        
    # get an array of all the starting and finishing gates of the routes
    def read_routes(self, scheme):
        with open(scheme) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.scheme.append(row)
    
    # read the coordinates of the logic gates
    def read_coordinates(self, read_file):
        # create a list of the coordinates of the logical gates
        with open(read_file) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                x = int(row[0])
                y = int(row[1])
                self.gate_coordinates.append([x, y])
    
    # set all the lists to their starting position
    def setup_list_step_list(self):
        for i in range(len(self.scheme)):
            self.list_step_list.append([])
            self.list_step_list_original.append([])
            self.route_list_x.append([])
            self.route_list_y.append([])
            self.route_list_z.append([])
            self.z_warning.append(False)
            self.x_warning.append(0)
            self.y_warning.append(0)
            self.tried_previous.append(0)
            self.z_warning_original.append(False)
            self.x_warning_original.append(0)
            self.y_warning_original.append(0)
            self.tried_previous_original.append(0)
    
    # set the order in which the routes are drawn, not necessary in this class, but
    # something that was copied from route_new and implemented here.
    def set_order(self):
        different = False
        if len(self.random_order) == 0:
            self.random_order = random.sample(range(len(self.scheme)), len(self.scheme))
        else:
            if random.random() > .95:
                self.random_order = list(self.best_order)
            while not different:
                index_1 = int(random.random() * len(self.random_order))
                index_2 = int(random.random() * len(self.random_order))
                if index_1 != index_2:
                    different = True
            num_1 = self.random_order[index_1]
            num_2 = self.random_order[index_2]
            self.random_order.pop(index_1)
            self.random_order.insert(index_1, num_2)
            self.random_order.pop(index_2)
            self.random_order.insert(index_2, num_1)
    
    # the main function in this class: it sets up the routes and starts
    # the actual algorithm
    def setup_route(self):
        # we make a list of matrices with an entry for each seperate layer
        self.matrix = self.matrix_inst.get_matrix()
        self.list_matrices.append(self.matrix)
        self.set_order()
        self.setup_list_step_list()
        for i in range(len(self.random_order)):
            self.routes_drawn = i
            self.route_number = self.random_order[i]
            self.set_up_conditions()
            # Make the route
            route_append = self.create_step_list()
            self.create_route_list()
        self.create_intersection_list()
        self.intersection_list_ordered = list(self.intersection_list)
        self.intersection_list_ordered.sort(key=lambda x: x[2])
        self.avoid_intersection()
            
    # create a list from the net list
    def set_up_conditions(self):
        route = self.scheme[self.route_number]
        
        # get the start and finish gate
        start_number = route[0]
        finish_number = route[1]
        start_coordinates = self.gate_coordinates[int(start_number)]
        finish_coordinates = self.gate_coordinates[int(finish_number)]

        self.x_0 = int(start_coordinates[0])
        self.y_0 = int(start_coordinates[1])
        self.x_1 = int(finish_coordinates[0])
        self.y_1 = int(finish_coordinates[1])
        
    # create a list of steps to be taken Manhattan Style
    def create_step_list(self):
        # calculate the (smallest) distance that needs to be traveled
        self.x_dist = self.x_1 - self.x_0
        self.y_dist = self.y_1 - self.y_0
        self.total_dist = abs(self.x_dist) + abs(self.y_dist)
        
        self.steps = []
        
        # store the least amount of times you need to go to the right
        if self.x_dist >= 0:
            for i in range (self.x_dist):
                self.steps.append(1)

        # store the least amount of times you need to go to the left
        else:
            for i in range (abs(self.x_dist)):
                self.steps.append(4)
        
        # store the least amount of times you need to go up        
        if self.y_dist >= 0:
            for j in range (self.y_dist):
                self.steps.append(2)
        
        # store the least amount of times you need to go down
        else:
            for j in range (abs(self.y_dist)):
                self.steps.append(5)
        
        random.shuffle(self.steps)
        self.list_step_list.pop(self.route_number)
        self.list_step_list.insert(self.route_number, self.steps)
        self.list_step_list_original = list(self.list_step_list)
        self.best_step_list = list(self.list_step_list)

    # create a list of all the routes using x, y and z coordinates
    def create_route_list(self):
        route_x = []
        route_y = []
        route_z = []
        x_ok = True
        y_ok = True
        z_ok = True
        current_x = self.x_0
        current_y = self.y_0
        current_z = 0
        self.steps = list(self.list_step_list[self.route_number])
        for i in range(len(self.steps)):
            step = self.steps[i]
            if step == 1:
                current_x += 1
            elif step == 2:
                current_y += 1
            elif step == 3:
                current_z += 1
            elif step == 4:
                current_x -= 1
            elif step == 5:
                current_y -= 1
            else:
                current_z -= 1
            
            route_x.append(current_x)
            route_y.append(current_y)
            route_z.append(current_z)
            if current_z == 7:
                self.z_warning[self.route_number] = True
                z_ok = False
            if current_x == 0:
                self.x_warning[self.route_number] = -1
                x_ok = False
            elif current_x == self.matrix_width:
                self.x_warning[self.route_number] = 1
                x_ok = False
                
            if current_y == 0:
                self.y_warning[self.route_number] = -1
                y_ok = False
            elif current_y == self.matrix_height:
                self.y_warning[self.route_number] = 1
                y_ok = False
        
        if x_ok:
            self.x_warning[self.route_number] = 0
        if y_ok:
            self.y_warning[self.route_number] = 0
        if z_ok:
            self.z_warning[self.route_number] = False
        self.route_list_x.pop(self.route_number)
        self.route_list_x.insert(self.route_number, route_x)
        self.route_list_y.pop(self.route_number)
        self.route_list_y.insert(self.route_number, route_y)
        self.route_list_z.pop(self.route_number)
        self.route_list_z.insert(self.route_number, route_z)
        
    # at every intersection: try to lower the line. If it is attempted a
    # number of times without success: change x and y coordinates.
    def avoid_intersection(self):
        while self.intersection_amount > 0:
            
            critical_point_index = random.randrange(0, len(self.intersection_list))
            critical_point = self.intersection_list[critical_point_index]
            routes = critical_point[1]
            if len(routes) == 0:
                continue
            route_to_manipulate = routes[0]
            self.route_number = route_to_manipulate[0]
            step_number = route_to_manipulate[1]
            self.set_up_conditions()
            steps = list(self.list_step_list[self.route_number])
            z_impossible = self.z_warning[self.route_number]
            attempt = self.tried_previous[self.route_number]
            # check whether the z-value at this point is not already 8 before
            # increasing it
            if attempt < 20 and not z_impossible and len(steps) > step_number:
                if steps[step_number] != 3 and steps[step_number] != 6:
                    steps.insert(step_number, 3)
                    insert = random.randrange(step_number + 1, len(steps))
                    steps.insert(insert, 6)
                elif steps[step_number] == 3:
                    test_step = step_number
                    while steps[test_step] == 3:
                        test_step += 1
                    steps.insert(step_number, 3)
                    insert = random.randrange(test_step + 1, len(steps))
                    steps.insert(insert, 6)
                else:
                    steps.pop(step_number)
                    insert = random.randrange(step_number, len(steps))
                    steps.insert(insert, 6)
            # insert a step to change the x or y direction.
            elif len(steps) > step_number:
                if z_impossible:
                    steps.remove(3)
                    steps.remove(6)
                    self.z_warning[self.route_number] = False
                self.tried_previous[self.route_number] = 0
                self.attempt_serious += 1
                step_to_try = [1, 2, 4, 5]
                if self.x_warning[self.route_number] == 1:
                    step_to_try.remove(1)
                elif self.x_warning[self.route_number] == -1:
                    step_to_try.remove(4)
                if self.y_warning[self.route_number] == 1:
                    step_to_try.remove(2)
                elif self.y_warning[self.route_number] == -1:
                    step_to_try.remove(5)
                random.shuffle(step_to_try)
                step_tried = step_to_try[0]
                if step_tried < 3:
                    opposite = step_tried + 3
                else:
                    opposite = step_tried - 3

                steps.insert(step_number, step_tried)
                insert = random.randrange(step_number, len(steps))
                steps.insert(insert, opposite)
                
            i = 0
            # remove a step and a step in the opposite direction if
            # they follow each other in the step list
            while i < len(steps) - 1:
                current_step = steps[i]
                if current_step <= 3:
                    opposite = current_step + 3
                else:
                    opposite = current_step - 3
                next_step = steps[i + 1]
        
                if next_step == opposite:
                    steps.pop(i)
                    steps.pop(i)
                    i += 2
                i += 1
            
            # if no improvement in amount of intersections is made: go back to the step list with 
            # the best performance (variation on Hill Climber)
            if self.attempt_serious > 50:
                self.list_step_list[self.route_number] = list(self.best_step_list[self.route_number])
            
            self.tried_previous[self.route_number] += 1
            self.list_step_list.pop(self.route_number)
            self.list_step_list.insert(self.route_number, steps)
            self.create_route_list()
            self.create_intersection_list()
            self.intersection_list_ordered = list(self.intersection_list)
            self.intersection_list_ordered.sort(key=lambda x: x[2])
            if self.intersection_amount < self.least_intersections:
                self.least_intersections = self.intersection_amount
                self.best_step_list = list(self.list_step_list)
                self.best_intersection_list = list(self.intersection_list)
                self.try_further = 0
            
            elif self.try_further > 1000:
                self.try_further = 0
                self.list_step_list = list(self.best_step_list)
                self.create_route_list()
                self.create_intersection_list()
                self.intersection_list_ordered.sort(key=lambda x: x[2])
                self.z_warning = list(self.z_warning_original)
                self.x_warning = list(self.x_warning_original)
                self.y_warning = list(self.y_warning_original)
                self.tried_previous = list(self.tried_previous_original)
            elif self.try_further % 100 == 0:
                for i in range(5):
                    back_to_original = random.randrange(0, len(self.list_step_list))
                    self.list_step_list[back_to_original] = list(self.list_step_list_original[back_to_original])
                    self.create_route_list()
                    self.create_intersection_list()
                    self.z_warning[back_to_original] = self.z_warning_original[back_to_original]
                    self.x_warning[back_to_original] = self.x_warning_original[back_to_original]
                    self.y_warning[back_to_original] = self.y_warning_original[back_to_original]
                    self.tried_previous[back_to_original] = self.tried_previous_original[back_to_original]
            self.try_further += 1

        print self.intersection_list_ordered


    def setup_intersection_list(self):
        self.intersection_list = []
        for k in range(8):
            for i in range(self.matrix_width):
                for j in range(self.matrix_height):
                    self.intersection_list.append([[i, j, k], [], 0])

    def setup_intersection_in_route(self):
        for i in range(len(self.scheme)):
            self.intersection_in_route.append([i, []])
    
    def insert_intersection_in_route(self, route, step_number):
        route = self.intersection_in_route[i]
        intersections = route[1]
        route.pop(1)
        intersections.append(step_number)
        route.insert(1, intersections)
        
    # insert an intersection in the intersection list, keeping track of x, y, z value, the lines that are
    # conflicting and the step where it takes place.
    def insert_intersection(self, route_1, route_2, step_number_1, step_number_2, x_value, y_value, z_value):
        entry_index = z_value * self.matrix_height * self.matrix_width + x_value * self.matrix_height + y_value
        entry = self.intersection_list[entry_index]
        coordinate = entry[0]
        if coordinate[0] != x_value or coordinate[1] != y_value and y_value != -1:
            print entry_index
            print coordinate
            print x_value
            print y_value
            print z_value
            print "something is wrong here"
        else:
            intersections = entry[1]
            if len(intersections) == 0:
                self.intersection_point_amount += 1
            amount = entry[2]
            entry.pop(1)
            entry.pop(1)
            if [route_1, step_number_1] not in intersections:
                intersections.append([route_1, step_number_1])
                amount += 1
            if [route_2, step_number_2] not in intersections and route_2 != -1:
                intersections.append([route_2, step_number_2])
                amount += 1
            random.shuffle(intersections)
            entry.insert(2, amount)
            entry.insert(1, intersections)
        
        self.intersection_list.pop(entry_index)
        self.intersection_list.insert(entry_index, entry)
        
    # find the current intersections by comparing each route with each route
    def create_intersection_list(self):
        self.setup_intersection_list()
        self.intersection_point_amount = 0
        intersectiones = False
        # detect a intersectioning of two routes (not perfectly efficient, but it works
        # rather nicely)
        self.intersection_amount = 0
        for i in range(len(self.route_list_x)):
            
            route_x_check_1 = self.route_list_x[i]
            route_y_check_1 = self.route_list_y[i]
            route_z_check_1 = self.route_list_z[i]
            for j in range(len(self.route_list_x)):
                if (j != i):
                    intersectiones = False
                    route_x_check_2 = self.route_list_x[j]
                    route_y_check_2 = self.route_list_y[j]
                    route_z_check_2 = self.route_list_z[j]
                    for k in range(len(route_x_check_1) - 2):
                        if (intersectiones):
                            break
                        x = route_x_check_1[k + 1]
                        y = route_y_check_1[k + 1]
                        z = route_z_check_1[k + 1]
                        if [x, y] in self.gate_coordinates and z == 0:
                            self.insert_intersection(i, -1, k + 1, -1, x, y, z)
                        for l in range(len(route_x_check_2) - 2):
                            if (route_x_check_2[l + 1] == x and route_y_check_2[l + 1] == y and
                                            route_z_check_2[l + 1] == z):
                                self.insert_intersection(i, j, k + 1, l + 1, x, y, z)
                                intersectiones = True
                                self.intersection_amount += 1
                                break
        print "intersection amount"
        print self.intersection_amount
        
        
        