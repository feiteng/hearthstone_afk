import pyscreenshot as ImageGrab
import pyautogui, random, PIL
import time, Utils
import getGameStatus

Minion_To = [970, 200] # [1400, 600]
TauntColor = [236, 227, 217]
Hero_Position = [960, 770]
Enemy_Hero_Position = [970, 200]
HeroPower_Position = [1130, 830]

util = Utils.utils()


def heroPower():
    pyautogui.moveTo(HeroPower_Position[0], HeroPower_Position[1])
    pyautogui.click()

def playHero():
    print("Hero attack..")
    pyautogui.moveTo(Hero_Position[0], Hero_Position[1])
    pyautogui.click()
    pyautogui.moveTo(Enemy_Hero_Position[0], Enemy_Hero_Position[1])
    pyautogui.click()
    # if taunted then attack minions
    for minion_x in range(560, 1500, 138):
        pyautogui.moveTo(minion_x, 430)
        # time.sleep(0.25)
        pyautogui.click()
    # im = ImageGrab.grab(bbox=(400, 430, 1500, 460))  # X1,Y1,X2,Y2

def playBoardCard(i):
    card = []
    # y = 530
    im = ImageGrab.grab(bbox=(490, 510, 1500, 540))  # X1,Y1,X2,Y2
    # im.save("Board_" + str(i) + ".png")
    foundGreenCard = False
    for x in range(0, 1000, 10):
        cordinate = x, 15
        r, g, b = im.getpixel(cordinate)
        if isGreen([r, g, b]):
            foundGreenCard = True
            card.append(x)

    if not foundGreenCard:
        print("no more board card... exiting")
        return False
    print("play board card... ")
    # print(card)
    # for card_x in card:
        # print(card_x + 490)
    pos = random.randint(0, len(card) - 1)
    # print(pos)
    card_x = card[pos]
    card_y = 580
    pyautogui.moveTo(card_x + 490, card_y )
    # print("%d %d" % (card_x + 650, card_y))
    pyautogui.click()
    # time.sleep(.5)
    pyautogui.moveTo(Minion_To[0], Minion_To[1])
    pyautogui.click()
    # determine if a taunt minion exists
    im = ImageGrab.grab(bbox=(1111, 696, 1115, 700))  # X1,Y1,X2,Y2
    cordinate = 0, 0
    r, g, b = im.getpixel(cordinate)
    tauntStatus = False # taunt or rush
    if isTaunt([r, g, b]): tauntStatus = True
    if tauntStatus:
        # pyautogui.rightClick()
        for minion_x in range(560, 1500, 138):
            pyautogui.moveTo(minion_x, 430)
            # time.sleep(0.25)
            pyautogui.click()
        # im = ImageGrab.grab(bbox=(400, 430, 1500, 460))  # X1,Y1,X2,Y2


    # print(tauntStatus)
    # find next available taunt minion

    return True

def isTaunt(rgb):
    TauntColor = [236, 227, 217]
    sum = 0
    for i in range(3):
        sum += (rgb[i] - TauntColor[i]) ** 2
    return sum < 5000

def isYellow(rgb):
    yellow = [255, 255, 33]
    sum = 0
    for i in range(3):
        sum += (rgb[i] - yellow[i]) ** 2
    return sum < 5000

def isGreen(rgb):
    endTurn = [33, 158, 3]
    sum = 0
    for i in range(3):
        sum += (rgb[i] - endTurn[i]) ** 2
    return sum < 5000

def playHandCard(i):
    card = []
    y = 1020
    im = ImageGrab.grab(bbox=(600, 1000, 1200, 1030))  # X1,Y1,X2,Y2
    # im.save("Hand_" + str(i) + ".png")
    foundGreenCard = False
    for x in range(0, 600, 5):
        cordinate = x, 15
        r, g, b = im.getpixel(cordinate)
        if isGreen([r, g, b]) or isYellow([r, g, b]):
            foundGreenCard = True
            card.append(x)

    # print(card)
    if not foundGreenCard:
        print("no more hand card... exiting")
        return False
    print("play hand card... ")

    pos = random.randint(0, len(card) - 1)
    # print(pos)
    card_x = card[pos]
    card_y = y
    pyautogui.moveTo(card_x + 620, card_y )
    # print("%d %d" % (card_x + 650, card_y))
    # time.sleep(.5)
    pyautogui.click()
    pyautogui.moveTo(Minion_To[0], Minion_To[1])
    pyautogui.click()

    # determine if impossible to play card
    im = ImageGrab.grab(bbox=(1111, 696, 1115, 700))  # X1,Y1,X2,Y2
    cordinate = 0, 0
    r, g, b = im.getpixel(cordinate)
    tauntStatus = False # taunt or rush
    if isTaunt([r, g, b]): tauntStatus = True
    if tauntStatus:
        # pyautogui.rightClick()
        for minion_x in range(560, 1500, 138):
            pyautogui.moveTo(minion_x, 430)
            # time.sleep(0.25)
            pyautogui.click()
        # im = ImageGrab.grab(bbox=(400, 430, 1500, 460))  # X1,Y1,X2,Y2


    return True

def moveTo(position):
    pyautogui.moveTo(position[0], position[1])

def emote():
    moveTo(util.HERO_POSITION)
    pyautogui.rightClick()
    emotes = util.EMOTE_POSITION
    rand = random.randint(0, len(emotes) - 1)
    moveTo(emotes[rand])
    pyautogui.click()


# for i in range(7):
#     playHandCard(i)

# for i in range(7):
# playBoardCard(0)