import pyscreenshot as ImageGrab
import pyautogui, random, PIL, time, getGameStatus, playCard, Game, Utils

def gameStatus2():
    playCard.heroPower()
    # for i in range(7):
    #     if not playCard.playHandCard(i): break
    #
    # for i in range(7):
    #     if not playCard.playBoardCard(i): break

    # playCard.playHero()

    rand = random.randint(55)
    time.sleep(rand)
