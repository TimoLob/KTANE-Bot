print("Enter the last digit of the serial number")
serial = int(input())
serialeven = False
if serial % 2 == 0:
    serialeven = True


print("Enter the number of batteries on the bomb:")
batteries = int(input())

print("Does the bomb have a parallel Port?(y/n)")
hasParallel = False
a = input()
if a == "y":
    hasParallel = True

for i in range(6):
    print(f"Cable nr {i+1}: Enter *,L,R,B as string")
    s = str.lower(input())
    hasStar = False
    hasLED = False
    isRed = False
    isBlue = False
    if "*" in s:
        hasStar = True
    if "l" in s:
        hasLED = True
    if "r" in s:
        isRed = True
    if "b" in s:
        isBlue = True

    
