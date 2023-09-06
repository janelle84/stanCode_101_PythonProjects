"""
File: bouncing_ball.py
Name: Janelle
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
trigger = True
count = 0


def main():
    """
    This program simulate the motion of a bouncing ball, activated by user's mouse click.
    """
    global trigger, count

    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(detect)
    # if count < 3:  # Can only react when ball is at starter point & play no more than 3 times
    while True:
        if not trigger:
            vy = 0
            count += 1
            while True:
                if ball.x > window.width:  # break the loop while x is out of sight
                    trigger = True
                    break

                else:
                    vy += GRAVITY
                    if ball.y + SIZE >= window.height:
                        vy = (-vy) * REDUCE  # reduce velocity when bounced

                    ball.move(VX, vy)
                    window.add(ball)
                    pause(DELAY)

            window.add(ball, x=START_X, y=START_Y)  # ball is back to starter point
        if count == 3:
            break
        pause(DELAY)


def detect(mouse):
    """
    This function determines when to stop the game.
    """
    global trigger
    if trigger:
        trigger = False


def drop_the_ball(_):
    """
    This function controls the start point of the ball.
    """
    global trigger, count

    trigger = False
    count += 1


if __name__ == "__main__":
    main()
