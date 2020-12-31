import pyautogui, random, PIL, time, getGameStatus, playCard, Game, Utils



def gameStatus2():
    util = Utils.utils()

    for i in range(7):
        if not playCard.playHandCard(i): break
    rand = random.random()
    if rand < 0.7:
        for i in range(7):
            if not playCard.playBoardCard(i): break
    #
    # playCard.playHero()

    rand = random.randint(5, 10)
    # if rand < 2 : playCard.emote()
    print("sleeping for %d seconds" % rand)

    time.sleep(rand)

    # heal self
    playCard.heroPower()
    pyautogui.click(util.HERO_POSITION)
    pyautogui.moveTo(util.END_TURN_POSITION[0], util.END_TURN_POSITION[1])
    pyautogui.click()

    # def heroPower(self):
    #     util = Utils.utils()
    #     print("[Priest] Ending turn..")

    #
    # def runGame(self):
    #     util = Utils.utils()
    #
    #     print("running as Priest..")
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
    #             self.click(self.random_card_Position())
    #             self.click(self.random_card_Position())
    #             self.click(util.CONFIRM_CARD_POSITION)
    #         if gameStatus == 2:
    #             print("game status... my turn")
    #             pyautogui.rightClick()
    #             # minions attack hero if possible
    #
    #             for i in range(7):
    #                 if not playCard.playHandCard(i): break
    #             # for i in range(7):
    #             #     if not playCard.playBoardCard(i): break
    #             # playCard.playHero()
    #
    #             self.endTurn()
    #         if gameStatus == 3:
    #             # turn over, wait for opponent
    #             print("My turn ends..")
    #
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
