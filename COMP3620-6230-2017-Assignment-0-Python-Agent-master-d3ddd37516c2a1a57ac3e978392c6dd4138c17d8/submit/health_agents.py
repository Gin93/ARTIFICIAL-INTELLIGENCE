""" File name:   health_agents.py
    Author:      Zi Jin u5541673
    Date:        8/3/2017
    Description: This file contains agents which fight disease. It is used
                 in Exercise 4 of Assignment 0.
"""

import random

class HealthAgent(object):
    """ A simple disease fighting agent. """
    
    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.
            
            (HealthAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an inalid move will cause the system to stop.
            
            Changing any of the mutable parameters will have no effect on the operation
            of the system.
            
            This agent will locally move to the highest disease, of there is
            is no nearby disease, it will act randomly.
            
            (HealthAgent, str, [str], [str], { str : float }, float, float, float) -> str  
        """
        max_disease = None
        max_move = None
        for move in valid_moves:
           if max_disease is None or disease[move] > max_disease:
               max_disease = disease[move]
               max_move = move
        
        if not max_disease:
            return random.choice(valid_moves)
        
        return max_move
        
#Make a new agent here called SmartHealthAgent, which extends HealthAgent and acts a bit more sensibly

class SmartHealthAgent(HealthAgent):
	
	def __init__(self,locations,conn):
		""" This contructor does nothing except save the locations and conn.
			Feel free to overwrite it when you extend this class if you want
			to do some initial computation.
			(HealthAgent, [str], { str : set([str]) }) -> None
		"""
		self.locations = locations
		self.conn = conn

	def choose_move(self, location, valid_moves, disease, threshold, growth, spread):
		""" Using given information, return a valid move from valid_moves.
		Returning an inalid move will cause the system to stop.
		
		
		This agent will always move to the highest disease region. 'region' means caculating the city and its neighboor disease
		If there are more than one shortest way going to the highest disease region, choose the city with higher disease. If still have more than one choice, go random from all of the 'best' path.

		
		(HealthAgent, str, [str], [str], { str : float }, float, float, float) -> str  
		"""
		
		
		max_city = location
		
		regional_disease = {}
		
		for city in disease: #find the city whose situation is worst.  worst means the sum of this city's disease plus its neighboor's 
			a = 0.0  # to store the neighboor's disease
			for i in self.conn[city]:
				a = disease[i] + a
			a = a / (len (self.conn[city]))
			regional_disease[city] = a + disease[city]
			
		for city in regional_disease: #find the city whose situation is worst 
			if regional_disease[city]>= regional_disease[max_city]:
				max_city=city

		
		goal = max_city # set the region center as the goal

		# following is the bfs alg, using bfs alg to find the shortest path to the goal, and return the next move. 
		frontier = set ()
		next_move = {} # record all of the possbile next move and the estimated cost from them to the goal.
		tem_queue = [] # to temporarily store the nodes expaned from the frontier 
		
		for city in self.conn[location]: # find the possbile next move 
			next_move[city] = 0
			#print(visited)
			if goal in self.conn[location]:  # if the agent can go to the goal directly, return the goal city 
				return goal
		
		for city in next_move:
			#print("now for city {}".format(city))
			visited = [] # the city already has been iterated 
			visited.append(location)# added the location and the neighboor to visited list
			
			for j in next_move:
				visited.append(j)
			tem_queue.append(city)
			
			while len(tem_queue) > 0:
				frontier = set ()
				for i in tem_queue:
					frontier.add(i)
				tem_queue = []
				
				if goal in frontier:

					break   # find the goal, finish the while loop, go to next "next_move"
				elif goal not in frontier:
					next_move[city] = next_move[city] + 1 # counter + 1
			
					for n in frontier:# enpand all of the un-vistied conn node for the nodes in frontier

						for m in self.conn[n]:
							if m not in visited:
								tem_queue.append(m)
								visited.append(i)
					
		moves = []  
		for i in range(10):
			if  len(moves) == 0:
				for city in next_move:
					if next_move[city] == i:
						moves.append(city)
			elif len(moves) > 0:
				break
		if len(moves) == 1: # the bfs alg finished. if only one shortest path, return the first city as next move. 
			return moves[0]
		elif len(moves) > 1: # in case there are more than one shortest way, the agent chooses the city with higher disease
			i = 0
			move_final = random.choice(moves)
			for city in moves:
				if disease[city] > i:
					move_final = city
			return move_final
		else:  # in case some unkonwn error happened, at least the agent can go to the highest disease region following by the shortest path. 
			return min(next_move.items(), key=lambda x: x[1])[0]
			
