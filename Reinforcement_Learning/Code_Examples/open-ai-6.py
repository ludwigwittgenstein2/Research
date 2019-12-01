#Naive Heuristic for RL

import gym
import numpy as np

def naive_sum_reward_agent(env, num_episodes=500):
    #this table will hold our rewards
    #each action in each state
    r_table = np.zeros((5,2))
    for g in range(num_episodes):
        s = env.reset()
        done = False 
        while not done: 
            if np.sum(r_table[s,:]) ==0:
                #make a selection
                a = np.random.randit(0,2)
            else: 
                a = np.argmax(r_table[s,:]
            new_s, r, done, _ = env.step(a)
            r_table[s,a] += r
            s = new_s
    return r_table
    