from ivclab.utils import imread, calc_psnr
from ivclab.image import yuv420compression
import numpy as np

image = imread('data/satpic1.bmp')

recon_image = yuv420compression(image)

psnr_recon = calc_psnr(image, recon_image)

print(f"Reconstructed image, not prefiltered, PSNR = {psnr_recon:.2f} dB")

