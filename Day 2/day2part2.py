def is_safe(data):
    differences = [data[i] - data[i+1] for i in range(len(data) - 1)]
    if all(0 < x <= 3 for x in differences) or all(-3 <= x < 0 for x in differences):
        return True
    return False


def is_safe_with_dampener(data):
    if is_safe(data):
        return True
    for i in range(len(data)):
        new_data = data[:i] + data[i+1:]
        if is_safe(new_data):
            return True
    return False


input = open("day2.txt")
input = input.readlines()
counter = 0
for report in input:
    data = list(map(int, report.split()))
    if is_safe_with_dampener(data):
        counter += 1
print(counter)
