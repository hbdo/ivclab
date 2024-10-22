import unittest
from ivclab.utils import imread, calc_mse, calc_psnr

class TestMeasurements(unittest.TestCase):

    def setUp(self) -> None:
        self.orig_img = imread('data/lena.tif')
        self.recon_img = imread('data/lena_rec.tif')
        return super().setUp()
    
    def test_correct_mse(self) -> None:
        mse = calc_mse(self.orig_img, self.recon_img)
        self.assertAlmostEqual(mse, 1849.6111, delta=2.0)
        
    def test_correct_psnr(self) -> None:
        psnr = calc_psnr(self.orig_img, self.recon_img)
        self.assertAlmostEqual(psnr, 15.4599, delta=0.2)

if __name__ == '__main__':
    unittest.main()