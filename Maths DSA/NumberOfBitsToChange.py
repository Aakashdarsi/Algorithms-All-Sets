import math
a = int(input())
b = int(input())
result = a^b 

number_of_digits = int(math.log(result,2))+1
print(number_of_digits)