import csv

class LineMatrix:

    # define variables
    list_hor = []
    list_ver = []
    
    hor = 0
    vert = 0
    results = []
    
    def __init__(self, a, b):
        # store the horizontal and vertical values
        list_ver = []
        self.hor = 2 * a - 1
        self.vert = 2 * b - 1
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
        self.around_chips()

    # create a matrix with the right dimensions filled with only zeroes
    def create_empty(self):
        self.list_ver = []
        for i in range(self.vert):
            self.list_hor = []
            for j in range(self.hor):
                if i % 2 == 0 and j % 2 == 1:
                    self.list_hor.append(1)
                elif i % 2 == 1 and j % 2 == 0:
                    self.list_hor.append(1)
                else:
                    self.list_hor.append("-|-  ")
            self.list_ver.append(self.list_hor)

    # place a gate having the negative gate number (-1-indexed) as its value
    def create_gate(self, a, b, value):
        list_temp = self.list_ver[b * 2]
        self.list_ver.pop(b * 2)
        list_temp.pop(a * 2)
        list_temp.insert(a * 2, -value)
        self.list_ver.insert(b * 2, list_temp)
        
    
    # get the value of the line between two corners
    def get_value(self, x_0, y_0, x_1, y_1):
        value = 0
        if x_0 == x_1:
            if y_0 < y_1:
                position_y = y_0 * 2 + 1
                position_x = x_0 * 2
            else:
                position_y = y_1 * 2 + 1
                position_x = x_0 * 2
        else:
            if x_0 < x_1:
                position_x = x_0 * 2 + 1
                position_y = y_0 * 2
            else:
                position_x = x_1 * 2 + 1
                position_y = y_0 * 2
        
        list_temp = self.list_ver[position_y]
        value = list_temp[position_x]
        return value

    
    # Set the fines for routes leading into gates to five, so it go deep before it crosses them.
    # The value can be set to one again when the gate is the supposed starting or finishing gate
    # of the route we are evaluating.
    def around_chips(self):
        for result in self.results:
            x_value = int(result[0] * 2)
            y_value = int(result[1] * 2)
            list_temp = self.list_ver[y_value]
            self.list_ver.pop(y_value)
            list_temp.pop(x_value - 1)
            list_temp.insert(x_value - 1, 5)
            list_temp.pop(x_value + 1)
            list_temp.insert(x_value + 1, 5)
            self.list_ver.insert(y_value, list_temp)
            list_temp = self.list_ver[y_value - 1]
            self.list_ver.pop(y_value - 1)
            list_temp.pop(x_value)
            list_temp.insert(x_value, 5)
            self.list_ver.insert(y_value - 1, list_temp)
            list_temp = self.list_ver[y_value + 1]
            self.list_ver.pop(y_value + 1)
            list_temp.pop(x_value)
            list_temp.insert(x_value, 5)
            self.list_ver.insert(y_value + 1, list_temp)
    
    # # we need to update the fines whenever a route is fully established or when a route changes
    # # its z-value.
    # def update_fines(self, route_x, route_y, route_z):
    #     for i in range(len(route_x) - 1):
    #         x_0 = route_x[i] * 2
    #         y_0 = route_y[i] * 2
    #         x_1 = route_x[i + 1] * 2
    #         y_1 = route_y[i + 1] * 2
    #         # if it's east or west...
    #         if x_0 != x_1:
    #             # TODO
    #         # or going north or south...
    #         elif y_0 != y_1:
    #             # TODO
    #         # or going in the z-direction
    #         else:
    #             # TODO
    
        
            
