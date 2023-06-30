def sameFreq(str):
    mapper = {}
    total = 0
    ans = "No"

    for i in range(len(str)):
        mapper[str[i]] = mapper.get(str[i], 0) + 1

        for count in mapper.values():
            total += count

        if total % len(mapper.keys()) == 0:
            ans = "Yes"

        if (total - 1) % len(mapper.keys()) == 0:
            ans = "Yes"

        return ans


print(sameFreq("aabccc"))
