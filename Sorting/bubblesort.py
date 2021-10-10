'''
used for sorting of elements.


in first pass largest element would be at last
at 2nd pass 2nd largest element would be at last

if there are no swaps then the array is sorted
'''
n = [-10,1,-1,3,56]
swap = False 
for i in range(len(n)):
    
    for j in range(1,len(n)-i):
        if n[j]<n[j-1]:
            n[j],n[j-1]=n[j-1],n[j]
            swap = True
    if swap ==False:
        break

    
    
print(n)