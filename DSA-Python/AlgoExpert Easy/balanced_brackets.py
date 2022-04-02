# Time complexity is O(N) because we need to traverse throughout the string 
# Space complexity is O(N) literally if we have all opening brackets 



def balanced_brackets(string):
    opening_brackets = '({['
    closing_brackets = '}])'
    matching_brackets = {'}':'{' ,']':'[' ,')':'('}
    stack = []
    for i in string:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            if len(stack) == 0:
                return False 
            if stack[-1] == matching_brackets[i]:
                stack.pop()
            else:
                return False 
    return len(stack) == 0
            
s = input()
print(balanced_brackets(s))
