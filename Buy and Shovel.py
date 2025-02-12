s, b = map(int, input().split())
constant = s
count = 1
while s%10 != 0 and s%10 != b:
    s += constant
    count += 1
print(count)
