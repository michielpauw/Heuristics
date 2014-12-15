from GridMatrix import GridMatrix 
from a_star import a_star, node
import sys
from random import randrange 
from Crosses import count_for_crosses, look_for_crosses

def main():
	x = 18
	y = 13
	route = GridMatrix(x, y)
	matrix = a_star(x, y, "grid_1.txt")
	routes = route.read_routes("g_scheme_3_grid_1.txt")
	routes_lijstje = []
	Total_routes = 0
	for i in range(len(routes)):
		# print "line: ", i
		i = matrix.new_line(routes[i][0],routes[i][1], i+1)
		routes_lijstje.append(i)
		Total_routes += len(i)

	# print routes_lijstje

	# for column in matrix.layers:
	# 	for row in column:
	# 		print
	# 		if isinstance(row, int):
	# 			sys.stdout.write("%03d " % (row))
	# 			sys.stdout.write(" ")
	# 			sys.stdout.flush()
	# 		else:
	# 			row = str(row)
	# 			sys.stdout.write(row)
	# 	print
	# x = 0
	# while x == 0:
	# 	continue
	loops = 0
	crosses = look_for_crosses(routes_lijstje)
	print count_for_crosses(routes_lijstje)
	while crosses != [] :
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
			print count_for_crosses(routes_lijstje)
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
		crosses = look_for_crosses(routes_lijstje)
	counter = 0 
	
	# check for empty last layer
	length_l = len(matrix.layers)
	empty = 0
	for i in matrix.layers:
		count = 0
		for j in i:
			d = sum(j)
			if d == 0:
				count += 1
			if count == y:
				empty += 1

	if empty > 0:
		for i in range(1, empty+1):
			matrix.layers.pop(length_l - i)


	for column in matrix.layers:
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

	print counter, count_for_crosses(routes_lijstje), Total_routes
	
if __name__ == "__main__":
    main()	