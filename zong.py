from sys import exit

def gold_room():
    print "the room is full of gold,How much do you take?"

    next=raw_input(">")
    if"0"in next or "1" in next:
        how_much=int(next)
    else:
        dead("Man,learn to type a number")

    if how_much<50:
        print "Nice you win"
        exit(0)
    else:
        dead("you greed bastard")

def bear_room():
    print "there is a bear in room"
    print "the bear has a bunch of honey"
    print "the fat bear is in front of another door"
    print "How are you going to move the bear"
    bear_moved=False

    while True:
     next=raw_input(">")
     if next=="take honney":
        dead("The bear looks at you then slaps your face off")
     elif next=="taunt bear"and not bear_moved:
        dead("the bear chews your leg off")
     elif next=="open door "and bear_moved:
        gold_room()
     else:
        print "I got no idea what that mean"

def cthulu_room():
    print "Here you see the great evil Cthulu"
    print "He it whatever stares at you and you go insane"
    print "Do you flee for your life or eat your head"
    
    next=raw_input(">")
    
    if"flee"in next:
        start()
    elif"head"in next:
        dead("well that was tasty")
    else:
        cthulu_room()

def dead(wyh):
    print wyh,"you dead good job"
    exit(0)
    
def start():
    print "you are in a dark room"
    print "there is a door to your right and left"
    print "Which one do you take"
    
    next=raw_input(">")
    
    if next=="left":
        bear_room()
    elif next=="right":
        cthulu_room()
    else:
        dead("you stumble around the room until you starve")
        
start()