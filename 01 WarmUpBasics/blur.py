"""
File: blur.py
Name: Janelle Lin
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            red = 0
            green = 0
            blue = 0
            count = 0

            for test_x in range(x-1, x+2, 1):  # text_x = x-1, x , x+1
                for test_y in range(y-1, y+2, 1):  # text_y = y-1, y , y+1
                    if img.width > test_x >= 0 and img.height > test_y >= 0:
                        count += 1
                        temp_pixel = img.get_pixel(test_x, test_y)
                        red += int(temp_pixel.red)
                        green += int(temp_pixel.green)
                        blue += int(temp_pixel.blue)

            new_pixel.red = red // count
            new_pixel.green = green // count
            new_pixel.blue = blue // count

    return new_img


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
