from GridMatrix import GridMatrix
from line_matrix import LineMatrix
# from route import Route
from route_new import Route
from graph_matrix import GraphMatrix
from layering import Layering
from clique_finder import CliqueFinder
import csv
import sys
import random

def main():
    # create an instance of the gridmatrix and new_route class
    
##    clique_finder = CliqueFinder(0)

    # load the chips in the matrix
    # matrix = GridMatrix(18, 13)
    # line_matrix = LineMatrix(18, 13)
    # line_matrix.read_coordinates('grid_1.txt')
    # matrix.read_coordinates('grid_1.txt')
    # results = matrix.get_results()
    
    # line_matrix_val = line_matrix.get_matrix()
    # for column in line_matrix_val:
    #     for row in column:
    #         if isinstance(row, int):
    #             sys.stdout.write("%03d " % (row))
    #             sys.stdout.write(" ")
    #             sys.stdout.flush()
    #         else:
    #             sys.stdout.write(row)
    #     print

    new_route = Route(18, 13, 'grid_1.txt')
    # create a list of all the gates that should be connected
    new_route.read_routes('scheme_test.txt')
    ready = new_route.create_routes()
    if not ready:
        print "CRAP"
    print "youpie"
    print new_route.list_steps
    print len(new_route.list_steps)
    print new_route.attempt_serious
    new_route.cross_matrix()
    
##    max_clique = 0

##    max_clique = clique_finder.clique_size(graph_matrix_val, 0)

##    print max_clique
    
    
##    graph_matrix_def = layering.get_matrix()

##    print route_list_x
##    print route_list_y
##    print route_list_depth
    
##    print graph_matrix_def
    
##    for column in graph_matrix_def:
##        for row in column:
##            sys.stdout.write("%02d " % (row))
##            sys.stdout.write(" ")
##            sys.stdout.flush()
##        print

##    print len(graph_matrix_val)

    # place the routes in the matrix, overwriting after a crossing
    

##    matrix_val = matrix.get_matrix()
##    # print the matrix as strings, so it's easy to read
##    for column in matrix_val:
##        for row in column:
##            sys.stdout.write("%03d " % (row))
##            sys.stdout.write(" ")
##            sys.stdout.flush()
##        print
##    count_lines = 0
##    count_lines_one = 0
##    count_lines_two = 0
##    count_lines_three = 0
##    count_lines_four = 0
##    route_list_x_best = []
##    route_list_y_best = []
##    route_list_depth_best = []
    # for i in range(1):
    #     # and connect them in a quite random order (still resulting in an infinite
    #     # loop, working on that)
    #     new_route.start_routes()
    #     new_route.draw_matrices()
    #     layering = Layering(new_route.route_list_x, new_route.route_list_y, new_route.route_list_depth)
    #
    #     layering.cross_matrix()
    #     graph_matrix_def = layering.get_matrix()
    #     for column in graph_matrix_def:
    #         for row in column:
    #             sys.stdout.write("%02d " % (row))
    #             sys.stdout.write(" ")
    #             sys.stdout.flush()
    #         print
    # variables for checking
    # begrijp niet waarom we zoveel counts hebben, die we ook niet allemaal gebruiken?
