from gui import Window, Line, Point


def main():
    win = Window(800, 600)

    l1 = Line(Point(45, 100), Point(200, 400))
    l2 = Line(Point(20, 50), Point(104, 150))

    win.draw_line(l1, "red")
    win.draw_line(l2, "black")

    win.wait_for_close()


main()
