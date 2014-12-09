from GridMatrix import GridMatrix 
from a_star import a_star, node

def main():

	# matrix1 = GridMatrix(18, 13)
	# matrix2 = GridMatrix(18, 13)
	# matrix1.read_coordinates('grid_1.txt')
	# matrix = a_star(matrix1.list_ver, matrix2.list_ver)
	matrix = a_star(18,13)
	a = matrix.new_line(90, 107, 11)
	b = matrix.new_line(9, 225, 22)
	print matrix.layers
	print a, b
	
if __name__ == "__main__":
    main()	