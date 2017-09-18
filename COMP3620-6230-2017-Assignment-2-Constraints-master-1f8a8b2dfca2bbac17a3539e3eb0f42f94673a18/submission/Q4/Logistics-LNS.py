import argparse
import sys
from subprocess import Popen, PIPE, STDOUT
import random
# Complete the file with your LNS solution

if __name__ =='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('problem_filename', help='problem file')
	parser.add_argument('start_solution_filename', help='file describing the solution to improve')
	args = parser.parse_args()
	start_solution_filename = args.start_solution_filename
	problem_filename = args.problem_filename
	iteration = 1
	sfile = open (start_solution_filename,"r") # read the start_solution_file
	f1 = sfile.readlines()
	start_solution = f1[0].split(',')
	num_truck = int (start_solution[0])
	num_cus = int (start_solution[1])
	solutionfile = 'best-solution-'+str(num_truck)+'-'+str(num_cus)+'.dzn'

	if num_truck < 20: # for the small case, run the LNS alg 50 itrations 
		max_iteration = 50
	else:				# for the large case, run 10 times
		max_iteration = 10
		
	while iteration <= max_iteration:
		if iteration == 1: # read the start_solution
			sfile = open (start_solution_filename,"r") # read the start_solution_file
		if iteration > 1:  # read the current solution
			sfile = open (solutionfile,"r" )

		f1 = sfile.readlines() # print the current cost 
		read_cost = f1[0].strip('\n')
		read_cost = read_cost.strip(' ')
		read_cost = read_cost.split(',')
		print('iteration:{0}'.format(iteration))
		print('current cost: {}'.format(read_cost[2]))

		
		
		pfile = open(problem_filename,"r") # read the problem file 
		f2 = pfile.readlines()
		a = open ('keep.dzn',"w")   
		for eachline in f2:
			a.write(eachline) # write the problem into the keep file, so that the MZN only need to read one DZN file


		var_name = 'delivery' # wrtie the var content into the keep file 
		a.write(var_name + '=' + " array2d(trucks,1..5*C," + '\n' + '[' +'\n')
		
		removed = '_' # start to remove some stuff from the current solution 
		myList = [([0] * num_cus*5) for i in range(num_truck)]
		for i in range (num_truck):
			for j in range(num_cus):
				myList[i][5*j] = i+1
				myList[i][5*j+2] = j+1
				if num_truck < 20:  # for the samll case, remove all of the infomation about sequence
					myList[i][5*j+1] = removed
				elif i < round(num_truck/2):
					myList[i][5*j+1] = removed # for the large case, remove half of the infomation about sequence (speed is a problem)
					
		current_solution = f1[1:]
		for eachline in current_solution:
			eachline = eachline.split(',')
			t = int(eachline[0])
			c = int(eachline[2])
			myList[t-1][c*5-5+1] =removed
			if iteration % 2 == 0: # in odd iterations, remove the ambient good delivery information 
				myList[t-1][c*5-5+3] = int(eachline[3])
				myList[t-1][c*5-5+4] =removed
			else:   			#in even iterations, remove the chilled good delivery information 
				myList[t-1][c*5-5+3] =removed
				myList[t-1][c*5-5+4] = int(eachline[4])

		removetimes = 35 # also remove some infomation randomly
		for i in range(removetimes):
			index_truck = random.randint(0,num_truck-1)
			index_cus = random.randint(0,num_cus*5-1)
			myList[index_truck][index_cus] = removed

		m = str(myList) # write the destroyed solution into the keep.dzn file 
		m = m.replace('[' ,'')
		m = m.replace(']' ,'')
		m = m.replace("'" ,'')
		a.write(m)
		a.write('\n' + "]);")
		a.close()
		
		#call cmd to run the MZN file with DZN file also output the result into solution file 
		cmd = "minizinc L4.mzn keep.dzn --soln-sep \"\" --search-complete-msg \"\" > " + solutionfile
		p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,stderr=STDOUT)
		output = p.stdout.read()
		
		iteration = 1 + iteration
		
