from __future__ import print_function

import os
from os import listdir
from os.path import join


def validate_coordinate(value, range_coordinates):
    if (value < 0) or (value > range_coordinates - 1):
        raise ValueError("Coordinates are not valid")


def validate_facing_direction(string_facing, cardinal_directions):
    if string_facing not in cardinal_directions:
        raise TypeError("Facing direction is not valid")


def get_commands_from_file(file):
    with open(file) as f:
        lines = f.readlines()
        actions_from_file = []
        for line in lines:
            actions_from_file.append(line.replace("\n", ''))

    return actions_from_file


def get_all_test_files(test_path):
    test_files = []
    for file in sorted(listdir(test_path)):
        test_files.append(join(test_path, file))

    return test_files


def build_table_board(table_board_width, table_board_height, Robot=None):
    # Initialize the table board's array
    table_board = [[0] * table_board_width] * table_board_height
    # Print the table board and the robot if exists
    for y in reversed(range(table_board_height)):
        for x in range(table_board_width):
            if Robot is not None and Robot.x == x and Robot.y == y:
                table_board[y][x] = "🤖"
            else:
                table_board[y][x] = "🔲"
            print(table_board[y][x], end="")
            if x == table_board_width - 1:
                print()

    return table_board


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

