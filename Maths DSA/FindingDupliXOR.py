def ans(a):
    uno = 0
    for i in a:
        uno^=i 
    return uno


a = [1,2,3,3,4,2,5,6,8]
print(ans(a))