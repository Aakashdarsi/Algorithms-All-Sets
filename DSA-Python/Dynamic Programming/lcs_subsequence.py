def LCS(string1,string2):
    lcs = [[[] for i in range(len(string1)+1)] for j in range(len(string2)+1)]
    for i in range(1,len(string2)+1):
        for j in  range(1,len(string1)+1):
            if string2[i-1] == string1[j-1]:
                lcs[i][j]= lcs[i-1][j-1]+[string1[j-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    for i in range(len(string2)+1):
        for j in range(len(string1)+1):
            print(lcs[i][j],end="|")
        print()
    return lcs[len(string2)][len(string1)]

string1 = input()
string2 = input()
print(*LCS(string1,string2))