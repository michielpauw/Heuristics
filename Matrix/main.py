import GridMatrix
import csv

def main():
    matrix = GridMatrix.GridMatrix(18, 12)
    matrix.create_empty()

 
    matrix.create_gate(2, 4)
    
    results = []
    with open('grid_1.txt') as inputfile:
        file = csv.reader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in file:
            results.append(row)
    for result in results:
        matrix.create_gate(int(result[0]), int(result[1]))

    
    print("\n".join(str(row) for row in matrix.list_ver))
    
if __name__ == "__main__":
    main()
