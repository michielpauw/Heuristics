import random
import csv
from GridMatrix import GridMatrix
import sys
from graph_matrix import GraphMatrix

class Route:

    #  class variables
    x = 0
    x_0 = 0
    x_1 = 0
    y = 0
    y_0 = 0
    y_1 = 0
    z = 0
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
        

    # get an array of all the starting and finishing gates of the routes
    def read_routes(self, scheme):
        with open(scheme) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.scheme.append(row)

    def create_routes(self):
        print "GAAN WE WEER"
        # the order in which the routes are drawn is random
        random_order = random.sample(range(len(self.scheme)), len(self.scheme))
        self.routes_drawn = 0
        # we make a list of matrices with an entry for each seperate layer
        self.matrix = self.matrix_inst.get_matrix()
        self.list_matrices.append(self.matrix_inst.get_matrix())
        for i in range(len(random_order)):
            print "HOLLA"
            self.route_number = random_order[i]
            self.set_up_conditions()
            # Make the route
            route_append = self.create_single_route()
            if not route_append:
                return False
            if self.routes_drawn == len(self.scheme):
                return True
          
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
        self.matrix_x = 0
        self.matrix_y = 0
        self.matrix_inst = GridMatrix(0, 0)
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
        
    def create_single_route(self):
        
        # get the matrix of the top layer
        self.matrix = self.list_matrices[0]
        
        # the starting coordinates are now the current coordinates
        self.x = self.x_0
        self.y = self.y_0
        self.z = 0

        self.create_step_list()
        print "route_number"
        print self.route_number + 1
        
        steps_original = self.steps
        route_finished = False
        attempt = 0
        self.attempt_serious = 0
        while not route_finished:
            continue_from_step = 0
            i = 0
            if attempt > 100:
                self.steps = steps_original
                attempt = 0
                self.attempt_serious += 1
                if self.attempt_serious > 100:
                    print "start over"
                    return False
            while i < len(self.steps) - 1:
                current_step = self.steps[i]
                in_bounds = self.update_position(current_step)
                if in_bounds < 0:
                    continue_from_step = self.find_solution(in_bounds, i)
                    i = continue_from_step
                    self.x = self.x_0
                    self.y = self.y_0
                    self.z = 0
                    attempt += 1
                    break
                else:
                    tile_is_free = self.check_free()
                    if not tile_is_free:
                        continue_from_step = self.find_solution(current_step, i)
                        i = continue_from_step
                        if not continue_from_step:
                            self.steps = steps_original
                            self.x = self.x_0
                            self.y = self.y_0
                            self.z = 0
                            i = 0
                            attempt += 1
                            break
                    else:
                        i += 1
                if i == len(self.steps) - 1:
                    route_finished = True
                    
        if route_finished:
            self.remove_useless_steps()
            self.routes_drawn += 1
            print self.routes_drawn
            print "attempt_serious"
            print self.attempt_serious
            self.tracker += 1
            self.draw_route()
            self.create_route_list()
            return True
                
    
    def remove_useless_steps(self):
        print "lengte"
        print len(self.steps)
        i = 0
        while i < len(self.steps) - 1:
            current_step = self.steps[i]
            if current_step <= 3:
                opposite = current_step + 3
            else:
                opposite = current_step - 3
            next_step = self.steps[i + 1]
            if next_step == opposite:
                print self.steps
                print i
                print next_step
                print opposite
                self.steps.pop(i)
                self.steps.pop(i)
                i -= 2
            i += 1
    
    def update_position(self, step):
        # update the relevant coordinate
        if step == 1:
            self.x += 1
            # check whether the route goes out of bounds
            if self.x == self.matrix_x - 1:
                return -1
            else:
                return 1
        elif step == 2:
            self.y += 1
            if self.y == self.matrix_y - 1:
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
               
    def check_free(self):
        # if the new position is in a non-existing layer: create a new one
        if self.z >= len(self.list_matrices):
            self.matrix_inst = GridMatrix(self.matrix_x, self.matrix_y)
            self.list_matrix_inst.append(self.matrix_inst)
            new_matrix = self.matrix_inst.get_matrix()
            self.list_matrices.append(new_matrix)
        current_layer = self.list_matrices[self.z]
        current_row = current_layer[self.y]
        print "soms error"
        print len(current_row)
        print self.x
        current_point = current_row[self.x]
        
        if current_point != 0:
            return False
        else:
            return True
        
        
    def find_solution(self, problem, step_number):
        random_value = random.random()
        # sometimes rearranging the steps gives the solution to both problems
        # and we should always attempt this first, because it will save steps
        if random_value < .99:
            self.attempt_shuffle += 1
            random.shuffle(self.steps)
            return 0
        else:
            # find deeper solution for out of bounds
            if problem < 0 and len(self.steps) > self.total_dist:
                # remove the step of which there are too many (and also a
                # step in the opposite direction)
                step_too_much = -problem
                if step_too_much <= 3:
                    opposite = step_too_much + 3
                else:
                    opposite = step_too_much - 3
                if step_too_much in self.steps and opposite in self.steps:
                    self.steps.remove(step_too_much)
                    self.steps.remove(opposite)
                else:
                    random.shuffle(self.steps)
                    return 0
            
            # find deeper solution for occupied tile
            elif problem < 0:
                random.shuffle(self.steps)
            else:
                # first go back to previous, unoccupied location
                continue_from_step = self.find_detour(problem, step_number)
                return continue_from_step
                    
                    
    def find_detour(self, step, step_number):
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
        random_try_step.remove(last_step)
        for i in range(5):
            step_to_try = random_try_step[i]
            
            if step_to_try<= 3:
                opposite = last_step + 3
            else:
                opposite = last_step - 3
            
            if self.z == 0 and step_to_try == 6:
                continue
            current_position = self.update_position(step_to_try)
            # if out of bounds (i.e. current position < 0)
            if current_position < 0:
                # go back if out of bounds
                self.update_position(opposite)
                continue
            else:
                free = self.check_free()
            # if a side is free: don't look further
            if free:
                break
            # if not free: go back and try again (or not)
            else:
                self.update_position(opposite)
                step_number = step_number - 1
                if step_number < 0:
                    return False
                return self.find_detour(self.steps[step_number], step_number)
        
        if free:
            self.steps.insert(step_number, step_to_try)
            if step_to_try <= 3:
                opposite = step_to_try + 3
            else:
                opposite = step_to_try - 3
            
            # if the solving step is taken in the opposite direction of the original
            # step, it will return to the same point, which is quite useless
            if step_to_try == opposite:
                index_original_step = int(len(self.steps) - random.random() * step_number)
                self.steps.pop[step_number]
                self.steps.insert(index_original_step, last_step)
            
            index_opposite = int(len(self.steps) - random.random() * step_number)
            self.steps.insert(index_opposite, opposite)
            return step_number          

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
             
                
    def create_route_list(self):
        print self.steps
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
                    for k in range(len(route_x_check_1)):
                        if (crosses):
                            break
                        x = route_x_check_1[k]
                        y = route_y_check_1[k]
                        z = route_z_check_1[k]
                        for l in range(len(route_x_check_2)):
                            if (route_x_check_2[l] == x and route_y_check_2[l] == y and
                                            route_z_check_2[l] == z):
                                graph_matrix.insert_node(i, j)
                                crosses = True
                                crossing_amount += 1
                                break
            # crossing_amount_list.append([i, crossing_amount])

        graph_matrix_val = graph_matrix.get_matrix()
        # sorted_by_second =  sorted(self.crossing_amount_list, key=lambda tup: tup[1])

        for column in graph_matrix_val:
            for row in column:
                if isinstance(row, int):
                    sys.stdout.write("%02d " % (row))
                    sys.stdout.write(" ")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(row)
            print
                
                