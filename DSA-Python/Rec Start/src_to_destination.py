def func(src,des):
    print(str(src)+"Curr pos and des pos "+str(des))
    if src == des:
        print("Reached destination")
        return
    func(src+1,des)



src = int(input())
des = int(input())
func(src,des)