# import nedded packsges
import imutils

"""--------------------------------------creat pyramid function------------------------------------------"""
"""
three arguments:
1- the image 
2- scale: controls by haow much the image is resized at each level 
    A small scale yields more layers in the pyramid. 
    And a larger scale yields less layers.
3- minSize: the minimum required width and height of the layer (width, height). 
    If an image in the pyramid falls below this minSize, we stop constructing the image pyramid.
"""
def scale_pyramid(image, scale=1.5, minSize=(30, 30)):
    """
    - yield the original image: start from the last image saved in previous iteration.
    - Not start with the original image
    - yields the original image in the pyramid (the bottom layer)
    """
    yield image

    # Looping over the pyramid
    while True:
        # compute the new dimensions of the image and resize it
        """
        image.shape : get dimensions of image
        it returns list of dimensions [Height, Width, Number of channels]
        image.shape[1] / scale: divide Width which is at index [1] by scale which is second pyramid function argument
        to reduce the size of image
        int(image.shape[1] / scale): use int() to take the integer number from divide operation and ignore floating part
        new_width: save new width in this variable 
        """
        new_width = int(image.shape[1] / scale)

        #imutils.resize(image, width=new_width): resize image with new width and save it in image
        image = imutils.resize(image, width=new_width)

        # if the resized image does not meet the supplied minimum
        # size, then stop constructing the pyramid
        """
        if height of the image less than minimum height which given in third pyramid function argument
        or width  of the image less than minimum width  which given in third pyramid function argument
        then stop constructing the pyramid
        """
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        # yield the next image in the pyramid
        # take this resized image and construct next pyramid image (level)
        yield image


