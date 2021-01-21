import pyscreenshot as ImageGrab, Utils
import pyautogui, random, PIL
import time
import getGameStatus
import playCard

# screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
# while(True):

CANNOT_START_GAME = [968, 608]
StartGame_Position = [1380, 850]
HeroPower_Position = [1130, 830]
EndTurn_Position = [1600, 500]
Minion_From = [811, 1050]
Minion_To = [970, 200]  # [1400, 600]
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


import Hunter, Priest, DemonHunter, Shaman

class Game:
    def __init__(self):
        self.util = Utils.utils()

    def clicks(self):
        cap = random.randint(1, 2)
        for i in range(cap):
            self.sleepClick()

    def sleepClick(self):
        time.sleep(0.1)
        pyautogui.click()

    def heroPower(self):
        print("playing hero power")
        pyautogui.moveTo(HeroPower_Position[0], HeroPower_Position[1])
        self.sleepClick()

    def endTurn(self):
        print("Ending turn..")
        step = random.randint(2, 7)
        time.sleep(step)
        self.heroPower()
        self.click(EndTurn_Position)
        # pyautogui.moveTo(EndTurn_Position[0], EndTurn_Position[1])
        # sleepClick()

    def click(self, position):
        pyautogui.moveTo(position[0], position[1])
        self.sleepClick()

    def random_card_Position(self):
        # p1 = [560, 500]
        # p2 = [960, 500]
        # p3 = [1330, 500]
        rand = random.randint(0, 2)
        # if rand == 1: return p1
        # if rand == 2: return p2
        return self.util.RANDOM_CARD_POSITION[rand]

    def gameStatus0(self):
        print("unknown game status... wait for 4 seconds")
        self.click(StartGame_Position)
        self.click(confirmCards_Position)
        self.click(Reconnect_Position)
        time.sleep(4)


    def gameStatus1(self):
        # game starts, click confirm
        # self.click(self.random_card_Position())
        # self.click(self.random_card_Position())
        self.click(confirmCards_Position)

    def gameStatus2(self):
        print("game status... my turn")
        pyautogui.rightClick()

        # minions attack hero if possible
        for i in range(7):
            if not playCard.playHandCard(i): break
        for i in range(7):
            if not playCard.playBoardCard(i): break
        playCard.playHero()
        self.endTurn()

    def gameStatus3(self):
        # turn over, wait for opponent
        print("My turn ends..")
        self.endTurn()

    def gameStatus4(self):
        print("game status.. enemy turn, wait for 4 seconds")
        # self.click(StartGame_Position)
        # self.click(confirmCards_Position)
        self.click(Reconnect_Position)
        time.sleep(4)

    def gameStatus5(self):
        print("game status.. select a card")
        self.click(self.random_card_Position())
        # click(selectCard_Position)

    def gameStatus6(self):
        print("out side game.. start")
        self.click(CANNOT_START_GAME)
        self.click(StartGame_Position)

    def runGame(self, choice):
        choiceList = ['Hunter', 'Demon Hunter', 'Priest', 'Shaman']
        gameStatusList = ['Unknown', 'Confirm', 'My Turn', 'End Turn', 'Enemy Turn', 'Select Card', 'Oustide Game']
        print("running as %s.." % choiceList[choice])

        while (True):
            # start game
            print("getting game status..")
            rand = random.random()
            if rand < 0.2:
                print("emote..")
                playCard.emote()
            gameStatus = getGameStatus.getStatus()
            # 1 - Confirm
            # 2 - My turn
            # 3 - End turn
            # 4 - Enemy turn
            # 0 - UNknown

            print("game status = ... %s " % gameStatusList[gameStatus])
            if gameStatus == 0:
                # unkown status
                self.gameStatus0()

            if gameStatus == 1:
                # game starts
                self.gameStatus1()

            if gameStatus == 2:
                # my turn, play hand, board and hero
                pyautogui.rightClick()

                if choice == 0: Hunter.gameStatus2()
                if choice == 1: DemonHunter.gameStatus2()
                if choice == 2: Priest.gameStatus2()
                if choice == 3: Shaman.gameStatus2()

                time_remaining = 26
                for i in range(time_remaining):
                    time.sleep(1)
                    if i % 5 == 0: print("wating.. %d seconds left.." % (time_remaining - i))

            if gameStatus == 3:
                # end of turn
                self.gameStatus3()

            if gameStatus == 4:
                # enemy turn
                self.gameStatus4()

            if gameStatus == 5:
                # choice - select a card
                self.gameStatus5()

            if gameStatus == 6:
                # disconnected from game, confirm opponent cannot connect
                self.gameStatus6()
