a=['左寸弦大','心實','氣滯','血痛','停飲','痰迷','暑閉','蟲嚙']
b='喘'
counter = 0
for element in a:
	if element in b:
		counter += 1
		print (counter)