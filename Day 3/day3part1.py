import re

input = open("day3.txt")
input = input.read()

answer = 0
mullies = re.findall("mul\(\d{0,3},\d{0,3}\)", input)
for mul in mullies:
    x = re.findall("\d{0,3},\d{0,3}", mul)[0].split(",")
    answer += int(x[0]) * int(x[1])
print(answer)
