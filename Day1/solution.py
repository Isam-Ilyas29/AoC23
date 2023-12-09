doc = open("Day1/calibration_document.txt", 'r')

sum_nums = []

def strToInt(word):
    if "one" in word:
        return 1
    if "two" in word:
        return 2
    if "three" in word:
        return 3
    if "four" in word:
        return 4
    if "five" in word:
        return 5
    if "six" in word:
        return 6
    if "seven" in word:
        return 7
    if "eight" in word:
        return 8
    if "nine" in word:
        return 9
    return -1

def lineToNums(line):
    nums = []
    buffer = ""
    i = 0
    while i < len(line):
        buffer += line[i]
        if strToInt(buffer) > 0:
            nums.append(strToInt(buffer))
            i -= 1
            buffer = ""
        if line[i].isdigit():
            nums.append(int(line[i]))
            buffer = ""
        i += 1
    return nums

for line in doc:
    line_nums = lineToNums(line)
    num = str(line_nums[0]) + str(line_nums[-1])
    sum_nums.append(int(num))

print(sum(sum_nums))
