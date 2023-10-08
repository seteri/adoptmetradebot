import pyautogui


def accept():
    pyautogui.moveTo(1090, 652)
    pyautogui.click(clicks=1, duration=2)
    pyautogui.moveRel(8,8, 1)
    pyautogui.click(clicks=3,duration=2)


