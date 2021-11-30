# To Print 1 too numbers using recursion
def printer(n):

    if n==1:
        print(1)

    else:
        printer(n-1)
        print(n)

n = int(input())
printer(n)