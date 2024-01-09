import random
posx = 0
posy = 0
stick = 0

def pos():
    global posy
    global posx
    theinput = input("press w a s or d then enter to move")
    if theinput == 'w':
        print('you go forward')
        posy += 1
        locations()
    elif theinput == 's':
        print('you go backward')
        posy -= 1
        locations()
    elif theinput == 'a':
        print('you go left')
        posx -= 1
        locations()
    elif theinput == 'd':
        print('you go right')
        posx += 1
        locations()
def locations():
    if (posy == 5 and posx == 2):
        print("you are at your house")
    elif (posy == -3 and posx == 4):
        print("you are at the store")
    randomevents()
    pos()
def randomevents():
    global stick
    if (random.randint(1,10) == 1 and stick == 0):
      stickinput = input("you find an awesome stick. do you pick it up? yes or no")
      if stickinput == 'yes':
       print('you got an awesome stick!')
       stick += 1
print(' \n your house is at (2,5)\n the store is at (-3,4) ')
pos()
