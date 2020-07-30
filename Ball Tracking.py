import argparse
from collections import deque
from imutils.video import VideoStream
import time
import imutils
import cv2
import numpy as np

ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", help="path to the video file I'm not using right now")
ap.add_argument("-b", "--buffer", type=int, default=30, help="maximum buffer size")
args = vars(ap.parse_args())

# Define the upper and lower boundaries of the shade of green for the ball.
green_upper = (64, 255, 255)
green_lower = (29, 86, 6)

# Initialize the list of tracked points
pts = deque(maxlen=args["buffer"])

# Reference the webcam
vs = VideoStream(src=0).start()

# Allow the webcam to warm up a bit
time.sleep(2.0)

while True:
    frame = vs.read()                    # Read the current frame

    if frame is None:
        break

    # Resize the frame, blur it and convert it to the HSV colour space
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Create a mask for the colour green then remove any blobs in the mask
    mask = cv2.inRange(hsv, green_lower, green_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours of the ball and the ball's centre point (x, y).
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    centre = None

    if len(contours) > 0:     # Once at least one contour is found
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and centroid.
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        centre = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            # draw the circle and centroid on the frame, then update
            # the list of tracked points.
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, centre, 2, (0, 0, 255), -1)

    pts.appendleft(centre)

    for i in range(1, len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue
        thickness = int(np.sqrt(args["buffer"] / float(i+10)) * 2.5)
        cv2.line(frame, pts[i-1], pts[i], (255, 0, 0), thickness)

    # Show the frame to the screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to stop the loop and quit the programme
    if key == ord("q"):
        break

# Stop the camera
vs.stop()

# Close the window
cv2.destroyAllWindows()
