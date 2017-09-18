""" File name:  dfa.py Author:  
		Zi Jin u5541673
Date:  4/3/2017
Description: This file defines a function which reads in
    a DFA described in a file and builds an appropriate datastructure.

                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.

                 It should be implemented for Exercise 3 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import os
def load_dfa(dfa_file_name):
    """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.

        (str) -> Object
    """
    dfa_file = open(dfa_file_name,'r')
    
    global start_states,accepting_states,edges
    edges = {}

    for line in dfa_file:
        line = line[:-1] # delete the /n
        line = line.split(' ') 

        if line [0] == 'initial':
            start_states = line [1:]
        elif line [0] == 'accepting':
            accepting_states = line [1:]          
        elif line [0] == 'transition':
            edges [line [1],line[3]] = line[2] # in dfa, there is only one value mapping to the current state and current input, therefore choose these two as keys and the next states as value.
            

    x = (start_states,accepting_states,edges)  
    return x



def accepts_word(dfa, word):
    """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
    """
    dfa = load_dfa(dfa)
    word = list(word)
    
    start = dfa[0]
    accepting = dfa[1]
    edges = dfa[2]

    state = start[0]
    
    for i in range ( len(word) ):        
        if ( state,word [i]) in edges:    # if the current input can be accepted, then go to next state 
            state = edges[ state, word[i]]
            i = i + 1
        else:            # if the input no in the dict, then reject 
            return 0
     
    if state  in accepting: # after accepting all of the inputs, judge if the final state in the set of accepting states
        return 1
    elif state  not in accepting:
            return 0


a = accepts_word("test2.dfa", "sang")
print (a)
