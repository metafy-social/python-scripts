
 import numpy as np
 import matplotlib.pyplot as plt
 import matplotlib.image as mpimg

 def rgb2gray(png_file='file_example.png'):
     img = mpimg.imread(png_file)
     gray = np.dot(img[:,:,:3], [0.2989, 0.5870, 0.1140])
     plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
     plt.axis('off')
     plt.savefig('gray_' + png_file + '.png', dpi=300)
