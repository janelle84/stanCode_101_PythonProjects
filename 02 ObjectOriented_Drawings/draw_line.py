"""
File: draw_line.py
Name: Janelle
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 3

# Global variables
count = 0
window = GWindow()
start_point = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    start_point.filled = False
    start_point.color = 'black'
    onmouseclicked(draw)


def draw(mouse):
    """
    :param mouse: the mouse click
    -----------------------------------------------------------------
    This function detects mouse click and draw lines on blank canvas.
    """
    global count

    if count % 2 == 0:
        window.add(start_point, x=mouse.x - SIZE/2, y=mouse.y - SIZE/2)

    else:
        window.remove(start_point)  # Remove the original dot
        line = GLine(start_point.x + SIZE/2, start_point.y + SIZE/2, mouse.x, mouse.y)
        window.add(line)  # Draw the line

    count += 1


if __name__ == "__main__":
    main()
