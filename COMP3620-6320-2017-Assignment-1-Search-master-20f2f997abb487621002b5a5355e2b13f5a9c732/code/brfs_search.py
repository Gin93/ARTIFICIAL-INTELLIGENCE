"""
    Enter your details below:

    Name: zi jin
    Student Code: u5541673
    email: u5541673@anu.edu.au
"""

import util
import search_strategies
import frontiers
import search_problems


def solve(problem) : # shuold store action rather than path
	frontier = frontiers.Queue() #FIFO 
	explored = set()
	actions = list()
	node = search_strategies.SearchNode(None,None,None,None,None)  # for the searchNode def __init__(self, state, action = None, path_cost = 0, parent = None, depth = 0):
	node.state = problem.get_initial_state()
	frontier.push(node)
	explored.add(node.state)
	
	while not frontier.is_empty():
	
		node=frontier.pop()
		
		if problem.goal_test(node.state):   
			while node.parent: # when the node has a parent
				actions.insert(0,node.action)
				node=node.parent
			return actions

		for successor,action,cost in problem.get_successors(node.state):  
			if successor not in explored:
				explored.add(successor)
				frontier.push(search_strategies.SearchNode(successor, action, cost, node, None))   





