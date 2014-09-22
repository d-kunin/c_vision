__author__ = '7times6'

from PIL import Image
from pylab import *

filename = 'center_stan.jpg'
image = Image.open(filename).convert('L')
im = array(image)

# create figure
figure()
# do not use colors
gray()
# show contour with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')

# interactive points input
print 'Please click 3 points'
x = ginput(3)
print 'You clicked:', x

figure()
hist(im.flatten(), 128)
show()