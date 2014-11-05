import GridMatrix
import route
import csv

def main():
    matrix = GridMatrix.GridMatrix(18, 12)
    matrix.create_empty()
    
    results = []
    with open('grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            results.append(row)
    for result in results:
        matrix.create_gate(int(result[0]), int(result[1]), int(result[2]))

    scheme = []
    with open('scheme_1_grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            scheme.append(row)

    matrix_val = matrix.get_matrix()
    new_route.import_matrix(matrix_val)
    route_list = new_route.createRoute()
    print("\n".join(str(row) for row in matrix_val))
        
if __name__ == "__main__":
    main()
