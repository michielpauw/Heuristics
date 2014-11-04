class GridMatrix:

    list_hor = []
    list_ver = []
    hor = 0
    vert = 0
    
    def __init__(self, a, b):
        self.hor = a
        self.vert = b
    
    def create_empty(self):
        for i in range(self.vert):
            self.list_hor = []
            for j in range(self.hor):
                self.list_hor.append(0)
            self.list_ver.append(self.list_hor)

    def create_gate(self, a, b):
        list_temp = self.list_ver[b]
        self.list_ver.pop(b)
        list_temp.pop(a)
        list_temp.insert(a, -1)
        self.list_ver.insert(b, list_temp)
