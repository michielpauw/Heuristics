import GridMatrix
from route import Route
import csv
import sys
import random

def main():
    # create an instance of the gridmatrix and new_route class
    matrix = GridMatrix.GridMatrix(18, 12)
    new_route = Route(18, 12)
    matrix.create_empty()

    # create a list of the coordinates of the logical gates
    results = []
    with open('grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            results.append(row)
    # and place them in the empty matrix
    for result in results:
        matrix.create_gate(int(result[0]), int(result[1]), int(result[2]))

    # create a list of all the gates that should be connected
    scheme = []
    with open('scheme_1_grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            scheme.append(row)

    # and connect them in a quite random order (still resulting in an infinite
    # loop, working on that)
    random_order = random.sample(range(len(scheme)), len(scheme))
    route_list_x = []
    route_list_y = []
    matrix_val = matrix.get_matrix()
    
    new_route.import_matrix(matrix_val)
    for i in range(len(scheme)):
        route_number = random_order[i]
        route = scheme[route_number]
        start_number = route[0]
        finish_number = route[1]
        start_coordinates = results[int(start_number)]
        finish_coordinates = results[int(finish_number)]
        x_0 = start_coordinates[0]
        y_0 = start_coordinates[1]
        x_1 = finish_coordinates[0]
        y_1 = finish_coordinates[1]
        route_append = new_route.createRoute(int(x_0), int(x_1), int(y_0), int(y_1), route)
        if (route_append):
            route_list_x.append(new_route.route_x)
            route_list_y.append(new_route.route_y)
        else:
            route_list.append("schijt")

    # place the routes in the matrix, overwriting after a crossing
    for i in range(len(route_list_x)):
        matrix.create_route(route_list_x[i], route_list_y[i], i)

    # print the matrix as strings, so it's easy to read
    for column in matrix_val:
        for row in column:
            sys.stdout.write("%03d " % (row))
            sys.stdout.write(" ")
            sys.stdout.flush()
        print
            
##    print("\n".join(str(row) for row in matrix_val))
        
if __name__ == "__main__":
    main()
