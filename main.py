import random

from mutants import base, m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19
import math

import unittest


def make_maze(w=30, h=30):
    """returns an ascii maze as a string"""
    # from random import shuffle, randrange
    # random.seed(2)
    # vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    # ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    # hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    #
    # def walk(x, y):
    #     vis[y][x] = 1
    #
    #     d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    #     shuffle(d)
    #     for (xx, yy) in d:
    #         if vis[yy][xx]:
    #             continue
    #         if xx == x:
    #             hor[max(y, yy)][x] = "+  "
    #         if yy == y:
    #             ver[y][max(x, xx)] = "   "
    #         walk(xx, yy)
    #
    # walk(randrange(w), randrange(h))
    # result = ''
    # for (a, b) in zip(hor, ver):
    #     result = result + (''.join(a + ['\n'] + b)) + '\n'
    # return result.strip()

    mazes = ['', '', '']

    mazes[0]  = '+--+--+--+--+--+--+--+--+--+--+\n'
    mazes[0] += '|        |        |           |\n'
    mazes[0] += '+--+  +  +  +--+  +  +  +--+  +\n'
    mazes[0] += '|  |  |  |  |  |     |  |  |  |\n'
    mazes[0] += '+  +  +  +  +  +--+--+  +  +  +\n'
    mazes[0] += '|     |                 |     |\n'
    mazes[0] += '+  +--+--+--+  +--+  +--+--+--+\n'
    mazes[0] += '|  |              |           |\n'
    mazes[0] += '+  +--+  +  +--+  +--+--+--+  +\n'
    mazes[0] += '|        |                    |\n'
    mazes[0] += '+--+--+--+--+--+--+--+--+--+--+'

    mazes[1]  = '+--+--+--+--+--+--+--+--+--+--+\n'
    mazes[1] += '|        |        |           |\n'
    mazes[1] += '+--+  +  +--+--+  +  +--+  +  +\n'
    mazes[1] += '|     |  |        |  |     |  |\n'
    mazes[1] += '+--+--+  +  +--+--+  +  +--+  +\n'
    mazes[1] += '|     |  |        |  |  |     |\n'
    mazes[1] += '+  +--+  +--+--+  +  +  +  +--+\n'
    mazes[1] += '|              |     |  |  |  |\n'
    mazes[1] += '+  +--+--+  +  +  +--+  +  +  +\n'
    mazes[1] += '|     |     |  |  |     |     |\n'
    mazes[1] += '+--+  +--+  +  +--+  +--+--+  +\n'
    mazes[1] += '|     |     |        |     |  |\n'
    mazes[1] += '+  +--+  +--+--+  +--+  +  +  +\n'
    mazes[1] += '|     |  |        |     |  |  |\n'
    mazes[1] += '+--+  +  +--+  +  +  +  +  +  +\n'
    mazes[1] += '|     |        |  |  |  |  |  |\n'
    mazes[1] += '+  +--+--+  +  +  +  +  +--+  +\n'
    mazes[1] += '|  |     |  |  |     |  |     |\n'
    mazes[1] += '+  +  +  +  +  +--+--+  +  +--+\n'
    mazes[1] += '|           |                 |\n'
    mazes[1] += '+--+--+--+--+--+--+--+--+--+--+'
    
    mazes[2]  = '+--+--+--+--+--+--+--+\n'
    mazes[2] += '|                 |  |\n'
    mazes[2] += '+--+--+--+--+  +--+  +\n'
    mazes[2] += '|                    |\n'
    mazes[2] += '+  +--+--+--+  +  +--+\n'
    mazes[2] += '|        |     |  |  |\n'
    mazes[2] += '+  +--+  +--+--+  +  +\n'
    mazes[2] += '|  |     |        |  |\n'
    mazes[2] += '+  +  +--+  +--+--+  +\n'
    mazes[2] += '|  |                 |\n'
    mazes[2] += '+--+--+--+--+--+--+--+'

    return mazes


def drawmaze(maze, set1=[], set2=[], c='#', c2='*'):
    """returns an ascii maze, drawing eventually one (or 2) sets of positions.
        useful to draw the solution found by the astar algorithm
    """
    set1 = list(set1)
    set2 = list(set2)
    lines = maze.strip().split('\n')
    width = len(lines[0])
    height = len(lines)
    result = ''
    for j in range(height):
        for i in range(width):
            if (i, j) in set1:
                result = result + c
            elif (i, j) in set2:
                result = result + c2
            else:
                result = result + lines[j][i]
        result = result + '\n'
    return result


# def solve_maze(mr):
#     # generate an ascii maze
#     size = 20
#     m = make_maze(10, 5)
#
#     # what is the size of it?
#     w = len(m.split('\n')[0])
#     h = len(m.split('\n'))
#
#     if mr == "base":
#         start = (1, 1)  # we choose to start at the upper left corner
#         goal = (w - 2, h - 2)  # we want to reach the lower right corner
#     if mr == "MR-1":
#         start = (w - 2, h - 2)
#         goal = (1, 1)
#     if mr == "MR-2":
#         start = (8, 5)
#         goal = (w - 2, h - 2)
#
#     # let's solve it
#     # foundPath = list(base.MazeSolver(m).astar(start, goal))
#
#     return drawmaze(m, list(foundPath))


# class MazeTests(unittest.TestCase):
#     def test_solve_maze(self):
#         solve_maze()

def is_sublist(A, B):
    if not A:
        return True
    if not B:
        return False
    if A[0] == B[0]:
        return is_sublist(A[1:], B[1:])
    return is_sublist(A, B[1:])


