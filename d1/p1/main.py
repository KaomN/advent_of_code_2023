
with open ("../input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

def get_digits(line):
    nums = []
    for i in range(len(line)):
        if line[i].isdigit():
            nums.append(line[i])
    if len(nums) > 1:
        num_str = nums[0] + nums[-1]
        return int(num_str)
    else:
        return int(nums[0] + nums[0])

answer = 0

for lines in puzzle_input:
   answer += get_digits(lines)

print("Answer:",answer)

