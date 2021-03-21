


print('本程序的功能是计算BMI')
a = input('请输入你的体重，以千克为单位: ')
a = float(a)

b = input('请输入你的身高，以米为单位: ')
b = float(b)

BMI = a / b ** 2

if BMI < 18.5:
    print('体重太轻')
elif BMI < 24:
    print('体重正常')
elif BMI < 27:
    print('体重过重')
elif BMI < 30:
    print('轻度肥胖')
elif BMI < 35:
    print('中度肥胖')
elif BMI >= 35:
    print('重度肥胖')

