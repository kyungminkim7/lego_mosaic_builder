import argparse
import numpy as np
import cv2 as cv
import sys

# Parse args
parser = argparse.ArgumentParser()

parser.add_argument('image_path')

args = parser.parse_args()

# Setup Windows
img_window = f'{args.image_path}'
mosaic_window = 'Mosaic'

cv.namedWindow(img_window, cv.WINDOW_NORMAL)
cv.namedWindow(mosaic_window, cv.WINDOW_NORMAL)

# Brick colors
colors = {
    'Black': (255, 255, 255)
}

# Load image
img = cv.imread(args.image_path)
mosaic_img = np.copy(img)

if img is None:
    raise SystemError(f'Failed to load img: {args.image_path}')

# Process mosaic
for r, row in enumerate(mosaic_img):
    for c, pixel in enumerate(row):
        mosaic_img[r, c] = colors['Black']

# Display images
cv.imshow(img_window, img)
cv.imshow(mosaic_window, mosaic_img)
k = cv.waitKey(0)
