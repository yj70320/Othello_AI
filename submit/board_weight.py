BOARD_WEIGHT = [[[0 for _ in range(11)] for _ in range(11)] for _ in range(11)]
BOARD_WEIGHT[4] = [
                [+100, +10, +10, +100],
                [+10,    0,   0,  +10],
                [+10,    0,   0,  +10],
                [+100, +10, +10, +100]
            ]

BOARD_WEIGHT[6] = [
                [+100,  -20,  +10,  +10,  -20, +100],
                [ -20,  -50,   +5,   +5,  -50,  -20],
                [ +10,   +5,    0,    0,   +5,  +10],
                [ +10,   +5,    0,    0,   +5,  +10],
                [ -20,  -50,   +5,   +5,  -50,  -20],
                [+100,  -20,  +10,  +10,  -50, +100],
            ]

BOARD_WEIGHT[8] = [
                [+100, -20, +10, +5, +5, +10, -20, +100],
                [-20,  -50,  -2, -1, -1, -2,  -50,  -20],
                [+10,   +1,  +5, +4, +4, +5,   +1,  +10],
                [+5,    +2,  +4,  0,  0, +4,   +2,   +5],
                [+5,    +2,  +4,  0,  0, +4,   +2,   +5],
                [+10,   +1,  +5, +4, +4, +5,   +1,  +10],
                [-20,  -50,  -2, -1, -1, -2,  -50,  -20],
                [+100, -20, +10, +5, +5, +10, -20, +100],
            ]
BOARD_WEIGHT[10]  = [              
                
                [+100, -20, +15, +10, +5, +5, +10, +15, -20, +100],
                [-20,  -50,  -2,  -1, -1, -1,  -1,  -2, -50,  -20],
                [+15,   -2,  +3,  +2, +2, +2,  +2,  +3,  -2,  +15],
                [+10,   -1,  +2,  +1,  0,  0,  +1,  +2,  -1,  +10],
                [+5,    -1,  +2,   0,  0,  0,   0,  +2,  -1,   +5],
                [+5,    -1,  +2,   0,  0,  0,   0,  +2,  -1,   +5],
                [+10,   -2,  +3,  +2, +2, +2,  +2,  +3,  -2,  +10],
                [+15,   -2,  +3,  +2, +2, +2,  +2,  +3,  -2,  +15],
                [-20,  -50,  -2,  -1, -1, -1,  -1,  -2, -50,  -20],
                [+100, -20, +15, +10, +5, +5, +10, +15, -20, +100]


            ]
