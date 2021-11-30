def rec_printer(n):
    if n==1:
        print(1)
    else:
        rec_printer(n-1)
        print(n)
n = int(input())
rec_printer(n)