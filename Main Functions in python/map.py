#suppose if we want to find the square of the element at particular index and create a list with the help of map we can accomplish this task in single line
def area(radius):
    return radius*radius
rl = [1,2,3,4]
print(list(map(area,rl)))