import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

counter = [0, 0, 0, 0, 0, 0]
sleep_count = [0 for i in range(24)]
height1 = 0
height2 = 0
number1 = 0
number2 = 0
BMI1 = 0
BMI2 = 0

with open('data/NHIS 2007 data.csv') as f:
    f.readline()
    for line in f:
        line = line.strip()
        line = line.split(',')
        gender = int(line[3])
        height = float(line[7]) * 0.0254
        weight = float(line[8]) * 0.45359237
        sleep = int(line[5])
        if float(line[7]) < 90 and float(line[8]) < 900 and float(line[5]) < 24:

            sleep_count[sleep] += 1
            BMI = weight / height ** 2
            print(BMI)
            if gender == 1:
                height1 += height
                BMI1 += BMI
                number1 += 1
            elif gender == 2:
                height2 += height
                BMI2 += BMI
                number2 += 1

    print(sleep_count)
    print(f'男生身高：{height1 / number1:.2f} 女生身高：{height2 / number2:.2f}')
    print(f'男生BMI：{BMI1 / number1:.2f} 女生BMI：{BMI2 / number2:.2f}')
    print(f'男生人数为:{number1}，女生人数为：{number2}')
    # print(height1, height2, number1, number2, height1 / number1, height2 / number2)

sns.barplot(x=[i for i in range(24)], y=sleep_count)
plt.show()
