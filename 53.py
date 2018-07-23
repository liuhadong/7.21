def judge(string):
    print(string.islower())
    if string.islower():
        print('是由小写字母和数字组成')
    else:
        print('不是由小写字母和数字组成')
word = input('请输入:')
judge(word)
