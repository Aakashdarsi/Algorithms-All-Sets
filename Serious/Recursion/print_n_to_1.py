#https://www.youtube.com/watch?v=un6PLygfXrA&t=372s
def print_n_1(n,i):
    if n<i:
        return
    print(n,end=" ")
    print_n_1(n-1,i)

n = int(input())
print_n_1(n,1)