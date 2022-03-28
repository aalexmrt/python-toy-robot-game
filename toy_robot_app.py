import argparse

from utilities.inputs import *
from utilities.utils import *

TABLE_BOARD_WIDTH = 5
TABLE_BOARD_HEIGHT = 5
CARDINAL_DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]


class Robot:

    def __init__(self):
        self._x = None
        self._y = None
        self._facing = ''

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        validate_coordinate(value, TABLE_BOARD_WIDTH)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        validate_coordinate(value, TABLE_BOARD_HEIGHT)
        self._y = value

    @property
    def facing(self):
        return self._facing

    @facing.setter
    def facing(self, string_facing):
        validate_facing_direction(string_facing, CARDINAL_DIRECTIONS)
        self._facing = string_facing

    def place(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

    def left(self):
        if (CARDINAL_DIRECTIONS.index(self.facing) - 1) < 0:
            self.facing = CARDINAL_DIRECTIONS[len(CARDINAL_DIRECTIONS) - 1]
            return self.facing
        else:
            self.facing = CARDINAL_DIRECTIONS[CARDINAL_DIRECTIONS.index(self.facing) - 1]
            return self.facing

    def right(self):
        if (CARDINAL_DIRECTIONS.index(self.facing) + 1) >= len(CARDINAL_DIRECTIONS):
            self.facing = CARDINAL_DIRECTIONS[0]
            return self.facing
        else:
            self.facing = CARDINAL_DIRECTIONS[CARDINAL_DIRECTIONS.index(self.facing) + 1]
            return self.facing

    def move(self):
        if self.facing == "WEST":
            self.x -= 1
        elif self.facing == "EAST":
            self.x += 1
        elif self.facing == "NORTH":
            self.y += 1
        elif self.facing == "SOUTH":
            self.y -= 1

    def report(self):
        print("\nREPORT\n{},{},{}".format(self.x, self.y, self.facing))

    def place(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

    def robot_not_placed(self):
        if self.x is None and self.y is None and not self.facing:
            return True


def main(actions=None, interactive_mode=False, testing_mode=False):
    robot = Robot()
    game_options = ["PLACE"]
    activate_all_options = False

    def run_action(action_to_submit):
        nonlocal activate_all_options
        try:
            if action_to_submit.startswith("PLACE"):
                # Extract the position parameters from the action. Ex: PLACE 2,1,NORTH
                # position[0] = x = 2
                # position[1] = y = 1
                # position[2] = facing = NORTH
                position = action_to_submit.split(" ")[-1].split(",")
                robot.place(int(position[0]), int(position[1]), position[2])
                if not activate_all_options:
                    activate_all_options = True
                    game_options.extend(("MOVE", "LEFT", "RIGHT", "REPORT"))
            # game_options[1:] skip the PLACE action because is already checked above
            if action_to_submit in game_options[1:]:
                if action_to_submit == "MOVE":
                    robot.move()
                elif action_to_submit == "LEFT":
                    robot.left()
                elif action_to_submit == "RIGHT":
                    robot.right()
                elif action_to_submit == "REPORT" and not robot.robot_not_placed():
                    robot.report()
        except ValueError:
            pass

    if testing_mode:
        for test_action in actions:
            robot = Robot()
            test_name = test_action.split("/")[1].split(".")[0].upper()
            print("\n\t{}\n{}".format(test_name, "=" * len(test_name) * 4))
            for run in get_commands_from_file(test_action):
                run_action(run)
            if robot.robot_not_placed():
                print('\nThe robot is not placed!!')

    elif interactive_mode:
        robot = Robot()
        while True:
            print_game_options(game_options)
            if robot.robot_not_placed():
                print_action_example()
            user_action = ask_user_input()
            run_action(user_action.upper())
            build_table_board(TABLE_BOARD_WIDTH, TABLE_BOARD_HEIGHT, robot)
            if not ask_user_to_continue():
                break
            if robot.robot_not_placed():
                print('\nThe robot is not placed!!')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--testing-path", type=dir_path, dest="dir",
                        help="run the available tests from the given path")
    parser.add_argument("--interactive", default=True, action="store_true", dest="interactive_mode",
                        help="run the game interactively through the terminal")
    args = parser.parse_args()

    if args.dir is not None:
        tests = get_all_test_files(args.dir)
        main(actions=tests, testing_mode=True)
    elif args.interactive_mode:
        main(interactive_mode=True)
