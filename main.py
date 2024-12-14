from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 800)
    win.draw_line(Line(Point(100, 100), Point(700, 700)), "red")
    win.draw_line(Line(Point(700, 100), Point(100, 700)), "green")
    win.draw_line(Line(Point(100, 100), Point(700, 100)), "blue")
    win.wait_for_close()

if __name__ == '__main__':
    main()