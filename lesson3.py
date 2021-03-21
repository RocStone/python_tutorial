counter = [0, 0, 0, 0, 0, 0]

with open('data/NHIS 2007 data.csv') as f:
    f.readline()
    for line in f:
        line = line.strip()
        line = line.split(',')
        height = float(line[7]) * 0.0254
        weight = float(line[8]) * 0.45359237
        print(f'{height:.2f} {weight:.2f}', end=' ')
        BMI = weight / height ** 2
        print(f'{BMI:.2f}', end=' ')

        if float(line[7]) < 90 and float(line[8]) < 900:
            if BMI < 18.5:
                print('体重太轻')
                counter[0] += 1
            elif BMI < 24:
                print('体重正常')
                counter[1] += 1
            elif BMI < 27:
                print('体重过重')
                counter[2] += 1
            elif BMI < 30:
                print('轻度肥胖')
                counter[3] += 1
            elif BMI < 35:
                print('中度肥胖')
                counter[4] += 1
            elif BMI >= 35:
                print('重度肥胖')
                counter[5] += 1

population = sum(counter)
print(counter)

percentage = [0, 0, 0, 0, 0, 0]
#            [64, 1186, 1053, 851, 720, 911]
for i, j in enumerate(counter):
    percentage[i] = j / population

for p in percentage:
    print(f"{p:.2f}", end=' ')

print()

import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

sns.barplot(x=['偏瘦', '正常', '偏重', '小胖', '中胖', '大胖'], y=percentage)
plt.show()