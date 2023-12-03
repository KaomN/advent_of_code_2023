
with open ("../input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

red = 12
green = 13
blue = 14
possible_games = []

def calculate_game(line):
    game = line.split(":")
    sub_set = game.pop(1).split(";")
    possible = True
    for sub in sub_set:
        cubes = sub.split(",")
        for cube in cubes:
            cube = cube.strip().split(" ")
            if cube[1] == "red" and not int(cube[0]) <= red:
                possible = False
            elif cube[1] == "green" and not int(cube[0]) <= green:
                possible = False
            elif cube[1] == "blue" and not int(cube[0]) <= blue:
                possible = False
    if possible:
        possible_games.append(int(game[0].split(" ")[1]))

for lines in puzzle_input:
    calculate_game(lines)

answer = sum(possible_games)

print("Answer:",answer)

