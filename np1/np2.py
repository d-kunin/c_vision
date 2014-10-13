__author__ = '7times6'
import imtools
from PIL import Image
import numpy as np
import pylab as mp

filename = 'center_stan.jpg'
im = np.array(Image.open(filename).convert('L'))
im_he, cdf = imtools.histeq(im)

mp.gray()
mp.figure()
mp.imshow(im)
mp.title('Original')

mp.figure()
mp.imshow(im_he)
mp.title('Equalized')
mp.show()

Image.fromarray(np.uint8(im_he)).save('eq_' + filename)
