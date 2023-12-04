
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

  name = cards_line[0]
  cards_line = cards_line[1].strip().split(" ")
  cards_line_copy = cards_line.copy()

  index = 0
  for elem in cards_line_copy:
    if not elem.isdigit():
      cards_line.pop(index)
      index -= 1
    index += 1
  return cards_line

def check_winning_numbers(boards, cards, index, scratch_card_list):
  matching = 0
  for number in cards:
    if number in boards:
      matching += 1

  if matching > 0:
     ## add 1 scratch card as we have 1 original scratch card
    scratch_card_list[index] += 1
    ## run for every copy of scratch card
    for x in range(0, scratch_card_list[index]):
      ## add 1 scratch card copy for each matching number
      for i in range(0, matching):
        scratch_card_list[i + 1 + index] += 1
  else:
    ## add 1 scratch card for no matching to current index for no matching as we have 1 original scratch card
    scratch_card_list[index] += 1
  return scratch_card_list

#answer = 0
scratch_card_list = []
for x in range(0, 200):
  scratch_card_list.append(0)

for index, lines in enumerate(puzzle_input):
  boards = get_board(lines)
  cards = get_cards(lines)
  scratch_card_list = check_winning_numbers(boards, cards, index, scratch_card_list)

answer = sum(scratch_card_list)
print("Answer:", answer)
