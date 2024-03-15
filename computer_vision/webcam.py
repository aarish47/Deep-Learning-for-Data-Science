import numpy as np 
import cv2 as cv 

# cap = cv.VideoCapture(0)
# if cap.isOpened():
#     ret, frame = cap.read()
# else:
#     ret = False
# while ret:
#     ret, frame = cap.read()
#     cv.imshow("webcam", frame)
#     if cv.waitKey(25) & 0xFF ==ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()

cap = cv.VideoCapture(0)

# change the cam into grayscale cam
while True:
    ret, frame = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow("webcam", gray_frame)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()