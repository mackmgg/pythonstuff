from exif import Image
import os
import matplotlib.pyplot as plt

lens = []
g5x = []
slr = []

directory = '/Users/mack/Pictures/2020' # Directory to search, will search recursively

for root, subdirs, files in os.walk(directory):
  files = [ fi for fi in files if fi.endswith(".JPG") ]
  for fi in files:
    f = open(root+'/'+fi, 'rb')
    pic = Image(f)
    
    crop_factor = (1.415/(pic.pixel_x_dimension / pic.focal_plane_x_resolution))
    lens.append(pic.focal_length*crop_factor)
    if crop_factor > 2: # G5x has ~2.7x crop factor
      g5x.append(pic.focal_length*crop_factor)
    else:
      slr.append(pic.focal_length*crop_factor)

plt.hist(lens, 100)
plt.show()
