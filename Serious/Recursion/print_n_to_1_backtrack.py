#https://www.youtube.com/watch?v=un6PLygfXrA&t=372s
def print_n(i,n):
    if i >n:
        return 
    print_n(i+1,n)
    print(i,end=" ")
    

n = int(input())
print_n(1,n)