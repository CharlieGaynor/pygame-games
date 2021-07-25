from tic_tac_toe_board import board
import random
import copy
import json





class q_strategy():

    def __init__(self, table):
        self.values = table


    #this bit is fine
    def SelectMove(self, board,actions, player_value):
        MaxValue = float('-inf')
        bestMove = actions[0]

#        ic(actions) - this works fine



        for (i,j) in actions:
            state2 = copy.deepcopy(board.get_state_list())
            state2[i][j] = player_value
            q_value = self.values.get(str(state2),0)

            #ic(str(state2)) works fine
            
            if q_value > MaxValue:
                MaxValue = q_value
                bestMove = (i,j)

        return bestMove