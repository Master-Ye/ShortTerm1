import csv

# 指定CSV文件路径和txt文件路径
csv_file_path = 'data.csv'
txt_file_path = 'data.txt'

# 加载CSV文件的第一列数据到txt文件
with open(csv_file_path, mode='r',encoding='utf-8') as csv_file, open(txt_file_path, mode='w',encoding='utf-8') as txt_file:
    reader = csv.reader(csv_file)
    next(reader)  # 跳过表头
    for row in reader:
        txt_file.write(row[0] + '\n')

print('数据加载到txt文件成功！')
