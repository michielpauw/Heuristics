import GridMatrix
from route import Route
import csv
import sys

def main():
    matrix = GridMatrix.GridMatrix(18, 12)
    new_route = Route(18, 12)
    matrix.create_empty()
    
    results = []
    with open('grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            results.append(row)
    for result in results:
        matrix.create_gate(int(result[0]), int(result[1]), int(result[2]))

    scheme = []
    with open('scheme_1_grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            scheme.append(row)

    route_list_x = []
    route_list_y = []
    matrix_val = matrix.get_matrix()
    
    new_route.import_matrix(matrix_val)
    for route in scheme:
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
    for i in range(len(route_list_x)):
        matrix.create_route(route_list_x[i], route_list_y[i], i)

    for column in matrix_val:
        for row in column:
            sys.stdout.write("%03d " % (row))
            sys.stdout.write(" ")
            sys.stdout.flush()
        print
            
##    print("\n".join(str(row) for row in matrix_val))
        
if __name__ == "__main__":
    main()
