from matplotlib.pyplot import imshow, figure, title, show, gray

__author__ = '7times6'

import numpy as np
from PIL import Image

# as uint8
filename = 'center_stan.jpg'
im = np.array(Image.open(filename))

print im.dtype, im.shape

# as float
im = np.array(Image.open(filename).convert('L'), 'f')
print im.dtype, im.shape

# simple gray scale
im = np.array(Image.open(filename).convert('L'))

im_invert = 255 - im
im_cl1 = (100.0/255) * im + 100
im_cl2 = 255.0 * (im/255.0) ** 2

figure()
gray()
imshow(im)
title('Original')

figure()
gray()
imshow(im_invert)
title('Inverted')

figure()
gray()
imshow(im_cl1)
title('clamped [100, 200]')

figure()
gray()
imshow(im_cl2)
title('Squared')
Image.fromarray(np.uint8(im_cl2)).save('hipsto_' + filename)

show()
