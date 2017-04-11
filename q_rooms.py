# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:11:30 2017

@author: xiex
"""

import numpy as np

# greedy
greedy = 0.9
# Learning rate
learning_rate = 1
# Discount factor
discount_factor = 0.8

# reward matrix
R = np.array([[-1, -1, -1, -1,  0, -1],
             [-1, -1, -1,  0, -1, 100],
             [-1, -1, -1,  0, -1, -1],
             [-1,  0,  0, -1,  0, -1],
             [ 0, -1, -1,  0, -1, 100],
             [-1,  0, -1, -1, -1, 100]])

# choose action
def choose_action(state, q):    
    # actions that can be applied on the state
    state_actions = np.where(R[state,:] >=0)[0]
    
    if (np.random.uniform() > greedy) or (q[state, state_actions].any() == False):
        action = np.random.choice(state_actions)
    else:
        action = state_actions[state_actions.argmax()]    
    return action
        
if __name__ == "__main__":

    # Q table is initialized with zeros
    Q = np.zeros(R.shape, np.int32)  
    target = R.shape[0]-1
        
    for i in range(100):
        # initial state
        s = np.random.randint(0,R.shape[0])
        steps = s
        reach_target = 0
        
        while not reach_target:
            a = choose_action(s, Q)
            if a == target:
                reach_target = 1                
            r = R[s, a]
            #Q[s,a]<-Q[s,a]+learning_rate*(r+discount_factor*max(Q[s_,a_])-Q[s,a])
            s_ = a
            steps = np.append(steps, a)
            Q[s,a]=Q[s,a]+learning_rate*(r+discount_factor*Q[s_,Q.argmax(1)[s_]]-Q[s,a])
            s = s_
            #print(Q)
        print("episode:",i, "steps:",steps)
        