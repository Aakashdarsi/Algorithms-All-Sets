# https://www.youtube.com/watch?v=b7AYbpM5YrE
s = input()
x = input()
n = len(s)
a = []

for num in range(0, 1<<n):
    substring = ""
    for i in range(n):
        if num & (1<<i):
            substring += s[i]
    a.append(substring)
print(a)
if x in a:
    print("yes")
else:
    print('no')
