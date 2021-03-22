from pprint import pprint

# 读取文件到字典
table = dict()
with open('./data/NHIS 2007 data.csv') as f:
    header = f.readline().strip().split(',')
    print(header)
    for line in f:
        line = line.strip().split(',')
        hhx = line[0]
        table[hhx] = dict()
        table[hhx][header[1]] = line[1]
        table[hhx][header[2]] = line[2]
        table[hhx][header[3]] = int(line[3])
        table[hhx][header[4]] = float(line[4])
        table[hhx][header[5]] = int(line[5])
        table[hhx][header[6]] = int(line[6])
        table[hhx][header[7]] = int(line[7])
        table[hhx][header[8]] = int(line[8])

# 对字典内容进行计算处理
for key, value in table.items():
    if value['weight'] < 400 and value['height'] < 90:
        new_BMI = value['weight'] * 0.45359237 / (value['height'] * 0.0254) ** 2
        print(new_BMI - value['BMI'])
