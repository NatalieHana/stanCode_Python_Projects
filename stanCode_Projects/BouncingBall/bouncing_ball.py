"""
File: bouncing_ball.py
Name: Jane
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 50
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
vy = 0
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def bounce(click):
    global ball, count, vy
    bouncing = False
    if vy == 0:
        bouncing = True

    while count < 3 and bouncing:
        vy += GRAVITY
        ball.move(VX, vy)
        pause(DELAY)
        if ball.y >= window.height:
            vy = -vy*REDUCE
        if ball.x > window.width:
            count += 1
            window.remove(ball)
            ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
            ball.filled = True
            window.add(ball)
            vy = 0  # 因為vy(全域)會停留在球移除前最後一個vy值, 所以要重定義vy = 0, 才可將開關打開
            break


if __name__ == "__main__":
    main()
