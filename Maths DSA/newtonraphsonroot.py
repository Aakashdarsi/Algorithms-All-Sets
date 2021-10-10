def nr(n):
    assumed_root = n 
    while True:
        calculated_root = 0.5*(assumed_root+ n/assumed_root)
        if (abs(calculated_root-assumed_root)<0.1):
            print(calculated_root)
            break 
        else:
            assumed_root = calculated_root



n = int(input())
nr(n)