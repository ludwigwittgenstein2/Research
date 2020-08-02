"""


Conceptualize Tic  Tac Toe RL

Class State - init, hash, end, next_state, print_state
get_all_state, get_all_state, all_state

Class Judger - init, reset, alternate, play,
Class Player - init, reset, set_state, set_symbol, backup, act, save_policy, load_policy
Class Human Player - init, reset, set_state, set_symbol, act
Function Train -
Function Compete -
Function Play -
Function Main - train, compete, play


"""

import numpy as np
import pickle


BOARD_ROWS = 3
BOARD_COLUMNS = 3
BOARD_SIZE = BOARD_ROWS * BOARD_COLUMNS


#print(BOARD_ROWS)
#print(BOARD_SIZE)
#print(BOARD_COLUMNS)

class State:
    def __init__(self):
        self.data = np.zeros(BOARD_COLUMNS, BOARD_ROWS)
        self.winner = None
        self.hash_value = None
        self.end = None


    def hash(self):
        if self.hash_value is None:
            self.hash_value = 0
            for i in np.nditer(self.data):
                self.hash_value = self.hash_value * 3 + i + 1
            return self.hash_value

    def end(self):
        if self.end is not None:
            return self.end
        results = []
        for i in range(BOARD_ROWS):
            results.append(np.sum(self.data[i, :]))
        for i in range(BOARD_COLS):
            results.append(np.sum(self.data[:,i]))

        trace = 0
        reverse_trace = 0

        #I don't understand this
        for i in range(BOARD_ROWS):
            trace += self.data[i, i]
            reverse_trace += self.data[i, BOARD_ROWS-1-i]
        results.append(trace)
        results.append(reverse_trace)

        for results in results:
            if result == 3:
                self.winner = 1
                self.end= True
                return self.end
            if result == -3:
                self.winner = -1
                self.end = True
                return self.end
