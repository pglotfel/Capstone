'''
Created on Jul 25, 2014

@author: Paul
'''
from __future__ import print_function
import time

#STATE INFORMATION##########################################################

#5 is ALWAYS BACK

#HOME SCREEN is 0 -> 1 report problem 2 view information

#VIEW INFORMATION is 2 ->

#REPORT A PROBLEM is 1 ->
#0 chain broken 
#1 seat damaged
#2 Flat tired
#3 Missing basket
#4 Other

#CHAIN BROKEN is 3 -> auto to 8
#SEAT DAMAGED is 4 -> auto to 8 
#FLAT TIRE is 5 -> auto to 8
#MISSING BASKET is 6 -> auto to 8
#OTHER is 7 -> auto to 8

#THANK YOU REPORT PROBLEM is 8 -> auto to home

#############################################################################

#Okay, I can definitely make these states better.  I should make them that you just initialize the state with a function
#that you want it to run and a dictionary of things to return based on the input it receives...


def mark_received(input_vector):
    for i in range(len(input_vector)):
        input_vector[i] = 0;

class State:
    def __init__(self, id, function, next_state):
        self.id = id
        self.function = function
        self.next_state = next_state
        
    def run(self, input_vector):
        
        try:
            current_input = input_vector.index(1);
        except ValueError:
            #Case when no input...
            self.function();
            if(type(self.next_state) is list):
                return self.id
            else:
                return self.next_state
        
        self.function();
        
        mark_received(input_vector)
        
        if(type(self.next_state) is list):     
            return self.next_state[current_input]
        else:
            return self.next_state

if __name__ == '__main__':
    pass

def generateInputVector(num_inputs):
    ret = []
    
    for i in range(num_inputs):
        ret.append(0)
        
    return ret
    
def state_one(input_vector):
    
    print('Report a problem!')
    
    ret = 1;
    
    if(input_vector[5]):
        ret = 0
    elif(input_vector[0]):
        ret = 3
    elif(input_vector[1]):
        ret = 4
    elif(input_vector[2]):
        ret = 5
    elif(input_vector[3]):
        ret = 6
    elif(input_vector[4]):
        ret = 7
      
    mark_received(input_vector) 
    return ret;

def state_three(input_vector):
    
    print('Chain broken report')
    
    return 8

def state_four(input_vector):
    
    print('Seat damaged')
    
    return 8

def state_five(input_vector):
    
    print('flat tire')
    
    return 8

def state_six(input_vector):
    
    print('Missing basket')
    
    return 8

def state_seven(input_vector):
    
    print('Other')
    
    return 8

def state_eight(input_vector):
    
    print('Thanks for reporting a problem')
    
    time.sleep(2)
      
    return 0
    
#Intialize state dictionary

#NEW STATES! :D Much fancier!

   
states = {0 : State(0, lambda: print('state_zero'), [0, 1, 2, 0, 0, 0]),
          1 : State(1, lambda: print('report a problem'), [3, 4, 5, 6, 7, 0]), 
          2 : State(2, lambda: print('view information '), [0, 0, 0, 0, 0, 0]), 
          3 : State(3, lambda: print('Chain broken report'), 8),
          4 : State(4, lambda: print('Seat damaged'), 8),
          5 : State(5, lambda: print('Flat tire'), 8),
          6 : State(6, lambda: print('Missing basket'), 8),
          7 : State(7, lambda: print('Other'), 8),
          8 : State(8, state_eight, 0)}

print(states.get(0).run([0, 0, 0, 0, 0, 0]))

print(states.get(3).run([0, 0, 0, 0, 0, 0]))

print(states.get(3).run([0, 1]));

current_state = 0
system_input = generateInputVector(5)


#Try making a test that has a 'forward' and a 'back' button.  Forward goes to some sort of information?  Maybe a map?

#while(1):
#   current_state = states.get(current_state).run(input_vector)
#  time.sleep(1)











    