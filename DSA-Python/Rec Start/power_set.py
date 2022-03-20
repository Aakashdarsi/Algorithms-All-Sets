# https://www.youtube.com/watch?v=b7AYbpM5YrE
s = input()
n = len(s)
for num in range(0, 1<<n):
    substring = ""
    for i in range(n):
        if num & (1<<i):
            substring += s[i]
    print(substring)
