word = input('请输入:')
a = word.lower()
zidian = {}
for i in a:
    if i in zidian.keys():
        zidian[i] += 1
    else:
        zidian[i] = 1
print(zidian)
