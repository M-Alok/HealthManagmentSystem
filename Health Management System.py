import time
print("\n*** Health Management System ***\n")
a = int(input("Press 1 for log\nPress 2 for retrive\n"))
def take(k):
    if k == 1:
        c = int(input("Press 1 for food\nPress 2 for exercise\n"))
        if c == 1:
            x=input("Type what you ate: \n")
            with open("Alok-food.txt", "a") as op:
                op.write(str([time.asctime(time.localtime(time.time()))])+": "+x+"\n")
            print("Entered successfully")
        elif c == 2:
            x = input("Type which exercise you did: \n")
            with open("Alok-exercise.txt", "a") as op:
                op.write(str([time.asctime(time.localtime(time.time()))])+": "+x+"\n")
            print("Entered successfully")
    elif k == 2:
        c = int(input("Press 1 for food\nPress 2 for exercise\n"))
        if c == 1:
            x = input("Type what you ate: \n")
            with open("Chetan-food.txt", "a") as op:
                op.write(str([time.asctime(time.localtime(time.time()))]) + ": " + x +"\n")
            print("Entered successfully")
        elif c == 2:
            x = input("Type which exercise you did: \n")
            with open("Chetan-exercise.txt", "a") as op:
                op.write(str([time.asctime(time.localtime(time.time()))]) + ": " + x +"\n")
            print("Entered successfully")
    elif k == 3:
        c = int(input("Press 1 for food\nPress 2 for exercise\n"))
        if c == 1:
            x = input("Type what you ate: \n")
            with open("Shravan-food.txt", "a") as op:
                op.write(str([time.asctime(time.localtime(time.time()))]) + ": " + x +"\n")
            print("Entered successfully")
        elif c == 2:
            x = input("Type which exercise you did: \n")
            with open("Shravan-exercise.txt", "a") as op:
                op.write(str([time.asctime(time.localtime(time.time()))]) + ": " + x +"\n")
            print("Entered successfully")
    else:
        print("You entered invalid input")
def retrive(k):
    if k == 1:
        d = int(input("Press 1 for food\nPress 2 for exercise\n"))
        if d == 1:
            op = open("Alok-food.txt")
            for i in op:
                print(i, end="")
        elif d == 2:
            op = open("Alok-exercise.txt")
            for i in op:
                print(i, end="")
    elif k == 2:
        d = int(input("Press 1 for food\nPress 2 for exercise\n"))
        if d == 1:
            op = open("Chetan-food.txt")
            for i in op:
                print(i, end="")
        elif d == 2:
            op = open("Chetan-exercise.txt")
            for i in op:
                print(i, end="")
    elif k == 3:
        d = int(input("Press 1 for food\nPress 2 for exercise\n"))
        if d == 1:
            op = open("Shravan-food.txt")
            for i in op:
                print(i, end="")
        elif d == 2:
            op = open("Shravan-exercise.txt")
            for i in op:
                print(i, end="")
    else:
        print("You entered invalid input")

if a == 1:
    b = int(input("Press 1 for Alok\nPress 2 for Chetan\nPress 3 for Shravan\n"))
    take(b)
elif a == 2:
    b = int(input("Press 1 for Alok\nPress 2 for Chetan\nPress 3 for Shravan\n"))
    retrive(b)
else:
    print("You entered invalid input")
