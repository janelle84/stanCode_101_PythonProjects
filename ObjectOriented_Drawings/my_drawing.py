"""
File: PowerPuff.py
Name: Janelle
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(300, 300, title='PowerPuff')


def main():
    """
    Title: PowerPuff
    This program draws Blossom, who is the red-haired, level-headed leader in PowerPuff.
    """

    hair0 = GRect(140, 80, x=window.width/2 - 70, y=220)
    hair0.filled = True
    hair0.fill_color = 'coral'

    cloth1 = GRect(60, 80, x=window.width/2 - 30, y=220)
    cloth1.filled = True
    cloth1.fill_color = 'hotpink'

    cloth2 = GRect(60, 20, x=window.width/2 - 30, y=275)
    cloth2.filled = True

    bow = GOval(20, 20, x=140, y=90)
    bow.filled = True
    bow.fill_color = 'orangered'

    bow_2 = GOval(60, 120, x=85, y=10)
    bow_2.filled = True
    bow_2.fill_color = 'orangered'

    bow_3 = GOval(60, 120, x=155, y=10)
    bow_3.filled = True
    bow_3.fill_color = 'orangered'

    face = GOval(200, 170, x=50, y=100)
    face.filled = True
    face.fill_color = 'bisque'

    eye1 = GOval(90, 90, x=50, y=140)
    eye1.filled = True
    eye1.fill_color = 'white'

    eye2 = GOval(90, 90, x=160, y=140)
    eye2.filled = True
    eye2.fill_color = 'white'

    eye1_1 = GOval(75, 75, x=65, y=145)
    eye1_1.filled = True
    eye1_1.color = 'hotpink'
    eye1_1.fill_color = 'hotpink'

    eye2_1 = GOval(75, 75, x=160, y=145)
    eye2_1.filled = True
    eye2_1.color = 'hotpink'
    eye2_1.fill_color = 'hotpink'

    eye1_2 = GOval(65, 65, x=75, y=150)
    eye1_2.filled = True

    eye2_2 = GOval(65, 65, x=160, y=150)
    eye2_2.filled = True

    eye1_3 = GOval(20, 20, x=115, y=170)
    eye1_3.filled = True
    eye1_3.color = 'white'
    eye1_3.fill_color = 'white'

    eye2_3 = GOval(20, 20, x=165, y=170)
    eye2_3.filled = True
    eye2_3.color = 'white'
    eye2_3.fill_color = 'white'

    mouth = GArc(10, 20, 180, 180)

    hair1 = GArc(240, 180, 80, 100)
    hair1.filled = True
    hair1.fill_color = 'coral'

    hair2 = GArc(240, 180, 0, 100)
    hair2.filled = True
    hair2.fill_color = 'coral'

    hair3 = GPolygon()
    hair3.add_vertex((142, 100))
    hair3.add_vertex((160, 100))
    hair3.add_vertex((165, 140))
    hair3.add_vertex((135, 140))
    hair3.filled = True
    hair3.fill_color = 'coral'

    window.add(bow_2)
    window.add(bow_3)
    window.add(bow)

    window.add(hair0)
    window.add(cloth1)
    window.add(cloth2)

    window.add(face)
    window.add(eye1)
    window.add(eye2)
    window.add(eye1_1)
    window.add(eye2_1)
    window.add(eye1_2)
    window.add(eye2_2)
    window.add(eye1_3)
    window.add(eye2_3)
    window.add(mouth, x=145, y=220)
    window.add(hair1, x=60, y=100)
    window.add(hair2, x=100, y=100)
    window.add(hair3)


if __name__ == '__main__':
    main()