def solve_maze(name, mazes, si, fi, module):
    results = []

    for i in range(0, len(mazes)):
        source_path = list(module.MazeSolver(mazes[i]).astar(si.start[i], si.goal[i]))

        if fi.type == "contains":
            followup_path = list(module.MazeSolver(mazes[i]).astar(source_path[round(len(source_path) / 2)], fi.goal[i]))
            if is_sublist(followup_path, source_path):
                results.append(0)
            else:
                results.append(1)

        elif fi.type == "length":
            followup_path = list(module.MazeSolver(mazes[i]).astar(fi.start[i], fi.goal[i]))
            if len(source_path) == len(followup_path):
                results.append(0)
            else:
                results.append(1)

        # print(drawmaze(mazes[i], list(followup_path)))

    outcome = 1 if sum(results) > 0 else 0
    if outcome == 1:
        print(f"{name}: FAIL ({results})")
    else:
        print(f"{name}: PASS ({results})")
    return outcome


# Types: Compare bottom, compare length
class Input(object):
    def __init__(self, start, goal, type=None):
        self.start = start
        self.goal = goal
        self.type = type


if __name__ == '__main__':
    m = make_maze()

    print("Test")

    si = Input([(1, 1), (1, 1), (1, 1)], [(29, 9), (29, 19), (20, 9)])
    fi_1 = Input([(29, 9), (29, 19), (20, 9)], [(1, 1), (1, 1), (1, 1)], "length")
    fi_2 = Input([(None, None), (None, None), (None, None)], [(29, 9), (29, 19), (20, 9)], "contains")
    # fi_2 = Input([(8, 5), (14, 10), (13, 3)], [(29, 9), (29, 19), (20, 9)], "contains")

    # Print solved mazes to ensure base program is working correctly
    for i in range(0, len(m)):
        path = list(base.MazeSolver(m[i]).astar(si.start[i], si.goal[i]))
        print(drawmaze(m[i], list(path)))

    # MR1
    print("MR-1")
    score = 0
    score += solve_maze("MR-1 - control", m, si, fi_1, base)
    score += solve_maze("MR-1 - m00", m, si, fi_1, m0)
    score += solve_maze("MR-1 - m01", m, si, fi_1, m1)
    score += solve_maze("MR-1 - m02", m, si, fi_1, m2)
    score += solve_maze("MR-1 - m03", m, si, fi_1, m3)
    score += solve_maze("MR-1 - m04", m, si, fi_1, m4)
    score += solve_maze("MR-1 - m05", m, si, fi_1, m5)
    score += solve_maze("MR-1 - m06", m, si, fi_1, m6)
    score += solve_maze("MR-1 - m07", m, si, fi_1, m7)
    score += solve_maze("MR-1 - m08", m, si, fi_1, m8)
    score += solve_maze("MR-1 - m09", m, si, fi_1, m9)
    score += solve_maze("MR-1 - m10", m, si, fi_1, m10)
    score += solve_maze("MR-1 - m11", m, si, fi_1, m11)
    score += solve_maze("MR-1 - m12", m, si, fi_1, m12)
    score += solve_maze("MR-1 - m13", m, si, fi_1, m13)
    score += solve_maze("MR-1 - m14", m, si, fi_1, m14)
    score += solve_maze("MR-1 - m15", m, si, fi_1, m15)
    score += solve_maze("MR-1 - m16", m, si, fi_1, m16)
    score += solve_maze("MR-1 - m17", m, si, fi_1, m17)
    score += solve_maze("MR-1 - m18", m, si, fi_1, m18)
    score += solve_maze("MR-1 - m19", m, si, fi_1, m19)

    print(f"MR1: {score}/20 = {score/20 * 100}%")

    # MR2
    print("\nMR-2")
    score = 0
    score += solve_maze("MR-2 - control", m, si, fi_2, base)
    score += solve_maze("MR-2 - m00", m, si, fi_2, m0)
    score += solve_maze("MR-2 - m01", m, si, fi_2, m1)
    score += solve_maze("MR-2 - m02", m, si, fi_2, m2)
    score += solve_maze("MR-2 - m03", m, si, fi_2, m3)
    score += solve_maze("MR-2 - m04", m, si, fi_2, m4)
    score += solve_maze("MR-2 - m05", m, si, fi_2, m5)
    score += solve_maze("MR-2 - m06", m, si, fi_2, m6)
    score += solve_maze("MR-2 - m07", m, si, fi_2, m7)
    score += solve_maze("MR-2 - m08", m, si, fi_2, m8)
    score += solve_maze("MR-2 - m09", m, si, fi_2, m9)
    score += solve_maze("MR-2 - m10", m, si, fi_2, m10)
    score += solve_maze("MR-2 - m11", m, si, fi_2, m11)
    score += solve_maze("MR-2 - m12", m, si, fi_2, m12)
    score += solve_maze("MR-2 - m13", m, si, fi_2, m13)
    score += solve_maze("MR-2 - m14", m, si, fi_2, m14)
    score += solve_maze("MR-2 - m15", m, si, fi_2, m15)
    score += solve_maze("MR-2 - m16", m, si, fi_2, m16)
    score += solve_maze("MR-2 - m17", m, si, fi_2, m17)
    score += solve_maze("MR-2 - m18", m, si, fi_2, m18)
    score += solve_maze("MR-2 - m19", m, si, fi_2, m19)

    print(f"MR2: {score}/20 = {score / 20 * 100}%")

