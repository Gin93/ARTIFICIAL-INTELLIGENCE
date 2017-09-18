
"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q1
Classes for representing a STRIPS planning task and capturing its semantics

Enter your details below:

Name: Zi JIN
Student Code:	u5541673
email: u5541673@anu.edu.au


Implements the Greedy Best First Search (GBFS) search algorithm for planning.

Method to be implemented is gbfs.

We provide imports for some basic data-structure that can be useful to tackle the problem. In particular have a look at heapq that
is an efficient implementation of a priority queue using heap
"""



import heapq
import logging

from search import searchspace
from planning_task import Task
from heuristics import BlindHeuristic
def gbfs(task, heuristic=BlindHeuristic):
	"""
	Searches for a plan in the given task using Greedy Best First Search search.

	@param task The task to be solved
	@param heuristic  A heuristic callable which computes the estimated steps
					  from a search node to reach the goal.
	"""
	heap = []
	
	root_node = searchspace.make_root_node(task.initial_state)   # def __init__(self, state, parent, action, g):
	explored = set()
	explored.add(root_node.state)
	counter = 1  # incase the heapq get stuck
	heapq.heappush(heap,( heuristic(root_node)  ,counter , root_node    ))
	node_expansion = 0  # the number of nodes expansion 
	while (True):
		node = heapq.heappop(heap)[2]
		node_expansion = node_expansion + 1  #  POP = node expansion  
		if task.goal_reached(node.state):
			print("------------------")
			print("node expasion:")
			print(node_expansion)   # print the node_expansion for question 3 
			print("------------------")
			return node.extract_solution()

		for successor in task.get_successor_states(node.state):  # pair  successor(1)  or  [1]
			succ_state = successor[1]
			succ_action = successor[0]
			if succ_state not in explored:  # in order loop
				new_node = searchspace.make_child_node(node,succ_action,succ_state)  #make_child_node(parent_node, action, state):
				explored.add(succ_state)
				counter = counter + 1
				heapq.heappush(heap,( heuristic(new_node) , counter ,new_node ))
	


