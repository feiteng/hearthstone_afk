import pyscreenshot as ImageGrab
import pyautogui, random, PIL, time, sys

pack_position = [373, 486]
open_position = [1111, 498]

white_card = [200, 215, 233]
blue_card = [78, 130, 200]

cardPositions = [[400, 370], [646, 367], [883, 369], [1130, 368],
                 [401, 750], [642, 750], [884, 750], [1125, 750]]

disenchant_Button = [799, 913]
disenchant_Confirm = [830, 640]

def moveTo(position):
    pyautogui.moveTo(position[0], position[1])

def distance(g1, g2):
    sum = 0
    for i in range(3):
        sum += (g1[i] - g2[i]) ** 2
    # print(g1)
    # print(g2)
    # print("distance.. %d" % sum)
    return sum

def getColor(rgb):
    err = 5000
    if distance(rgb, white_card) < err: return 'white'
    if distance(rgb, blue_card) < err : return 'blue'
    return 'unknown'


def color(position):
    px = position[0]
    py = position[1]
    im = ImageGrab.grab(bbox=(px, py, px + 5, py + 5))  # X1,Y1,X2,Y2
    im.save('Destrcut Card @ %d %d' % (px, py) + '.jpg')
    cordinate = 0, 0
    r, g, b = im.getpixel(cordinate)
    return getColor([r, g, b])



# 0 Hunter
# 1 Demon Hunter
# 2 Priest



limit = 6
try:
    input = sys.argv
    limit = int(input[1])
except:
    pass
# Game.Game().runGame(choice)


for i in range(limit):
    # im = ImageGrab.grab(bbox=(0, 0, 1820, 1070))  # X1,Y1,X2,Y2
    position = cardPositions[0]
    # print(color(position))
    moveTo(position)
    pyautogui.rightClick()
    #
    moveTo(disenchant_Button)
    pyautogui.click()
    moveTo(disenchant_Confirm)
    pyautogui.click()
    # moveTo(disenchant_Button)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.click()
    # moveTo(disenchant_Confirm)
    # pyautogui.click()

    time.sleep(0.75)

