
"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q2

Enter your details below:

Name: Zi JIN
Student Code:	u5541673
email: u5541673@anu.edu.au


Implements the A* (a-star) search algorithm for planning.

Method to be implemented is a_star.

We import some basic data-structure that can be useful to tackle the problem. 
Have a look at *heapq* that is an efficient implementation of a priority queue using a heap data-structure
Have a look at searchspace that gives you an implementation of a searchnode. In particular look at make_root_node and make_child_node
"""

import heapq  # heapq.xxxx
import logging

from search import searchspace   # make_root_node   # make_child_node   # extract_solution
from planning_task import Task
from heuristics import BlindHeuristic



def a_star(task, heuristic=BlindHeuristic):
	"""
	Searches for a plan in the given task using A* search.

	@param task The task to be solved
	@param heuristic  A heuristic callable which computes the estimated steps
					  from a search node to reach the goal.
	"""
	
	heap = []
	root_node = searchspace.make_root_node(task.initial_state)   # def __init__(self, state, parent, action, g):
	explored = {}
	
	
	explored [root_node.state] =  root_node.g

	counter = 1 
	heapq.heappush(heap,( root_node.g+ heuristic(root_node)  ,counter , root_node    ))
	node_expansion = 0 
	
	while (True):
		node = heapq.heappop(heap)[2]
		node_expansion = node_expansion + 1
		if task.goal_reached(node.state):
			print("------------------")
			print("node expasion:")
			print(node_expansion)
			print("------------------")
			return node.extract_solution()

		for successor in task.get_successor_states(node.state):  # pair  successor(1)  or  [1]
			succ_state = successor[1]
			succ_action = successor[0]
			

			new_node = searchspace.make_child_node(node,succ_action,succ_state)  #make_child_node(parent, action, state):

			if (succ_state in explored and explored[succ_state] > new_node.g) or (succ_state not in explored) : # reopen! 
				counter = counter + 1
				heapq.heappush(heap,( new_node.g+ heuristic(new_node) , counter ,new_node ))
				explored [succ_state] =  new_node.g
			
			
			'''
			skip = False # if the state is already in the heapq, then update it rather than push it 
			for elem in heap :  
				if elem[2].state == succ_state:
					a_counter = a_counter +1
					skip = True 
					elem[2].parent = new_node.parent
					elem[2].action = succ_action
					elem[2].g = new_node.g
			'''
			
			#if not skip:
			'''
			if succ_state not in explored:
				counter = counter + 1
				heapq.heappush(heap,( new_node.g+ heuristic(new_node) , counter ,new_node ))
				explored [succ_state] =  new_node.g
			'''

			
	'''
	def find(heap, f):
		""" Returns some item n from the queue such that f(n) == True and None 
			if there is no such item. 
			(PriorityQueue, (object) -> object/None) -> object
		"""
		for elem in heap:
			if f(elem[2]):
				return elem[2]
		return None
		
	def change_priority(heap, item, priority,counter):
		""" Change the priority of the given item to the specified value. If
			the item is not in the queue, a ValueError is raised.
			(PriorityQueue, object, int) -> None
		"""
		for eid, elem in enumerate(heap):
			if elem[2] == item:
				heap[eid] = (priority, count, item)
				count += 1
				heapq.heapify(heap)
				return
		raise ValueError("Error: " + str(item) + " is not in the PriorityQueue.")
	'''
			

				
				
				
				