import random
import csv
from GridMatrix import GridMatrix
import sys

class Route:

    # global variables
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

    # get the dimensions of the matrix and fill in the gates
    def __init__(self, x, y, grid):
        self.matrix_x = x
        self.matrix_y = y
        self.matrix_inst = GridMatrix(x, y)
        self.list_matrix_inst.append(self.matrix_inst)
        self.matrix_inst.read_coordinates(grid)
        self.results = self.matrix_inst.get_results()

    
    def read_routes(self, scheme):
        with open(scheme) as inputfile:
            file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in file:
                self.scheme.append(row)

        
