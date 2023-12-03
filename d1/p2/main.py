
import re

with open ("../input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

numbers_as_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_as_strings_reversed = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def get_digits(line):
    nums = {}
    reversed_line = line[::-1]
    str_len = len(line)

    for match in re.finditer("|".join(numbers_as_strings), line):
        nums[match.start()] = numbers_as_strings.index(match.group()) + 1

    for match in re.finditer("|".join(number_as_strings_reversed), reversed_line):
        nums[str_len - match.start()] = number_as_strings_reversed.index(match.group()) + 1

    for i in range(len(line)):
        if line[i].isdigit():
            nums[i] = int(line[i])
    
    if len(nums) > 1:
        num_str = str(nums[min(nums.keys())]) + str(nums[max(nums.keys())])
        return int(num_str)
    else:
        key = list(nums.keys())[0]
        return int(str(nums[key]) + str(nums[key]))

answer = 0
for lines in puzzle_input:
   answer += get_digits(lines)

print("Answer:",answer)

#54925