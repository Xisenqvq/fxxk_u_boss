# 跑路必备
# 用于批量删除python程序的注释

import re
import tkinter as tk
from tkinter import filedialog
import codecs

def remove_comments(file_path):
    # 读取文件内容
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式匹配注释，并删除它们，保留三引号注释防止误伤字符串
    pattern = r'#(?!\").*?(?=\n|$)|\'\'\'.*?(\'\'\')|\"\"\".*?(\"\"\")'
    result = re.sub(pattern, '', content, flags=re.DOTALL)

    # 将处理后的文本写回到原文件
    with codecs.open(file_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print('速速跑路！')

# 创建一个Tkinter窗口，用于选择文件
root = tk.Tk()
root.withdraw()

# 请求用户选择.py文件
file_path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')])

# 删除注释
remove_comments(file_path)

