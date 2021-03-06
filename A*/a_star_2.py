try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class a_star():

    def __init__(self, matrix):
        self.matrix = matrix
        self.layers = [matrix]
        self.score_list = []
        self.dim_x = len(self.matrix[0])
        self.dim_y = len(self.matrix)



    def new_line(self, start, goal):
        # nodes evaluated a dictionary with every node represented by their label and shortest route towards it
        closedset =  {start : [start]}
        
        # cost from start along best known path.
        steps = 0

        first = node(start, 0, goal, steps, self.dim_x, self.dim_y, self.layers)
        # list of potential nodes weighed by their score (sorted list)
        #openset = [(first.node_score, first)]


        openset = Q.PriorityQueue()
        openset.put((first.node_score, first))
        while not openset.empty():
        # run routes untill all the routes have been created
        #while openset != []:
            # get the length of the set for the search later on
            #length_openset = len(openset)

            # get all the attributes of the first node of the sorted list
            #current = openset[0]
            current = openset.get()
            current = current[1]
            # remove the node from the openset
            #openset.pop(0)

            path = list(closedset[current.label])

            # if the current node is the same as the goal
            if current.node == goal:
                # get the path from the closed set
                path = closedset[current.label]
                return path

            # you make a step so update the score by 1
            amount_of_steps = current.steps + 1

            #print current.label, path 
            for i in range(openset.qsize()):
                print openset[i]
            # go over the accompaniying nodes
            for i in current.sides:

                # store their attributes
                i = node(i[0], i[1], goal, amount_of_steps, self.dim_x, self.dim_y, self.layers)
                temp_path = list(path)
                temp_path.append(i.label)         

                # if the neighbor is already valued skip it
                if i.label in closedset:
                    continue
                # otherwise put it in the closedset
                else:
                    closedset[i.label] = temp_path
                    openset.put((i.score, i))
                
                # put it somewhere in the openset
                # if openset == []:
                #     openset.append(i)
                # else:
                #     index = self.binary_search(openset, i.node_score, i.steps)
                #     # index = self.liniar_search(openset, i.node_score)
                #     openset.insert(index, i)

        # if for some reason it steps out of the loop without returning a path alert
        return False


    def binary_search(self, array, key, steps):
        high = len(array) - 1
        mid = (high / 2)
        if mid <= 0:
            return 0

        if array[mid].node_score > key:
            return self.binary_search(array[:mid - 1], key, steps)
        elif array[mid].node_score < key:
            return self.binary_search(array[mid + 1:], key, steps)
        else:
            while array[mid].steps > steps and array[mid].node_score == key:
                mid -= 1
                if mid == 0:
                    break
            while array[mid].steps < steps and array[mid].node_score == key:
                mid += 1
                if mid == high:
                    break

            return mid



    def liniar_search(self, array, key):
        length_array = len(array)
        for i in range(length_array):
            if array[i].node_score > key:
                return i
            if i == length_array - 1:
                return i + 1

class node():
        
    def __init__(self, target, z, goal, steps, dim_x_m, dim_y_m, layers):
        self.dim_x_m = dim_x_m
        self.dim_y_m = dim_y_m
        self.goal_x = self.calc_x(goal)
        self.goal_y = self.calc_y(goal)
        self.goal_z = 0
        self.node = target
        self.steps = steps
        self.node_x = self.calc_x(self.node)
        if self.node_x > self.dim_x_m - 1:
            raise "this is not good"
        self.node_y = self.calc_y(self.node)
        if self.node_y > self.dim_y_m -1:
            raise "a little bit better"
        self.node_layer = z 
        self.label = self.node_layer * 1000 + self.node
        self.layers = layers
        self.node_score = self.score(steps)
        self.sides = self.neighbors()

    def calc_x(self, node):
        return node % (self.dim_x_m - 1)

    def calc_y(self, node):
        return int(node / (self.dim_x_m - 1))

    def calc_node(self, x, y):
        return x + y * self.dim_x_m

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
            # side_nodes.append("")
            side_nodes.append(left_node)
            # side_nodes.append("")
            side_nodes.append(below_node)
        elif place == 2: 
            #side_nodes.append("")
            side_nodes.append(left_node)
            side_nodes.append(above_node)
            #side_nodes.append("")
        elif place == 3:
            #side_nodes.append("")
            side_nodes.append(left_node)
            side_nodes.append(above_node)
            side_nodes.append(below_node)
        elif place == 4:
            side_nodes.append(right_node)
            #side_nodes.append("")
            #side_nodes.append("")
            side_nodes.append(below_node)
        elif place == 5:
            side_nodes.append(right_node)
            #side_nodes.append("")
            side_nodes.append(above_node)
            #side_nodes.append("")
        elif place == 6:
            side_nodes.append(right_node)
            #side_nodes.append("")
            side_nodes.append(above_node)
            side_nodes.append(below_node)
        elif place == 7:
            side_nodes.append(right_node)
            side_nodes.append(left_node)
            #side_nodes.append("")
            side_nodes.append(below_node)
        elif place == 8:
            side_nodes.append(right_node)
            side_nodes.append(left_node)
            side_nodes.append(above_node)
            #side_nodes.append("")
        else:
            print "JOEEEEEEEE"

        if self.node_layer <= 0:
            #side_nodes.append("") 
            side_nodes.append(layer_down_node)
        elif self.node_layer >= 7:
            side_nodes.append(layer_up_node)
            #side_nodes.append("")
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

    def score(self, current_score):
        score = current_score + self.mh_dis()
        if self.node_layer > (len(self.layers) - 1):
            self.layers.append(self.layers[0])

        if self.layers[self.node_layer][self.node_y][self.node_x] != 0:
            score = 100000
        return score

    def mh_dis(self):
        xdis = abs(self.goal_x - self.node_x)
        ydis = abs(self.goal_y - self.node_y)
        zdis = abs(self.goal_z - self.node_layer)
        return (xdis + ydis + zdis)
