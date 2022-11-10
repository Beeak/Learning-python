import random

while True:
    plr_choice = input("Enter a choice (rock, paper, scissors): ")
    rps_option = ["rock", "paper", "scissors"]
    rps_choice = random.choice(rps_option)
    print(f"\nYou chose {plr_choice}, computer chose {rps_choice}.\n")

    if plr_choice == rps_choice:
        print(f"Both players selected {plr_choice}. It's a tie!")
    elif plr_choice == "rock":
        if rps_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif plr_choice == "paper":
        if rps_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif plr_choice == "scissors":
        if rps_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    replay = input("Play again? (y/n): ")
    if replay.lower() != "y":
        break
