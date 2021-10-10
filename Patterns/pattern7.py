n = int(input())
for i in range(1,n+1):
    no_of_spaces = " "*n - i 
    if i==1:
        print(no_of_spaces+str(1))
    else:
        no_of_repeats = i+2 
        
