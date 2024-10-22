from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def imread(filepath: str):
    with Image.open(filepath) as data:
        img = np.asarray(data)
    return img

def imshow(ax: plt.axes, img: np.array, title=None, hide_ticks=True):
    
    if img.shape[-1] == 1:
        ax.imshow(img, cmap='gray')
    else:
        ax.imshow(img)
    
    if title is not None:
        ax.set_title(title)

    if hide_ticks:
        ax.set_xticks([])
        ax.set_yticks([])

