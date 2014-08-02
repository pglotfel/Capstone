'''
Created on Jul 25, 2014

@author: Paul
'''

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


if __name__ == '__main__':
    pass

def generateInputVector(num_inputs):
    ret = []
    
    for i in range(num_inputs):
        ret.append(0)
        
    return ret

def mark_received(input_vector):
    for i in range(len(input_vector)):
        input_vector[i] = 0;

#Make states return the next state...

def state_zero(input_vector):
    
    print('state zero!')
    
    ret = 0;
    
    if(input_vector[1]):
        ret = 1
    
    elif(input_vector[2]):
        ret = 2
        
    mark_received(input_vector)
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
    
states = {0 : state_zero,
          1 : state_one,  
          3 : state_three,
          4 : state_four, 
          5 : state_five,
          6 : state_six,
          7: state_seven,
          8 : state_eight}

current_state = 0
system_input = generateInputVector()

#Try making a test that has a 'forward' and a 'back' button.  Forward goes to some sort of information?  Maybe a map?

while(1):
    current_state = states.get(current_state)(system_input)
    time.sleep(1)











    