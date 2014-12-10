from GridMatrix import GridMatrix 
from a_star import a_star, node
import sys

def main():
	route = GridMatrix(18,13)
	matrix = a_star(18,13)
	# a = matrix.new_line(90, 107, 11)
	# b = matrix.new_line(9, 225, 22)
	
	routes = route.read_routes("scheme_1_grid_1.txt")
	routes_lijstje = []
	Total_routes = 0
	for i in range(len(routes)):
		i = matrix.new_line(routes[i][0],routes[i][1], i+1)
		routes_lijstje.append(i)
		# print i
		Total_routes += len(i)


	counter = 0
	crosses = 0
	a = matrix.layers
	for column in a:
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
						print "route:", i, "node:", routes_lijstje[i][k], "with:", j, "node:",routes_lijstje[j][l]

	print counter, crosses, Total_routes
	# print a, b
	
if __name__ == "__main__":
    main()	