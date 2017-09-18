"""
    Enter your details below:

    Name: ZI JIN
    Student Code: U5541673	
    email: U5541673@ANU.EDU.AU
"""
'''
3. It produces an **optimal** solution, (that is the number of steps is minimal)  # SHOULD NOT USE EXPLORED(),
4. The number of nodes on the fringe is **linear** in the depth of the deepest node
5. In case no solution is found, the procedure prints a valid **lower-bound** for the
   solution on the standard output
4. In order to achieve our similar performances, you need a smart way to detect
   loops, which does not compromise optimality, and preserves the O(bm) space requirement
'''
import util
import search_strategies
import frontiers
import search_problems


def solve( problem ) :
	actions = list()
	depth = 1;
	while True:
		a = DLS(problem,depth)["solution"]
		if a == 'done':
			return DLS(problem,depth)['path']
		elif a == 'cutoff':
			depth = depth + 1
			print(depth)


def DLS(problem,depth): 
	node = search_strategies.SearchNode(None,None,None,None,0)  # for the searchNode def __init__(self, state, action = None, path_cost = 0, parent = None, depth = 0):
	node.state = problem.get_initial_state()
	explored = set()
	explored.add(node.state)
	return  Recursive_DLS (node,problem,depth,explored)
	
def Recursive_DLS (node,problem,depth,explored):  # this part implements the pseudo-code of the lecture node
	ex = explored.copy()
	
	if problem.goal_test(node.state):

		actions = list()
		while node.parent: # if the node has a parent
			actions.insert(0,node.action)
			node=node.parent
		return {"solution" : 'done' , "path" : actions}
	
	elif node.depth == depth:
		return {"solution" : 'cutoff' , "path" : None}
	else:
		cutoff_occ = False
		
		for successor,action,cost in problem.get_successors(node.state): 
			ex.add(successor) # detect the loop
			if successor not in explored:
				new_node=search_strategies.SearchNode(successor, action, cost, node, node.depth + 1)
				result = Recursive_DLS(new_node,problem,depth,ex)
				if result['solution'] == 'cutoff':
					cutoff_occ = True
				elif result['solution'] != 'gg':
					return result
		if cutoff_occ == True:
			return {"solution" : 'cutoff' , "path" : None}
		else:
			return {"solution" : 'gg' , "path" : None}


	
	
	
	
	
	
	
	
	
	

