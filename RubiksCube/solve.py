import numpy as np
import random
import matplotlib.pyplot as plt
import math
import csv

"""完成形"""
def SolvedState():
    SolvedState = np.array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
                        [10, 11, 12, 13, 14, 15, 16, 17, 18],
                        [20, 21, 22, 23, 24, 25, 26, 27, 28],
                        [30, 31, 32, 33, 34, 35, 36, 37, 38],
                        [40, 41, 42, 43, 44, 45, 46, 47, 48],
                        [50, 51, 52, 53, 54, 55, 56, 57, 58]
                       ])
    return SolvedState

"""すべての動き3*6通り"""
"""白面Wの左右の動き"""
def WL(state):
    BackState = state.copy()
    state[0][1], state[0][2], state[0][3], state[0][4], state[0][5], state[0][6], state[0][7], state[0][8] = \
    BackState[0][4], BackState[0][1], BackState[0][2], BackState[0][3], BackState[0][8], BackState[0][5], BackState[0][6], BackState[0][7]
    state[1][3], state[1][4], state[1][8] = BackState[4][2], BackState[4][3], BackState[4][7]
    state[2][1], state[2][4], state[2][5] = BackState[1][4], BackState[1][3], BackState[1][8]
    state[3][1], state[3][2], state[3][6] = BackState[2][4], BackState[2][1], BackState[2][5]
    state[4][2], state[4][3], state[4][7] = BackState[3][1], BackState[3][2], BackState[3][6]
    return state

def WR(state):
    BackState = state.copy()
    state[0][1], state[0][2], state[0][3], state[0][4], state[0][5], state[0][6], state[0][7], state[0][8] = \
    BackState[0][2], BackState[0][3], BackState[0][4], BackState[0][1], BackState[0][6], BackState[0][7], BackState[0][8], BackState[0][5]
    state[1][3], state[1][4], state[1][8] = BackState[2][4], BackState[2][1], BackState[2][5]
    state[2][1], state[2][4], state[2][5] = BackState[3][2], BackState[3][1], BackState[3][6]
    state[3][1], state[3][2], state[3][6] = BackState[4][2], BackState[4][3], BackState[4][7]
    state[4][2], state[4][3], state[4][7] = BackState[1][3], BackState[1][4], BackState[1][8]
    return state

def W2(state):
    BackState = state.copy()
    state[0][1], state[0][2], state[0][3], state[0][4], state[0][5], state[0][6], state[0][7], state[0][8] = \
    BackState[0][4], BackState[0][1], BackState[0][2], BackState[0][3], BackState[0][8], BackState[0][5], BackState[0][6], BackState[0][7]
    state[1][3], state[1][4], state[1][8] = BackState[4][2], BackState[4][3], BackState[4][7]
    state[2][1], state[2][4], state[2][5] = BackState[1][4], BackState[1][3], BackState[1][8]
    state[3][1], state[3][2], state[3][6] = BackState[2][4], BackState[2][1], BackState[2][5]
    state[4][2], state[4][3], state[4][7] = BackState[3][1], BackState[3][2], BackState[3][6]
    BackState = state.copy()
    state[0][1], state[0][2], state[0][3], state[0][4], state[0][5], state[0][6], state[0][7], state[0][8] = \
    BackState[0][4], BackState[0][1], BackState[0][2], BackState[0][3], BackState[0][8], BackState[0][5], BackState[0][6], BackState[0][7]
    state[1][3], state[1][4], state[1][8] = BackState[4][2], BackState[4][3], BackState[4][7]
    state[2][1], state[2][4], state[2][5] = BackState[1][4], BackState[1][3], BackState[1][8]
    state[3][1], state[3][2], state[3][6] = BackState[2][4], BackState[2][1], BackState[2][5]
    state[4][2], state[4][3], state[4][7] = BackState[3][1], BackState[3][2], BackState[3][6]
    return state
    
