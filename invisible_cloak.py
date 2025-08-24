import numpy as np
import cv2

print("""
Harry :  Hey !! Would you like to try my invisibility cloak ??
         Its awesome !!
        
         Prepare to get invisible .....................
""")

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')   # Make sure image.jpg (your background) exists!

while cap.isOpened():
    ret, frame = cap.read()         # TAKE EACH FRAME

    if ret:
        # Convert frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold the HSV values to get only BLUE color
        lower_blue = np.array([94, 80, 2])        # LOWER RANGE
        upper_blue = np.array([126, 255, 255])    # UPPER RANGE

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # All things BLUE → replaced with background
        part1 = cv2.bitwise_and(back, back, mask=mask)

        # All things NOT BLUE → stay as original
        mask_not = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask_not)

        # Final output
        cv2.imshow("cloak", part1 + part2)
        
        if cv2.waitKey(5) == ord('q'):          # PRESS 'Q' TO EXIT
            break

cap.release()
cv2.destroyAllWindows()
