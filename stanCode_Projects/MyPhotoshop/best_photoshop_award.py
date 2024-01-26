"""
File: best_photoshop_award.py
Name: Jane
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 0.98
BLACK_PIXEL = 250


def main():
    """
    回童年最喜歡的卡通
    """
    fig = SimpleImage("images/IMG_0477.jpg")
    bg = SimpleImage("images/childhood.jpg")
    fig.show()
    bg.make_as_big_as(fig)
    combine_img = combine(fig, bg)
    combine_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_p = fig.get_pixel(x, y)
            avg = (fig_p.red + fig_p.green + fig_p.blue) // 3
            total = fig_p.red + fig_p.green + fig_p.blue
            if fig_p.blue > avg*THRESHOLD and total > BLACK_PIXEL:
                bg_p = bg.get_pixel(x, y)
                fig_p.red = bg_p.red
                fig_p.green = bg_p.green
                fig_p.blue = bg_p.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
