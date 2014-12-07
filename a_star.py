
class a_star(self, x, y, z):

    def __init__(self, matrix):
        self.matrix = matrix

    def nodes(matrix):
        nodes append : node + 1, node - 1 (if < 0 niet toevoegen), 

    def new_line(start, goal):
        # nodes evaluated a dictionary with every node represented by their number and shortest route towards it
        closedset =  dict()
        
        # list of potential nodes weighed by their score (sorted list)
        openset =  []

        # the map of navigated nodes
        came_from = previous node   
        
        # cost from start along best known path.
        g_score[start] = 0

        # estimated total cost from start to goal through y.
        f_score[start] := g_score[start] + heuristic_cost_estimate(start, goal)
     
        # run routes untill all the routes have been created
        while openset is not empty
            current = openset[0]
            if current = goal
                return reconstruct_path(came_from, goal)
                remove current from openset
                add current to closedset
            
            for each neighbor in neighbor_nodes(current)
                if neighbor in closedset
                    continue
                tentative_g_score = g_score[current] + dist_between(current,neighbor)
     
                if neighbor not in openset or tentative_g_score < g_score[neighbor] 
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
                    if neighbor not in openset
                        add neighbor to openset
     
        return failure
     
        def reconstruct_path(came_from, current):
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path.append(current)
            return total_path

    class nodes:
        def __init__(self, target):
            self.node = target
            self.score = 0
            self.neighbors = neighbors(node)

        def neighbors(node, matrix, x, y, z):
            neigbors = []
            total_per_layer = x * y
            if node < 1:
                neigbors.append(1, x + 1, x * y + 1)
            if node > x * y 

            return neighbors

        def score(self, current_score):
            self.score = current_score + mh_dis

