pw = ["about","after","again","below","could","every","first","found","great","house","large","learn","never","other","plays","plant","point","right"
, "small","sound","spell","still","study","their","there","these","thing","think","three","water","where","which","world","would","write"]


for i in range(5):
    print(f"Column {i+1}, enter all the letters")
    l = input()
    l = [c for c in l]
    pw = [p for p in pw if p[i] in l]
    print(pw)



input()
