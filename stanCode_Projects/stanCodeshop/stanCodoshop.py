"""
File: stanCodoshop.py
Name: Natalie
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os  # 執行與目錄(folder)相關操作
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = math.sqrt((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)
    return dist


def get_average(pixels):  # pixels(list): Ｎ張圖片在某相同位置 (x, y) 上的 pixels
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # red_t = 0
    # green_t = 0
    # blue_t = 0
    # for i in range(len(pixels)):
    #     pixel = pixels[i]
    #     red_t += pixel.red
    #     green_t += pixel.green
    #     blue_t += pixel.blue
    red_t = sum(pixel.red for pixel in pixels)
    green_t = sum(pixel.green for pixel in pixels)
    blue_t = sum(pixel.blue for pixel in pixels)
    red = red_t//len(pixels)
    green = green_t//len(pixels)
    blue = blue_t//len(pixels)
    average = [red, green, blue]
    return average


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # dist_min = float("inf")
    # best = None
    # pixel_avg = get_average(pixels)
    # for i in range(len(pixels)):
    #     dist = get_pixel_dist(pixels[i], pixel_avg[0], pixel_avg[1], pixel_avg[2])
    #     if dist < dist_min:
    #         dist_min = dist
    #         best = pixels[i]
    # return best

    dist_list = []
    pixel_avg = get_average(pixels)
    for pixel in pixels:
        dist = get_pixel_dist(pixel, pixel_avg[0], pixel_avg[1], pixel_avg[2])
        dist_list.append((dist, pixel))
    return min(dist_list, key=lambda t: t[0])[1]  # 雖然會先比較dist, 但當dist相同會比較pixel, 但pixel是物件會error, 所以還是要用lambda將條件鎖住


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for x in range(width):
        for y in range(height):
            pixels = []  # 清空pixels list
            for i in range(len(images)):
                image = images[i]
                img_p = image.get_pixel(x, y)
                pixels.append(img_p)
            best = get_best_pixel(pixels)
            result_p = result.get_pixel(x, y)
            result_p.red = best.red
            result_p.green = best.green
            result_p.blue = best.blue
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # geen_im = SimpleImage.blank(20, 20, "green")  # SimpleImage.balnk(寬, 高, 背景色)
    # green_pixel = geen_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # green_pixel = SimpleImage.blank(20, 20, "green").get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, "red").get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, "blue").get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):  # 用os.listdir來獲取folder路徑(dir)的內容列表
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))  # 將folder路徑(dir)與文件名稱合併成一個完整文件路徑
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)  # 每張圖的檔案路徑list
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images  # 回傳每張圖的list


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]  # py stanCodeshop.py hoover -> [hoover]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
