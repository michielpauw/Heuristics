from graph_matrix import GraphMatrix
import sys

class Layering:

    route_list_x = []
    route_list_y = []
    route_list_depth = []
    graph_matrix = GraphMatrix(0)
    graph_matrix_val = []
    crossing_amount_list = []
    sorted_by_second = []
    amount_lines = 0
    amount_on_layer = []
    sorted_per_layer = []
    deepest_layer = 0
    
    
    def __init__(self, route_list_x, route_list_y, route_list_depth):
        self.route_list_x = route_list_x
        self.route_list_y = route_list_y
        self.route_list_depth = route_list_depth
        self.sorted_per_layer = []
        self.amount_on_layer = []
        # create a matrix representing a graph of all the routes in the scheme
        self.graph_matrix = GraphMatrix(len(route_list_x))
        self.graph_matrix_val = self.graph_matrix.get_matrix()

    def get_matrix(self):
        return self.graph_matrix.get_matrix()

    def cross_matrix(self):
        self.graph_matrix_val = self.graph_matrix.get_matrix()
        crosses = False
        # detect a crossing of two routes (not perfectly efficient, but it works
        # rather nicely)
        for i in range(len(self.route_list_x)):
            crossing_amount = 0
            route_x_check_1 = self.route_list_x[i]
            route_y_check_1 = self.route_list_y[i]
            route_depth_check_1 = self.route_list_depth[i]
            for j in range(len(self.route_list_x)):
                if (j != i):
                    crosses = False
                    route_x_check_2 = self.route_list_x[j]
                    route_y_check_2 = self.route_list_y[j]
                    route_depth_check_2 = self.route_list_depth[j]
                    for k in range(len(route_x_check_1)):
                        if (crosses):
                            break
                        x = route_x_check_1[k]
                        y = route_y_check_1[k]
                        depth = route_depth_check_1[k]
                        for l in range(len(route_x_check_2)):
                            if (route_x_check_2[l] == x and route_y_check_2[l] == y and
                                            route_depth_check_2[l] == depth):
                                self.graph_matrix.insert_node(i, j)
                                crosses = True
                                crossing_amount += 1
                                break
            self.crossing_amount_list.append([i, crossing_amount])

        self.graph_matrix_val = self.graph_matrix.get_matrix()
        self.sorted_by_second =  sorted(self.crossing_amount_list, key=lambda tup: tup[1])

        return self.graph_matrix_val 

    # a method to move an entire route to a deeper level
    def move_deep(self):
        most_crosses = len(self.sorted_by_second)
        move_arr = self.sorted_by_second[most_crosses - 1]
        most_crosses_int = move_arr[1]
        if (most_crosses_int > 0):
            move_route = move_arr[0]
            route = self.route_list_depth[move_route]
            self.route_list_depth.pop(move_route)
            for i in range(len(route)):
                value = route[i]
                route.pop(i)
                route.insert(i, value + 1)
            self.route_list_depth.insert(move_route, route)
            self.crossing_amount_list = []
            self.cross_matrix()
            self.move_deep()

        else:
            self.deepest_layer = 0
            for depths in self.route_list_depth:
                depth = depths[0]
                if (depth > self.deepest_layer):
                    self.deepest_layer = depth

            for i in range(self.deepest_layer + 1):
                self.amount_on_layer.append(0)
            
            for depths in self.route_list_depth:
                depth = depths[0]
                self.amount_on_layer[depth] += 1
                
            self.sorted_per_layer = sorted(self.amount_on_layer)
            self.sorted_per_layer.reverse()
            self.graph_matrix = GraphMatrix(len(self.route_list_x))
            self.graph_matrix_val = self.graph_matrix.get_matrix()
            self.cross_matrix()
            
    def count_lines(self):
        self.amount_lines = 0
        layer_penalty = 0
        lines_2D = 0
##        print "class method"
##        print self.sorted_per_layer
        for route_depth in self.route_list_depth:
            lines_2D += len(route_depth)
        for i in range(len(self.sorted_per_layer)):
            layer_penalty += self.sorted_per_layer[i] * i * 2

##        print layer_penalty
##        print lines_2D
        self.amount_lines = layer_penalty + lines_2D

        return self.amount_lines



        
