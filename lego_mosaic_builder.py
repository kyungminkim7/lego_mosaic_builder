import argparse
import math
import numpy as np
import cv2 as cv
import sys

from collections import defaultdict

# Parse args
parser = argparse.ArgumentParser()

parser.add_argument('image_path')

args = parser.parse_args()

# Setup Windows
img_window = f'{args.image_path}'
mosaic_window = 'Mosaic'

#cv.namedWindow(img_window, cv.WINDOW_NORMAL)
cv.namedWindow(mosaic_window, cv.WINDOW_NORMAL)

# Brick colors
brick_colors = {
    'Black': (0, 0, 0),
    'Medium Stone Grey': (150, 150, 150),
    'Dark Stone Grey': (100, 100, 100),
    'White': (255, 255, 255),
    'Sand Yellow': (139, 124, 103),
    'Medium Blue': (117, 153, 205),
    'Dark Red': (111, 38, 49),
    'Reddish Brown': (84, 43, 22),
    'Bright Orange': (221, 126, 42),
    'Dark Green': (46, 162, 83),
    'Medium Lavender': (140, 98, 161),
    'Brick Yellow': (179, 164, 111),
    'Bright Green': (87, 175, 66),
    'Nougat': (193, 131, 94),
    'Lavender': (181, 144, 195),
    'Dark Orange': (142, 76, 45),
    'Light Royal Blue': (160, 183, 218),
    'Light Nougat': (243, 181, 149),
    'Earth Green': (53, 83, 59),
    'Dark Azur': (54, 131, 176),
    'Bright Yellowish Green': (151, 190, 65),
    'Medium Lilac': (92, 67, 146),
    'Bright Purple': (216, 54, 160),
    'Bright Bluish Green': (28, 143, 139),
    'Dark Brown': (68, 51, 21),
    'Medium Azur': (98, 160, 189),
    'Bright Reddish Violet': (134, 63, 122),
    'Warm Gold': (178, 153, 79),
    'Aqua': (186, 211, 205),
    'Cool Yellow': (252, 227, 107),
    'Olive Green': (106, 112, 50),
    'Light Purple': (240, 151, 199),
    'Flame Yellowish Orange': (243, 157, 30),
    'Medium Nougat': (133, 95, 67),
    'Sand Green': (118, 156, 131),
    'Vibrant Coral': (254, 99, 136),
    'Bright Red': (190, 4, 4),
    'Earth Blue': (37, 61, 102),
    'Bright Yellow': (246, 196, 3),
    'Bright Blue': (36, 97, 178)
}

rgb2color = dict((v, k) for k, v in brick_colors.items())

brick_counter = defaultdict(int)

def get_closest_color(pixel):
    global brick_counter

    closest_pixel = min(brick_colors.values(), 
                        key=lambda brick_color: math.dist(pixel, brick_color))

    color = rgb2color[closest_pixel]
    brick_counter[color] += 1
    return color

# Load image
img = cv.imread(args.image_path)

if img is None:
    raise SystemError(f'Failed to load img: {args.image_path}')

# Resize image for mosaic
height, width, channels = img.shape
scale = 64 / width
mosaic_img = cv.resize(img, None, fx=scale, fy=scale)

scaled_height, scaled_width, channels = mosaic_img.shape
print(f"Mosaic dimensions(wxhxc): {scaled_width} x {scaled_height} x {channels}\n")

# Process mosaic
for r, row in enumerate(mosaic_img):
    for c, pixel in enumerate(row):
        brick_color = brick_colors[get_closest_color(pixel)]
        mosaic_img[r, c] = brick_color
        #pass

# Display images
#cv.imshow(img_window, img)
cv.imshow(mosaic_window, mosaic_img)

for color, count in brick_counter.items():
    print(f"{color:20}: {count}")

print(f'{sum(brick_counter.values())}')
k = cv.waitKey(0)
