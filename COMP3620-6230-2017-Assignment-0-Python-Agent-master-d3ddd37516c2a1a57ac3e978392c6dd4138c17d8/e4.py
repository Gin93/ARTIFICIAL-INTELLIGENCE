def read_scenario_file(scenario_file_name):
	content = open (scenario_file_name,'r')
	tem_conn = []
	locations = [] # list 
	disease ={} # dict
	conn = {}   # dict
	for line in content:
		line = line[:-1]
		line = line.split(' ')

		if line [0] == 'threshold':
			threshold = line [1]
		elif line [0] == 'growth':
			growth = line [1]
		elif line [0] == 'spread':
			spread = line [1]
		elif line [0] == 'location':
			locations.append(line [1]) # a list to store all of the cities
		elif line [0] == 'start':
			location = line [1]  # to store the start city 
		elif line [0] == 'disease':
			disease [line [1]] = line [2]  #a location and x is the quantity of disease at that location in the beginning of the scenario
		elif line [0] == 'conn':
			conn.setdefault(line[1],set()).add(line[2])
			conn.setdefault(line[2],set()).add(line[1]) 

	for city in locations:  # to set the default value 0 to other cities
		if city not in disease:
			disease[city] = 0
	
	for city in locations: # to set the default value empty set to other cities
		if city not in conn:
			conn[city] = set()




	print(threshold)
	print(growth)
	print(spread)
	print(locations)
	print(location)
	print(disease)
	print(conn)

	
	return 1

read_scenario_file ("scenario1.scn")
