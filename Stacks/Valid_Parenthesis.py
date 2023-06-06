def checkValidParenthesis(exp):
    stack = []
    left_par = ['(', '[', '{']
    right_par = [')', ']', '}']

    for i in (exp):
        if i in left_par:
            stack.append(i)
        elif i in right_par:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if left_par.index(top) != right_par.index(i):
                return False

    return True


exp = "({)"
y = checkValidParenthesis(exp)
print(y)