"""赤面Rの左右の動き"""
def RL(state):
    BackState = state.copy()
    state[0][1], state[0][2], state[0][6] = BackState[2][1], BackState[2][2], BackState[2][6]
    state[1][1], state[1][2], state[1][3], state[1][4], state[1][5], state[1][6], state[1][7], state[1][8] = \
    BackState[1][4], BackState[1][1], BackState[1][2], BackState[1][3], BackState[1][8], BackState[1][5], BackState[1][6], BackState[1][7]
    state[2][1], state[2][2], state[2][6] = BackState[5][1], BackState[5][2], BackState[5][6]
    state[4][1], state[4][2], state[4][6] = BackState[0][1], BackState[0][2], BackState[0][6]
    state[5][1], state[5][2], state[5][6] = BackState[4][1], BackState[4][2], BackState[4][6]
    return state

def RR(state):
    BackState = state.copy()
    state[0][1], state[0][2], state[0][6] = BackState[4][1], BackState[4][2], BackState[4][6]
    state[1][1], state[1][2], state[1][3], state[1][4], state[1][5], state[1][6], state[1][7], state[1][8] = \
    BackState[1][2], BackState[1][3], BackState[1][4], BackState[1][1], BackState[1][6], BackState[1][7], BackState[1][8], BackState[1][5]
    state[2][1], state[2][2], state[2][6] = BackState[0][1], BackState[0][2], BackState[0][6]
    state[4][1], state[4][2], state[4][6] = BackState[5][1], BackState[5][2], BackState[5][6]
    state[5][1], state[5][2], state[5][6] = BackState[2][1], BackState[2][2], BackState[2][6]
    return state

def R2(state):
    BackState = state.copy()
    state[0][1], state[0][2], state[0][6] = BackState[2][1], BackState[2][2], BackState[2][6]
    state[1][1], state[1][2], state[1][3], state[1][4], state[1][5], state[1][6], state[1][7], state[1][8] = \
    BackState[1][4], BackState[1][1], BackState[1][2], BackState[1][3], BackState[1][8], BackState[1][5], BackState[1][6], BackState[1][7]
    state[2][1], state[2][2], state[2][6] = BackState[5][1], BackState[5][2], BackState[5][6]
    state[4][1], state[4][2], state[4][6] = BackState[0][1], BackState[0][2], BackState[0][6]
    state[5][1], state[5][2], state[5][6] = BackState[4][1], BackState[4][2], BackState[4][6]
    BackState = state.copy()
    state[0][1], state[0][2], state[0][6] = BackState[2][1], BackState[2][2], BackState[2][6]
    state[1][1], state[1][2], state[1][3], state[1][4], state[1][5], state[1][6], state[1][7], state[1][8] = \
    BackState[1][4], BackState[1][1], BackState[1][2], BackState[1][3], BackState[1][8], BackState[1][5], BackState[1][6], BackState[1][7]
    state[2][1], state[2][2], state[2][6] = BackState[5][1], BackState[5][2], BackState[5][6]
    state[4][1], state[4][2], state[4][6] = BackState[0][1], BackState[0][2], BackState[0][6]
    state[5][1], state[5][2], state[5][6] = BackState[4][1], BackState[4][2], BackState[4][6]
    return state

"""青面Bの左右の動き"""
def BL(state):
    BackState = state.copy()
    state[0][2], state[0][3], state[0][7] = BackState[3][2], BackState[3][3], BackState[3][7]
    state[1][2], state[1][3], state[1][7] = BackState[0][2], BackState[0][3], BackState[0][7]
    state[2][1], state[2][2], state[2][3], state[2][4], state[2][5], state[2][6], state[2][7], state[2][8] = \
    BackState[2][4], BackState[2][1], BackState[2][2], BackState[2][3], BackState[2][8], BackState[2][5], BackState[2][6], BackState[2][7]
    state[3][2], state[3][3], state[3][7] = BackState[5][4], BackState[5][1], BackState[5][5]
    state[5][1], state[5][4], state[5][5] = BackState[1][3], BackState[1][2], BackState[1][7]
    return state

