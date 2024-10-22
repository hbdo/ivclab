import numpy as np
from scipy.signal import decimate, resample

def yuv420compression(image: np.ndarray):
    """
    Steps:
    1. Convert an image from RGB to YCbCr
    2. Compress the image
        A. Pad the image with 4 pixels symmetric pixels on each side
        B. Downsample only Cb and Cr channels with prefiltering (use scipy.signal.decimate for it)
        C. Crop the image 2 pixels from each side to get rid of padding
    3. Apply rounding to Y, Cb and Cr channels
    4. Decompress the image
        A. Pad the image with 4 pixels symmetric pixels on each side
        B. Upsample Cb and Cr channels (use scipy.signal.resample for it)
        C. Crop the image 2 pixels from each side to get rid of padding
    5. Convert the YCbCr image back to RGB

    image: np.array of shape [H, W, C]

    returns 
        output_image: np.array of shape [H, W, C]
    """
    # Cast image to floating point
    image = image * 1.0

    # YOUR CODE STARTS HERE

    
    #YOUR CODE ENDS HERE

    # Cast output to integer again
    output = np.round(output).astype(np.uint8)
    return output