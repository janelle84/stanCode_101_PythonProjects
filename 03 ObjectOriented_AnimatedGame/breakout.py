"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program is the user-end of a breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 30         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    loose_lives = 0

    # Add the animation loop here!
    while True:
        count_bricks = graphics.brick_num
        if loose_lives == NUM_LIVES or count_bricks == 0:
            break
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)
        pause(FRAME_RATE)

        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            loose_lives += 1
            graphics.restart()

        if graphics.ball.y <= 0:
            graphics.set_dy(-vy)

        if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
            graphics.set_dx(-vx)

        graphics.check_collision()


if __name__ == '__main__':
    main()
