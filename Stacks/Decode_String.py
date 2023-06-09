def decodeString(exp: str):
    times = 1
    out = " "
    for i in range(len(exp)):
        if exp[i] == '1' or '2' or '3':
            y = exp[i].isnumeric()
            times = times*y

    print(times)
# s = ['1', '2', '3', '4', '5']
# exp = "[ab]"
# middle = ""
# i = 0

# while i < len(exp):
#     if exp[i] == '[':
#         i += 1
#         while exp[i] != ']':
#             middle += exp[i]
#             i += 1
#     i += 1


# print(middle)
decodeString("[ab]")
