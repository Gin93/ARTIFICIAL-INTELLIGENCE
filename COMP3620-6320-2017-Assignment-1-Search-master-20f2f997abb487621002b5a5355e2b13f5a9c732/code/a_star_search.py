"""
    Enter your details below:

    Name: zi jin
    Student Code:	u5541673
    email: u5541673@anu.edu.au
"""

import util
import search_strategies
import frontiers
import search_problems
import heuristics


def solve(problem, heuristic) :

	frontier = frontiers.PriorityQueue() 
	actions = list()
	explored = set()
	
	node = search_strategies.SearchNode(None,None,0,None,0)  # for the searchNode def __init__(self, state, action = None, path_cost = 0, parent = None, depth = 0):
	node.state = problem.get_initial_state()
	frontier.push(node,heuristic(node.state,problem))
	
	explored.add(node.state)
	while not frontier.is_empty():
	
		node=frontier.pop()
		if problem.goal_test(node.state):   
			while node.parent: 
				actions.insert(0,node.action)
				node=node.parent
			return actions
		for successor,action,cost in problem.get_successors(node.state):  
			if successor not in explored:
				explored.add(successor)
				new_node = search_strategies.SearchNode(successor, action, cost + node.path_cost , node, 0)
				frontier.push(new_node, new_node.path_cost + heuristic(new_node.state,problem))   



