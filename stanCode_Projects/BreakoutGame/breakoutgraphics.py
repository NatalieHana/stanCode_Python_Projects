"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self._ball_radius = ball_radius
        self._offset = paddle_offset
        self._brick_rows = brick_rows
        self._brick_cols = brick_cols
        self._brick_width = brick_width
        self._brick_height = brick_height
        self._brick_offset = brick_offset
        self._brick_spacing = brick_spacing

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=(window_height-brick_offset))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width/2-ball_radius), y=(window_height/2-ball_radius))
        self.ball.filled = True
        self.window.add(self.ball)

        # Draw bricks
        colors = ["#495049", "#57898a", "#b3b89a", "#ccae66", "#cb9362"]
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=j*brick_width+j*brick_spacing, y=brick_offset+i*brick_height+i*brick_spacing)
                self.brick.filled = True
                self.brick.color = colors[i//(brick_rows//5)]
                self.brick.fill_color = colors[i//(brick_rows//5)]
                self.window.add(self.brick)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.change_position)
        onmouseclicked(self.ball_start)
        self.starting = False  # starting:球靜止等待滑鼠按下才能啟動

    def set_ball_velocity(self):  # 定義速度初始值
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def ball_start(self, event):
        if not self.starting:
            self.starting = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def change_position(self, event):
        if event.x < self.paddle.width:
            self.paddle.x = 0
        elif event.x > self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    # get private keyword args
    def get_brick_rows(self):
        return self._brick_rows

    def get_brick_cols(self):
        return self._brick_cols





