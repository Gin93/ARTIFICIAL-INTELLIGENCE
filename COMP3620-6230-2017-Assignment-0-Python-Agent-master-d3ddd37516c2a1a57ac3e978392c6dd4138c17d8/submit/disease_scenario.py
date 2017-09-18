""" File name:   disease_scenario.py
    Author:    Zi JIN  u5541673
    Date:      5/3/2017  
    Description: This file represents a scenario simulating the spread of an
                 infectious disease around Australia. It should be 
                 implemented for Part 1 of Exercise 4 of Assignment 0.
                 
                 See the lab notes for a description of its contents.
"""
class DiseaseScenario (object):

	def __init__(self, treshold=0.0, growth=0.0, spread=0.0, locations=[], location='', disease={}, conn={}): 
		'''
		save all of the info needed by the cases and agent.
		
		(HealthAgent, float,float,float ,[str], str, { str : float }, { str : set( ) }) -> None
		'''
		self.treshold=treshold
		self.growhth=growth
		self.spread=spread
		self.locations=list(locations)
		self.location=str(location)
		self.disease=dict(disease)
		self.conn=dict(conn)
		

	def read_scenario_file(self, scenario_file_name):
		'''
		read the file to save all of the info 
		
		(DiseaseScenario, str) --> None
		'''
		try:
			content = open(scenario_file_name,'r')
			for line in content:
				line = line[:-1] # to remove /n
				line = line.split(' ')
				
				if line [0] == 'threshold':
					self.threshold = float(line [1])  
				elif line [0] == 'growth':
					self.growth = float(line [1])
				elif line [0] == 'spread':
					self.spread = float (line [1])
				elif line [0] == 'location':
					self.locations.append(line [1]) # a list to store all of the cities
				elif line [0] == 'start':
					self.location = str (line [1])  # to store the start city initialy, and can be replaced by current location
				elif line [0] == 'disease':
					self.disease [line [1]] = float(line [2])  #a location and x is the quantity of disease at that location in the beginning of the scenario
				elif line [0] == 'conn':
					self.conn.setdefault(line[1],set()).add(line[2])  # a dict to show the connection with the 'key' city
					self.conn.setdefault(line[2],set()).add(line[1]) 
					
			for city in self.locations:  # to set the default value 0 to other cities
				if city not in self.disease:
					self.disease[city] = 0.0
			
			for city in self.locations: # to set the default value empty set to other cities
				if city not in self.conn:
					self.conn[city] = set()

			return True
			
		except IOError:
			return False
			
	def valid_moves(self):   
		'''
		return a list of valid moves. Each valid move is either a neighbouring location or the current location of the agent (which indicates that the agent stays put).

		(DiseaseScenario) -> [str]
		'''
		moves = [self.location] # add current location
		for city in self.conn[self.location]: # add connection
			moves.append(city)
		return moves
	
	def move(self,loc):  
		'''
		 move the agent to the specified location and clear the disease there
		(DiseaseScenario, str) -> None
		'''
		
		#self.disease[self.location] = 0
		if loc in self.valid_moves():
			self.location = loc
			self.disease[self.location] = 0
		else:
			raise ValueError ("from {} to {} is not a invalid move".format(self.location,loc))
	
	def spread_disease(self):
		'''
		spread the disease according the threshold,trowth,spread,and connection between locations.
		(DiseaseScenario) -> None
		'''
		increase={} # all of the cities should be increased simultaneously rather than one by one.
		self.disease[self.location] = 0
		for city in self.locations:
			self_growth = self.disease[city] * (1 + self.growth)  # caculate the self_growth
			spread_by_others = 0.0
			for conn_city in self.conn[city]:
				if self.disease[conn_city] >= self.threshold:
					spread_by_others = self.disease[conn_city] * self.spread + spread_by_others # caculate the spread value 
			increase[city] = self.disease[city] * (1 + self.growth) + spread_by_others  # add, temporarily store the value.
		for city in increase:
			self.disease[city] = increase[city]
			increase[city] = 0
		self.disease[self.location] = 0 # for the city agent is in, it shouldn't increase.
		
	
			
		
		
	


