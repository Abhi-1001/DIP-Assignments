# In[1]:
import cv2
import matplotlib.pyplot as plt
import numpy as np

# %%

# Load Image
lena_grey = cv2.imread("./Lena.png", 0)
cv2.imshow("lena", lena_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%

# Resized lena images
img1 = cv2.resize(lena_grey, (128, 128))
img2 = cv2.resize(lena_grey, (64, 64))
img3 = cv2.resize(lena_grey, (32, 32))
img4 = cv2.resize(lena_grey, (16, 16))
# %%

# Aliasing is sampling a signal by changing its parameters but indistinguishable from the original
# Display images with different sizes
titles = ['Original','128X128', '64X64','32X32', '16X16']
images =[lena_grey, img1, img2, img3, img4]

# quality reduces, details are lost
for i in range(5):
    plt.subplot(2, 3, i+1) 
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis("off")


# %%
def modify_intensity(gray,scale):
    s = gray.shape
    res = np.zeros(s)
    max = np.max(gray) 
    min = np.min(gray) 
    i_range = max-min   
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            val = gray[i][j] - min
            val = val / i_range
            val = val * scale 
            val = int(round(val))
            res[i][j] = val
    res = res.astype('uint8') 
    return res

# %%

# False Contouring
# Display images with different intensities, Quantization
titles = ["0-255", "0-127", "0-63", "0-31", "0-15", "0-7", "0-3", "0-1"]
fig = plt.figure(1, (8,8))
# contrast reduces, loss in sense of texture
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(modify_intensity(lena_grey, pow(2, 8 - i) - 1), cmap = 'gray')
    plt.title(titles[i])
    plt.axis("off") 

# %%