def BR(state):
    BackState = state.copy()
    state[0][2], state[0][3], state[0][7] = BackState[1][2], BackState[1][3], BackState[1][7]
    state[1][2], state[1][3], state[1][7] = BackState[5][4], BackState[5][1], BackState[5][5]
    state[2][1], state[2][2], state[2][3], state[2][4], state[2][5], state[2][6], state[2][7], state[2][8] = \
    BackState[2][2], BackState[2][3], BackState[2][4], BackState[2][1], BackState[2][6], BackState[2][7], BackState[2][8], BackState[2][5]
    state[3][2], state[3][3], state[3][7] = BackState[0][2], BackState[0][3], BackState[0][7]
    state[5][1], state[5][4], state[5][5] = BackState[3][3], BackState[3][2], BackState[3][7]
    return state

def B2(state):
    BackState = state.copy()
    state[0][2], state[0][3], state[0][7] = BackState[3][2], BackState[3][3], BackState[3][7]
    state[1][2], state[1][3], state[1][7] = BackState[0][2], BackState[0][3], BackState[0][7]
    state[2][1], state[2][2], state[2][3], state[2][4], state[2][5], state[2][6], state[2][7], state[2][8] = \
    BackState[2][4], BackState[2][1], BackState[2][2], BackState[2][3], BackState[2][8], BackState[2][5], BackState[2][6], BackState[2][7]
    state[3][2], state[3][3], state[3][7] = BackState[5][4], BackState[5][1], BackState[5][5]
    state[5][1], state[5][4], state[5][5] = BackState[1][3], BackState[1][2], BackState[1][7]
    BackState = state.copy()
    state[0][2], state[0][3], state[0][7] = BackState[3][2], BackState[3][3], BackState[3][7]
    state[1][2], state[1][3], state[1][7] = BackState[0][2], BackState[0][3], BackState[0][7]
    state[2][1], state[2][2], state[2][3], state[2][4], state[2][5], state[2][6], state[2][7], state[2][8] = \
    BackState[2][4], BackState[2][1], BackState[2][2], BackState[2][3], BackState[2][8], BackState[2][5], BackState[2][6], BackState[2][7]
    state[3][2], state[3][3], state[3][7] = BackState[5][4], BackState[5][1], BackState[5][5]
    state[5][1], state[5][4], state[5][5] = BackState[1][3], BackState[1][2], BackState[1][7]
    return state

"""オレンジ面Oの左右の動き"""
def OL(state):
    BackState = state.copy()
    state[0][3], state[0][4], state[0][8] = BackState[4][3], BackState[4][4], BackState[4][8]
    state[2][3], state[2][4], state[2][8] = BackState[0][3], BackState[0][4], BackState[0][8]
    state[3][1], state[3][2], state[3][3], state[3][4], state[3][5], state[3][6], state[3][7], state[3][8] = \
    BackState[3][4], BackState[3][1], BackState[3][2], BackState[3][3], BackState[3][8], BackState[3][5], BackState[3][6], BackState[3][7]
    state[4][3], state[4][4], state[4][8] = BackState[5][3], BackState[5][4], BackState[5][8]
    state[5][3], state[5][4], state[5][8] = BackState[2][3], BackState[2][4], BackState[2][8]
    return state

def OR(state):
    BackState = state.copy()
    state[0][3], state[0][4], state[0][8] = BackState[2][3], BackState[2][4], BackState[2][8]
    state[2][3], state[2][4], state[2][8] = BackState[5][3], BackState[5][4], BackState[5][8]
    state[3][1], state[3][2], state[3][3], state[3][4], state[3][5], state[3][6], state[3][7], state[3][8] = \
    BackState[3][2], BackState[3][3], BackState[3][4], BackState[3][1], BackState[3][6], BackState[3][7], BackState[3][8], BackState[3][5]
    state[4][3], state[4][4], state[4][8] = BackState[0][3], BackState[0][4], BackState[0][8]
    state[5][3], state[5][4], state[5][8] = BackState[4][3], BackState[4][4], BackState[4][8]
    return state

