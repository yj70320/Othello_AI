import copy
import random
import sys

from board_weight import BOARD_WEIGHT
from time_related import get_time

DEPTH = 5

DIRC = [
    [-1,  1,  0,  0,  -1,  -1,   1,   1 ],
    [ 0,  0,  1, -1,  -1,   1,   1,  -1 ],
    ['N','S','E','W','NW','NE','SE','SW']
]

N = int(input("Board Size, N = ")) # Board size
if N not in [4,6,8,10]:
    print("Board size can only be 4, 6, 8 or 10. Exiting...")
    sys.exit()  # 退出程序

def print_board(board_size, board):
    print("  ", sep="", end="")
    for i in range(board_size):
        print(i, sep="", end="")
        if i < board_size - 1 : print("|", sep="", end="") #
    print()      
    
    for i in range(board_size):
        print(str(i) + "|", sep="", end="")
        for j in range(board_size):
            print(board[i][j], sep="", end="")
            print("|", sep="", end="") #
        print(str(i))
    
    print("  ", sep="", end="")
    for i in range(board_size):
        print(i, sep="", end="")
        if i < board_size - 1 : print("|", sep="", end="") #
    print()

def check_directions(row_change, col_change, move, board_size, board, turn, opp):
    found_self = False
    r,c = move
    r += row_change
    c += col_change
    if r >= 0 and r < board_size and c >= 0 and c < board_size:
        if board[r][c] != opp:
            return False

    while (r >= 0 and r < board_size and c >= 0 and c < board_size) or (found_self):
        r += row_change
        c += col_change
        if r < 0 or r >= board_size or c < 0 or c >= board_size: break
        if board[r][c] == ' ':
            return False
        if board[r][c] == turn:
            found_self = True
            return True
    return False

def validate(move, board_size, board, turn, opp):
    direction = []
    
    for i in range(len(DIRC[1])):
        valid = check_directions(DIRC[0][i], DIRC[1][i], move, board_size, board, turn, opp)
        if valid: direction.append(DIRC[2][i])
    
    if len(direction) > 0: valid = True
    return valid, direction
    

def flip_stone(board_size, board, turn, dirs, move):
    for d in dirs:          
        if d in DIRC[2]:  # 确保方向有效
            i = DIRC[2].index(d)  # 获取方向在 DIRC[2] 中的索引            
            flip(board_size, board, turn, DIRC[0][i], DIRC[1][i], move)

def create_possible_moves(board_size, board, turn, opp):
    moves = [] 
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == ' ':
                move = (i, j)
                is_valid, direction = validate(move, board_size, board, turn, opp)
                if is_valid: moves.append((move, direction))

    return moves # moves format: ((i,j), ['ESWN'])

def flip(board_size, board, turn, row_change, col_change, move):
    r,c = move
    r += row_change
    c += col_change
    while r >= 0 and r < board_size and c >= 0 and c < board_size \
          and board[r][c] != turn:
        board[r][c] = turn
        r += row_change
        c += col_change

def play_move(board_size, board, turn, move, dirs):
    r,c = move
    board[r][c] = turn
    flip_stone(board_size, board, turn, dirs, move)

def get_random_move(board_size, board, turn):
    opp = 'B' if turn == 'W' else 'W'
    move_list = create_possible_moves(board_size, board, turn, opp)
    random_move = random.randint(0, len(move_list) - 1)
    move, dirs = move_list[random_move]
    return move, dirs

def generate_successors(board, moves, turn, opp):
    successors = []
    #print(moves)
    for m,d in moves:
        changed_board = copy.deepcopy(board)
        #print(m, d)
        play_move(len(board), changed_board, turn, m, d)
        successors.append((changed_board, m))
    return successors

def heuristic(board, turn, max_, move):
    # if move == 
    opp = 'B' if turn == 'W' else 'W'
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == turn:
                if max_:
                    count += 1
                else:
                    count -= 1
    r,c = move
    if max_:        
        count -= BOARD_WEIGHT[N][r][c]
    else:
        count += BOARD_WEIGHT[N][r][c]
    return count                    
        
