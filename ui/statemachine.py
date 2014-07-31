'''
Created on Jul 25, 2014

@author: Paul
'''

import time

if __name__ == '__main__':
    pass

def generateInputVector(num_inputs):
    ret = []
    
    for i in range(num_inputs):
        ret.append(0)
        
    return ret

#Make states return the next state...

def state_zero(input_vector):
    
    print('state zero!')
    
    if(input_vector[0] is 0):
        return 0
    else:
        return 1;  
    
def state_one():
    return 0
    
    
    
states = {0 : state_zero,
          1 : state_one,   
          }

current_state = 0
system_input = generateInputVector(2)

#Try making a test that has a 'forward' and a 'back' button.  Forward goes to some sort of information?  Maybe a map?

while(1):
    current_state = states.get(current_state)(system_input)
    time.sleep(1)











    