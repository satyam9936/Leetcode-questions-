# Knight Tour using Backtracking

def is_safe(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def knight_tour(x, y, move_count, board, move_x, move_y, N):

    # Base case → all squares visited
    if move_count == N * N:
        return True

    # Try all 8 possible knight moves
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if is_safe(next_x, next_y, board, N):
            board[next_x][next_y] = move_count

            if knight_tour(next_x, next_y, move_count + 1, board, move_x, move_y, N):
                return True

            # 🔴 BACKTRACK (very important)
            board[next_x][next_y] = -1

    return False


def solve_knight_tour(N):

    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Knight moves
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # start from (0,0)
    board[0][0] = 0

    if not knight_tour(0, 0, 1, board, move_x, move_y, N):
        print("No solution exists")
        return

    print_board(board)


def print_board(board):
    for row in board:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()


# Run
solve_knight_tour(8)
                



