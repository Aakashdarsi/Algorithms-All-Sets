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
# Edge cases 
# If we come across a closing paranthesis but the stack is empty then it is not balanced 
# If the stack is not empty then we check the top value of stack if both are matching then pop the element from stack
# If it is not matching clearly it is unbalanced 