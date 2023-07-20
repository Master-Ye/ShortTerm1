import csv
import re
from collections import defaultdict
def format_data1(raw_data):
    date_counts = defaultdict(int)
    for row in raw_data:
        date_string = row[0]
        date_counts[date_string] += 1

    formatted_data = [[date, str(count)] for date, count in date_counts.items()]

    return formatted_data
def format_data(raw_data):
    formatted_data = []
    for row in raw_data[1:]:
        time_string = row[1]
        date_string = format_date(time_string)

        formatted_row = [date_string, row[0]]
        formatted_data.append(formatted_row)

    return formatted_data

def format_date(time_string):
    # 使用正则表达式提取时间字符串中的年、月、日信息
    match = re.search(r'(\d{1,2})月(\d{1,2})日', time_string)
    if match:
        month = match.group(1)
        day = match.group(2)
    else:
        match = re.search(r'(\d{1,2}):(\d{1,2})', time_string)
        month = '01'  # 默认月份为1月
        day = '08'  # 默认日期为8日

    date_string = f'2023-{month.zfill(2)}-{day.zfill(2)}'

    return date_string

with open('data.csv', 'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    raw_data = list(reader)

formatted_data = format_data(raw_data)

formatted_data = format_data1(formatted_data)

for i, row in enumerate(formatted_data):
    print(row, end='')
    if i < len(formatted_data) - 1:
        print(',', end='')
