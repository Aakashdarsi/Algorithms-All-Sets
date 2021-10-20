def bubble_sort(a):
    for i in range(len(a)-1):
        pointer = 0 
        flag = False
        while pointer <len(a) - i:
            if pointer == len(a) - 1:
                break
            else:
                if a[pointer]>a[pointer+1]:
                    a[pointer],a[pointer+1] = a[pointer+1],a[pointer]
                    flag = True 
                pointer+=1 
        if flag == False:
            break        
        
            
                
                    
               
        
        
            
            
    print(a)


a = list(map(int,input().split()))
bubble_sort(a)