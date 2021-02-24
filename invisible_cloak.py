import numpy as np
from cv2 import cv2

print("""
Harry :  Hey !! Would you like to try my invisibility cloak ??
         Its awesome !!
        
         Prepare to get invisible .....................
    """)

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()         # TAKE EACH FRAME

    if ret :
        # HOW TO CONVERT RGB TO HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        # THRESHHOLD THE HSV VALUES TO GET ONLY RED COLOR.
        l_red = np.array([0,100,100])           # LOWER RANGE
        u_red = np.array([10, 255, 255])        # UPPER RANGE

        mask = cv2.inRange(hsv, l_red, u_red)
        # ALL THINGS RED
        part1 = cv2.bitwise_and(back, back, mask=mask)

        mask =  cv2.bitwise_not(mask)
        # ALL THINGS NOT RED
        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("cloak", part1 + part2)
        
        if cv2.waitKey(5) == ord('q'):          # PRESS 'Q' TO EXIT
            break

cap.release()
cv2.destroyAllWindows()