##    count_lines = 0
##    count_lines_one = 0
##    count_lines_two = 0
##    count_lines_three = 0
##    count_lines_four = 0
##    route_list_x_best = []
##    route_list_y_best = []
##    route_list_depth_best = []
##    for i in range(1):
##        new_route.start_routes(scheme, matrix, results)
##        route_list_x = new_route.route_list_x
##        route_list_y = new_route.route_list_y
##        route_list_depth = new_route.route_list_depth
##        layering = Layering(route_list_x, route_list_y, route_list_depth)
##        
##        layering.cross_matrix()
##        graph_matrix_def = layering.get_matrix()
##        for column in graph_matrix_def:
##            for row in column:
##                sys.stdout.write("%02d " % (row))
##                sys.stdout.write(" ")
##                sys.stdout.flush()
##            print
##        layering.move_deep()
##        print route_list_depth[0]
##        print new_route.matrix
##        print route_list_x
##        print route_list_y
##        for i in range(len(route_list_x)):
##            matrix.create_route(route_list_x[i], route_list_y[i], route_list_depth[i], i)
##        amount_lines = layering.count_lines()
##        if (amount_lines < count_lines_one or i == 0):
##            count_lines_one = amount_lines
##        if (amount_lines < count_lines or i == 0):
##            count_lines = amount_lines
##            route_list_x_best = route_list_x
##            route_list_y_best = route_list_y
##            route_list_depth_best = route_list_depth
##    print count_lines_one
##        layering.move_deep()
##        print route_list_depth[0]
##        print matrix.get_matrix()
##        print len(route_list_x)
##        print len(route_list_y)
##
##        # print the lines in the matrix
##        for i in range(len(route_list_x)):
##            matrix.create_route(route_list_x[i], route_list_y[i], route_list_depth[i], i)
##        print matrix.get_matrix()
##        amount_lines = layering.count_lines()
##
##        # lijkt mij twee maal hetzelfde?
##        if (amount_lines < count_lines_one or i == 0):
##            count_lines_one = amount_lines
##        if (amount_lines < count_lines or i == 0):
##            count_lines = amount_lines
##            route_list_x_best = route_list_x
##            route_list_y_best = route_list_y
##            route_list_depth_best = route_list_depth
##    print count_lines_one
    
##    for i in range(10000):
##        # and connect them in a quite random order (still resulting in an infinite
##        # loop, working on that)
##        new_route.start_routes(scheme, matrix, results)
##        route_list_x = new_route.route_list_x
##        route_list_y = new_route.route_list_y
##        route_list_depth = new_route.route_list_depth
##        layering = Layering(route_list_x, route_list_y, route_list_depth)
##        layering.cross_matrix()
##        layering.move_deep()
##        amount_lines = layering.count_lines()
##        if (amount_lines < count_lines_two or i == 0):
##            count_lines_two = amount_lines
##        if (amount_lines < count_lines):
##            count_lines = amount_lines
##            route_list_x_best = route_list_x
##            route_list_y_best = route_list_y
##            route_list_depth_best = route_list_depth
##    print count_lines_two
##    
##    for i in range(10000):
##        # and connect them in a quite random order (still resulting in an infinite
##        # loop, working on that)
##        new_route.start_routes(scheme, matrix, results)
##        route_list_x = new_route.route_list_x
##        route_list_y = new_route.route_list_y
##        route_list_depth = new_route.route_list_depth
##        layering = Layering(route_list_x, route_list_y, route_list_depth)
##        layering.cross_matrix()
##        layering.move_deep()
##        amount_lines = layering.count_lines()
##        if (amount_lines < count_lines_three or i == 0):
##            count_lines_three = amount_lines
##        if (amount_lines < count_lines):
##            count_lines = amount_lines
##            route_list_x_best = route_list_x
##            route_list_y_best = route_list_y
##            route_list_depth_best = route_list_depth
##    print count_lines_three
##    
##    for i in range(10000):
##        # and connect them in a quite random order (still resulting in an infinite
##        # loop, working on that)
##        new_route.start_routes(scheme, matrix, results)
##        route_list_x = new_route.route_list_x
##        route_list_y = new_route.route_list_y
##        route_list_depth = new_route.route_list_depth
##        layering = Layering(route_list_x, route_list_y, route_list_depth)
##        layering.cross_matrix()
##        layering.move_deep()
##        amount_lines = layering.count_lines()
##        if (amount_lines < count_lines_four or i == 0):
##            count_lines_four = amount_lines
##        if (amount_lines < count_lines):
##            count_lines = amount_lines
##            route_list_x_best = route_list_x
##            route_list_y_best = route_list_y
##            route_list_depth_best = route_list_depth
##    print count_lines_four
    
            
##    print "main"
##    print count_lines
##    print "main"
##    print route_list_x_best
##    print "main"
##    print route_list_y_best
##    print "main"
##    print route_list_depth_best
##    print("\n".join(str(row) for row in matrix_val))
        
if __name__ == "__main__":
    main()
