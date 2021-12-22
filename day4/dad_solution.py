with open('input.txt', 'r') as f:
    numbers = f.readline()
    f.readline()

##
    boards = f.read().strip().split('\n\n')
new_boards = []
for board in boards:
    new_board = [int(i) for i in board.split() if i.isdigit()]
    new_boards.append(new_board)

