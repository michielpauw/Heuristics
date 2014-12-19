class CliqueFinder:

    # max_clique = 0
    # collection = []
    # value = 0
    #
    # def __init__(self, max_clique):
    #     self.max_clique = max_clique
    #
    # def clique_size(self, collection, value):
    #     print value
    #     self.collection = collection
    #     if (len(self.collection) == 0):
    #         if (value > self.max_clique):
    #             self.max_clique = value
    #     i = 0
    #     while (len(self.collection) > 0):
    #         print i
    #         collection_new = []
    #         node = self.collection[0]
    #         print len(self.collection)
    #         # realize collection_new is only a few entries long. It doesn't know which nodes it contains.
    #         # They're only relevant if they also appear in each others list, so keep track of that. Only keep
    #         # the nodes in collection_new that are in the original list 0
    #         for connected in range(i, len(node)):
    #             if (node[connected] != -1):
    #                 collection_new.append(self.collection[connected])
    #
    #         i += 1
    #         self.collection.pop(0)
    #         print len(collection_new)
    #         print self.collection
    #         self.clique_size(collection_new, value + 1)
    #
    #     return value

    clique_list = []
    matrix = []
    matrix_current = []
    current_clique = []
    current_node = 0
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_current = matrix
        
    def clique_finder_1(self):
        # for all lines, check which lines they cross
        while (len(self.matrix) > 0):
            list_crossed = []
            # keep track of the size of the clique the current line is in (always 1)
            clique_size = 1
            to_check = self.matrix[0]
            self.matrix.pop(0)
            current_node += 1
            for row in self.matrix:
                row.pop(0)
            # get a list of the lines that cross this line
            for check in to_check:
                if check > -1:
                    list_crossed.append(check)
            # for all these lines, check which lines they cross
            clique_finder_2(list_crossed)
                
    def clique_finder_2(self, list_to_check_num):
        list_to_check = self.matrix(list_to_check_num - self.current_node)
        