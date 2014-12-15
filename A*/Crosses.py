# a file that checks for crosses

def count_for_crosses(dataset):
	crosses = 0
	lines_w_cross = []
	for i in range(len(dataset)):
		for j in range(i+1,len(dataset)):

			if i == j:
				continue
			for k in range(len(dataset[i])):
				if k == 0:
					continue
				elif k == (len(dataset[i]) - 1):
					continue
				for l in range(len(dataset[j])):
					if l == 0:
						continue
					elif l == (len(dataset[j]) - 1):
						continue
					if dataset[i][k] == dataset[j][l]:
						crosses += 1
						# print "route:", i, "node:", dataset[i][k], "with:", j

	return crosses

def look_for_crosses(dataset):
	lines_w_cross = []
	for i in range(len(dataset)):
		for j in range(i+1,len(dataset)):
			if i == j:
				continue
			for k in range(len(dataset[i])):
				if k == 0:
					continue
				elif k == (len(dataset[i]) - 1):
					continue
				for l in range(len(dataset[j])):
					if l == 0:
						continue
					elif l == (len(dataset[j]) - 1):
						continue
					if dataset[i][k] == dataset[j][l]:
						# print "route:", i, "node:", dataset[i][k], "with:", j
						lines_w_cross.append([i,j])
						# return i, j
	return lines_w_cross