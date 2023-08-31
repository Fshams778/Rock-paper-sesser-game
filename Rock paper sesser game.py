import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
tries=0
comp = 0
player_score = 0
while tries<6:
    player = input("Rock, Paper or  Scissors?").capitalize()
    
    if player == computer:
        print("Equate")
        tries+=1
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            comp+=1
            tries+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
            tries+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            comp+=1
            tries+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
            tries+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            comp+=1
            tries+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
            tries+=1
            break
    
print("\n Total Scores:")
print(f"Computer:{comp}")
print(f"You:{player_score}")
print("\n\n*******Done By Fatma Mohammed*********\n\n")
        