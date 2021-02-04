import random, time


matches = 20
print("x{} ".format(matches), "{}".format("|" * matches))
print()
while matches > 0:
    m = int(input("YOU take matches: "))
    if m > 3:
        print("no more than three!")
        print()
        continue

    matches -= m
    print("x{} ".format(matches), "{}".format("|" * matches))
    print()

    if matches == 0:
        print("YOU WIN")
        exit()

    time.sleep(1)

    if matches <= 3:
        m1 = matches
        print("COMPUTER takes {} matches".format(m1))
        matches -= m1
        print("x{} ".format(matches), "{}".format("|" * matches))
        print()

    else:
        m1 = random.randint(1, 3)
        print("COMPUTER takes {} matches".format(m1))
        matches -= m1
        print("x{} ".format(matches), "{}".format("|" * matches))
        print()

print("COMPUTER WIN")


