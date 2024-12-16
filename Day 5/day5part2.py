def get_rules_and_points(input):
    rules = []
    pages = []
    for line in input.splitlines():
        if "|" in line:
            point1, point2 = line.split("|")
            rules.append((point1, point2))
        if "," in line:
            pages.append(line.split(','))
    return rules, pages


def search_rule(page, rule1, rule2):
    if rule1 in page and rule2 in page:
        return page.index(rule1) < page.index(rule2)
    return True

def count_middles(pages):
    ans = 0
    for page in pages:
        m = len(page)//2
        ans += int(page[m])
    return ans

input = open("day5.txt")
input = input.read()

rules, pages = get_rules_and_points(input) 
print(pages)

filtered_pages = []
for page in pages:
    corrected_page = page[:]
    corrected = False
    while True:
        corrected = False
        for rule in rules:
            if not search_rule(corrected_page, rule[0], rule[1]):
                a, b = corrected_page.index(rule[0]), corrected_page.index(rule[1])
                corrected_page[a], corrected_page[b] = corrected_page[b], corrected_page[a]
                corrected = True
        if not corrected:
            break
    if corrected_page != page:
        filtered_pages.append(corrected_page)

print(count_middles(filtered_pages))

# 6726 was too high
# 6336