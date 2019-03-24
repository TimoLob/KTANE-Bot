from communication import *

def defuseWires():
    say("Defusing wires")
    say("How many wires are there?")
    while True:
        answer = listen()
        if answer:
            if answer == "cancel":
                say("Cancel")
                return
            n = getNumber(answer)
            if n == 3:
                wire3()
                return
            if n == 4:
                wire4()
                return


def wire3():
    say("Are there red cables?")
    a = listen()
    if a.startswith("y"):
        say("Cut the 2nd cable")
        return
    say("is the last cable white")
    a = listen()
    if a.startswith("y"):
        say("cut this wire")
        return
    say("is there more than 1 blue cable")
    a = listen()
    if a.startswith("y"):
        say("cut the last blue wire")
        return
    say("cut the last wire")

def wire4():
    say("not implemented yet")