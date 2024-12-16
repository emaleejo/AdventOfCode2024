def get_rules_and_points(input):
    rules = []
    pages = []
    for line in input.splitlines():
        if "|" in line:
            point1, point2 = line.split("|")
            rules.append((point1, point2))
        if "," in line:
            pages.append(line)
    return rules, pages


def search_rule(page, rule1, rule2):
    page_rules = page.split(",")
    if rule1 in page_rules and rule2 in page_rules:
        return page_rules.index(rule1) < page_rules.index(rule2)
    return True

def count_middles(pages):
    ans = 0
    for page in pages:
        page = page.split(",")
        m = len(page)//2
        ans += int(page[m])
    return ans

input = open("day5.txt")
input = input.read()

rules, pages = get_rules_and_points(input) 
filtered_pages = [page for page in pages if all(search_rule(page, rule[0], rule[1]) for rule in rules)]
print(count_middles(filtered_pages))