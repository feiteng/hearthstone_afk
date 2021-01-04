import pyautogui, random, PIL, time, sys

pack_position = [373, 486]
open_position = [1111, 498]
cardPositions = [[403, 365], [641, 365], [878, 365], [1126, 365],
                 [403, 753], [641, 753], [878, 753], [1126, 753]]

disenchant_Button = [799, 913]
disenchant_Confirm = [830, 640]

def moveTo(position):
    pyautogui.moveTo(position[0], position[1])

choice = 1

for i in range(len(cardPositions)):
    position = cardPositions[i]
    moveTo(position)
    pyautogui.rightClick()

    moveTo(disenchant_Button)
    pyautogui.click()
    moveTo(disenchant_Confirm)
    pyautogui.click()
    moveTo(disenchant_Button)
    pyautogui.click()
    pyautogui.click()
    pyautogui.rightClick()

    time.sleep(1)

