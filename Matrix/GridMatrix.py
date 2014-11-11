import csv

class GridMatrix:

    list_hor = []
    list_ver = []
    hor = 0
    vert = 0
    results = []
    
    def __init__(self, a, b):
        self.hor = a
        self.vert = b
        self.create_empty()

    def get_matrix(self):
        return self.list_ver

    def get_results(self):
        return self.results

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
        for i in range(self.vert):
            self.list_hor = []
            for j in range(self.hor):
                self.list_hor.append(0)
            self.list_ver.append(self.list_hor)

    # place a gate having the negative gate number (1-indexed) as its value
    def create_gate(self, a, b, value):
        list_temp = self.list_ver[b]
        self.list_ver.pop(b)
        list_temp.pop(a)
        list_temp.insert(a, -value)
        self.list_ver.insert(b, list_temp)

    # create a route in the matrix, overwriting previously established routes
    # for now
    def create_route(self, route_x, route_y, route_depth, value):
        if (len(route_x) != len(route_y)):
            return False
        
        length = len(route_y)
        for i in range(length):
            if route_depth[0] == 0:
                b = route_y[i]
                a = route_x[i]
                list_temp = self.list_ver[b]
                self.list_ver.pop(b)
                list_temp.pop(a)
                list_temp.insert(a, value + 1)
                self.list_ver.insert(b, list_temp)
        
            
