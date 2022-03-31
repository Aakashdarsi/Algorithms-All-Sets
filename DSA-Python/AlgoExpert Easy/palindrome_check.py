# Approach 1
def palindrome_1(string):
    x = string[::-1]
    return x == string
# Approach 2
def palindrome_2(string):
    low = 0 
    high = len(string)-1
    while low < high :
        if string[low] != string[high]:
            return "Non palindrome"

        else:
            low+=1 
            high -= 1
    return "It's a palindrome"
