def power_set(s):
    n = len(s)
    for num in range(0,2**(n-1)):
        for i in range(num):
            substring = ""
            if num & 1<<i:
                substring+=s[i]
        print(substring)
    
