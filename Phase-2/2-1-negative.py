import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
Image URL: https://en.wikipedia.org/wiki/Fingerprint
"""
img = cv2.imread('fingerprint.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""
Using NumPy. Faster.
"""
neg = 255 - img

"""
Using cv2
"""
# neg = cv2.bitwise_not(img)

cv2.imwrite('fingerprint-neg.jpg', neg)