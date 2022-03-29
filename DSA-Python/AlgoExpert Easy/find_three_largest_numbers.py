def find_3_largest(array):
    threeLargest = [None,None,None]
    for i in array:
        update_largest(threeLargest,i)
    return threeLargest
def update_largest(threeLargest,number):
    if threeLargest[2] == None or number > threeLargest[2]:
        shiftAndUpdate(threeLargest,number,2) #Todo
    elif threeLargest[1] == None or number> threeLargest[1]:
        shiftAndUpdate(threeLargest,number,1)
    elif threeLargest[0] == None or number > threeLargest[0]:
        shiftAndUpdate(threeLargest,number,0)

def shiftAndUpdate(array,number,index):
    # [0,1,2]
    # [x,y,z]
    # for i in range(2+1):
    # if i == 2:
    # then update at that particular position
    # otherwise array[i] == array[i+1]
    for i in range(index+1):
        if i == index:
            array[i] = number
        else:
            array[i] = array[i+1]
l = list(map(int,input().split()))
print(find_3_largest(l))
