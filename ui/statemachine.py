'''
Created on Jul 25, 2014

@author: Paul
'''

if __name__ == '__main__':
    pass

def generateInputVector(num_inputs):
    ret = []
    
    for i in range(num_inputs):
        ret.append(0)
        
    return ret

def stateone():
    return 1
    
def statetwo():
    return 2
    
    
    
states = {0 : stateone,
          1 : statetwo,   
          }


print(states.get(1)())
print(states.get(0)())
print(generateInputVector(5))





#This works as expected!  Now make the actual program to switch between states...

    