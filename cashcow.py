import pyautogui as autogui
import time


def main():

    time.sleep(1)

    while True:
        for yV in range(684, 688, 70):
            for xV in range(296, 630, 70):
                autogui.click(xV, yV)


if __name__ == "__main__":
    main()
