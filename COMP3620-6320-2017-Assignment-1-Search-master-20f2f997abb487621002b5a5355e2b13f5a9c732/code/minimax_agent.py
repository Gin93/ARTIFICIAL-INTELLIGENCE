# minimax_agent.py
# --------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:

    Name:ZI JIN
    Student Code:u5541673
    email:u5541673@ANU.EDU.AU
"""

from agents import Agent
import util
from actions import Directions, Actions
from search_problems import AdversarialSearchProblem

class MinimaxAgent(Agent):
	""" The agent you will implement to compete with the black bird to try and
		save as many yellow birds as possible. """

	def __init__(self, max_player, depth="2"):
		""" Make a new Adversarial agent with the optional depth argument.
			(MinimaxAgent, str) -> None
		"""
		self.max_player = max_player
		self.depth = int(depth)

	def evaluation(self, problem, state):
		"""
			(MinimaxAgent, AdversarialSearchProblem,
				(int, (int, int), (int, int), ((int, int)), number, number))
					-> number
		"""
		player, red_pos, black_pos, yellow_birds, score, yb_score = state
		
 # this parameter can value the remaining goals.
		
		red_dis = 0
		black_dis = 0
		space = problem.get_width()*problem.get_height()
		
		if problem.get_maximizing_player()== player:
		
			for yellow_pos in yellow_birds:
				red_dis += problem.maze_distance(red_pos,yellow_pos)
			extra_red = space / (1+red_dis)
			
			return score + extra_red
		
		else:
			for yellow_pos in yellow_birds:
				black_dis += problem.maze_distance(black_pos,yellow_pos)
			extra_black = space / (1+black_dis)
			
			return score + extra_black


		
	def maximize(self, problem, state, current_depth):
		"""
			This method should return a pair (max_utility, max_action).
			 (MinimaxAgent, AdversarialSearchProblem,
				 (int, (int, int), (int, int), ((int, int)), number, number)
					 -> (number, str)
		"""

		if problem.terminal_test(state) or current_depth == self.depth:
			return (self.evaluation (problem,state) ,Directions.STOP )
			
		v = - 99999
		max_action=Directions.STOP

		for next_state,action,cost in problem.get_successors( state ):
			player, red_pos, black_pos, yellow_birds, score, yb_score = next_state
			
			if red_pos != black_pos:
				new_v = self.minimize (problem,next_state,current_depth + 1) 
				
				if new_v > v:
					v = new_v
					max_action = action 
					
		return (v,max_action)



	def minimize(self, problem, state, current_depth):
		"""
			This function should just return the minimum utility.

			(MinimaxAgent, AdversarialSearchProblem,
				 (int, (int, int), (int, int), ((int, int)), number, number)
					 -> number
		"""

		if problem.terminal_test(state) or current_depth == self.depth: # terminal/stop
			return self.evaluation (problem,state)
			
		v =  99999 
		
		for next_state,action,cost in problem.get_successors( state ):
			player, red_pos, black_pos, yellow_birds, score, yb_score = next_state
			
			if red_pos == black_pos:  # in case max is eaten by min 
				return -99999

			else:
				v = min(v,self.maximize(problem,next_state,current_depth + 1)[0]) 
				
		return v


	def get_action(self, game_state):
		""" This method is called by the system to solicit an action from
			MinimaxAgent. It is passed in a State object.

			Like with all of the other search problems, we have abstracted
			away the details of the game state by producing a SearchProblem.
			You will use the states of this AdversarialSearchProblem to
			implement your minimax procedure. The details you need to know
			are explained at the top of this file.
		"""
		#We tell the search problem what the current state is and which player
		#is the maximizing player (i.e. who's turn it is now).
		problem = AdversarialSearchProblem(game_state, self.max_player)
		state = problem.get_initial_state()
		utility, max_action = self.maximize(problem, state, 0)
		print("At Root: Utility:", utility, "Action:", max_action, "Expanded:", problem._expanded)
		return max_action