def minimax(board_size, board, turn, best_MAX, best_MIN, depth, max_, move):
    opp = 'B' if turn == 'W' else 'W'
    moves = create_possible_moves(board_size, board, turn, opp)
    
    if depth >= DEPTH or len(moves) == 0:
        #print(heuristic(board, turn, max_, move))
        return (heuristic(board, turn, max_, move), None)
    else:
        depth += 1
        ret = -99
        s = generate_successors(board, moves, turn, opp)
        index = -1
        move = 0
        if max_:
            ret = -100
            count = 0
            for successor,action in s:
                count += 1
                index += 1
                v,m = minimax(board_size, successor, opp, ret, best_MIN, depth, False, action)
                # if first:
                #     print("Line 206: MAX V:", v)
                #     print("Line 207: CONSIDERED MOVE:", action)
                if v > ret:
                    ret = v
                    move = index
                    # if first:
                    #     print("MAX MOVE:", move, moves[move])
                    if ret > best_MIN:
                        return best_MIN, moves[move]
                        
        else:
            ret = 100
            count = 1
            for successor,action in s:
                count += 1
                index += 1
                v,m = minimax(board_size, successor, opp, best_MAX, ret, depth, True, action)
                if v < ret:
                    ret = v
                    move = index
                    if ret < best_MAX:
                        return best_MAX, moves[move]

        if move == None:
            return ret, None
        # print("Line 230, ret, moves: ",ret, moves)
        return ret, moves[move]

def get_AI_move(board_size, board, turn):
    n = board_size - 1
    corners = [(0,0), (0, n), (n, 0), (n, n)]
    opp = 'B' if turn == 'W' else 'W'
    moves = create_possible_moves(board_size, board, turn, opp)
    if moves == []:
        return (None, 0)
    for v,r in moves:
        if v in corners:
            return(v, r)
    move = minimax(board_size, board, turn, -1000, 1000, 0, True, (board_size//2, board_size//2))
    # print("Line 246: move ",move)
    _,move = move # delete the ret in move
    move,d = move
    # print("AI suggestion:", move, d)
    print("AI suggestion:", move)
    return move,d

def get_move(board_size, board, turn, time_left, opp_time_left):
    move, dirs = get_AI_move(board_size, board, turn)
    return move, dirs

def end_game(board_size, board):
    b_score = 0
    w_score = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'W': w_score += 1
            if board[i][j] == 'B': b_score += 1
    print("Player B scored:", b_score)
    print("Player W scored:", w_score)
    if b_score > w_score: print("Player B Wins!")
    elif w_score > b_score: print("Player W Wins!")
    else: print("It was a draw!!!")

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

board = [[' ' for x in range(N)] for x in range(N)] # Create board
board[(N-1)//2][(N-1)//2] = 'W'
board[(N)//2][(N)//2] = 'W'
board[(N-1)//2][(N)//2] = 'B'
board[(N)//2][(N-1)//2] = 'B'
print_board(N, board)

c = 0
while 1:
    t0 = get_time()
    w_moves = create_possible_moves(N, board, 'B', 'W')
    b_moves = create_possible_moves(N, board, 'W', 'B')
    if len(w_moves) == 0 and len(b_moves) == 0: break
    else:
        if c % 2 == 0 and len(w_moves) > 0:
            print("\nPlayer B's Turn")
            move, dirs = get_move(N, board, 'B', 0, 0)
            # print("move = ",move)
            # print("direction = ", dirs)
            
            play_move(N, board, 'B', move, dirs)
        elif len(b_moves) > 0:
            print("\nPlayer W's Turn")

            # # PVE
            # # move, dirs = get_random_move(N, board, 'W')
            # _, _ = get_move(N, board, 'W', 0, 0)
            # # print("length of move: ", len(move))
            # # move = input("move: ")#get_random_move(N, board, 'W')
            # user_input = input("row, column: ")
            # try:
            #     move = tuple(map(int, user_input.split(',')))
            # except ValueError:
            #     print("input error")
            # # print("length of move: ", len(move))
            # dirs = [input("direction, NSWE: ")]
            # # print("move: ", move)
            # # print("dirs: ", dirs)

            # EVE
            move, dirs = get_move(N, board, 'W', 0, 0)

            play_move(N, board, 'W', move, dirs)
        print_board(N, board)
        c += 1
        
end_game(N, board)



