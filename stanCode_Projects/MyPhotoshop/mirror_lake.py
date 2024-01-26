"""
File: mirror_lake.py
Name: Jane
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the fiel path of the original image
    :return: SimpleImage, with relfection of the original image
    """
    lake = SimpleImage(filename)
    mirror = SimpleImage.blank(lake.width, lake.height*2)
    for x in range(lake.width):
        for y in range(lake.height):
            lake_p = lake.get_pixel(x, y)

            top_mirror = mirror.get_pixel(x, y)
            top_mirror.red = lake_p.red
            top_mirror.green = lake_p.green
            top_mirror.blue = lake_p.blue

            bottom_mirror = mirror.get_pixel(x, mirror.height-1-y)
            bottom_mirror.red = lake_p.red
            bottom_mirror.green = lake_p.green
            bottom_mirror.blue = lake_p.blue
    return mirror


def main():
    """
    create the reflection of image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
