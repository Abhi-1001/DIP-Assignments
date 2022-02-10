import cv2
import settings

videoCaptureObject = cv2.VideoCapture(0)
i = 1
while(i <= 100):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite(f"./images/Face_{i}.jpg",frame)
    i += 1
videoCaptureObject.release()
cv2.destroyAllWindows()