class route:

    x_0 = 0
    y_0 = 0
    x_1 = 0
    y_1 = 0
    x_dist = 0
    y_dist = 0
    route_x = []
    route_y = []
    matrix = []
    
    def __init__(self, x_0, y_0, x_1, y_1):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_dist = abs(x_1 - x_0)
        self.y_dist = abs(y_1 -y_0)

    def import_matrix(matrix):
        self.matrix = matrix

    def createRoute():
        if x_0 <= x_1:
            for i in range x_dist:
                route_x.append(x_0)
                x_0++
        else:
            for i in range x_dist:
                route_x.append(x_0)
                x_0++
        
            
