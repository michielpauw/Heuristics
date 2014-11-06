class GridMatrix:

    list_hor = []
    list_ver = []
    hor = 0
    vert = 0
    
    def __init__(self, a, b):
        self.hor = a
        self.vert = b

    def get_matrix(self):
        return self.list_ver

    # create a matrix with the right dimensions filled with only zeroes
    def create_empty(self):
        for i in range(self.vert):
            self.list_hor = []
            for j in range(self.hor):
                self.list_hor.append(0)
            self.list_ver.append(self.list_hor)

    # place a gate having the negative gate number (1-indexed) as its value
    def create_gate(self, a, b, value):
        list_temp = self.list_ver[b]
        self.list_ver.pop(b)
        list_temp.pop(a)
        list_temp.insert(a, -value)
        self.list_ver.insert(b, list_temp)

    # create a route in the matrix, overwriting previously established routes
    # for now
    def create_route(self, route_x, route_y, value):
        if (len(route_x) != len(route_y)):
            return False
        
        length = len(route_y)
        for i in range(length):
            b = route_y[i]
            a = route_x[i]
            list_temp = self.list_ver[b]
            self.list_ver.pop(b)
            list_temp.pop(a)
            list_temp.insert(a, value + 1)
            self.list_ver.insert(b, list_temp)
        
            
