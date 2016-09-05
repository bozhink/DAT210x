# -*- coding: utf-8 -*-
# Uses the Image module (PIL)
from scipy import misc

# Load the image up
img = misc.imread('../Module1/Course Golden Ratio.png')
print type(img)
print img.shape, img.dtype

# Is the image too big? Resample it down by an order of magnitude
img = img[::2, ::2]

# Scale colors from (0-255) to (0-1), then reshape to 1D array per pixel
X = (img / 255.0).reshape(-1, 4)


red = X[:,0]
green = X[:,1]
blue = X[:,2]

gray = (0.299*red + 0.587*green + 0.114*blue)

print img.shape
print gray.shape

