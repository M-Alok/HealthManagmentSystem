import random
l=["c","v","b"]

total_chance=10
chance_left=0
com_chance=0
my_chance=0

print("\t\t\tStone-Paper-Scissor\n")
print("c for stone\nv for paper\nb for scissor\n")

while chance_left<total_chance:
    me=input("Stone,Paper,Scissor:")
    com=random.choice(l)

    if me==com:
        print("Tie, 0 points to each")

    elif me=="c" and com=="v":
        com_chance+=1
        print(f"Your guess is {me} and computer guess is {com}")
        print("You lost and computer wins")
        print(f"Your score is {my_chance} and computer score is {com_chance}")

    elif me=="c" and com=="b":
        my_chance+= 1
        print(f"Your guess is {me} and computer guess is {com}")
        print("You win and computer lost")
        print(f"Your score is {my_chance} and computer score is {com_chance}")

    elif me=="v" and com=="c":
        my_chance+= 1
        print(f"Your guess is {me} and computer guess is {com}")
        print("You win and computer lost")
        print(f"Your score is {my_chance} and computer score is {com_chance}")

    elif me=="v" and com=="b":
        com_chance+= 1
        print(f"Your guess is {me} and computer guess is {com}")
        print("You lost and computer wins")
        print(f"Your score is {my_chance} and computer score is {com_chance}")

    elif me=="b" and com=="c":
        com_chance+= 1
        print(f"Your guess is {me} and computer guess is {com}")
        print("You lost and computer wins")
        print(f"Your score is {my_chance} and computer score is {com_chance}")

    elif me=="b" and com=="v":
        my_chance+= 1
        print(f"Your guess is {me} and computer guess is {com}")
        print("You win and computer lost")
        print(f"Your score is {my_chance} and computer score is {com_chance}")

    else:
        print("You entered wrong input\n")

    chance_left+=1
    print(f"{total_chance - chance_left} chances left out of {total_chance}\n")

print("\t\t\tGame Over\n")

print(f"Your points are: {my_chance} and Computer points are: {com_chance}\n")

if com_chance>my_chance:
    print("\t\t\tComputer Wins...")

elif my_chance>com_chance:
    print("\t\t\tYou Wins...")

else:
    print("\t\tGame tie, Both Wins...")
