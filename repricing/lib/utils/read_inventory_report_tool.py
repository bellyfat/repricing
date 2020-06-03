import os

import sys

sys.path.append('..')


def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    return file_new


def read_file_by_size(file, size):
    with open(file, 'r') as f:
        lines = []
        while len(lines) < size:
            line = f.readline()
            lines.append(line)
        f.close()
    return lines[1:]


if __name__ == '__main__':
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + '/reports'
    print(file_path)
    file = new_report(file_path)
    lines = read_file_by_size(file, 4)
    print(lines)
# /Users/enxiaoxu/Projects/Repricing/reports
# ['JiuUSBk2016-0620-C09022,B01FEOIW0Q,30.14,3\n', 'JiuUSBk2016-0620-C14250,B01FEOLGLS,31.11,3\n', 'JiuUSBk2016-0620-C15273,B01FEOI7ZQ,37.49,3\n']