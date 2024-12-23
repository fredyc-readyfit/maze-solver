from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                col_cells.append(Cell(x1, x2, y1, y2, self._win))
            self._cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = []
            if i > 0 and not self._cells[i-1][j].visited:
                directions.append((i-1, j))

            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                directions.append((i+1, j))

            if j > 0 and not self._cells[i][j-1].visited:
                directions.append((i, j-1))
            
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                directions.append((i, j+1))
            
            if len(directions) == 0:
                self._cells[i][j].draw()
                return
            else:
                direction = random.choice(directions)
                if direction[0] == i-1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                elif direction[0] == i+1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                elif direction[1] == j - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
                elif direction[1] == j + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(direction[0], direction[1])

