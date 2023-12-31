
with open ("../input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

num_list = []
temp_list = []

def is_symbol(element):
  return element == "*"

def get_element(x, y):
  return puzzle_input[y][x]

def get_number(x, y):
  start_x = x
  end_x = x

  for i in range(x, len(puzzle_input[y]) + 1):
    if i == len(puzzle_input[y]):
      end_x = i
      break
    if not get_element(i, y).isdigit():
      end_x = i
      break

  for i in range(x, -1, -1):
    if i == 0:
      start_x = i
      break
    if not get_element(i - 1, y).isdigit():
      start_x = i
      break

  temp_list.append(int(puzzle_input[y][start_x:end_x]))

def check_adjacent(x, y):
  ## Check top of the element
  exactly_two = 0

  if y > 0 and get_element(x, y-1).isdigit(): # check up
    get_number(x, y-1)
    exactly_two += 1
  else:
    pass
    if x > 0 and y > 0 and get_element(x-1, y-1).isdigit(): # check up left
      get_number(x-1, y-1)
      exactly_two += 1
    if x < len(puzzle_input[y])-1 and y > 0 and get_element(x+1, y-1).isdigit(): # check up right
      get_number(x+1, y-1)
      exactly_two += 1
  ## check bottom of the element
  if y < len(puzzle_input)-1 and get_element(x, y+1).isdigit(): # check down 
    get_number(x, y+1)
    exactly_two += 1
  else:
    if x > 0 and y < len(puzzle_input)-1 and get_element(x-1, y+1).isdigit(): # check down left
      get_number(x-1, y+1)
      exactly_two += 1
    if x < len(puzzle_input[y])-1 and y < len(puzzle_input)-1 and get_element(x+1, y+1).isdigit(): # check down right
      get_number(x+1, y+1)
      exactly_two += 1
  ## check left of the element
  if x > 0 and get_element(x-1, y).isdigit(): # check left
    get_number(x-1, y)
    exactly_two += 1
  ## check right of the element
  if x < len(puzzle_input[y])-1 and get_element(x+1, y).isdigit(): # check right
    get_number(x+1, y)
    exactly_two += 1
  
  if exactly_two == 2: # if there are exactly two numbers
    num_list.append(temp_list[0] * temp_list[1]) # multiply them
  temp_list.clear() # clear the temp list

for y, lines in enumerate(puzzle_input):
  for x, element in enumerate(lines):
    if is_symbol(element):
      check_adjacent(x, y)

answer = sum(num_list)

print("Answer:",answer)
