try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from GridMatrix import GridMatrix

# class that, makes the routes and layers
class a_star():

    # initialize some variables like a grid and some layers with probes
    def __init__(self, x, y, grid):
        matrix_temp1 = GridMatrix(x, y)
        matrix_temp3 = GridMatrix(x, y)
        matrix_temp3.gate_lead(grid)
        self.matrix = list(matrix_temp1.list_ver)
        matrix_temp2 = GridMatrix(x, y)
        matrix_temp2.read_coordinates(grid)
        self.layers = [list(matrix_temp2.list_ver), list(matrix_temp3.list_ver), list(matrix_temp3.list_ver), list(matrix_temp3.list_ver), list(matrix_temp3.list_ver)]
        self.dim_x = x
        self.dim_y = y

    # function to delete a line
    def delete_line(self, path):
        for i in range(len(path)):
            if i == 0 or i == len(path) - 1:
                continue
            z = self.calc_z(path[i])
            x = self.calc_x(path[i], z)
            y = self.calc_y(path[i], z)
            list_temp = list(self.layers[z][y])

            # remove the line from the grid
            self.layers[z].pop(y)
            list_temp.pop(x)
            list_temp.insert(x, 0)
            self.layers[z].insert(y, list_temp)

    def new_line(self, start, goal, value):
        # nodes evaluated a dictionary with every node represented by their label and shortest route towards it
        closedset =  {start : [start]}
        
        # cost from start along best known path.
        steps = 0


        first = node(start, 0, goal, steps, self.dim_x, self.dim_y, self.layers, list(self.matrix))

        # list of potential nodes weighed by their score (sorted list)
        openset = Q.PriorityQueue()
        openset.put((first.node_score, first))

        while not openset.empty():

            current = openset.get()
            current = current[1]
            path = list(closedset[current.label])

            # you make a step so update the score by 1
            amount_of_steps = current.steps + 1
            
            # go over the accompaniying nodes
            for i in current.sides:

                # store their attributes
                i = node(i[0], i[1], goal, amount_of_steps, self.dim_x, self.dim_y, self.layers, list(self.matrix))
                temp_path = list(path)
                temp_path.append(i.label)         

                # if the neighbor is already valued skip it
                if i.label in closedset:
                    continue
                # otherwise put it in the closedset
                else:
                    closedset[i.label] = temp_path
                    openset.put((i.node_score, i))

                if i.label == goal:
                    # get the path from the closed set
                    path = temp_path
                    for i in path:
                        if i == start or i == goal:
                            continue
                        z = self.calc_z(i)
                        x = self.calc_x(i, z)
                        y = self.calc_y(i, z)
                        list_temp = list(self.layers[z][y])
                        self.layers[z].pop(y)
                        list_temp.pop(x)
                        list_temp.insert(x, value)
                        self.layers[z].insert(y, list_temp)
                    return path

        # if for some reason it steps out of the loop without returning a path alert
        return False

    # function to calculate the x coordinate of a node
    def calc_x(self, node, z):
        return (int(node - (z * 1000)) % self.dim_x)

    # function to calculate the y coordinate of a node
    def calc_y(self, node, z):
        return (int((node - (z * 1000)) / self.dim_x))

    # function to calculate the z coordinate of a node
    def calc_z(self,node):
        return int(node / 1000)

