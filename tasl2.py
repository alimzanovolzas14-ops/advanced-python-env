a = input()
b = input()
m = len(b)
bb = b+b
count = 0

for i in range (len(a)-m+1):
    psrt = a[i:i+m]
    if part in bb:
        count +=1

print(count)
