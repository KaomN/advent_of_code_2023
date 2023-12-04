
with open ("../input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

def get_board(lines):
  board_line = lines.split("|")[1].strip().split(" ")
  board_line_copy = board_line.copy()

  index = 0
  for elem in board_line_copy:
    if not elem.isdigit():
      board_line.pop(index)
      index -= 1
    index += 1
  return board_line

def get_cards(lines):
  cards_line = lines.split("|")[0].strip().split(":")
  cards_line = cards_line[1].strip().split(" ")
  cards_line_copy = cards_line.copy()

  index = 0
  for elem in cards_line_copy:
    if not elem.isdigit():
      cards_line.pop(index)
      index -= 1
    index += 1
  return cards_line

def check_winning_numbers(boards, cards):
  points = 0
  for number in cards:
    if number in boards:
      if points == 0:
        points += 1
      else:
        points *= 2
  return points

answer = 0

for y, lines in enumerate(puzzle_input):
  boards = get_board(lines)
  cards = get_cards(lines)
  answer += check_winning_numbers(boards, cards)

print("Answer:", answer)
