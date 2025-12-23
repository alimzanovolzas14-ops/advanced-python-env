good = "ABCEHKMOPTXY"
n = int(input())

for _ in range(n):
    s = input()

    if len(s) == 6 and s[0] in good and s[4] in good and s[5] in good and s[1:4].isdigit():
        print("Yes")
    else:
        print("No")
