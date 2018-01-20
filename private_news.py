# -*- coding:utf-8 -*-
# 导入 os 模块
import os
def rename_files():
    '''
    函数用于获取文件的文件名称，并去除文件名称中指定的数字
    '''
    # 第一步：从文件夹获取文件的文件名称
    rename_list = os.listdir(r"/Users/cunxi/Python_Project/private_news/prank")

    # 获取当前的工作目录
    saved_path = os.getcwd()
    # 打印工作目录
    print('当前的工作目录是：' + saved_path)

    # 切换当前的工作目录至要命名文件的所在目录
    os.chdir(r'/Users/cunxi/Python_Project/private_news/prank')
    # 第二步：针对列表中每一个文件的文件名称，去除数字，对其重新命名
    for rename_file in rename_list:
        # 打印重命名前的文件的文件名称
        print("原始文件名称：" + rename_file)
        # 去除文件名称中的数字，对其重命名
        os.rename(rename_file,rename_file.translate(None,'0123456789'))
        # 打印重命名后的文件的文件名称
        print("重命名后的文件名称：" + rename_file.translate(None,'0123456789'))

# 执行函数
rename_files()

