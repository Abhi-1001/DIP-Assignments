# In[0]:
import cv2
import os
import numpy as np
from sklearn.metrics import mean_squared_error as mse
import math
import matplotlib.pyplot as plt

# In[1]:

# Reference Image
ref_image = cv2.imread("./images/Face_1.jpg", 1)
ref_image_grey = cv2.imread("./images/Face_1.jpg", 0)
cv2.imshow("myface", ref_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[2]:

# load all images in RGB and GREY_SCALE
rgb_images = []
gs_images = []
path = "./images/"
for image in os.listdir("./images/"):
    image_path = path + str(image)
    if image_path == "./images/Face_1.jpg":
        continue
    rgb_image = cv2.imread(image_path, 1)
    gs_image = cv2.imread(image_path, 0)
    rgb_images.append(rgb_image)
    gs_images.append(gs_image)

# In[2]:

# calculate RSME values

ref_image = ref_image
ref_image_grey = ref_image_grey.flatten()

RMSE = []
for image in rgb_images:
    error = 0
    for i in range(3):
        error += mse(ref_image[:,:,i].flatten(), image[:,:,i].flatten())
    RMSE.append(math.sqrt(error / 3))

RMSE_GREY = []
for image in gs_images:
    image = image.flatten()
    RMSE_GREY.append(math.sqrt(mse(ref_image_grey, image)))

# %%

# rgb plot
# y,binEdges=np.histogram(RMSE,bins=255)
# bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
# plt.plot(bincenters,y,'-')
# plt.hist(RMSE, bins = 255)
plt.plot(RMSE)
plt.xlabel('Index')
plt.ylabel('RMSE')
plt.show()


# %%

# grey scale plot
# y,binEdges=np.histogram(RMSE_GREY,bins=255)
# bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
# plt.plot(bincenters,y,'-')
# plt.hist(RMSE_GREY, bins = 255)
plt.plot(RMSE_GREY)
plt.xlabel('Index')
plt.ylabel('RMSE')
plt.show()
# %%

# error difference
for i in range(100):
    print(RMSE[i] - RMSE_GREY[i])

# both are supposed to be the same

# %%
plt.plot(RMSE)
