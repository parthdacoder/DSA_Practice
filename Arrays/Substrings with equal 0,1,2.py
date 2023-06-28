def getSubstringWithEqual012(string):
    mp = dict()
    mp[(0, 0)] = 1

    zc, oc, tc = 0, 0, 0

    res = 0

    for i in range(len(string)):
        if string[i] == "0":
            zc += 1
        elif string[i] == "1":
            oc += 1
        elif string[i] == "2":
            tc += 1

        tmp = (zc - oc, zc - tc)

        if tmp not in mp:
            res += 0
        else:
            res += mp[tmp]

        if tmp in mp:
            mp[tmp] += 1
        else:
            mp[tmp] = 1

    return res


if __name__ == "__main__":
    string = "0102010"
    print(getSubstringWithEqual012(string))
