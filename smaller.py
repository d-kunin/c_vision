__author__ = '7times6'


dIn  = '/Users/7times6/Dropbox/Camera Uploads/droidconse'
dOut = '/Users/7times6/Downloads/droidconse_small'


from PIL import Image
import os
import imtools

# create thumbnail

for f in [x for x in os.listdir(dIn) if x.endswith('.jpg')]:
    print f
    filein = os.path.join(dIn, f)
    fileout = os.path.join(dOut, f)
    image = Image.open(filein)
    width = 640
    h, w = image.size
    height = h * width/w
    size = (height, width)
    imtools.im_resize(image, size).save(fileout)

