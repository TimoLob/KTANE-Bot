from communication import *
import wires


def listenForModule():
    say("What module should be defused next?")
    answer = listen()
    if answer == "wires" or answer=="fires" or answer == "cables" or answer=="tables":
        wires.defuseWires()



say("Hello World")
#answer = listen()
while True:
    listenForModule()