def O2(state):
    BackState = state.copy()
    state[0][3], state[0][4], state[0][8] = BackState[4][3], BackState[4][4], BackState[4][8]
    state[2][3], state[2][4], state[2][8] = BackState[0][3], BackState[0][4], BackState[0][8]
    state[3][1], state[3][2], state[3][3], state[3][4], state[3][5], state[3][6], state[3][7], state[3][8] = \
    BackState[3][4], BackState[3][1], BackState[3][2], BackState[3][3], BackState[3][8], BackState[3][5], BackState[3][6], BackState[3][7]
    state[4][3], state[4][4], state[4][8] = BackState[5][3], BackState[5][4], BackState[5][8]
    state[5][3], state[5][4], state[5][8] = BackState[2][3], BackState[2][4], BackState[2][8]
    BackState = state.copy()
    state[0][3], state[0][4], state[0][8] = BackState[4][3], BackState[4][4], BackState[4][8]
    state[2][3], state[2][4], state[2][8] = BackState[0][3], BackState[0][4], BackState[0][8]
    state[3][1], state[3][2], state[3][3], state[3][4], state[3][5], state[3][6], state[3][7], state[3][8] = \
    BackState[3][4], BackState[3][1], BackState[3][2], BackState[3][3], BackState[3][8], BackState[3][5], BackState[3][6], BackState[3][7]
    state[4][3], state[4][4], state[4][8] = BackState[5][3], BackState[5][4], BackState[5][8]
    state[5][3], state[5][4], state[5][8] = BackState[2][3], BackState[2][4], BackState[2][8]
    return state

"""緑面Gの左右の動き"""
def GL(state):
    BackState = state.copy()
    state[0][1], state[0][4], state[0][5] = BackState[1][1], BackState[1][4], BackState[1][5]
    state[1][1], state[1][4], state[1][5] = BackState[5][3], BackState[5][2], BackState[5][7]
    state[3][1], state[3][4], state[3][5] = BackState[0][1], BackState[0][4], BackState[0][5]
    state[4][1], state[4][2], state[4][3], state[4][4], state[4][5], state[4][6], state[4][7], state[4][8] = \
    BackState[4][4], BackState[4][1], BackState[4][2], BackState[4][3], BackState[4][8], BackState[4][5], BackState[4][6], BackState[4][7]
    state[5][2], state[5][3], state[5][7] = BackState[3][4], BackState[3][1], BackState[3][5]
    return state

def GR(state):
    BackState = state.copy()
    state[0][1], state[0][4], state[0][5] = BackState[3][1], BackState[3][4], BackState[3][5]
    state[1][1], state[1][4], state[1][5] = BackState[0][1], BackState[0][4], BackState[0][5]
    state[3][1], state[3][4], state[3][5] = BackState[5][3], BackState[5][2], BackState[5][7]
    state[4][1], state[4][2], state[4][3], state[4][4], state[4][5], state[4][6], state[4][7], state[4][8] = \
    BackState[4][2], BackState[4][3], BackState[4][4], BackState[4][1], BackState[4][6], BackState[4][7], BackState[4][8], BackState[4][5]
    state[5][2], state[5][3], state[5][7] = BackState[1][4], BackState[1][1], BackState[1][5]
    return state

def G2(state):
    BackState = state.copy()
    state[0][1], state[0][4], state[0][5] = BackState[1][1], BackState[1][4], BackState[1][5]
    state[1][1], state[1][4], state[1][5] = BackState[5][3], BackState[5][2], BackState[5][7]
    state[3][1], state[3][4], state[3][5] = BackState[0][1], BackState[0][4], BackState[0][5]
    state[4][1], state[4][2], state[4][3], state[4][4], state[4][5], state[4][6], state[4][7], state[4][8] = \
    BackState[4][4], BackState[4][1], BackState[4][2], BackState[4][3], BackState[4][8], BackState[4][5], BackState[4][6], BackState[4][7]
    state[5][2], state[5][3], state[5][7] = BackState[3][4], BackState[3][1], BackState[3][5]
    BackState = state.copy()
    state[0][1], state[0][4], state[0][5] = BackState[1][1], BackState[1][4], BackState[1][5]
    state[1][1], state[1][4], state[1][5] = BackState[5][3], BackState[5][2], BackState[5][7]
    state[3][1], state[3][4], state[3][5] = BackState[0][1], BackState[0][4], BackState[0][5]
    state[4][1], state[4][2], state[4][3], state[4][4], state[4][5], state[4][6], state[4][7], state[4][8] = \
    BackState[4][4], BackState[4][1], BackState[4][2], BackState[4][3], BackState[4][8], BackState[4][5], BackState[4][6], BackState[4][7]
    state[5][2], state[5][3], state[5][7] = BackState[3][4], BackState[3][1], BackState[3][5]
    return state

