print("                  (")
print(" Welcomee to guess the value game!")
print("              (   ()   )")
print("    ) ________    //  )")
print(" ()  |\       \  //")
print("( \\__ \ ______\//")
print("   \__) |       |")
print("     |  |       |")
print("      \ |       |")
print("       \|_______|")
print("       //    \\")
print("      ((     ||")
print("       \\    ||")
print("     ( ()    ||")
print("     ( ()    ||")

def bys():
    print("\nwe are waiting for you again")
    print("         ____")
    print("       _(____)_")
    print("___ooO_(_o__o_)_Ooo___")


trial = 10
number = 0
score = 0
while True:
    user_input = input("Enter a value (enter Q or q to quit): ")
    if user_input in "Qq" and user_input:
        print("the game is over at your request your score: {} ".format(score))
        break
    if (trial < 2):
            print("you lose, your trial is over")
            break
    if ((user_input).isnumeric()):
        if (int(user_input) < 1 and int(user_input) > 100):
            print("your predicted value is not in the range")
            trial -= 1
            continue
        elif (trial > 0):
            if (number - int(user_input) <= 3 and (number - int(user_input) )>= 0 and number != int(user_input)):
                trial -= 1
                print("increment your guess, you're close")
            elif (number - int(user_input) >= -3 and (number - int(user_input) <= 0) and number != int(user_input)):
                trial -= 1
                print("reduce your guess, you're close")
            elif (int(user_input) == number):
                trial -= 1
                print("Congrats you took the :)))")
                number += 10 - trial
                trial = 10
                score += 1
            else: trial -= 1
    else:
        trial -= 1
        print("check the value you entered your trial")
bys()
