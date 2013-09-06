print "\n\nWelcome to King of the Flesh Munchers"

waiting = True
while waiting:
    print "What is your race?\n1.Human\n2.Dworf\n3.Elf\n4.Black Guy"
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
        print "You hide very pointy ears behinid those flowing locks of yours."
        waiting = False
    elif choice == 4:
        print "No you're not\n"
    else:
        print "That is not an option"
    
print "\n\nand your name...? "
playerName = raw_input()

print "\n\nThat is the worst %s name i've ever heard, but okay..." % (playerRace)
print "You are Lord %s. Warrior for the %s race" % (playerName, playerRace)

print "your mother"