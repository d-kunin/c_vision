__author__ = '7times6'

import os
from PIL import Image
import numpy as np


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def im_resize(im, sz):
    pil_im = Image.fromarray(np.uint8(im))
    return pil_im.resize(sz)


def histeq(im, nbr_bins=256):
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]  # normalize
    im_interp = np.interp(im.flatten(), bins[:-1], cdf)  # linear interpolation of cdf

    return im_interp.reshape(im.shape), cdf


def compute_average(imlist):
    averageim = np.array(Image.open(imlist[0]), 'f')
    for iname in imlist[1:]:
        try:
            averageim += np.array(Image.open(iname), 'f')
        except:
            print iname + ' skipped'
    averageim /= len(imlist)

    return np.array(np.uint8(averageim))