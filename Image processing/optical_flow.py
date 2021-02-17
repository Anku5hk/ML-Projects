"""
THis simple program allows to select a point, then track its motion/optical flow. Press escape to stop.

"""
import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Home/Downloads/vid.mp4") # just change the path 
_, old_frame = cap.read()
old_frame_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

lk_params = dict(
winSize = (10, 10),
maxLevel = 4,
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

point_selected = False
mask = np.zeros_like(old_frame) # empty mask for drawing line

# to return point to track from
def point(event,x,y,flags,params):
    global old_points, points, point_selected
    if event == cv2.EVENT_LBUTTONDOWN:
        points = (x,y)
        point_selected = True
        old_points = np.array([[x,y]], dtype=np.float32)

cv2.namedWindow("Select point")
cv2.setMouseCallback("Select point", point)        

while 1:
    _ , frame = cap.read()
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if point_selected:
        current_points, status, error = cv2.calcOpticalFlowPyrLK(old_frame_gray, new_frame, old_points, None, **lk_params)

        x, y = current_points.ravel()
        mask = cv2.line(mask, points, (x,y), [0,0,255], 1)    

        old_frame_gray = new_frame.copy()
        old_points = current_points

        frame = cv2.add(frame, mask) # add to original frame

    cv2.imshow("Select point", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
