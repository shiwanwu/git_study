from docx import Document
import os
import win32com.client


with open('pi_digits.txt') as f: # 打开文件
    contents = f.read() # 读取文件内容
    print("-------------without rstrip()-------------")
    print(contents)
    print("-------------with rstrip()-------------")
    print(contents.rstrip()) # 去掉末尾的换行符

file_path = 'D:\\resume\\sv.doc'
if not os.path.exists(file_path):
    print("File not found.")
else:
    with open(file_path) as f2:
        contents = f2.read()       # 读取文件内容
        print("\n文档内容")
        print("-"* 50)
        print(contents)
        print("-"* 50)