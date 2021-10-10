import math 

big = int(input())
small = int(input())

number_of_bits = int(math.log(big,2))+1 
result = 0
while small!=0:
    mask = 0<<number_of_bits
    if small&1 == 1:
        mask = ~ mask 
        result = result+big&mask
    small = small>>1 
    big = big<<1 
print(result)
