from GridMatrix import GridMatrix 
from a_star import a_star, node
import sys

def main():
	route = GridMatrix(18,17)
	matrix = a_star(18,17, "grid_2.txt")
	
	routes = route.read_routes("g_scheme_3_grid_2.txt")
	routes_lijstje = []
	Total_routes = 0
	for i in range(len(routes)):
		i = matrix.new_line(routes[i][0],routes[i][1], i+1)
		routes_lijstje.append(i)
		# print i
		Total_routes += len(i)


	counter = 0
	crosses = 0
	# check for empty last layer
	length_l = len(matrix.layers)
	empty = 0
	for i in matrix.layers[length_l - 1]:
		for j in i:
			if j != 0:
				empty += 1

	if empty == 0:
		matrix.layers.pop(length_l - 1)




	for column in matrix.layers:
		counter += 1 
		# print column
		for row in column:
			print
			if isinstance(row, int):
				sys.stdout.write("%03d " % (row))
				sys.stdout.write(" ")
				sys.stdout.flush()
			else:
				row = str(row)
				sys.stdout.write(row)
		print
	for i in range(len(routes_lijstje)):
		for j in range(i+1,len(routes_lijstje)):
			if i == j:
				continue

			for k in range(len(routes_lijstje[i])):
				if k == 0:
					continue
				elif k == (len(routes_lijstje[i]) - 1):
					continue

				for l in range(len(routes_lijstje[j])):
					if l == 0:
						continue
					elif l == (len(routes_lijstje[j]) - 1):
						continue

					if routes_lijstje[i][k] == routes_lijstje[j][l]:
						crosses += 1
						# print "route:", i, "node:", routes_lijstje[i][k], "with:", j, "node:",routes_lijstje[j][l]

	print counter, crosses, Total_routes
	# print a, b
	
if __name__ == "__main__":
    main()	