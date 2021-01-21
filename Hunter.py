import pyscreenshot as ImageGrab
import pyautogui, random, PIL
import time
import getGameStatus
import playCard

import Game

CANNOT_START_GAME = [968, 608]
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

def gameStatus2():
    print("game status... my turn")
    for i in range(7):
        if not playCard.playHandCard(i): break
    for i in range(7):
        if not playCard.playBoardCard(i): break
    playCard.playHero()
    playCard.heroPower()
    # time.sleep(15)

    # def runGame(self):
    #     # game = Game.Game()
    #     print("running as Hunter..")
    #     while (True):
    #         # start game
    #         print("getting game status..")
    #         gameStatus = getGameStatus.getStatus()
    #         # 1 - Confirm
    #         # 2 - My turn
    #         # 3 - End turn
    #         # 4 - Enemy turn
    #         # 0 - UNknown
    #
    #         print("game status = ... %d " % gameStatus)
    #         if gameStatus == 0:
    #             self.gameStatus0()
    #
    #         if gameStatus == 1:
    #             self.gameStatus1()
    #         if gameStatus == 2:
    #             self.gameStatus2()
    #
    #             # minions attack hero if possible
    #             for i in range(7):
    #                 if not playCard.playHandCard(i): break
    #             for i in range(7):
    #                 if not playCard.playBoardCard(i): break
    #             playCard.playHero()
    #             self.endTurn()
    #
    #         if gameStatus == 3:
    #             self.gameStatus3()
    #
    #         if gameStatus == 4:
    #             self.gameStatus4()
    #
    #         if gameStatus == 5:
    #             self.gameStatus5()
    #
    #         if gameStatus == 6:
    #             self.gameStatus6()