"""黄色面Yの左右の動き"""
def YL(state):
    BackState = state.copy()
    state[1][1], state[1][2], state[1][6] = BackState[2][2], BackState[2][3], BackState[2][7]
    state[2][2], state[2][3], state[2][7] = BackState[3][3], BackState[3][4], BackState[3][8]
    state[3][3], state[3][4], state[3][8] = BackState[4][4], BackState[4][1], BackState[4][5]
    state[4][1], state[4][4], state[4][5] = BackState[1][2], BackState[1][1], BackState[1][6]
    state[5][1], state[5][2], state[5][3], state[5][4], state[5][5], state[5][6], state[5][7], state[5][8] = \
    BackState[5][4], BackState[5][1], BackState[5][2], BackState[5][3], BackState[5][8], BackState[5][5], BackState[5][6], BackState[5][7]
    return state

def YR(state):
    BackState = state.copy()
    state[1][1], state[1][2], state[1][6] = BackState[4][4], BackState[4][1], BackState[4][5]
    state[2][2], state[2][3], state[2][7] = BackState[1][1], BackState[1][2], BackState[1][6]
    state[3][3], state[3][4], state[3][8] = BackState[2][2], BackState[2][3], BackState[2][7]
    state[4][1], state[4][4], state[4][5] = BackState[3][4], BackState[3][3], BackState[3][8]
    state[5][1], state[5][2], state[5][3], state[5][4], state[5][5], state[5][6], state[5][7], state[5][8] = \
    BackState[5][2], BackState[5][3], BackState[5][4], BackState[5][1], BackState[5][6], BackState[5][7], BackState[5][8], BackState[5][5]
    return state

def Y2(state):
    BackState = state.copy()
    state[1][1], state[1][2], state[1][6] = BackState[2][2], BackState[2][3], BackState[2][7]
    state[2][2], state[2][3], state[2][7] = BackState[3][3], BackState[3][4], BackState[3][8]
    state[3][3], state[3][4], state[3][8] = BackState[4][4], BackState[4][1], BackState[4][5]
    state[4][1], state[4][4], state[4][5] = BackState[1][2], BackState[1][1], BackState[1][6]
    state[5][1], state[5][2], state[5][3], state[5][4], state[5][5], state[5][6], state[5][7], state[5][8] = \
    BackState[5][4], BackState[5][1], BackState[5][2], BackState[5][3], BackState[5][8], BackState[5][5], BackState[5][6], BackState[5][7]
    BackState = state.copy()
    state[1][1], state[1][2], state[1][6] = BackState[2][2], BackState[2][3], BackState[2][7]
    state[2][2], state[2][3], state[2][7] = BackState[3][3], BackState[3][4], BackState[3][8]
    state[3][3], state[3][4], state[3][8] = BackState[4][4], BackState[4][1], BackState[4][5]
    state[4][1], state[4][4], state[4][5] = BackState[1][2], BackState[1][1], BackState[1][6]
    state[5][1], state[5][2], state[5][3], state[5][4], state[5][5], state[5][6], state[5][7], state[5][8] = \
    BackState[5][4], BackState[5][1], BackState[5][2], BackState[5][3], BackState[5][8], BackState[5][5], BackState[5][6], BackState[5][7]
    return state

def MultipleMove(state, MoveList):
    moves = {
    "WL": WL, "WR": WR, "W2": W2,
    "RL": RL, "RR": RR, "R2": R2,
    "BL": BL, "BR": BR, "B2": B2,
    "OL": OL, "OR": OR, "O2": O2,
    "GL": GL, "GR": GR, "G2": G2,
    "YL": YL, "YR": YR, "Y2": Y2
    }
    for move in MoveList:
        if move in moves:
            state = moves[move](state)
        else:
            print("MoveList Spelling Error")
    return state

