import os

def rename_files():

    # 从文件夹获取文件名称,r告诉python 接收这个字符串本身，不要用其他方式解读它

    rename_list = os.listdir(r"C:\OOP\prank")



    # 针对每一个文件名称，对其重新命名