#https://www.youtube.com/watch?v=un6PLygfXrA&t=372s
def print_n(n,i):
    if n<i:
        return 
    print_n(n-1,i)
    print(n,end=" ")
    

n = int(input())
print_n(n,1)