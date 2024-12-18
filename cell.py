from line import Line
from point import Point
from window import Window

class Cell:
    def __init__(self, x1, x2, y1, y2, win: Window = None, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        if self._win is None:
            return
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_righ = Point(self._x2, self._y2)
        
        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        righ_wall = Line(top_right, bottom_righ)
        bottom_wall = Line(bottom_left, bottom_righ)

        if self.has_left_wall:
            left_wall.draw(self._win.canvas, 'black')
        else:
            left_wall.draw(self._win.canvas, 'white')

        if self.has_top_wall:
            top_wall.draw(self._win.canvas, 'black')
        else:
            top_wall.draw(self._win.canvas, 'white')

        if self.has_right_wall:
            righ_wall.draw(self._win.canvas, 'black')
        else:
            righ_wall.draw(self._win.canvas, 'white')
        
        if self.has_bottom_wall:
            bottom_wall.draw(self._win.canvas, 'black')
        else:
            bottom_wall.draw(self._win.canvas, 'white')
    
    def draw_move(self, to_cell, undo = False):
        center = Point(self._x1 + abs((self._x2 - self._x1) / 2), self._y1 + abs((self._y2 - self._y1)/2))
        to_center = Point(to_cell._x1 + abs((to_cell._x2 - to_cell._x1) / 2), to_cell._y1 + abs((to_cell._y2 - to_cell._y1) / 2))
        move = Line(center, to_center)

        if not undo:
            color = 'red'
        else:
            color = 'gray'

        move.draw(self._win.canvas, color) 
