'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''


n = int(input())
no_of_rows = 2*n 
for i in range(1,2*n):
    if i<=n:
        res = "* "*i 
        print(res)
    else:
        res = "* "*(no_of_rows-i)
        print(res)
    