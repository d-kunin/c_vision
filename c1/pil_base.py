__author__ = '7times6'

from PIL import Image

filename = 'stan.jpg'
im = Image.open(filename)
im_gray = Image.open(filename).convert('L')

# convert to another format
import os
filepng = os.path.splitext(filename)[0] + '.png'
try:
    Image.open(filename).save(filepng)
except IOError:
    print 'cannot convert', filename, filepng

# create thumbnail
thumb_size = (128, 128)
thumb = Image.open(filename)
thumb.thumbnail(thumb_size)
filethumb = 'thumb_' + filename
thumb.save(filethumb)

# copy-paste region
w, h = im.size
print 'size is:', w, h
mindimen = min(w, h)
x0 = (w - mindimen)/2
y0 = (h - mindimen)/2
x1 = x0 + mindimen
y1 = y0 + mindimen
print 'going to crop:', x0, y0, x1, y1

box = (x0, y0, x1, y1)
region = im.crop(box)
region.save('center_' + filename)

# resize & rotate
small = im.resize((640, 640)).rotate(45)
small.save('transformed_' + filename)