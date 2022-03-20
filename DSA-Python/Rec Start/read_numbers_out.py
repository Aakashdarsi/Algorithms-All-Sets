def read_loud(n,a):
    if n == 0:
        return
    x = n%10 
    read_loud(n//10,a)

    print(a[x],end=" ")
    
n = int(input())
a = ['zero','one','two','three','four','five','six','seven','eight','nine']
read_loud(n,a)