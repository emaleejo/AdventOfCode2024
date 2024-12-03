input = open("day2.txt")
input = input.readlines()

counter = 0
for report in input:
    data = list(map(int, report.split()))
    if sorted(data) == list(data) or sorted(data, reverse=True) == list(data):
        skip_report = False
        for i in range(len(data) - 1):
            x = abs(data[i] - data[i+1])
            if x > 3 or x < 1:
                skip_report = True
        if not skip_report:
            counter += 1
print(counter)