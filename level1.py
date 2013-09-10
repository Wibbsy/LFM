asciiFile = open('art/gameTitle.txt')
lines = asciiFile.readlines()
asciiFile.close()
for line in lines:
    print line.rstrip()

print "\n\nWelcome to King of the Flesh Munchers"

waiting = True
while waiting:
    print "What is your race?\n1.Human\n2.Dworf\n3.Elf\n"
    choice = int(raw_input())
    if choice == 1:
        playerRace = "Human"
        waiting = False
        print "I thought you smelled kind of funny"
    elif choice == 2:
        playerRace = "Dworf"
        print "Ah, a majesticly short, fat, bearded  clan. Good choice."
        waiting = False
    elif choice == 3:
        playerRace = "Elf"
        print "You hide very pointy ears behind those flowing locks of yours."
        waiting = False
    else:
        print "That is not an option"
    
print "\n\nand your name...? "
playerName = raw_input()

print "\n\nThat is the worst %s name i've ever heard, but okay..." % (playerRace)
print "You are Lord %s. Warrior for the %s race" % (playerName, playerRace)

print "\nHow about your loyal canine friend. What's his name?"
dogsName = raw_input()
print "\n"
print "Your name: %s" % (playerName)
print "Your race: %s" % (playerRace)
print "Your dog's name: %s" % (dogsName)
print"\nIs this correct?(y/n)"

waiting = True
while waiting:
    playerInput = raw_input()
    if playerInput == "y":
        waiting = False
    elif playerInput == "n":
        print "\nGame Over...\nYou couldn't even handle entering simple information about yourself.\nThere is no way you could handle the rest of this game"
    else:
        print "That is not an option"