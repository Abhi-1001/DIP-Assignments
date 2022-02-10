# %%
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

# %%
def imrotate(img, ang, point):
    rad = (math.pi*ang)/180
    sine = math.sin(rad)
    cosine = math.cos(rad)
    w, h, l = img.shape
    xc = point[0]//2
    yc = point[1]//2
    res = np.zeros((w,h,l))
    for k in range(l):
        for i in range(w):
            for j in range(h):
                x = int((i - xc)*cosine + (j - yc)*sine)
                y = int(-(i - xc)*sine + (j - yc)*cosine)
                xs = math.floor(x)
                ys = math.floor(y)
                a = x - xs
                b = y - ys
                idx_x = xs + xc
                idx_y = ys + yc
                if i+1<w and j+1<h and idx_x>=0 and idx_y>=0 and idx_x + 1 <w and idx_y + 1<h:
                    res[i][j][k] = (1-a)*(1-b)*img[idx_x][idx_y][k] + (1-a)*b*img[idx_x][idx_y+1][k] + (1-b)*a*img[idx_x+1][idx_y][k] + a*b*img[idx_x+1][idx_y+1][k]
    res = res.astype(np.int32)
    return res

# %%
pisa = cv2.imread("./PISA.jpg",1)
img = cv2.cvtColor(pisa, cv2.COLOR_BGR2RGB)
cv2.imshow('pisa',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
ang = 8
point = (113, 153)
res = imrotate(img, ang, point)
res.shape
plt.figure(figsize=(20,20))
plt.subplot(1,2,2)
plt.imshow(res)
plt.show()
# %%
