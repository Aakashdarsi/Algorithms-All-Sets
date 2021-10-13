# BF indicates brute force
# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a langua ge that has finite-precision arithmetic.
# sample input -> [1,2,9],[1,3,1]
# sample output - > [1,3,0],[1,3,2]
n = input().split()
int_str = ''
for i in n:
    int_str +=i 
int_int = str(int(int_str)+ 1)
print(list(int_int))
