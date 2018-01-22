
import pyscreenshot as ImageGrab
import pyautogui as autogui
import time
from PIL import ImageChops

# from https://stackoverflow.com/questions/35176639/compare-images-python-pil
def imEqual(im1, im2):
  return ImageChops.difference(im1, im2).getbbox() is None

def main():
    autogui.click(480,400)
    prevIm = ImageGrab.grab(bbox=(440, 430, 30, 30))
    same = False
    autogui.click(480,680)
    time.sleep(0.1)
    count = 0;
    while True:
        count = count +1;
        im = ImageGrab.grab(bbox=(440, 430, 30, 30))
        if(imEqual(im,prevIm)):
            autogui.click(570, 660)
            same = True
        else:
            autogui.click(400, 650)
            same = False

        if (count<120):
            sleepTime = 0.5
        else:
            sleepTime = 0.3

        print( str(count)+ " " + str(same) + " "  + str(sleepTime))
        time.sleep(sleepTime)

        prevIm = im


if __name__ == "__main__":
    main()
