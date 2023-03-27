from PIL import Image
import numpy as np
im = Image.open("ronaldo1.bmp")
np_im = np.array(im)
print("Kich thuoc file anh: ", np_im.shape)
im.save("ronaldo1.bmp")