"""R, B, O, G各面の左右セクシームーブ2*4通り"""
def RedLeftSexyMove(state):
    MoveList = ["BL", "YL", "BR", "YL", "BL", "YL", "YL", "BR"]
    MultipleMove(state, MoveList)
    return state

def RedRightSexyMove(state):
    MoveList = ["GR", "YR", "GL", "YR", "GR", "YR", "YR", "GL"]
    MultipleMove(state, MoveList)
    return state

def BlueLeftSexyMove(state):
    MoveList = ["OL", "YL", "OR", "YL", "OL", "YL", "YL", "OR"]
    MultipleMove(state, MoveList)
    return state

def BlueRightSexyMove(state):
    MoveList = ["RR", "YR", "RL", "YR", "RR", "YR", "YR", "RL"]
    MultipleMove(state, MoveList)
    return state

def OrangeLeftSexyMove(state):
    MoveList = ["GL", "YL", "GR", "YL", "GL", "YL", "YL", "GR"]
    MultipleMove(state, MoveList)
    return state

def OrangeRightSexyMove(state):
    MoveList = ["BR", "YR", "BL", "YR", "BR", "YR", "YR", "BL"]
    MultipleMove(state, MoveList)
    return state

def GreenLeftSexyMove(state):
    MoveList = ["RL", "YL", "RR", "YL", "RL", "YL", "YL", "RR"]
    MultipleMove(state, MoveList)
    return state

def GreenRightSexyMove(state):
    MoveList = ["OR", "YR", "OL", "YR", "OR", "YR", "YR", "OL"]
    MultipleMove(state, MoveList)
    return state

"""セクシームーブなども含めたmove用関数"""
def MoveSet(state, MoveList):
    moves = {
            "WL": WL, "WR": WR, "W2": W2,
            "RL": RL, "RR": RR, "R2": R2,
            "BL": BL, "BR": BR, "B2": B2,
            "OL": OL, "OR": OR, "O2": O2,
            "GL": GL, "GR": GR, "G2": G2,
            "YL": YL, "YR": YR, "Y2": Y2,
            "RedLeftSexyMove": RedLeftSexyMove,
            "RedRightSexyMove": RedRightSexyMove,
            "BlueLeftSexyMove": BlueLeftSexyMove,
            "BlueRightSexyMove": BlueRightSexyMove,
            "OrangeLeftSexyMove": OrangeLeftSexyMove,
            "OrangeRightSexyMove": OrangeRightSexyMove,
            "GreenLeftSexyMove": GreenLeftSexyMove,
    }
     
    for move in MoveList:
        if move in moves:
            state = moves[move](state)
        else:
            print("MoveList Spelling Error")
    return state

"""ステップ1白のクロスを作る"""
def WhiteCross(state):
    """06ピースを揃える"""
    MoveList = []
    
    if state[0][5] == 6: 
        MoveList = ["WL"]
    if state[0][7] == 6:
        MoveList = ["WR"]
    if state[0][8] == 6:
        MoveList = ["W2"]
        
    if state[1][5] == 6:
        MoveList = ["GL", "WL"]
    if state[1][6] == 6:
        MoveList = ["RR", "GL", "WL"]
    if state[1][7] == 6:
        MoveList = ["R2", "GL", "WL"] 
    if state[1][8] == 6:
        MoveList = ["RL", "GL", "WL"]
        
    if state[2][5] == 6:
        MoveList = ["BL", "RL"]
    if state[2][6] == 6:
        MoveList = ["RL"]
    if state[2][7] == 6:
        MoveList = ["BR", "RL"]
    if state[2][8] == 6:
        MoveList = ["B2", "RL"]
        
    if state[3][5] == 6:
        MoveList = ["GR", "WL"] 
    if state[3][6] == 6:
        MoveList = ["OR", "GR", "WL"]   
    if state[3][7] == 6:
        MoveList = ["O2", "GR", "WL"]
    if state[3][8] == 6:
        MoveList = ["OL", "GR", "WL"]
        
    if state[4][5] == 6:
        MoveList = ["GL", "RR"] 
    if state[4][6] == 6:
        MoveList = ["RR"] 
    if state[4][7] == 6:
        MoveList = ["GR", "RR"] 
    if state[4][8] == 6:
        MoveList = ["G2", "RR"]
        
    if state[5][5] == 6:
        MoveList = ["YL", "R2"] 
    if state[5][6] == 6:
        MoveList = ["R2"] 
    if state[5][7] == 6:
        MoveList = ["YR", "R2"] 
    if state[5][8] == 6:
        MoveList = ["Y2", "R2"]
