import GridMatrix
from route import Route
from graph_matrix import GraphMatrix
from clique_finder import CliqueFinder
import csv
import sys
import random

def main():
    # create an instance of the gridmatrix and new_route class
    matrix = GridMatrix.GridMatrix(18, 12)
    new_route = Route(18, 12)
    matrix.create_empty()
    clique_finder = CliqueFinder(0)

    matrix.read_coordinates('grid_1.txt')
    results = matrix.get_results()

    # create a list of all the gates that should be connected
    scheme = []
    with open('scheme_1_grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            scheme.append(row)

    # create a matrix representing a graph of all the routes in the scheme
    graph_matrix = GraphMatrix(len(scheme))
    graph_matrix_val = graph_matrix.get_matrix()
    
    
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
        route_append = new_route.createRoute(int(x_0), int(x_1),
                                             int(y_0), int(y_1), route)
        if (route_append):
            route_list_x.append(new_route.route_x)
            route_list_y.append(new_route.route_y)
        else:
            route_list.append("schijt")
            return False

    crossing_amount_list = []
    
    crosses = False
    # detect a crossing of two routes (not perfectly efficient, but it works
    # rather nicely)
    for i in range(len(route_list_x)):
        crossing_amount = 0
        route_x_check_1 = route_list_x[i]
        route_y_check_1 = route_list_y[i]
        for j in range(len(route_list_x)):
            if (j != i):
                crosses = False
                route_x_check_2 = route_list_x[j]
                route_y_check_2 = route_list_y[j]
                for k in range(len(route_x_check_1)):
                    if (crosses):
                        break
                    x = route_x_check_1[k]
                    y = route_y_check_1[k]
                    for l in range(len(route_x_check_2)):
                        if (route_x_check_2[l] == x and route_y_check_2[l] == y):
                            graph_matrix.insert_node(i, j)
                            crosses = True
                            crossing_amount += 1
                            break
        crossing_amount_list.append([i, crossing_amount])

    graph_matrix_val = graph_matrix.get_matrix()

    max_clique = 0

##    max_clique = clique_finder.clique_size(graph_matrix_val, 0)

    print max_clique
    sorted_by_second = sorted(crossing_amount_list, key=lambda tup: tup[1])
    
    for column in graph_matrix_val:
        for row in column:
            sys.stdout.write("%02d " % (row))
            sys.stdout.write(" ")
            sys.stdout.flush()
        print

    print sorted_by_second
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
