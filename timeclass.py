import csv
from datetime import datetime

# 定义时间段的范围
time_ranges = [
    ("00:00", "04:00"),
    ("04:00", "08:00"),
    ("08:00", "12:00"),
    ("12:00", "16:00"),
("16:00", "20:00"),
("20:00", "23:59")
]

# 创建一个字典来保存每个时间段的数量
time_counts = {range: 0 for range in time_ranges}

# 读取CSV文件
with open('data.csv', 'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    for row in reader:
        # 解析时间列
        time_str = row[1].split(' ')[1]  # 提取时间部分，忽略日期和来自信息
        if time_str:
            hour = int(time_str.split(':')[0])

            # 检查时间所属的时间段
            for time_range in time_ranges:
                start_time = int(time_range[0].split(':')[0])
                end_time = int(time_range[1].split(':')[0])
                if start_time <= hour < end_time:
                    # 增加对应时间段的计数
                    time_counts[time_range] += 1
                    break

# 打印每个时间段的数量
for time_range, count in time_counts.items():
    print(f"{time_range[0]} - {time_range[1]}: {count}")