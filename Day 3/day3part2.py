import re

input = open("day3.txt")
input = input.read()

answer = 0
do = re.split("do\(\)", input)

for d in do:
    if re.search("don't\(\)", d):
        add = re.split("don't\(\)", d)
        mullies = re.findall("mul\(\d{0,3},\d{0,3}\)", add[0])
        for mul in mullies:
            x = re.findall("\d{0,3},\d{0,3}", mul)[0].split(",")
            answer += int(x[0]) * int(x[1])
    else:
        mullies = re.findall("mul\(\d{0,3},\d{0,3}\)", d)
        for mul in mullies:
            x = re.findall("\d{0,3},\d{0,3}", mul)[0].split(",")
            answer += int(x[0]) * int(x[1])
print(answer)
