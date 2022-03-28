def print_game_options(game_options, running=False):
    print("GAME OPTIONS 🎲\t", end="")
    for option in game_options:
        print("#{}\t".format(option), end="")
    print()


def print_action_example():
    print("\nExample: PLACE 2,2,NORTH")


def ask_user_to_continue():
    print("Do you want to continue? (y/n)")
    while True:
        reply = input().lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
        else:
            print("Not valid, please try again (y/n)")


def ask_user_input():
    action = input()
    return action
