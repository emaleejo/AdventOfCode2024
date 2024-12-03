input = open("day1.txt")
input = input.readlines()

l1 = []
l2 = []
for line in input:
    n1, n2 = line.split()
    l1.append(int(n1))
    l2.append(int(n2))

l1 = sorted(l1)
l2 = sorted(l2)

answer = 0
for i in l1:
    count = l2.count(i)
    answer += i * count
print(answer)
