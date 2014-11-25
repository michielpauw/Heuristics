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
                    self.list_hor.append(" .   ")
            self.list_ver.append(self.list_hor)

    # place a gate having the negative gate number (-1-indexed) as its value
    def create_gate(self, a, b, value):
        list_temp = self.list_ver[b * 2]
        self.list_ver.pop(b * 2)
        list_temp.pop(a * 2)
        list_temp.insert(a * 2, -value)
        self.list_ver.insert(b * 2, list_temp)

    
        
            
