"""
Detect global motion 

"""
import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Nikhil/Downloads/vidd(0).mp4") # just change the path 
_, old_frame = cap.read()
old_frame_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

fb_params = dict(flow=None, pyr_scale = 0.5,
levels = 5, winsize = 9,
iterations = 5, poly_n = 5,
poly_sigma = 1.1, flags = 0
)

mask = np.zeros_like(old_frame) # empty mask for drawing points    
mask[..., 1] = 255

while 1:
    _ , frame = cap.read()
    new_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # returns flow which is opt flow vetor(u,v)
    flow = cv2.calcOpticalFlowFarneback(old_frame_gray, new_frame_gray, **fb_params)

    # we then calculate thier mag and angle
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    mask[..., 0] = angle*180/np.pi/2  
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # convert heu to bgr
    bgr_mask = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

    dense_flow = cv2.addWeighted(frame, 1,bgr_mask, 2, 0)

    old_frame_gray = new_frame_gray
    cv2.imshow("show", dense_flow)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
