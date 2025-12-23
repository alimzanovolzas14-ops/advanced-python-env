items = input().split()
count = {}

for item in items:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for k in count:
    print(k, count[k])
