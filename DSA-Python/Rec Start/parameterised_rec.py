def cal(n,sum):
    if n< 1:
        print(sum)
        return
    cal(n-1,sum+n) # Making changes in parameter for causing recursion
    # (2,0) -> (1,2) - > (0,3) recursion going on like this 
    # we can see that how recursion is mainly affecting parameters
    # this is called parameterised recursion
    
        

n = int(input())
cal(n,0)
