with open('input.txt', 'r') as f:
    move_list = f.readline().replace('\n', '').split(',')
    for index, move in enumerate(move_list):
        move_list[index] = int(move_list[index])

    f.readline()

    board_list = f.read().strip().split('\n\n')

boards = []
for board in board_list:
    new_board = [int(i) for i in board.split() if i.isdigit()]
    boards.append(new_board)


class Board:
    def __init__(self, board_numbers):
        self.board = board_numbers
        self.status = [0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0]

    def checkForWinner(self):
        for i in range(5):
            if self.status[i] == self.status[i+5] == self.status[i+10] == self.status[i+15] == self.status[i+20] == 1:
                return True

        for i in range(0, 21, 5):
            if self.status[i] == self.status[i+1] == self.status[i+2] == self.status[i+3] == self.status[i+4] == 1:
                return True


board_list = []

for board in boards:
    board_list.append(Board(board))

won = [False] * len(board_list)

for move in move_list:
    for i, board in enumerate(board_list):
        for index, number in enumerate(board.board):
            if number == move:
                board.status[index] = 1

            if board.checkForWinner():
                won[i] = True
                if all(won):
                    total = 0
                    for index, value in enumerate(board.board):
                        if board.status[index] != 1:
                            total += int(value)
                    total = total * move
                    print(total)
                    exit()
