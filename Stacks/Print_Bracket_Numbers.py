def BracketNumber(exp, n):
    left_bnum = 1

    right_bnum = list()

    for i in range(n):
        if exp[i] == '(':
            print(left_bnum, end='')
            right_bnum.append(left_bnum)
            left_bnum += 1

        elif exp[i] == ')':
            print(right_bnum[-1], end='')
            right_bnum.pop()


if __name__ == "__main__":
    exp = "(a+(b*c))+(d/e)"
    n = len(exp)

    BracketNumber(exp, n)
