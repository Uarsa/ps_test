import random, time

matches = 20
while matches > 0:
    m = int(input("YOU take matches: "))
    if m > 3:
        print("no more than three!")
        print()
        continue
    
    matches -= m
    print("|" * matches, "x{} left".format(matches))
    print()
    
    if matches == 0:
        print("YOU WIN")
        exit()
    
    time.sleep(1)
    
    if matches <= 3:
        m1 = random.randint(1, matches)
        print("COMPUTER take {} matches".format(m1))
        matches -= m1
        print("|" * matches, "x{} left".format(matches))
        print()
        
    else:    
        m1 = random.randint(1, 3)
        print("COMPUTER take {} matches".format(m1))
        matches -= m1
        print("|" * matches, "x{} left".format(matches))
        print()
        
print("COMPUTER WIN")  


