class node():
        
    def __init__(self, target, z, goal, g_score, dim_x_m, dim_y_m, layers):
        self.dim_x_m = dim_x_m
        self.dim_y_m = dim_y_m
        self.goal_x = self.calc_x(goal)
        self.goal_y = self.calc_y(goal)
        self.goal_z = 0
        self.node = target
        self.node_x = self.calc_x(self.node)
        if self.node_x > self.dim_x_m - 1:
            return False
        self.node_y = self.calc_y(self.node)
        if self.node_y > self.dim_y_m -1:
            return False
        self.node_layer = z - 1 
        self.label = self.node_layer * 1000 + self.node
        self.layers = layers
        self.node_score = self.score(g_score)
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
        if self.layers[self.node_layer][self.node_y][self.node_x] != 0:
            score = 100000
        return score

    def mh_dis(self):
        xdis = abs(self.goal_x - self.node_x)
        ydis = abs(self.goal_y - self.node_y)
        zdis = abs(self.goal_z - self.node_layer)
        return (xdis + ydis)