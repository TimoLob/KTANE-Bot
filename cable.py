




def cable3():
    print("No red cables?(y/n)")
    a = input()
    if a == "y":
        print("cut 2nd cable")
        return
    print("last cable white?(y/n)")
    a = input()
    if a == "y":
        print("cut this wire")
        return
    print("more than 1 blue cable?(y/n)")
    a = input()
    if a == "y":
        print("cut the last blue wire")
        return
    print("cut the last wire")

def cable4():
    print("not implemented yet")