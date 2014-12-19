import random
import csv
from GridMatrix import GridMatrix
import sys
from graph_matrix import GraphMatrix
import copy

class Route:

    #  class variables
    x = 0
    x_0 = 0
    x_1 = 0
    y = 0
    y_0 = 0
    y_1 = 0
    z = 0
    z_max = 0
    x_dist = 0
    y_dist = 0
    results = []
    route_x = []
    route_list_x = []
    route_y = []
    route_list_y = []
    route_z = []
    route_list_z = []
    scheme = []
    steps = []
    matrix = []
    matrix_x = 0
    matrix_y = 0
    matrix_inst = GridMatrix(0, 0)
    list_matrices = []
    list_matrix_inst = []
    amount_steps = 0
    route = False
    tried_up = False
    route_number = 0
    total_dist = 0
    tracker = 0
    attempt_shuffle = 0
    attempt_serious = 0
    grid = ""
    routes_drawn = 0
    list_steps = []
    steps_original = []
    attempt_super_serious = 0
    random_order = []
    lines = 0
    most_routes_drawn = 0
    best_order = []
    

    # get the dimensions of the matrix and fill in the gates
    def __init__(self, x, y, grid):
        self.grid = grid
        self.list_matrices = []
        self.matrix_x = x
        self.matrix_y = y
        self.matrix_inst = GridMatrix(x, y)
        self.list_matrix_inst.append(self.matrix_inst)
        self.matrix_inst.read_coordinates(grid)
        self.results = self.matrix_inst.get_results()
        
    # vary with the order in which the routes are drawn using a Hill Climber algorithm
    def set_order(self):
        different = False
        if len(self.random_order) == 0:
            self.random_order = random.sample(range(len(self.scheme)), len(self.scheme))
            for i in range(8):
                self.random_order.remove(i + 12)
                self.random_order.insert(0, i + 12)
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

    # get an array of all the starting and finishing gates of the routes
    def read_routes(self, scheme):
        with open(scheme) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.scheme.append(row)
    
    
    # start creating all the routes
    def create_routes(self):
        append = True
        self.routes_drawn = 0
        # we make a list of matrices with an entry for each seperate layer
        self.matrix = self.matrix_inst.get_matrix()
        self.list_matrices.append(self.matrix_inst.get_matrix())
        
        for i in range(len(self.random_order)):
            self.routes_drawn = i
            self.route_number = self.random_order[i]
            self.set_up_conditions()
            # Make the route
            route_append = self.create_single_route()
            if not route_append:
                append = False
                break
            if self.routes_drawn == len(self.scheme):
                return True
        if not append:
            if self.routes_drawn > self.most_routes_drawn:
                self.most_routes_drawn = self.routes_drawn
                self.best_order = list(self.random_order)
            return False
          
    # a function that sets all the variables to their initial values
    def clear_everything(self):
        self.x = 0
        self.x_0 = 0
        self.x_1 = 0
        self.y = 0
        self.y_0 = 0
        self.y_1 = 0
        self.z = 0
        self.x_dist = 0
        self.y_dist = 0
        self.route_x = []
        self.route_list_x = []
        self.route_y = []
        self.route_list_y = []
        self.route_z = []
        self.route_list_z = []
        self.steps = []
        self.matrix = []
        self.matrix_inst = GridMatrix(self.matrix_x, self.matrix_y)
        self.list_matrices = []
        self.list_matrix_inst = []
        self.amount_steps = 0
        self.route = False
        self.tried_up = False
        self.route_number = 0
        self.total_dist = 0
        self.tracker = 0
        self.attempt_shuffle = 0
        self.attempt_serious = 0
        self.grid = ""
        self.routes_drawn = 0
        self.steps_list = []
        self.z_max = 0
        self.lines = 0
        
    def set_up_conditions(self):
        route = self.scheme[self.route_number]
        
        # get the start and finish gate
        start_number = route[0]
        finish_number = route[1]
        start_coordinates = self.results[int(start_number)]
        finish_coordinates = self.results[int(finish_number)]

        self.x_0 = int(start_coordinates[0])
        self.y_0 = int(start_coordinates[1])
        self.x_1 = int(finish_coordinates[0])
        self.y_1 = int(finish_coordinates[1])
    
    # create a list of steps going north, south, east, west
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
    
    # try to draw a single route    
    def create_single_route(self):
        
        # get the matrix of the top layer
        self.matrix = self.list_matrices[0]
        
        # the starting coordinates are now the current coordinates
        self.x = self.x_0
        self.y = self.y_0
        self.z = 0

        self.create_step_list()
        
        self.steps_original = []
        self.steps_original = list(self.steps)
        route_finished = False
        be_patient = False
        attempt = 0
        self.attempt_serious = 0
        while not route_finished:
            continue_from_step = 0
            i = 0
            if attempt > 98:
                self.x = self.x_0
                self.y = self.y_0
                self.z = 0
                self.steps = []
                self.steps = list(self.steps_original)
                append_down = int(random.random() * self.attempt_serious / 10)
                for k in range(append_down):
                    self.steps.insert(0, 3)
                    self.steps.append(6)
                attempt = 0
                self.attempt_serious += 1
                if self.attempt_serious > 100:
                    return False
            if len(self.steps) == 1:
                route_finished = True
                continue
            while i < len(self.steps) - 1 and attempt < 100:
                current_step = self.steps[i]
                in_bounds = self.update_position(current_step)
                if in_bounds < 0:
                    self.steps = []
                    self.steps = list(self.steps_original)
                    self.x = self.x_0
                    self.y = self.y_0
                    self.z = 0
                    i = 0
                    attempt += 1
                    continue
                else:
                    tile_is_free = self.check_free()
                    if not tile_is_free:
                        continue_from_step = self.find_solution(current_step, i)
                        if not continue_from_step:
                            if len(self.steps) <= len(self.steps_original) + 4:
                                i = 0
                                attempt += 1
                                self.x = self.x_0
                                self.y = self.y_0
                                self.z = 0
                                continue
                            self.steps = list(self.steps_original)
                            random.shuffle(self.steps)
                            self.x = self.x_0
                            self.y = self.y_0
                            self.z = 0
                            i = 0
                            attempt += 1
                            continue
                        else:
                            attempt += 1
                            i = 0
                            self.x = self.x_0
                            self.y = self.y_0
                            self.z = 0
                    else:
                        i += 1
                        
                if i == len(self.steps) - 1:
                    route_finished = True
                    
        if route_finished:
            self.remove_useless_steps()
            self.routes_drawn += 1
            self.tracker += 1
            self.draw_route()
            self.create_route_list()
            self.list_steps.append(self.steps)
            self.count_lines()
            return True
            
    # change the current x, y, z position based on the step taken from steps            
    def update_position(self, step):
        # update the relevant coordinate
        if step == 1:
            self.x += 1
            # check whether the route goes out of bounds
            if self.x >= self.matrix_x - 1:
                return -1
            else:
                return 1
        elif step == 2:
            self.y += 1
            if self.y >= self.matrix_y - 1:
                return -2
            else:
                return 1
        elif step == 3:
            self.z += 1
            if self.z == 8:
                return -3
            else:
                return 1
        elif step == 4:
            self.x -= 1
            if self.x == -1:
                return -4
            else:
                return 1
        elif step == 5:
            self.y -= 1
            if self.y == -1:
                return -5
            else:
                return 1
        elif step == 6:
            self.z -= 1
            if self.z == -1:
                return -6
            else:
                return 1
    
    # check whether a coordinate is free  
    def check_free(self):
        # if the new position is in a non-existing layer: create a new one
        if self.z >= len(self.list_matrices):
            self.matrix_inst = GridMatrix(self.matrix_x, self.matrix_y)
            self.list_matrix_inst.append(self.matrix_inst)
            new_matrix = self.matrix_inst.get_matrix()
            self.list_matrices.append(new_matrix)
        current_layer = self.list_matrices[self.z]
        current_row = current_layer[self.y]
        current_point = current_row[self.x]
        
        if current_point != 0:
            return False
        else:
            return True
        
    
    def find_solution(self, problem, step_number):
        random_value = random.random()
        # sometimes rearranging the steps gives the solution to both problems
        # and we should always attempt this first, because it will save steps
        if random_value < .01:
            return False
        else:
            # first go back to previous, unoccupied location
            continue_from_step = self.find_detour(problem, step_number)
            return continue_from_step

    # try to find a detour
    def find_detour(self, step, step_number):
        opposite = 0
        step_to_try = 0
        # last move is illegal, so go back to last legally reached tile
        last_step = step
        if last_step <= 3:
            opposite = last_step + 3
        else:
            opposite = last_step - 3
        self.update_position(opposite)

        free = False
        i = 0
        # try every direction from this tile
        random_try_step = random.sample([1, 2, 3, 4, 5, 6], 6)
        for i in range(int(self.attempt_serious / 8)):
            random_try_step.append(3)
        random.shuffle(random_try_step)
        random_try_step.remove(last_step)
        for i in range(len(random_try_step)):
            step_to_try = random_try_step[i]

            if step_to_try <= 3:
                opposite_to_try = step_to_try + 3
            else:
                opposite_to_try = step_to_try - 3
                
            current_position = self.update_position(step_to_try)
            # if out of bounds (i.e. current position < 0)
            if current_position < 0:
                # go back if out of bounds
                self.update_position(opposite_to_try)
                continue
            else:
                free = self.check_free()
            self.update_position(opposite_to_try)
            # if a side is free: don't look further
            if free:
                break

        if free:
            self.steps.insert(step_number, step_to_try)
            index_opposite = int(len(self.steps) - random.random() * step_number)
            self.steps.insert(index_opposite, opposite_to_try)
            return step_number

        # if not free: go back and try again (or not)
        else:
            step_number = step_number - 1
            if step_number < 0:
                return False
            else:
                return self.find_detour(self.steps[step_number], step_number)
    
    # draw the route in the matrix
    def draw_route(self):
        self.x = self.x_0
        self.y = self.y_0
        self.z = 0
        for i in range(len(self.steps) - 1):
            
            self.update_position(self.steps[i])
            
            current_matrix = self.list_matrices[self.z]
            self.list_matrices.pop(self.z)
            
            current_row = current_matrix[self.y]
            current_matrix.pop(self.y)
            
            current_row.pop(self.x)
            current_row.insert(self.x, self.route_number + 1)
            
            current_matrix.insert(self.y, current_row)
            self.list_matrices.insert(self.z, current_matrix)
    
    # draw the actual matrix      
    def draw_matrix(self):
        for matrix in self.list_matrices:
            for column in matrix:
                for row in column:
                    if row == 0:
                        # sys.stdout.write("%03d " % (row))
                        sys.stdout.write("---  ")
                        sys.stdout.flush()
                    else:
                        sys.stdout.write("%03d " % (row))
                        sys.stdout.write(" ")
                        sys.stdout.flush()
                print
            print
        print len(self.list_matrices)
             
    # create a route based on the steps from the list            
    def create_route_list(self):
        route_x = []
        route_y = []
        route_z = []
        current_x = self.x_0
        current_y = self.y_0
        current_z = 0
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
            
        self.route_list_x.append(route_x)
        self.route_list_y.append(route_y)
        self.route_list_z.append(route_z)
    
    # check whether everything went well: if the matrix is only -1's, there
    # are no intersections
    def cross_matrix(self):
        # create a matrix representing a graph of all the routes in the scheme
        graph_matrix_val = []
        graph_matrix = GraphMatrix(len(self.route_list_x))
        graph_matrix_val = graph_matrix.get_matrix()
        crosses = False
        # detect a crossing of two routes (not perfectly efficient, but it works
        # rather nicely)
        crossing_amount = 0
        for i in range(len(self.route_list_x)):
            
            route_x_check_1 = self.route_list_x[i]
            route_y_check_1 = self.route_list_y[i]
            route_z_check_1 = self.route_list_z[i]
            for j in range(len(self.route_list_x)):
                if (j != i):
                    crosses = False
                    route_x_check_2 = self.route_list_x[j]
                    route_y_check_2 = self.route_list_y[j]
                    route_z_check_2 = self.route_list_z[j]
                    for k in range(len(route_x_check_1) - 1):
                        if (crosses):
                            break
                        x = route_x_check_1[k]
                        y = route_y_check_1[k]
                        z = route_z_check_1[k]
                        for l in range(len(route_x_check_2) - 1):
                            if (route_x_check_2[l] == x and route_y_check_2[l] == y and
                                            route_z_check_2[l] == z):
                                graph_matrix.insert_node(i, j)
                                crosses = True
                                crossing_amount += 1
                                break

        for column in graph_matrix_val:
            for row in column:
                if isinstance(row, int):
                    sys.stdout.write("%02d " % (row))
                    sys.stdout.write(" ")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(row)
            print
    # remove steps if they form a loop in any way            
    def remove_useless_steps(self):
        i = 0
        if len(self.steps) == 2:
            return True
        while i < len(self.steps) - 1:
            current_step = self.steps[i]
            if current_step <= 3:
                opposite = current_step + 3
            else:
                opposite = current_step - 3
            next_step = self.steps[i + 1]
            
            if next_step == opposite:
                self.steps.pop(i)
                self.steps.pop(i)
                i += 2
            i += 1
        # check for loops we don't want
        while i < len(self.steps) - 1:
            j = i
            amount_pos_x = 0
            amount_pos_y = 0
            amount_pos_z = 0
            amount_neg_x = 0
            amount_neg_y = 0
            amount_neg_z = 0
            while j < len(self.steps) - 1:
                step = self.steps[j]
                if step == 1:
                    amount_pos_x += 1
                elif step == 2:
                    amount_pos_y += 1
                elif step == 3:
                    amount_pos_z += 1
                elif step == 4:
                    amount_neg_x += 1
                elif step == 5:
                    amount_neg_y += 1
                elif step == 6:
                    amount_neg_z += 1
                j += 1
                if amount_pos_x == amount_neg_x and amount_pos_y == amount_neg_y and amount_pos_z == amount_neg_z:
                    k = i
                    while k < j:
                        self.steps.pop[i]
                        k += 1
                    j = i
                    
    def count_lines(self):
        for i in range(len(self.steps)):
            self.lines += 1
    