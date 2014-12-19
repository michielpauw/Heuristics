import csv
import random

class GridMatrix:

    # define variables
    list_hor = []
    list_ver = []

    scheme = []
    
    hor = 0
    vert = 0
    results = []
    
    def __init__(self, a, b):
        # store the horizontal and vertical values
        list_ver = []
        self.hor = a
        self.vert = b
        self.create_empty()

    # return a matrix
    def get_matrix(self):
        return self.list_ver

    # return the gates for the matrix
    def get_results(self):
        return self.results

    # read the coordinates from a file
    def read_coordinates(self, read_file):

        # create a list of the coordinates of the logical gates
        with open(read_file) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.results.append(row)
                
        # and place them in the empty matrix
        for result in self.results:
            self.create_gate(int(result[0]), int(result[1]), int(result[2]))

    # create a matrix with the right dimensions filled with only zeroes
    def create_empty(self):
        self.list_ver = []
        for i in range(self.vert):
            self.list_hor = []
            for j in range(self.hor):
                self.list_hor.append(0)
            self.list_ver.append(self.list_hor)

    def gate_lead(self, read_file):
         # create a list of the coordinates of the logical gates
        with open(read_file) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.results.append(row)
                
        # and place them in the empty matrix
        for result in self.results:
            a = int(result[0])
            b = int(result[1])

            list_temp = self.list_ver[b]
            # list_temp2 = self.list_ver[b - 1]
            # list_temp3 = self.list_ver[b + 1]

            self.list_ver.pop(b)
            list_temp.pop(a)
            list_temp.insert(a, 100)
            # list_temp.pop(a - 1)
            # list_temp.insert(a - 1, 100)
            # list_temp.pop(a + 1)
            # list_temp.insert(a + 1, 100)
            self.list_ver.insert(b, list_temp)

            # self.list_ver.pop(b - 1)
            # list_temp2.pop(a)
            # list_temp2.insert(a, 100)
            # self.list_ver.insert(b - 1, list_temp2)
            # self.list_ver.pop(b + 1)
            # list_temp3.pop(a)
            # list_temp3.insert(a, 100)
            # self.list_ver.insert(b + 1, list_temp3)


    # place a gate having the negative gate number (1-indexed) as its value and add the leads
    def create_gate(self, a, b, value):
        list_temp = self.list_ver[b]
        list_temp2 = self.list_ver[b - 1]
        list_temp3 = self.list_ver[b + 1]
        self.list_ver.pop(b)
        list_temp.pop(a)
        list_temp.insert(a, -value)
        if list_temp[a - 1] >= 0:
            list_temp.pop(a - 1)
            list_temp.insert(a - 1, 100)

        if list_temp[a + 1] >= 0:
            list_temp.pop(a + 1)
            list_temp.insert(a + 1, 100)

        self.list_ver.insert(b, list_temp)
        
        if list_temp2[a] >= 0:
            self.list_ver.pop(b - 1)
            list_temp2.pop(a)
            list_temp2.insert(a, 100)
            self.list_ver.insert(b - 1, list_temp2)

        if list_temp3[a] >= 0:
            self.list_ver.pop(b + 1)
            list_temp3.pop(a)
            list_temp3.insert(a, 100)
            self.list_ver.insert(b + 1, list_temp3)

    def read_routes(self, scheme):
        with open(scheme) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.scheme.append(row)

        # start with a random route in the scheme
        random_order = random.sample(range(len(self.scheme)), len(self.scheme))

        routes_list = []

        # create a route for every connection in the scheme
        for i in range(len(self.scheme)):
            # take the route from the scheme
            route_number = random_order[i]
            route = self.scheme[i]#route_number]
            # get the start and finish gate
            start_number = route[0]
            finish_number = route[1]
            start_coordinates = self.results[int(start_number)]
            finish_coordinates = self.results[int(finish_number)]
            start_node = self.calc_node(start_coordinates[0], start_coordinates[1])
            finish_node = self.calc_node(finish_coordinates[0], finish_coordinates[1])
            route_l = [start_node, finish_node, i]#route_number]
            routes_list.append(route_l)

        return routes_list

    def calc_node(self, x, y):
        return int(x + y * self.hor)

    
        
            
