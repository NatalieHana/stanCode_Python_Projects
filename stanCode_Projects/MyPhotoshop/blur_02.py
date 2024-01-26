"""
File: blur.py
Name: Nearest Neighbors
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original image
    :return: SimpleImage, blur image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            new_img_p = new_img.get_pixel(x, y)
            new_r = 0
            new_g = 0
            new_b = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            new_r += img.get_pixel(pixel_x, pixel_y).red
                            new_g += img.get_pixel(pixel_x, pixel_y).green
                            new_b += img.get_pixel(pixel_x, pixel_y).blue
                            count += 1
            new_img_p.red = new_r // count
            new_img_p.green = new_g // count
            new_img_p.blue = new_b // count
    return new_img


def main():
    """
    blur image with adjacent pixel
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
