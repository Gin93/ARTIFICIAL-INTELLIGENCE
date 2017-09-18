# heuristics.py
# ----------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

""" This class contains heuristics which are used for the search procedures that
    you write in search_strategies.py.

    The first part of the file contains heuristics to be used with the algorithms
    that you will write in search_strategies.py.

    In the second part you will write a heuristic for Q4 to be used with a
    MultiplePositionSearchProblem.
"""

#-------------------------------------------------------------------------------
# A set of heuristics which are used with a PositionSearchProblem
# You do not need to modify any of these.
#-------------------------------------------------------------------------------

import search_problems

def null_heuristic(pos, problem):
    """ The null heuristic. It is fast but uninformative. It always returns 0.
        (State, SearchProblem) -> int
    """
    return 0

def manhattan_heuristic(pos, problem):
  """ The Manhattan distance heuristic for a PositionSearchProblem.
      ((int, int), PositionSearchProblem) -> int
  """
  return abs(pos[0] - problem.goal_pos[0]) + abs(pos[1] - problem.goal_pos[1])

def euclidean_heuristic(pos, problem):
    """ The Euclidean distance heuristic for a PositionSearchProblem
        ((int, int), PositionSearchProblem) -> float
    """
    return ((pos[0] - problem.goal_pos[0]) ** 2 + (pos[1] - problem.goal_pos[1]) ** 2) ** 0.5

#Abbreviations
null = null_heuristic
manhattan = manhattan_heuristic
euclidean = euclidean_heuristic

#-------------------------------------------------------------------------------
# You have to implement the following heuristics for Q4 of the assignment.
# It is used with a MultiplePositionSearchProblem
#-------------------------------------------------------------------------------

#You can make helper functions here, if you need them

def bird_counting_heuristic(state, problem) :
    position, yellow_birds = state
    heuristic_value = len(yellow_birds)

    """ *** YOUR CODE HERE *** """

    return heuristic_value

bch = bird_counting_heuristic


def every_bird_heuristic(state, problem):
	"""    
		(((int, int), ((int, int))), MultiplePositionSearchProblem) -> number
	"""
	position, yellow_birds = state
	distance = 0
	distance1 = 99999
	h1 = h2= h3 =0
	
	for goal in yellow_birds:
		a = problem.maze_distance(position,goal)
		if a > distance:
			distance = a     # max distance to a goal 
		if a < distance1:
			distance1 = a    # min distance to a goal 

	num = len(yellow_birds)
	heuristic_value = distance + num - 1
	if num >= 2:  # caculate three admissiable heuristics, choose the maximal value
		threshold = 23
		b = 0
		for i in range(num):
			for j in range(num):
				b = problem.maze_distance(yellow_birds[i],yellow_birds[j]) + b 
		average = b / ((num-1)* (num-1))
		if num > 10 and average > threshold:
			h1 = average * (num-2) + distance1
		# ########################
		index = 9999
		for i in range(num):
			for j in range(num):
				b = problem.maze_distance(yellow_birds[i],yellow_birds[j])
				if b > 0:
					if b < index:
						index = b
		h2 = index * (num-1) + distance1
		# ##############################
		b = 0
		for i in range(num):
			for j in range(num):
				c = problem.maze_distance(yellow_birds[i],yellow_birds[j])
				if c > b:
					b = c
		h3=b+distance1
		
		return max([h1,h2,h3])
		
	return heuristic_value
		
	
 
every_bird = every_bird_heuristic

