import pyscreenshot as ImageGrab
import pyautogui, random, PIL
import time
import getGameStatus
import playCard

# screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
# while(True):

StartGame_Position = [1380, 850]
HeroPower_Position = [1130, 830]
EndTurn_Position = [1600, 500]
Minion_From = [811, 1050]
Minion_To = [970, 200] # [1400, 600]
Minion_Initial_Pos = [930, 580]
Enemy_Minion_Position = [937, 405]
Hero_Position = [960, 770]
Enemy_Hero_Position = [970, 200]
Reconnect_Position = [800, 830]
confirmCards_Position = [950, 850]

# pyautogui.moveTo(StartGame_Position[0], StartGame_Position[1])
# time.sleep(1)
# pyautogui.moveTo(HeroPower_Position[0], HeroPower_Position[1])
# time.sleep(1)
# pyautogui.moveTo(EndTurn_Position[0], EndTurn_Position[1])


def clicks():
    cap = random.randint(1, 2)
    for i in range(cap):
        sleepClick()

def sleepClick():
    time.sleep(0.1)
    pyautogui.click()



def heroPower():
    pyautogui.moveTo(HeroPower_Position[0], HeroPower_Position[1])
    sleepClick()

def endTurn():
    print("Ending turn..")
    step = random.randint(2, 7)
    time.sleep(step)
    heroPower()
    click(EndTurn_Position)
    # pyautogui.moveTo(EndTurn_Position[0], EndTurn_Position[1])
    # sleepClick()


def click(position):
    pyautogui.moveTo(position[0], position[1])
    sleepClick()

def random_card_Position():
    p1 = [560, 500]
    p2 = [960, 500]
    p3 = [1330, 500]
    rand = random.randint(1, 3)
    if rand == 1: return p1
    if rand == 2: return p2
    return p3

while (True):
    # start game
    print("getting game status..")
    gameStatus = getGameStatus.getStatus()
    # 1 - Confirm
    # 2 - My turn
    # 3 - End turn
    # 4 - Enemy turn
    # 0 - UNknown

    print("game status = ... %d " % gameStatus)
    if gameStatus == 0:
        print("unknown game status... wait for 4 seconds")
        click(StartGame_Position)
        click(confirmCards_Position)
        click(Reconnect_Position)
        time.sleep(4)
    if gameStatus == 1:
        # game starts, click confirm
        click(confirmCards_Position)
    if gameStatus == 2:
        print("game status... my turn")
        pyautogui.rightClick()
        # randomMoves()
        # heroAttack()

        # minions attack hero if possible
        for i in range(7):
            if not playCard.playHandCard(i): break
        for i in range(7):
            if not playCard.playBoardCard(i): break
        playCard.playHero()

        endTurn()
    if gameStatus == 3:
        # turn over, wait for opponent
        print("My turn ends..")
        endTurn()
    if gameStatus == 4:
        print("game status.. enemy turn, wait for 4 seconds")
        click(StartGame_Position)
        click(confirmCards_Position)
        click(Reconnect_Position)
        time.sleep(4)

    if gameStatus == 5:
        print("game status.. select a card")
        click(random_card_Position())
        # click(selectCard_Position)

