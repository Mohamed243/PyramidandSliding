from pyramid import scale_pyramid
import argparse #this library to build command line interfaces
import cv2      #to import images and read them

# Pyramid code 
"""-------------------------------------------------load the image--------------------------------------------------"""
image_path = ('ME.jpg')
image = cv2.imread(image_path)
"""--------------------------------------Loop over the image pyramid------------------------------------------------"""
"""
 enumerate(): to keep a count of iterations. it returns tuple (iteration number, value or object)
                                                              ( 1 iteration, first  pyramid image/level) 
                                                              ( 2 iteration, second pyramid image/level)
 we loop over pyramid levels and save "number of iteration/pyramid level- starts from 0" in pyramid_level
                             and save "resized image/scaled image"                       in resized
 
 provide these arguments to pyramid function which imported in first line:
 1- image: image path which saved from args dictionary key 'image'.                             
 2- scale=args["scale"]: read scale factor from args dictionary key 'scale'. if user doesn't write it, the default = 1.5
"""
for (pyramid_level, resized) in enumerate(scale_pyramid(image, scale=1.5)):
    """
     each iteration do this:
     1- "Layer {}".format(pyramid_level+1): print image with label "Layer pyramid_level number"
     2- resized: print resized image
    """
    cv2.imshow("Layer {}".format(pyramid_level+1), resized)
    """
    cv2.waitKey(specified milliseconds)
    The function waits for specified milliseconds for any keyboard event. 
    If you press any key in that time, the program continues. 
    If 0 is passed, it waits indefinitely for a key stroke.
    """
    cv2.waitKey(0)
"""----------------------------------------------close all windows-----------------------------------------------"""
"""
program waits for any key press in specified milliseconds in cv2.waitKey() function above
If you press any key in that time, the program continues to this line and close all windows  
cv2.destroyAllWindows(): simply destroys all the windows we created
"""
cv2.destroyAllWindows()


