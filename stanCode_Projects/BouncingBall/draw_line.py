"""
File: draw_line.py
Name: Jane
-------------------------
use global variable for event-driven case
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow()
SIZE = 10
count = 0
pen_stroke = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(click):
    global count, pen_stroke
    count += 1
    if count % 2 == 1:
        pen_stroke = GOval(SIZE, SIZE, x=click.x - SIZE / 2, y=click.y - SIZE / 2)
        window.add(pen_stroke)
    else:
        pen_stroke.color = "white"
        pen_line = GLine(pen_stroke.x, pen_stroke.y, click.x, click.y)
        window.add(pen_line)


if __name__ == "__main__":
    main()
