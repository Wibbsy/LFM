import sys

asciiFile = open('art/gameTitle.txt')
lines = asciiFile.readlines()
asciiFile.close()
for line in lines:
    print line.rstrip()
    
def gameOver(string):
    asciiFile = open('art/gameOver.txt')
    print asciiFile.read()
    asciiFile.close()
    print(string)
    sys.exit()

def swingWeapon(weaponType,weaponDmg):
    print("You are using %s.") % (weaponType)
    enemyHp = 100
    print("Enemy health is %s.") % (enemyHp)
    enemyHp -= weaponDmg   
    print("Enemy's health is %s.") % (enemyHp)