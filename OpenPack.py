import pyautogui, random, PIL, time, sys

pack_position = [373, 486]
open_position = [1111, 498]
pack = [[822,395],[1106,283],[1416,370],[928,771],[1260,779]]
confirm_position = [1112, 539]

def moveTo(position):
    pyautogui.moveTo(position[0], position[1])

choice = 1
try:
    input = sys.argv
    choice = int(input[1])
except:
    pass


for i in range(choice):
    moveTo(pack_position)

    pyautogui.mouseDown(button='left')

    pyautogui.dragTo(open_position[0], open_position[1], duration=0.4)#, button='left')
    time.sleep(1.5)
    moveTo(confirm_position)
    pyautogui.click()
    time.sleep(2)
    for j in range(5):
        moveTo(pack[j])
        pyautogui.click()

    time.sleep(2)
    moveTo(confirm_position)
    pyautogui.click()
