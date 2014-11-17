import random

class Route:

    # global variables
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

    # get the dimensions of the matrix
    def __init__(self, x, y):
        self.matrix_x = x
        self.matrix_y = y

    # if either the begin points of x or y are larger than the end points we
    # switch them (going from a to b is the same as going from b to a in
    # this problem.
    # hadden we dit niet verwijderd?!!!
    #def switch_coordinates(self):
     #   if self.x_0 > self.x_1:
            #temp = self.x_0

            # switch the x coordinates
      #      self.x_0, self.x_1 = self.x_1, self.x_0
            #self.x_1 = temp
            #temp = self.y_0

            # switch the y coordinates
       #     self.y_0, self.y_1 = self.y_1, self.y_2
            #self.y_1 = temp
    
    # create all the routes from gate to gate        
    def start_routes(self, scheme, matrix, results):

        # start with a random route in the scheme
        random_order = random.sample(range(len(scheme)), len(scheme))
        
        # create the variables for the routes
        self.route_list_x = []
        self.route_list_y = []
        self.route_list_depth = []
        matrix_inst = matrix
        self.matrix = matrix_inst.get_matrix()

        # create a route for every connection in the scheme
        for i in range(len(scheme)):

            # take the route from the scheme
            route_number = random_order[i]
            route = scheme[route_number]

            # get the start and finish gate
            start_number = route[0]
            finish_number = route[1]
            start_coordinates = results[int(start_number)]
            finish_coordinates = results[int(finish_number)]

            # store the routes in global variables
            x_0 = start_coordinates[0]
            y_0 = start_coordinates[1]
            x_1 = finish_coordinates[0]
            y_1 = finish_coordinates[1]

            # Make the route
            route_append = self.createRoute(int(x_0), int(x_1),
                                                 int(y_0), int(y_1), route)

            # check if a route is found
            if (route_append):
                self.route_list_x.append(self.route_x)
                self.route_list_y.append(self.route_y)
                self.route_list_depth.append(self.route_depth)
            else:
                route_list.append("schijt")
                return False

    # import the current matrix so we can check for crossing logical gates
    # and later on also crossing routes
    def import_matrix(self, matrix_in):
        self.matrix = matrix_in

    # a method that creates a route (for now in 2D only)
    def createRoute(self, x_0, x_1, y_0, y_1, route):
        
        # store the coordinates in local variables
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1

        # calculate the distance that needs to be traveled
        self.x_dist = self.x_1 - self.x_0
        self.y_dist = self.y_1 - self.y_0
        total_dist = self.x_dist + self.y_dist
        
        # dit is behoorlijk dubbel (er uit halen???)
        self.x_dist = x_1 - x_0
        self.y_dist = y_1 - y_0
        total_dist = self.x_dist + self.y_dist

        # store the start coordinates
        self.x_0_original = self.x_0
        self.y_0_original = self.y_0
        
        # creae the lists and counters for the routes
        self.route_x = []
        self.route_y = []
        self.route_depth = []
        self.steps = []
        attempt = 0
        attempt_serious = 0
        
        # volgens mij is de ; overbodig
        left_added = 0;
        up_added = 0;

        # We first try to draw a route which goes from a to b in as few steps
        # as possible in 2D. For now we only take into account crossing logical
        # gates a route should not cross.
        
        # store the amount of times you need to go to the right
        if self.x_dist >= 0:
            for i in range (self.x_dist):
                self.steps.append(0)

        # store the amount of times you need to go to the left
        else:
            for i in range (abs(self.x_dist)):
                self.steps.append(2)
        
        # store the amount of times you need to go up        
        if self.y_dist >= 0:
            for j in range (self.y_dist):
                self.steps.append(1)
        
        # store the amount of times you need to go down
        else:
            for j in range (abs(self.y_dist)):
                self.steps.append(3)

        # create the route bool for the loop
        route = False

        # create random steps in a list(?)
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

                # reset the counter
                attempt = 0
                attempt_serious += 1

                # create a new random route
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


        # create an array of the depth of the route, so far only zeroes (needs to be added?)
        for i in range(len(self.steps) - 1):
            self.route_depth.append(0)

        return self.steps

    # actually move to the right
    def go_right(self):

        # update the coordinate
        self.x_0 += 1

        # check if the move to the right is within the matrix
        if (self.x_0 == self.matrix_x):
            return False

        # check if the the step is upon a logical gate
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False

        # save the coordinates of the step in a the list
        self.route_x.append(self.x_0)
        self.route_y.append(self.y_0)
        return True

    # actually move to the left
    def go_left(self):

        # update the coordinate
        self.x_0 -= 1

        # check if the move to the right is within the matrix
        if (self.x_0 == 0):
            return False

        # check if the the step is upon a logical gate
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False

        # save the coordinates of the step in a the list
        self.route_x.append(self.x_0)
        self.route_y.append(self.y_0)
        return True

    # actually move down
    def go_down(self):

        # update the coordinate
        self.y_0 += 1

        # check if the move to the right is within the matrix
        if (self.y_0 == self.matrix_y):
            return False

        # check if the the step is upon a logical gate
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False

        # save the coordinates of the step in a the list
        self.route_y.append(self.y_0)
        self.route_x.append(self.x_0)
        return True

    # actually move up
    def go_up(self):

        # update the coordinate
        self.y_0 -= 1

        # check if the move to the right is within the matrix
        if (self.y_0 == 0):
            return False

        # check if the the step is upon a logical gate
        list_temp = self.matrix[self.y_0]
        matrix_entry = list_temp[self.x_0]
        if matrix_entry < 0:
            return False

        # save the coordinates of the step in a the list
        self.route_y.append(self.y_0)
        self.route_x.append(self.x_0)
        return True
        
