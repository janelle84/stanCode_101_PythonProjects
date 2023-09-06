"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program is the coder-end of a breakout game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
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

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(window_width - paddle_width)//2, y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius,
                          x=(window_width - ball_radius)//2, y=(window_height - ball_radius)//2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.trigger = True
        self.brick_num = brick_rows * brick_cols

        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.detect)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT,
                                   x=i*(BRICK_WIDTH + BRICK_SPACING), y=j*(BRICK_HEIGHT + BRICK_SPACING))
                self.brick.filled = True

                if j < BRICK_ROWS//5:
                    self.brick.color = 'indianred'
                    self.brick.fill_color = 'indianred'

                elif j < BRICK_ROWS//5*2:
                    self.brick.color = 'coral'
                    self.brick.fill_color = 'coral'

                elif j < BRICK_ROWS//5*3:
                    self.brick.color = 'gold'
                    self.brick.fill_color = 'gold'

                elif j < BRICK_ROWS//5*4:
                    self.brick.color = 'lightseagreen'
                    self.brick.fill_color = 'lightseagreen'

                else:
                    self.brick.color = 'indigo'
                    self.brick.fill_color = 'indigo'

                self.window.add(self.brick)

    def paddle_position(self, move):
        """
        :param move: the movement of user's mouse
        ------------------------------------------------
        This function controls the movement of the paddle.
        """
        self.paddle.x = move.x - self.paddle.width/2

        if move.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

        elif move.x - self.paddle.width/2 < 0:
            self.paddle.x = 0

        self.window.add(self.paddle, x=self.paddle.x, y=self.window.height - PADDLE_OFFSET)

    def detect(self, mouse):
        if self.trigger:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

            self.__dy = INITIAL_Y_SPEED
            self.trigger = False

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def restart(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width)//2,
                        y=(self.window.height - self.ball.height)//2)
        self.__dx = 0
        self.__dy = 0
        self.trigger = True

    def check_collision(self):
        for x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                maybe_obj = self.window.get_object_at(x, y)

                if maybe_obj is not None:
                    if maybe_obj is not self.paddle:
                        self.brick_num -= 1
                        self.window.remove(maybe_obj)
                        self.__dy = -self.__dy

                    else:
                        if self.__dy > 0:
                            self.__dy = -self.__dy

                    return
