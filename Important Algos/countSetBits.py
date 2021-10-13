#Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

#Return the count modulo 109 + 7. INTERVIEW BIT
def result( a ):
    sum_el = 0
    for i in range(1,a+1):
        count = 0
        while i != 0:
            count += 1
            i &= (i-1)
        sum_el+=count
    return  sum_el%((1000000000)+7)

a = int(input())
print(result(a))
