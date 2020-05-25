from ImagePyramid.pyramid import scale_pyramid
from SlidingWindow import Sliding_Window
import argparse
import time
import cv2

"""-------------------------------------------------load the image--------------------------------------------------"""
# read image
image_path = ('ME2.jpg')
image = cv2.imread(image_path)
"""--------------------------------------define the window width and height------------------------------------------"""
(winH, winW) = (50, 50)

"""------------------------------------loop over each pyramid level with sliding window------------------------------"""
# creat pyramid levels
for (pyramid_level, scaled_image) in enumerate(scale_pyramid(image, scale=1.5)):
    """
    scaled_image: each level in pyramid
    stepsize=30: skip 30 pixels in both x, y directions each iteration 
    windowsize=(winW, winH): our boundary box with (height = 100, width = 100)
    this function returns: x-coordinate value, y-coordinate value, and boundary box from each iteration 
    then we save them in : x, y, and boundary_box variables respectively  
    """
    for (x, y, boundary_box) in Sliding_Window(scaled_image, stepsize=30, windowsize=(winH, winW)):
        """
        check if boundary box bigger or smaller than window size, ignore this iteration (ignore this box)
        and go to next iteration and extract next box.
        if box = window size print it. 
        """
        if boundary_box.shape[0] != winH or boundary_box.shape[1] != winW:
            continue

        """
        this area where you can process your boundary box,
        applying ML classifier to classify the contents of your box
        """
        # for now, we do not have a classifier, we'll just draw the window
        """-------------------------------------------Draw The Window------------------------------------------------"""

        """
        take a copy from original image to make changes on it (add boundary box to it) without changing the original.
        """
        image_copy = scaled_image.copy()

        """
        draw boundary box using rectangle() method:
        cv2.rectangle(image, start_point, end_point, color, thickness)
        Parameters:
        1- image: It is the image on which rectangle is to be drawn.
        2- start_point: It is the starting coordinates of rectangle. 
        The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
        3- end_point: It is the ending coordinates of rectangle. 
        The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
        4- color: It is the color of border line of rectangle to be drawn.
        For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
        5- thickness: It is the thickness of the rectangle border line in px. 
        Thickness of -1 px will fill the rectangle shape by the specified color.
        """
        cv2.rectangle(image_copy, (x,y), (x+winW, y+winH), (0, 255, 0), 2)

        """
        each iteration do this:
        1- "Layer {}".format(pyramid_level+1): print image with label "Layer pyramid_level number"
        2- resized: print resized image
        """
        cv2.imshow("Layer {}".format(pyramid_level+1) + "and Sliding Window", image_copy)
        """
        cv2.waitKey(specified milliseconds)
        The function waits for specified milliseconds for any keyboard event. 
        If you press any key in that time, the program continues. Otherwise window will close
        If 0 is passed, it waits indefinitely for a key stroke.
        Note: move from frame to next frame in this time (refresh frame every 1 millisecond in case no keyboard event 
        occur in that time)
        """
        cv2.waitKey(1)

        """
        move from current frame to next frame with speed (cv2.waitKey(time)), and 
        stay in each frame for time (time.sleep(time))
        """

        """
        stop code for any period of time
        we use it here to see window in image
        Note: freeze current frame for this time. this doesn't care about changing frame time (waitkey(1)) 
        """
        time.sleep(0.05)



