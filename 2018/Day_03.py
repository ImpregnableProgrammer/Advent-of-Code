def First_Part(claims):
	Count = 0
	Sheet = [[' '] * 1000 for i in range(1010)]
	for claim in claims:
		coords = claim.split(' ')[2].split(',')
		x = int(coords[1][:-1])
		y = int(coords[0])
		dims = claim.split(' ')[3].split('x')
		width = int(dims[1])
		height = int(dims[0])
		#print(width, height, x, y, claim.split(' ')[0])
		for i in range(x, x + width):
			for j in range(y, y + height):
				Count += Sheet[i][j] == '.'
				Sheet[i][j] = '.' if Sheet[i][j] == ' ' else 'X'
	return Count

Input = open("Inputs/Day_03.txt", "r").read()[:-1]
print(First_Part(Input.split('\n')))

def Second_Part(claims):
	Sheet = [[' '] * 1000 for i in range(1010)]
	for claim in claims:
		coords = claim.split(' ')[2].split(',')
		x = int(coords[1][:-1])
		y = int(coords[0])
		dims = claim.split(' ')[3].split('x')
		width = int(dims[1])
		height = int(dims[0])
		for i in range(x, x + width):
			for j in range(y, y + height):
				Sheet[i][j] = '.' if Sheet[i][j] == ' ' else 'x'	
	for claim in claims:
		coords = claim.split(' ')[2].split(',')
		x = int(coords[1][:-1])
		y = int(coords[0])
		dims = claim.split(' ')[3].split('x')
		width = int(dims[1])
		height = int(dims[0])
		Overlap = 0
		for i in range(x, x + width):
			for j in range(y, y + height):
				Overlap = Sheet[i][j] == 'x' or Overlap
		if not Overlap:
			return claim.split(' ')[0]

Input = open("Inputs/Day_03.txt", "r").read()[:-1]
print(Second_Part(Input.split('\n')))
