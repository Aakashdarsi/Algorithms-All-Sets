def rec_subset_sum(subset,n,sume_e):
    if n==0 or sume_e==0:
        return True
    else:
        
    
        return rec_subset_sum(subset,n-1,sum_e) or rec_subset_sum(subset,n-1,sume_e-subset[n-1])


subset = [1,2,3]
sum_e = 5 
n = len(subset)
res= rec_subset_sum(subset,n,sum_e)
print(res)