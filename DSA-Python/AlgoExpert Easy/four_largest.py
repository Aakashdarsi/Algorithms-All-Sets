from re import L


def four_largest(array):
    if len(array) < 4:
        return "4 largest can't be found"

    else:
        a = [None,None,None,None]
        for i in array:
            shiftAndUpdate(a,i)
        return a 
def shiftAndUpdate(larray,number):
    if larray[3] == None or number > larray[3]:
        insert_into_pos(larray,3,number)
    elif larray[2] == None or number > larray[2]:
        insert_into_pos(larray,2,number)
    elif larray[1] == None or number > larray[1]:
        insert_into_pos(larray,1,number)
        
    elif larray[0] == None or number > larray[0]:
        insert_into_pos(larray,0,number)
                 


def insert_into_pos(larray,index,number):
    for i in range(index+1):
        if i == index:
            larray[i] = number 
        else:
            larray[i] = larray[i+1]

l = list(map(int,input().split()))
print(four_largest(l))
