month = int(input('请输入月份(例如:5):'))
date = int(input('请输入日期(例如:17):'))
if month == 3 and date in range(21,32) or month == 4 and date in range(1,20):
    print('%d月%d日星座为:白羊座')
if month == 4 and date in range(20,31) or month == 5 and date in range(1,21):
    print('%d月%d日星座为:金牛座')
if month == 5 and date in range(21,32) or month == 6 and date in range(1,22):
    print('%d月%d日星座为:双子座')
if month == 6 and date in range(22,31) or month == 7 and date in range(1,23):
    print('%d月%d日星座为:巨蟹座')
if month == 7 and date in range(23,32) or month == 8 and date in range(1,23):
    print('%d月%d日星座为:狮子座')
if month == 8 and date in range(23,32) or month == 9 and date in range(1,23):
    print('%d月%d日星座为:处女座')
if month == 9 and date in range(23,31) or month == 10 and date in range(1,24):
    print('%d月%d日星座为:天秤座')
if month == 10 and date in range(24,32) or month == 11 and date in range(1,23):
    print('%d月%d日星座为:天蝎座')
if month == 11 and date in range(23,31) or month == 12 and date in range(1,22):
    print('%d月%d日星座为:射手座')
if month == 12 and date in range(22,32) or month == 1 and date in range(1,20):
    print('%d月%d日星座为:摩羯座')
if month == 1 and date in range(20,32) or month == 2 and date in range(1,19):
    print('%d月%d日星座为:水瓶座')
if month == 2 and date in range(19,30) or month == 3 and date in range(1,21):
    print('%d月%d日星座为:双鱼座')


















