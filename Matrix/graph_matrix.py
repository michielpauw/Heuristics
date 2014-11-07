class GraphMatrix:

    list_1 = []
    list_2 = []
    size = 0
    
    def __init__(self, size):
        self.size = size
        self.create_empty()

    def get_matrix(self):
        return self.list_2
    
    # create a matrix with the right dimensions filled with only zeroes
    def create_empty(self):
        for i in range(self.size):
            self.list_1 = []
            for j in range(self.size):
                self.list_1.append(-1)
            self.list_2.append(self.list_1)

    def insert_node(self, a, b):
        if (a != b):           
            list_temp = self.list_2[b]
            self.list_2.pop(b)
            list_temp.pop(a)
            list_temp.insert(a, a)
            self.list_2.insert(b, list_temp)
