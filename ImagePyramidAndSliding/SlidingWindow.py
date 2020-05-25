
"""
image: image path that we are going to loop over it with window
stepsize: The stepSize indicates how many pixels we are going to “skip” in both the (x, y) direction.
In practice, it’s common to use a stepSize of 4 to 8 pixels.
Remember, the smaller your step size is, the more windows you’ll need to examine.
windowsize: defines the width and height (in terms of pixels) of the window we are going to extract from our image.
"""
def Sliding_Window (image, stepsize, windowsize):

    """
    in y-direction start window from y = 0 to y = maximum image height with step = step size
    """
    for y_co in range (0, image.shape[0], stepsize):
        """
        in x-direction start window from x = 0 to x = maximum image width with step = step size
        Note: after x loop reaches maximum image width, y loop increased by step size and repeat x loop again
        and so on till x and y reach the maximum image width and maximum image height respectively.  
        """
        for x_co in range(0, image.shape[1], stepsize):
            """
            :returns from image:
            1- x,y: the x and y coordinates of the sliding window
            2- boundary box: we use this "image[y_co:y_co + windowsize[1], x_co:x_co + windowsize[0]]" to crop image
            height = from "y_co --> the current y position" to "y_co + windowsize[1] --> the end of the window height"
            width =  from "x_co --> the current x position" to "x_co + windowsize[0] --> the end of the window width "
            if we have window: height = 30, width = 30 with step size = 5 
            in first loop : window = "height = 0:30, width = 0:30"
            in second loop: window moves in x with 5 pixels, then start = 5 and the end = 30 + 5 = 35
            window = "height = 0:30, width = 5:35" --> height doesn't change because we still in the same row of image
            ------------------
            after first row finishes:
            window = "height = 5:35, width = 0:30" --> width back to initial value because we back to the first column 
            of the image. 
            
            we save the position from previous iteration to the next one by "yield" 
            """
            yield (x_co,y_co, image[y_co:y_co + windowsize[1], x_co:x_co + windowsize[0]])

