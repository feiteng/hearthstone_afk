import pyscreenshot as ImageGrab
import pyautogui, random, PIL, time, getGameStatus, playCard, Game, Utils

def gameStatus2():
    playCard.heroPower()
    for i in range(7):
        if not playCard.playHandCard(i): break

    for i in range(7):
        if not playCard.playBoardCard(i): break

    playCard.playHero()

    rand = random.randint(5, 15)
    time.sleep(rand)


    # def runGame(self):
    #     util = Utils.utils()
    #     print("running as Demon Hunter..")
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
    #             print("unknown game status... wait for 4 seconds")
    #             self.click(util.START_GAME_POSITION)
    #             self.click(util.CONFIRM_CARD_POSITION)
    #             self.click(util.RECONNECT_BUTTON_POSITION)
    #             time.sleep(4)
    #         if gameStatus == 1:
    #             # game starts, click confirm
    #             self.click(util.CONFIRM_CARD_POSITION)
    #         if gameStatus == 2:
    #             print("game status... my turn")
    #             pyautogui.rightClick()
    #             # minions attack hero if possible
    #
    #             for i in range(7):
    #                 if not playCard.playHandCard(i): break
    #             for i in range(7):
    #                 if not playCard.playBoardCard(i): break
    #             self.heroPower()
    #             playCard.playHero()
    #
    #             self.endTurn()
    #         if gameStatus == 3:
    #             # turn over, wait for opponent
    #             print("My turn ends..")
    #             self.endTurn()
    #         if gameStatus == 4:
    #             print("game status.. enemy turn, wait for 4 seconds")
    #             self.click(util.START_GAME_POSITION)
    #             self.click(util.CONFIRM_CARD_POSITION)
    #             self.click(util.RECONNECT_BUTTON_POSITION)
    #             time.sleep(4)
    #
    #         if gameStatus == 5:
    #             print("game status.. select a card")
    #             self.click(self.random_card_Position())
