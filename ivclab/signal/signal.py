import numpy as np
from scipy.signal import convolve2d

def downsample(image):
    """
    Selects only the even positioned pixels of an image
    to downsample it.

    image: np.array of shape [H, W, C]

    returns 
        downsampled_image: np.array of shape [H // 2, W // 2, C]
    """
    downsampled_image = image[0::2, 0::2, :]
    return downsampled_image

def upsample(image):
    """
    Upsamples an image by filling new pixels with zeroes.

    image: np.array of shape [H, W, C]

    returns 
        upsampled_image: np.array of shape [H * 2, W * 2, C]
    """
    H, W, C = image.shape
    upsampled_image = np.zeros((2 * H, 2 * W, C), dtype=image.dtype)
    upsampled_image[0::2, 0::2, :] = image
    return upsampled_image

def lowpass_filter(image, kernel):
    """
    Applies a given kernel on each channel of an image separately
    with convolution operation. 

    image: np.array of shape [H, W, C]
    kernel: np.array of shape [kernel_height, kernel_width]

    returns 
        filtered: np.array of shape [H, W, C]
    """
    filtered = np.zeros_like(image)

    # YOUR CODE STARTS HERE
    

    # YOUR CODE ENDS HERE
    return filtered

class FilterPipeline:

    def __init__(self, kernel):
        """
        Initializes a filtering pipeline with the given kernel 

        kernel: np.array of shape [kernel_height, kernel_width]
        """
        self.kernel = kernel / np.sum(kernel)

    def filter_img(self, image: np.ndarray, prefilter: bool=True):
        """
        Applies prefiltering to an image (optional), downsamples, 
        upsamples and filters the output with a lowpass filter. 

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
    
window_order_40 = np.asarray([
    -1.56111078131637e-18,
    -0.00143682673655179,
    2.00044643181557e-18,
    0.00243957821061731,
    -3.27544814881085e-18,
    -0.00456211392411543,
    5.26130988078338e-18,
    0.00811826330004546,
    -7.76364164509541e-18,
    -0.0135598005342035,
    1.05374977738855e-17,
    0.0216692211979930,
    -1.33113539026756e-17,
    -0.0340919105367977,
    1.58136856669876e-17,
    0.0551498175592887,
    -1.77995473989601e-17,
    -0.100902655692560,
    1.90745491159554e-17,
    0.316881088663691,
    0.500590676985187,
    0.316881088663691,
    1.90745491159554e-17,
    -0.100902655692560,
    -1.77995473989601e-17,
    0.0551498175592887,
    1.58136856669876e-17,
    -0.0340919105367977,
    -1.33113539026756e-17,
    0.0216692211979930,
    1.05374977738855e-17,
    -0.0135598005342035,
    -7.76364164509541e-18,
    0.00811826330004546,
    5.26130988078338e-18,
    -0.00456211392411543,
    -3.27544814881085e-18,	
    0.00243957821061731,
    2.00044643181557e-18,
    -0.00143682673655179,
    -1.56111078131637e-18
])

kernel_order_40 = window_order_40[:,None] * window_order_40[None, :]