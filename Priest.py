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

