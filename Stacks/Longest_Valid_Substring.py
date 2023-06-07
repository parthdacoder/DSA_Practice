def solve(s, n):
    left = 0
    right = 0
    maxlength = 0

    for i in range(n):
        if (s[i] == '('):
            left += 1
        else:
            right += 1

    if (left == right):
        maxlength = max(maxlength, right*2)

    elif (right > left):
        left = right = 0

    left = right = 0

    for i in range(n-1, -1, -1):
        if (s[i] == '('):
            left += 1
        else:
            right += 1

        if (left == right):
            maxlength = max(maxlength, left*2)

        elif (left > right):
            left = right = 0

    return maxlength


print(solve("(((())))))", 10))  # wrong set of parenthseis
print(solve("((()()()()(((())", 16))  # right set of parenthesis
