print('定制自己的手机套餐:')
zidian1 = {1:'.0分钟',2:'.20分钟',3:'.100分钟',4:'.300分钟',5:'.不限量'}
zidian2 = {1:'.0M',2:'.500M',3:'.1G',4:'.5G',5:'.不限量'}
zidian3 = {1:'.0条',2:'.50条',3:'.100条'}
print('A.请设置通话时长:')
for k,v in zidian1.items():
    print(k,v)
k = int(input('输入选择的通话时间编号:'))
print('B.请设置流量:')
for a,b in zidian2.items():
    print(a,b)
a = int(input('输入选择的通话时间编号:'))
print('C.请设置短信条数:')
for i,o in zidian3.items():
    print(i,o)
i = int(input('输入选择的通话时间编号:'))
print('您的手机套餐定制成功:免费通话时长为%s/月，流量为%s/月，短信条数%s/月'%(zidian1[k],zidian2[a],zidian3[i]))
