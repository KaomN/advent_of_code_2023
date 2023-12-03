
with open ("../input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

red = 12
green = 13
blue = 14
possible_games = []

def calculate_game(line):
    game = line.split(":")
    sub_set = game.pop(1).split(";")
    min_red = 0
    min_green = 0
    min_blue = 0
    for sub in sub_set:
        cubes = sub.split(",")
        for cube in cubes:
            cube = cube.strip().split(" ")
            if cube[1] == "red":
                if min_red == 0:
                    min_red = int(cube[0])
                elif int(cube[0]) > min_red:
                    min_red = int(cube[0])
            elif cube[1] == "green":
                if min_green == 0:
                    min_green = int(cube[0])
                elif int(cube[0]) > min_green:
                    min_green = int(cube[0])
            elif cube[1] == "blue":
                if min_blue == 0:
                    min_blue = int(cube[0])
                elif int(cube[0]) > min_blue:
                    min_blue = int(cube[0])
    possible_games.append(min_red * min_green * min_blue)

for lines in puzzle_input:
    calculate_game(lines)

answer = sum(possible_games)

print("Answer:",answer)

