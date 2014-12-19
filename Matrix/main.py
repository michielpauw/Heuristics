from GridMatrix import GridMatrix
from route_new import Route
import csv
import sys
import random
from route_3 import route_3

def main():
    do_route_3 = False
    do_new_route = True
    
    
    # the code for running the Removing Intersections algorithm
    if do_route_3:
        route = route_3(18, 17, 'grid_2.txt')
        route.read_routes('g_scheme_3_grid_2.txt')
        route.setup_route()
    
    # the code for running the Avoiding Intersections algorithm,
    # also implementing part of the Hill Climber algorithm
    if do_new_route:
        new_route = Route(18, 17, 'grid_2.txt')
        # create a list of all the gates that should be connected
        new_route.read_routes('g_scheme_3_grid_2.txt')
        new_route.set_order()
        ready = new_route.create_routes()
        i = 0
        no_improvement = 0
        what_went_wrong = []
        # continue trying to create as many routes possible
        while not ready:
            i += 1
            new_route.clear_everything()
            new_route.set_order()
            ready = new_route.create_routes()
            what_went_wrong.append(new_route.route_number + 1)
            print what_went_wrong
            print new_route.random_order
            print new_route.most_routes_drawn
            if new_route.most_routes_drawn > new_route.routes_drawn:
                no_improvement += 1
            else:
                no_improvement = 0
            if no_improvement > 70:
                new_route.random_order = []
                new_route.most_routes_drawn = 0
        
        # if all routes are drawn: print the routes and also a matrix
        # which, if everything is alright, shows that there are no 
        # intersections
        new_route.draw_matrix()
        print new_route.lines
        print new_route.random_order
        print "youpie"
        print new_route.list_steps
        print len(new_route.list_steps)
        print new_route.attempt_serious
        new_route.cross_matrix()
        
if __name__ == "__main__":
    main()
