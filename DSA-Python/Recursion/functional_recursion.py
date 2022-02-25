#https://www.youtube.com/watch?v=69ZCDFy-OUo&t=212s
# Here the output should be returned by the function not by the parameters of the function
from shutil import register_unpack_format


def function_stp(n):
    if n == 0:
        return 0
    return n+function_stp(n-1)
n = int(input())
a = function_stp(n)
print(a)