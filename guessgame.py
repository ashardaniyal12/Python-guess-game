chances = 5
won = False

while chances > 0 and not won:
    print('Chances remaining =', chances)
    guesses_remaining = 4
    print("Enter your Number")
    number=int(input())
    if number==20:
        print("winner")
        won = True
        break
    elif number>30 and chances > 1:
        print("You number is too much high")
    elif number>20 or number>29 and chances > 1:
        print("decrease Your number")
        continue
    elif number<10 or number ==10 and chances > 1:
        print("Increase Number")
    elif number<15 and chances > 1:
        print("Increase A litlle bit")
        continue
    elif number==19 or number<19 and chances > 1:
        print("You are Too close")
        continue
chances -= 1
