import numpy as np
from PIL import ImageChops
from pyscreenshot import grab
import cv2
from acceptTrade import accept  # Assuming you have an accept function in acceptTrade module


class TradeBot:

    def __init__(self, threshold=0.8, currentStage=None):

        self.threshold = threshold
        self.currentStage = currentStage
        self.im = grab()

    def detect_trade(self, img):
        new_img = grab()
        diff = ImageChops.difference(new_img, self.im)
        bbox = diff.getbbox()

        if bbox is not None:  # Exact comparison
            reference_image = cv2.cvtColor(np.array(new_img), cv2.COLOR_RGB2BGR)
            target_image = cv2.imread(img)

            result = cv2.matchTemplate(target_image, reference_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val > self.threshold:
                print("Trade detected")
                self.im = new_img
                return True

        return False

    def perform_trade(self):

        if self.detect_trade('pets2/tradeOfferImg.png'):
            self.currentStage = "tradeReceived"
            accept()
            self.currentStage = "tradeAccepted"


if __name__ == "__main__":
    bot = TradeBot(threshold=0.8, currentStage=None)

    while True:
        bot.perform_trade()

        print(bot.currentStage)
