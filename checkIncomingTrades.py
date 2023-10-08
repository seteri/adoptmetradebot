
import numpy as np
from PIL import ImageChops  # $ pip install pillow
from pyscreenshot import grab  # $ pip install pyscreenshot
import cv2
from acceptTrade import accept
threshold = 0.8  # Adjust the threshold as needed
im = grab()

while True:
    newImg = grab()
    diff = ImageChops.difference(newImg, im)
    bbox = diff.getbbox()

    if bbox is not None:

        reference_image = cv2.cvtColor(np.array(newImg), cv2.COLOR_RGB2BGR)
        target_image = cv2.imread('pets2/tradeOfferImg.png')
        result = cv2.matchTemplate(target_image, reference_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > threshold:
            print("treidi movida")
            accept()
            x, y = max_loc
        im = newImg
