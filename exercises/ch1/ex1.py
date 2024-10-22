from ivclab.utils import imread, imshow
from ivclab.signal import rgb2gray
import matplotlib.pyplot as plt

# read images
img_lena = imread('data/lena.tif')
img_lena_gray = rgb2gray(img_lena)
img_smandril = imread('data/smandril.tif')
img_smandril_gray = rgb2gray(img_smandril)

# plot images
fig, axs = plt.subplots(2,2)
imshow(axs[0][0], img_lena, title='Original Lena Image')
imshow(axs[0][1], img_lena_gray, title='Compressed Lena Image')
imshow(axs[1][0], img_smandril, title='Original Smandril Image')
imshow(axs[1][1], img_smandril_gray, title='Compressed Smandril Image')

plt.show()

