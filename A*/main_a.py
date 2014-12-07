from GridMatrix import GridMatrix 
from a_star import a_star, node

def main():

	matrix = GridMatrix(18, 13)
	matrix = a_star(matrix.list_ver)
	print matrix.new_line(0,13)
	# startnode = node(0, 1, 13, 0 , 18, 13, matrix.layers)

if __name__ == "__main__":
    main()