__author__ = '7times6'

from PIL import Image
from pylab import *

# read image as array
filename = 'center_stan.jpg'
image = Image.open(filename)
im = array(image)

# plot image
imshow(im)

# create points
w, h = image.size
x = [w/10, w/5, w/2, w/2]
y = [h/10, h/2, h/10, h/2]

# plot points with red stars
plot(x, y, 'r*')

# line plot -- connect first 2 points
plot(x[:3], y[:3], 'ks:')

# add title
title('Plotting: "%s"' % filename)

# turn off axes for beauty
axis('off')

show()