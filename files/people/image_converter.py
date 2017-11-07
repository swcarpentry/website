#!/usr/bin/env python

"Resize an image (by default, so that width is 120 pixels)."

import sys
from PIL import Image

SCALE = 120

if len(sys.argv) == 3:
    infile, outfile = sys.argv[1:3]
elif len(sys.argv) == 4:
    infile, outfile, SCALE = sys.argv[1:4]
    SCALE = int(SCALE)
else:
    assert False, 'usage: resize infile outfile [x_dim]'

src = Image.open(infile)
src_x, src_y = src.size
dst_y = int(src_y * SCALE / src_x)
dst_x = SCALE
print('({0}, {1}) => ({2}, {3})'.format(src_x, src_y, dst_x, dst_y))
dst = src.resize((dst_x, dst_y), Image.ANTIALIAS)
dst.save(outfile)
