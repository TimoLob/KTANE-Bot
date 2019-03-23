def longPress():
    print("Press and hold the button")
    print("what color is the stripe?")
    stripe = input()
    stripe = str.lower(stripe)
    if stripe == "blue":
        print("Release on 4")
    elif stripe == "white":
        print("Release on 1")
    elif stripe == "yellow":
        print("Release on 5")
    else:
        print("Release on 1")

def main():
    print("Enter the text of the button")
    text = input()
    text = str.lower(text)

    print("Enter the color of the button")
    color = input()
    color = str.lower(color)

    if color == "blue" and text == "abort":
        longPress()
        return

    if text == "detonate":
        print("more than 1 battery?(y/n)")
        a = input()
        if a=="y":
            print("Press and release button")
            return


    if color == "white":
        print("LED with CAR?(y/n)")
        a = input()
        if a == "y":
            longPress()
            return

    print("Are there more than 2 batteries? AND is there an LED with FRK?(y/n)")
    a = input()
    if a == "y":
        print("Press and release button")
        return

    if color == "yellow":
        longPress()
        return

    if color == "red" and text == "hold":
        print("Press and release button")
        return

    longPress()


main()