#     stateの更新
    print(MoveList)
    state = MoveSet(state, MoveList)
    
    """07ピースを揃える"""
    MoveList = []
    
    if state[0][5] == 7: 
        MoveList = ["G2", "Y2", "B2"]
    if state[0][8] == 7: 
        MoveList = ["O2", "YL", "B2"]
        
    if state[1][5] == 7: 
        MoveList = ["GR", "Y2", "B2"]
    if state[1][6] == 7: 
        MoveList = ["RL", "BR", "RR"]
    if state[1][7] == 7: 
        MoveList = ["BR"]

    if state[2][5] == 7: 
        MoveList = ["BL", "RR", "YR", "RL", "B2"]
    if state[2][6] == 7: 
        MoveList = ["RR", "YR", "RL", "B2"]
    if state[2][7] == 7: 
        MoveList = ["BR", "RR", "YR", "RL", "B2"]
    if state[2][8] == 7: 
        MoveList = ["B2", "RR", "YR", "RL", "B2"]
  
    if state[3][5] == 7: 
        MoveList = ["O2", "BL"]
    if state[3][6] == 7: 
        MoveList = ["OL", "BL"]
    if state[3][7] == 7: 
        MoveList = ["BL"]
    if state[3][8] == 7: 
        MoveList = ["OR", "BL"]

    if state[4][5] == 7: 
        MoveList = ["GR", "OR", "YL", "B2"]
    if state[4][6] == 7: 
        MoveList = ["G2", "OR", "YL", "B2"]
    if state[4][7] == 7: 
        MoveList = ["GL", "OR", "YL", "B2"]
    if state[4][8] == 7: 
        MoveList = ["OR", "YL", "B2"]
        
    if state[5][5] == 7: 
        MoveList = ["B2"]
    if state[5][6] == 7: 
        MoveList = ["YR", "B2"]
    if state[5][7] == 7: 
        MoveList = ["Y2", "B2"]
    if state[5][8] == 7: 
        MoveList = ["YL", "B2"]
#     stateの更新
    print(MoveList)
    state = MoveSet(state, MoveList)
    
    """08ピースを揃える"""
    MoveList = []
    
    if state[0][5] == 8: 
        MoveList = ["G2", "YL", "O2"]

    if state[1][5] == 8: 
        MoveList = ["GR", "YL", "O2"]
    if state[1][6] == 8: 
        MoveList = ["RR", "GR", "RL", "YL", "O2"]
    if state[1][7] == 8: 
        MoveList = ["R2", "GR", "R2", "YL", "O2"]
  
    if state[2][6] == 8: 
        MoveList = ["B2", "OR", "B2"]
    if state[2][7] == 8: 
        MoveList = ["BL", "OR", "BR"]
    if state[2][8] == 8: 
        MoveList = ["OR"]

    if state[3][5] == 8: 
        MoveList = ["GL", "YL", "O2"] 
    if state[3][6] == 8: 
        MoveList = ["OR", "GL", "YL", "O2"]
    if state[3][7] == 8: 
        MoveList = ["O2", "GL", "YL", "O2"] 
    if state[3][8] == 8: 
        MoveList = ["OL", "GL", "YL", "O2"]
        
    if state[4][5] == 8:
        MoveList = ["GR", "OL"] 
    if state[4][6] == 8: 
        MoveList = ["G2", "OL"]
    if state[4][7] == 8: 
        MoveList = ["GL", "OL"]        
    if state[4][8] == 8: 
        MoveList = ["OL"]
        
    if state[5][5] == 8: 
        MoveList = ["YR", "O2"] 
    if state[5][6] == 8: 
        MoveList = ["Y2", "O2"] 
    if state[5][7] == 8: 
        MoveList = ["YL", "O2"] 
    if state[5][8] == 8: 
        MoveList = ["O2"]
