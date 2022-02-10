# %% 
import cv2
import numpy as np
import math

# %%

def rotate_image(image, angle, point):
  rot_mat = cv2.getRotationMatrix2D(point, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# %%
img = cv2.imread("./PISA.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
# angle = (127, 43) - (113, 153)
bottom = (115, 154)
top = (128, 45)
angle = -(top[1]- bottom[1]) / (top[0] -bottom[0])
new_img = rotate_image(img , angle, bottom)
cv2.imshow("image", new_img)
cv2.imwrite("./not_leaning_anymore_pisa.jpg", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(90 - math.degrees(math.atan(angle)))
# %%
