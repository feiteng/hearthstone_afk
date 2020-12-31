import pyautogui, random, PIL, sys, time

Buy_Button = [1455, 812]
Confirm_Button = [965, 795]

def moveTo(position):
    pyautogui.moveTo(position[0], position[1])


try:
    input = sys.argv
    choice = int(input[1])
except:
    pass


for i in range(choice):
    moveTo(Buy_Button)
    pyautogui.click()
    time.sleep(0.5)
    moveTo(Confirm_Button)
    pyautogui.click()