#     stateの更新
    state = MoveSet(state, MoveList)
    print(MoveList)
    
    """09ピースを揃える"""    
    MoveList = []
    
    if state[1][5] == 5: 
        MoveList = ["GL"]
    if state[1][6] == 5: 
        MoveList = ["RR", "GL", "RL"]
    if state[1][7] == 5: 
        MoveList = ["R2", "GL", "R2"]

    if state[2][6] == 5: 
        MoveList = ["RR", "YL", "RL", "G2"]
    if state[2][7] == 5: 
        MoveList = ["BR", "RR", "YL", "RL", "BL", "G2"]
    if state[2][8] == 5: 
        MoveList = ["OL", "YR", "OR", "G2"]

    if state[3][5] == 5: 
        MoveList = ["GR"]
    if state[3][7] == 5: 
        MoveList = ["O2", "GR", "O2"]
    if state[3][8] == 5: 
        MoveList = ["OL", "GR", "OR"]
        
    if state[4][5] == 5: 
        MoveList = ["GL", "RL", "YL", "RR", "G2"]
    if state[4][6] == 5: 
        MoveList = ["RL", "YL", "RR", "G2"]
    if state[4][7] == 5: 
        MoveList = ["GR", "RL", "YL", "RR", "G2"]
    if state[4][8] == 5: 
        MoveList = ["G2", "RL", "YL", "RR", "G2"]
    
    if state[5][5] == 5: 
        MoveList = ["Y2", "G2"]
    if state[5][6] == 5: 
        MoveList = ["YL", "G2"]
    if state[5][7] == 5: 
        MoveList = ["G2"]
    if state[5][8] == 5: 
        MoveList = ["YR", "G2"]        
    #     stateの更新
    print(MoveList)
    state = MoveSet(state, MoveList)
    
    return state

"""シャッフル"""
def ShuffleState():
    SolvedState = np.array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
                        [10, 11, 12, 13, 14, 15, 16, 17, 18],
                        [20, 21, 22, 23, 24, 25, 26, 27, 28],
                        [30, 31, 32, 33, 34, 35, 36, 37, 38],
                        [40, 41, 42, 43, 44, 45, 46, 47, 48],
                        [50, 51, 52, 53, 54, 55, 56, 57, 58]
                       ])
    moves = ["WL", "WR", "W2", "RL", "RR", "R2", "BL", "BR", "B2", "OL", "OR", "O2", "GL", "GR", "G2", "YL", "YR", "Y2"]
    MoveList = random.choices(moves, k=30)
    state = MoveSet(SolvedState, MoveList)
    return state

"""展開図"""
def DevelopedView(state):
    plt.rcParams["figure.figsize"] = (12, 9)
    plt.rcParams["font.family"] = "Arial"

    ColorList = ["lightgray", "red", "skyblue", "orange", "limegreen", "y"]
    FaceLocationList = np.array([[9, 9], [9, 15], [3, 9], [9, 3], [15, 9], [21, 9]])
    PeaceLocationList = np.array([[0, 0], [2, 2], [-2, 2], [-2, -2], [2, -2], [2, 0], [0, 2], [-2, 0], [0, -2]])
    for j in range(6):
        FaceLocation = FaceLocationList[j]
        for i in range(9):
            ColorResult = math.floor(state[j][i] / 10)
            color = ColorList[ColorResult]
            PeaceLocation = PeaceLocationList[i]
            location = FaceLocation + PeaceLocation
            plt.scatter(location[0], location[1], s=1000, color=color, marker=",")
            plt.text(location[0]-0.4, location[1]+0.1, f"[{j}{i}]", fontsize = 15)
            plt.text(location[0]-0.2, location[1]-0.4, state[j][i])

    plt.xlim(0, 24)
    plt.ylim(0, 18)
    plt.xticks(np.linspace(0, 24, 5))
    plt.yticks(np.linspace(0, 18, 4))
    plt.xticks()
    plt.grid(linestyle = "dashed")
    plt.show()

filename = 'populationdata.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)

state = ShuffleState()
state = WhiteCross(state)
DevelopedView(state)