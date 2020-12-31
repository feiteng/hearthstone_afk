import pyscreenshot as ImageGrab
# import colormap

Play_Button = [255, 255, 255]
confirmButton = [126, 195, 255]
myTurn = [206, 163, 2]
enemyTurn = [82, 73, 62]
endTurn = [33, 158, 3]

def rgb2hex(r, g, b):
    return '%02x%02x%02x' % (r, g, b)

def distance(g1, g2):
    sum = 0
    for i in range(3):
        sum += (g1[i] - g2[i]) ** 2
    # print(g1)
    # print(g2)
    # print("distance.. %d" % sum)
    return sum

def getStatus():


    cordinate = 0, 0
    err = 5000
    im = ImageGrab.grab(bbox=(1355, 887, 1360, 888))  # X1,Y1,X2,Y2
    r, g, b = im.getpixel(cordinate)

    # out side game
    if distance([r, g, b], Play_Button) < err:
        print("Outside Game.. ")
        return 6

    # selecting card
    im = ImageGrab.grab(bbox=(540, 790, 550, 793))  # X1,Y1,X2,Y2
    r, g, b = im.getpixel(cordinate)

    if distance([r, g, b], confirmButton) < err:
        print("Selecting Card..")
        return 5


    im = ImageGrab.grab(bbox=(890, 830, 891, 831))  # X1,Y1,X2,Y2
    r, g, b = im.getpixel(cordinate)
    if distance([r, g, b], confirmButton) < err:
        print("Confirm button..")
        return 1    # 开局点确认



    im = ImageGrab.grab(bbox=(1578, 478, 1580, 480))  # X1,Y1,X2,Y2
    r, g, b = im.getpixel(cordinate)
    if distance([r, g, b], myTurn) < err:
        print("My turn..")
        return 2

    if distance([r, g, b], endTurn) < err:
        print("My turn ends..")
        return 3 # 结束战斗

    if distance([r, g, b], enemyTurn) < err:
        print("Enemy turn..")
        return 4



    print("Unknown Status..")
    return 0 # outside game

# while(True):
#     print(getStatus())