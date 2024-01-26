"""
File: blur.py
Name: Jane
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

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                for i in range(2):
                    for j in range(2):
                        new_r += img.get_pixel(i, j).red // 4
                        new_g += img.get_pixel(i, j).green // 4
                        new_b += img.get_pixel(i, j).blue // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                for i in range(1, 3):
                    for j in range(2):
                        new_r += img.get_pixel(img.width-i, j).red // 4
                        new_g += img.get_pixel(img.width-i, j).green // 4
                        new_b += img.get_pixel(img.width-i, j).blue // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                for i in range(2):
                    for j in range(1, 3):
                        new_r += img.get_pixel(i, img.height-j).red // 4
                        new_g += img.get_pixel(i, img.height-j).green // 4
                        new_b += img.get_pixel(i, img.height-j).blue // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                for i in range(1, 3):
                    for j in range(1, 3):
                        new_r += img.get_pixel(img.width-i, img.height-j).red // 4
                        new_g += img.get_pixel(img.width-i, img.height-j).green // 4
                        new_b += img.get_pixel(img.width-i, img.height-j).blue // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                for i in range(-1, 2):
                    for j in range(2):
                        new_r += img.get_pixel(x-i, j).red // 6
                        new_g += img.get_pixel(x-i, j).green // 6
                        new_b += img.get_pixel(x-i, j).blue // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b
            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                for i in range(-1, 2):
                    for j in range(1, 3):
                        new_r += img.get_pixel(x-i, img.height-j).red // 6
                        new_g += img.get_pixel(x-i, img.height-j).green // 6
                        new_b += img.get_pixel(x-i, img.height-j).blue // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                for i in range(2):
                    for j in range(-1, 2):
                        new_r += img.get_pixel(i, y-j).red // 6
                        new_g += img.get_pixel(i, y-j).green // 6
                        new_b += img.get_pixel(i, y-j).blue // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                for i in range(1, 3):
                    for k in range(-1, 2):
                        new_r += img.get_pixel(img.width-i, y-j).red // 6
                        new_g += img.get_pixel(img.width-i, y-j).green // 6
                        new_b += img.get_pixel(img.width-i, y-j).blue // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            else:
                # Inner pixels.
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_r += img.get_pixel(x-i, y-j).red // 9
                        new_g += img.get_pixel(x-i, y-j).green // 9
                        new_b += img.get_pixel(x-i, y-j).blue // 9
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b
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
