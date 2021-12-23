with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for index, line in enumerate(lines):
        lines[index] = line.split(' -> ')
        for index_1, pair in enumerate(lines[index]):
            lines[index][index_1] = pair.split(',')
            for index_2, num in enumerate(lines[index][index_1]):
                lines[index][index_1][index_2] = int(num)


class Grid:
    def __init__(self, coordinate_pairs):
        self.coordinate_pairs = coordinate_pairs
        self.grid = []
        for i in range(1000):
            self.grid.append([])
        for row in self.grid:
            for i in range(1000):
                row.append(0)

    def mark_cell(self, x, y):
        self.grid[y][x] += 1

    def draw_line(self, x1, y1, x2, y2):
        if x1 == x2:
            if y1 > y2:
                self.mark_cell(x1, y1)
                for i in range((y1 - y2)):
                    self.mark_cell(x2, y2 + i)
            elif y2 > y1:
                self.mark_cell(x1, y1)
                for i in range((y2 - y1)):
                    self.mark_cell(x2, y2 - i)

        elif y1 == y2:
            if x1 > x2:
                self.mark_cell(x1, y1)
                for i in range((x1 - x2)):
                    self.mark_cell(x2 + i, y2)
            elif x2 > x1:
                self.mark_cell(x1, y1)
                for i in range((x2 - x1)):
                    self.mark_cell(x2 - i, y2)

    def calculate_non_safe_spaces(self):
        non_safe_spaces = 0
        for row in self.grid:
            for number in row:
                if number >= 2:
                    non_safe_spaces += 1
        return non_safe_spaces

    def draw_coordinate_pairs(self):
        for coord_pair in self.coordinate_pairs:
            self.draw_line(coord_pair[0][0], coord_pair[0][1], coord_pair[1][0], coord_pair[1][1])


grid = Grid(lines)
grid.draw_coordinate_pairs()
print(grid.calculate_non_safe_spaces())