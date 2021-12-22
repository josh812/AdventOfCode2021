with open('input.txt', 'r') as f:
    move_list = f.readline().replace('\n', '')
    move_list = move_list.split(',')

    for index in range(len(move_list)):
        move_list[index] = int(move_list[index])

    b = f.read().split('\n\n')

    for index in range(len(b)):
        b[index] = b[index].replace('\n', ' ')
        b[index] = b[index].replace('  ', ' ')

    b[0] = b[0][1:]

    b_list = []
    for board in b:
        b_list.append(board.split(' '))

    for board in b_list:
        for index in range(len(board)):
            try:
                board[index] = int(board[index])
            except ValueError:
                continue


class Board:
    def __init__(self, board):
        self.board = board
        self.status = [0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0]

    def checkWinner(self):
        j = 0
        for i in range(4):
            if self.status[j] == self.status[j+5] == self.status[j+10] == self.status[j+15] == self.status[j+20] == 1:
                return True

            if j == 0:
                j = 1
            elif j == 1:
                j = 2
            elif j == 2:
                j = 3
            elif j == 3:
                j = 4

        j = 0
        for i in range(4):
            if self.status[j] == self.status[j+1] == self.status[j+2] == self.status[j+3] == self.status[j+4] == 1:
                return True

            if j == 0:
                j = 5
            elif j == 5:
                j = 10
            elif j == 10:
                j = 15
            elif j == 15:
                j = 20


boards = []

for board in b_list:
    boards.append(Board(board))

for move in move_list:
    for board in boards:
        for index, number in enumerate(board.board):
            if number == move:
                board.status[index] = 1

        if board.checkWinner():
            win_board = board
            win_number = move
            break

    try:
        if win_board:
            break
    except NameError:
        continue

total = 0

for status_index, status in enumerate(win_board.status):
    for board_index, value in enumerate(win_board.board):
        if status_index == board_index and status_index != 1:
            total += value
total = total * win_number

print(win_board.board)
print(win_board.status)
print(win_number)
print(total)
