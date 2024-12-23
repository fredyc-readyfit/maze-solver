from window import Window
# from line import Line
# from point import Point
# from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    # win.draw_line(Line(Point(100, 100), Point(700, 700)), "red")
    # win.draw_line(Line(Point(700, 100), Point(100, 700)), "green")
    # win.draw_line(Line(Point(100, 100), Point(700, 100)), "blue")

    # Cell(100, 200, 100, 200, win).draw()
    # Cell(150, 175, 50, 75, win, has_left_wall=False).draw()
    # Cell(350, 400, 350, 400, win, has_top_wall=False).draw()
    # Cell(100, 400, 150, 200, win, has_right_wall=False).draw()
    # Cell(600, 700, 600, 700, win, has_bottom_wall=False).draw()

    # c1 = Cell(10, 30, 10, 30, win,  has_right_wall=False)
    # c2 = Cell(30, 50, 10, 30, win, has_left_wall=False, has_right_wall=False)
    # c3 = Cell(50, 70, 10, 30, win, has_left_wall=False, has_bottom_wall=False)
    # c4 = Cell(50, 70, 30, 50, win, has_top_wall=False, has_bottom_wall=False)
    # c5 = Cell(50, 70, 50, 70, win, has_top_wall=False, has_left_wall=False)
    # c6 = Cell(30, 50, 50, 70, win, has_top_wall=False, has_left_wall=False, has_right_wall=False)
    # c7 = Cell(30, 50, 30, 50, win, has_bottom_wall=False)
    # c8 = Cell(10, 30, 50, 70, win, has_right_wall=False, has_bottom_wall=False)
    # c9 = Cell(10, 30, 70, 90, win, has_top_wall=False, has_bottom_wall=False)

    # c1.draw()
    # c2.draw()
    # c3.draw()
    # c4.draw()
    # c5.draw()
    # c6.draw()
    # c7.draw()
    # c8.draw()
    # c9.draw()
    
    # c1.draw_move(c2)
    # c2.draw_move(c3)
    # c3.draw_move(c4)
    # c4.draw_move(c5)
    # c5.draw_move(c6)
    # c6.draw_move(c7)
    # c7.draw_move(c6, undo=True)
    # c6.draw_move(c8)
    # c8.draw_move(c9)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    win.wait_for_close()

if __name__ == '__main__':
    main()