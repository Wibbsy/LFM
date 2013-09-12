import random

def createBadGuys(numberOfBadGuys):
    x = 0
    listOfBadGuys = []
    while x < numberOfBadGuys:
        badGuyHp = 100
        listOfBadGuys.append(badGuyHp)
        x += 1
    return listOfBadGuys

def zuesLighting(badGuyList):
    x = 0
    for badGuy in badGuyList:
        badGuyList[x] -= 20
        print "Bad Guy %s has %s health remaining" % (x,badGuyList[x])
        x += 1
        
def swingSword(target):
    swordDmg = random.randint(5,12)
    print "Who do you target?"
    x = 0
    for badGuy in badGuyList:
        print "%s - bad guy #%s" % (x,x)
        x += 1
    target = int(raw_input())
    badGuyList[target] -= swordDmg
    print "Bad Guy %s has %s health remaining" % (target,badGuyList[target])
    
def badGuysAlive(badGuyList):
    alive = False
    for badGuy in badGuyList:
        if badGuy > 0:
            alive = True
    return alive
    
if __name__ == "__main__":
    numberOfBadGuys = random.randint(2,5)
    badGuyList = createBadGuys(numberOfBadGuys)
    gameOver = False
    print "You've been jumped by %s guys. What do you do?" % (numberOfBadGuys)
    
    while gameOver == False:
        print "\nSelect an option"
        print "1. Swing Sword\n2. Zues Lighting"
        option = int(raw_input())
        if option == 1:
            swingSword(badGuyList)
        elif option == 2:
            zuesLighting(badGuyList)
        else:
            print "That is not an option"
            
        if badGuysAlive(badGuyList) == False:
            gameOver = True
            
    print "\nThanks for playing this random demo! "