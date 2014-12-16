from GridMatrix import GridMatrix 
from a_star import a_star, node
import sys
from random import randrange 
from Crosses import count_for_crosses, look_for_crosses

def main():
	x = 18
	y = 17
	route = GridMatrix(x, y)
	matrix = a_star(x, y, "grid_2.txt")
	routes = route.read_routes("g_scheme_3_grid_2.txt")
	routes_lijstje = []
	Total_routes = 0
	for i in range(len(routes)):
		i = matrix.new_line(routes[i][0],routes[i][1], i+1)
		routes_lijstje.append(i)
		Total_routes += len(i)

	loops = 0
	crosses = look_for_crosses(routes_lijstje)
	best_cross = count_for_crosses(routes_lijstje)
	best_lines = routes_lijstje
	best_layers = matrix.layers
	print count_for_crosses(routes_lijstje)
	while crosses != [] :
		routes_lijstje = best_lines
		matrix.layers = best_layers
		loops += 1
		# print crosses , loop
		if (loops%10) == 0:
			if crosses == []:
				break
			rand = randrange(len(routes_lijstje) - 1)
			rand2 = randrange(len(routes_lijstje) - 1)
			rand3 = randrange(len(routes_lijstje) - 1)
			rand4 = randrange(len(routes_lijstje) - 1)

			cross_length = randrange(len(crosses))

			if rand == rand2:
				rand2 += 1
				rand2 = rand2%(len(routes_lijstje) - 1)
			if rand3 == rand:
				rand3 += 2
				rand3 = rand3%(len(routes_lijstje) - 1)
			elif rand3 == rand2:
				rand3 += 1
				rand3 = rand3%(len(routes_lijstje) - 1)

			if rand4 == rand:
				rand4 -= 1
				rand4 = rand4%(len(routes_lijstje) - 1)
			elif rand4 == rand2:
				rand3 += 2
				rand3 = rand4%(len(routes_lijstje) - 1)
			elif rand4 == rand3:
				rand4 += 1
				rand4 = rand4%(len(routes_lijstje) - 1)


			matrix.delete_line(routes_lijstje[rand])
			matrix.delete_line(routes_lijstje[rand2])
			matrix.delete_line(routes_lijstje[rand3])
			matrix.delete_line(routes_lijstje[rand4])
			matrix.delete_line(routes_lijstje[crosses[cross_length][0]])
			newline = matrix.new_line(routes[crosses[cross_length][0]][0],routes[crosses[cross_length][0]][1], crosses[cross_length][0] + 1)
			newline1 = matrix.new_line(routes[rand][0],routes[rand][1], rand + 1)
			newline2 = matrix.new_line(routes[rand2][0],routes[rand2][1], rand2 + 1)
			newline3 = matrix.new_line(routes[rand3][0],routes[rand3][1], rand3 + 1)
			newline4 = matrix.new_line(routes[rand4][0],routes[rand4][1], rand4 + 1)
			routes_lijstje.pop(rand)
			routes_lijstje.insert(rand, newline1)
			routes_lijstje.pop(rand2)
			routes_lijstje.insert(rand2, newline2)
			routes_lijstje.pop(rand3)
			routes_lijstje.insert(rand3, newline3)
			routes_lijstje.pop(rand4)
			routes_lijstje.insert(rand4, newline4)
			routes_lijstje.pop(crosses[cross_length][0])
			routes_lijstje.insert(crosses[cross_length][0], newline)
			count_cross = count_for_crosses(routes_lijstje)
			print count_cross

		else:
			rand = randrange(len(routes_lijstje) - 1)
			cross_length = randrange(len(crosses))
			matrix.delete_line(routes_lijstje[crosses[cross_length][1]])
			matrix.delete_line(routes_lijstje[crosses[cross_length][0]])
			newline = matrix.new_line(routes[crosses[cross_length][0]][0],routes[crosses[cross_length][0]][1], crosses[cross_length][0] + 1)
			newline1 = matrix.new_line(routes[crosses[cross_length][1]][0],routes[crosses[cross_length][1]][1], crosses[cross_length][1] + 1)
			routes_lijstje.pop(crosses[cross_length][1])
			routes_lijstje.insert(crosses[cross_length][1], newline1)
			routes_lijstje.pop(crosses[cross_length][0])
			routes_lijstje.insert(crosses[cross_length][0], newline)
			count_cross = count_for_crosses(routes_lijstje)
			print count_cross
		crosses = look_for_crosses(routes_lijstje)
		temp_total = 0
		for i in routes_lijstje:
			temp_total += len(i)

		if count_cross < best_cross:
			best_cross = count_cross
			best_lines = routes_lijstje
			best_layers = matrix.layers
		elif count_cross == best_cross and temp_total < Total_routes:
			best_cross = count_cross
			best_lines = routes_lijstje
			best_layers = matrix.layers

		if loops == 200:
			break

	counter = 0 
	
	# check for empty last layer
	length_l = len(matrix.layers)
	empty = 0
	for i in best_layers:
		count = 0
		for j in i:
			d = sum(j)
			if d == 0:
				count += 1
			if count == y:
				empty += 1

	if empty > 0:
		for i in range(1, empty+1):
			best_layers.pop(length_l - i)


	for column in best_layers:
		counter += 1 
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

	print counter, count_for_crosses(best_lines), Total_routes
	
if __name__ == "__main__":
    main()	