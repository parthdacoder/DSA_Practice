from collections import Counter


def isPossible(s):
    a = Counter(s)
    a = dict(a)
    c = 0

    for i in a.values():
        if i % 2 == 1:
            c += 1
    if c > 1:
        return False
    return True


print(isPossible("geeksogeeks"))