class node():
        
    def __init__(self, target, z, goal, steps, dim_x_m, dim_y_m, layers, matrix):
        self.dim_x_m = dim_x_m
        self.dim_y_m = dim_y_m
        self.goal_x = self.calc_x(goal)
        self.goal_y = self.calc_y(goal)
        self.goal_z = 0
        self.node = target
        self.steps = steps
        self.node_x = self.calc_x(self.node)

        # error checking
        if self.node_x > self.dim_x_m - 1:
            raise "this is not good"
        self.node_y = self.calc_y(self.node)
        if self.node_y > self.dim_y_m - 1:
            raise "a little bit better"
       
        self.node_layer = z 
        self.label = self.node_layer * 1000 + self.node
        self.matrix = list(matrix)
        self.layers = layers
        self.node_score = self.score(steps)
        self.sides = self.neighbors()

    # calculate x coordinate
    def calc_x(self, node):
        return (node % (self.dim_x_m))

    # calculate y coordinate
    def calc_y(self, node):
        return (int(node / (self.dim_x_m)))

    # calculate the node from it's coordinate
    def calc_node(self, x, y):
        return x + y * self.dim_x_m

    # define the neighbors of a node
    def neighbors(self):
        side_nodes = list()
        right_node = [self.calc_node(self.node_x + 1, self.node_y), self.node_layer]
        left_node = [self.calc_node(self.node_x - 1, self.node_y), self.node_layer]
        above_node = [self.calc_node(self.node_x, self.node_y - 1), self.node_layer]
        below_node = [self.calc_node(self.node_x, self.node_y + 1), self.node_layer]
        layer_up_node = [self.calc_node(self.node_x, self.node_y), self.node_layer - 1]
        layer_down_node = [self.calc_node(self.node_x, self.node_y), self.node_layer + 1]
        place = self.place_node()
        if place == 0:
            side_nodes.append(right_node)
            side_nodes.append(left_node)
            side_nodes.append(above_node)
            side_nodes.append(below_node)
        elif place == 1:
            side_nodes.append(left_node)
            side_nodes.append(below_node)
        elif place == 2: 
            side_nodes.append(left_node)
            side_nodes.append(above_node)
        elif place == 3:
            side_nodes.append(left_node)
            side_nodes.append(above_node)
            side_nodes.append(below_node)
        elif place == 4:
            side_nodes.append(right_node)
            side_nodes.append(below_node)
        elif place == 5:
            side_nodes.append(right_node)
            side_nodes.append(above_node)
        elif place == 6:
            side_nodes.append(right_node)
            side_nodes.append(above_node)
            side_nodes.append(below_node)
        elif place == 7:
            side_nodes.append(right_node)
            side_nodes.append(left_node)
            side_nodes.append(below_node)
        elif place == 8:
            side_nodes.append(right_node)
            side_nodes.append(left_node)
            side_nodes.append(above_node)
        else:
            # should not happen, thus an absurd error is printed
            print "JOEEEEEEEE"

        if self.node_layer <= 0:
            side_nodes.append(layer_down_node)
        elif self.node_layer >= 7:
            side_nodes.append(layer_up_node)
        else:
            side_nodes.append(layer_up_node)
            side_nodes.append(layer_down_node)
        

        return side_nodes


    def place_node(self):
        # right upper corner = 1, right lower corner = 2, right side = 3
        # left upper corner = 4, left lower corner = 5, left side = 6
        # upper side = 7, lower side = 8, not a side node = 0

        # check if on the right
        if self.node_x >= self.dim_x_m - 1:
            # check for upper side
            if self.node_y <= 0:
                return 1

            #check for lowerside
            elif self.node_y >= self.dim_y_m - 1:
                return 2
            else:
                return 3

        # check for left side
        elif self.node_x <= 0:
             # check for upper side
            if self.node_y <= 0:
                return 4

            #check for lowerside
            elif self.node_y >= self.dim_y_m - 1:
                return 5

            else: 
                return 6

        # check for upperside
        elif self.node_y <= 0:
            return 7

        # check for lowerside
        elif self.node_y >= self.dim_y_m - 1:
            return 8

        else:
            return 0

    # a function to calculate the score of a node
    def score(self, current_score):
        # add extra layers if needed (max 8)
        if self.node_layer > (len(self.layers) - 1):
            self.layers.append(list(self.matrix))
        
        # cross a route/wire if no other possibility
        if self.layers[self.node_layer][self.node_y][self.node_x] > 0 and self.layers[self.node_layer][self.node_y][self.node_x] < 100:
            score = 2000000

        # if near the goal, put it in fornt of the list
        elif self.node_y == self.goal_y and self.node_x == self.goal_x:
            score = 1
        elif self.node_layer == 0 and self.node_x == self.goal_x and (self.node_y == self.goal_y + 1 or self.node_y == self.goal_y - 1):
            score = 1
        elif self.node_layer == 0 and self.node_y == self.goal_y and (self.node_x == self.goal_x + 1 or self.node_x == self.goal_x - 1):
            score = 1

        # only cross a lead if no free space left
        elif self.layers[self.node_layer][self.node_y][self.node_x] == 100: 
            score = 1000000

        # do not cross gates
        elif self.layers[self.node_layer][self.node_y][self.node_x] < 0:
            score = 400000000

        # with this part you drive a node to layer 6
        elif self.node_layer > 6:
            score = int(current_score + self.mh_dis() -  12)
        elif self.node_layer > 0:
            score = int(current_score + self.mh_dis() -  (self.node_layer * 2))
        
        # the simpelest score
        else:
            score = current_score + self.mh_dis()

        return score

    # manhatten distiance funtion
    def mh_dis(self):
        xdis = abs(self.goal_x - self.node_x)
        ydis = abs(self.goal_y - self.node_y)
        zdis = abs(self.goal_z - self.node_layer)
        return (xdis + ydis + zdis)
