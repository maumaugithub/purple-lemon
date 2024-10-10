from scipy.datasets import face
import matplotlib.pyplot as plt

img = face()
print(f'image dimension: {img.ndim}D')

ires = img[:, :, 0].shape
print(f'image resolution: {ires}')

img_rgb_array = img / 255

img_red_array = img_rgb_array[:, :, 0]
img_green_array = img_rgb_array[:, :, 1]
img_blue_array = img_rgb_array[:, :, 2]


plt.imshow(img)
plt.show()
