# adventure_game.py - A text-based adventure game where the player searches for a legendary treasure.

print("Adventure Game setup successful!")

def restart_game():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("\nThank you for playing the Adventure Game. Goodbye!")
            return False
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")


def win_game(player_name):
    print(f"\nCongratulations, {player_name}!")
    print("You found the legendary treasure and completed your quest successfully!")
    return restart_game()


def lose_game(player_name, reason):
    print(f"\nOh no, {player_name}!")
    print(reason)
    print("Your adventure has come to an end.")
    return restart_game()


def forest_path(player_name):
    print("\nYou enter the dark forest.")
    print("The trees are tall, and strange sounds echo around you.")
    print("Soon, you reach a clearing and notice two possible actions.")
    print("1. Follow the river")
    print("2. Climb a tree")

    choice = input("What do you choose? (river/tree): ").strip().lower()

    if choice == "river":
        print("\nYou carefully follow the river.")
        print("After walking for some time, you discover an old wooden bridge and a boat.")
        print("1. Cross the bridge")
        print("2. Use the boat")

        second_choice = input("What do you choose? (bridge/boat): ").strip().lower()

        if second_choice == "bridge":
            print("\nYou cross the bridge safely and find a glowing map on the other side.")
            print("The map leads you directly to the treasure chamber.")
            return win_game(player_name)
        elif second_choice == "boat":
            return lose_game(player_name, "The boat had a leak and sank in the river.")
        else:
            return lose_game(player_name, "You got confused in the forest and lost your way.")
    elif choice == "tree":
        print("\nYou climb the tallest tree to get a better view.")
        print("From the top, you spot ancient ruins and also a sleeping giant eagle.")
        print("1. Head toward the ruins")
        print("2. Try to take a feather from the eagle")

        second_choice = input("What do you choose? (ruins/feather): ").strip().lower()

        if second_choice == "ruins":
            print("\nYou quietly move toward the ruins.")
            print("Inside the ruins, you solve a simple path puzzle and discover the hidden treasure.")
            return win_game(player_name)
        elif second_choice == "feather":
            return lose_game(player_name, "The eagle wakes up and chases you out of the forest.")
        else:
            return lose_game(player_name, "You hesitated too long and night fell before you could continue.")
    else:
        return lose_game(player_name, "You made an invalid decision and wandered aimlessly in the forest.")


def cave_path(player_name):
    print("\nYou step into the mysterious cave.")
    print("The air is cold, and the path ahead is dark and silent.")
    print("You must decide how to continue.")
    print("1. Light a torch")
    print("2. Proceed in the dark")

    choice = input("What do you choose? (torch/dark): ").strip().lower()

    if choice == "torch":
        print("\nYou light a torch and the cave becomes easier to navigate.")
        print("You see two tunnels ahead.")
        print("1. Enter the left tunnel")
        print("2. Enter the right tunnel")

        second_choice = input("What do you choose? (left/right): ").strip().lower()

        if second_choice == "left":
            print("\nThe left tunnel leads to an ancient stone door.")
            print("A symbol on the wall suggests pressing a hidden switch.")
            print("1. Press the switch")
            print("2. Force the door open")

            third_choice = input("What do you choose? (switch/force): ").strip().lower()

            if third_choice == "switch":
                print("\nThe stone door opens slowly, revealing a chamber full of gold and jewels.")
                return win_game(player_name)
            elif third_choice == "force":
                return lose_game(player_name, "A trap is triggered, and the cave collapses around you.")
            else:
                return lose_game(player_name, "You waited too long and your torch burned out.")
        elif second_choice == "right":
            return lose_game(player_name, "The right tunnel leads to a dead end filled with poisonous gas.")
        else:
            return lose_game(player_name, "You became disoriented and could not find your way in the cave.")
    elif choice == "dark":
        print("\nYou move forward in complete darkness.")
        print("You hear strange noises and feel the ground becoming uneven.")
        print("1. Keep walking")
        print("2. Turn back")

        second_choice = input("What do you choose? (walk/back): ").strip().lower()

        if second_choice == "walk":
            return lose_game(player_name, "You fall into a hidden pit in the darkness.")
        elif second_choice == "back":
            print("\nYou safely return to the cave entrance and notice a hidden torch on the ground.")
            print("You pick it up, light it, and re-enter the cave.")
            print("This time, you find a marked tunnel leading to the treasure room.")
            return win_game(player_name)
        else:
            return lose_game(player_name, "You got lost in the darkness of the cave.")
    else:
        return lose_game(player_name, "You made an invalid choice and the cave became too dangerous to continue.")


def start_game():
    print("\n" + "=" * 70)
    print("WELCOME TO THE PYTHON ADVENTURE GAME")
    print("=" * 70)
    print("You are an explorer searching for a legendary treasure hidden in an ancient land.")

    player_name = input("Enter your name, adventurer: ").strip()

    if not player_name:
        player_name = "Explorer"

    print(f"\nWelcome, {player_name}!")
    print("Your quest begins now.")
    print("\nChoose your path:")
    print("1. Explore the dark forest")
    print("2. Enter the mysterious cave")

    paths = ["forest", "cave"]

    while True:
        choice = input("What do you choose? (forest/cave): ").strip().lower()

        if choice in paths:
            if choice == "forest":
                return forest_path(player_name)
            else:
                return cave_path(player_name)
        else:
            print("Invalid choice. Please type 'forest' or 'cave'.")


def main():
    playing = True

    while playing:
        playing = start_game()


main()