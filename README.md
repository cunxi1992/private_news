
## 项目背景


一天早上，我找不到房子的钥匙了，不久我收到朋友发来的信息，信息上说：“你房子的钥匙

被我们藏起来了，要找到钥匙必须解决一个谜题，在你的电脑上有一个文件夹，里面有很多张图片，

当照片的文件名中的数字被移除时，这些重命名后的照片会显露出一个隐秘的信息，它能够指引你找到房子的钥匙”

逐个命名这50张照片会花上好长时间，于是我必须在我朋友回来之前想办法解决这个谜题。





## 项目目标



写一个程序，移除图片名称中的数字，使得重新命名后的图片显示出一个隐秘的信息



附上处理前和处理后的



模块 os 的文档  练习6



## 思考



请先思考，如何编写这个程序





打开sublime 编辑器，新建文件，并将文件命名为 rename_files.py





## 用到的函数



字符串行数 translat() 接收2个参数，第一个参数是一个数据表，其能将一个字符集转译程另一个字符集，我们这里不需要，因此可以使用关键字None。

第二个参数是一个列表，包含了我们想要从字符串中移除的所有字符，这里指的是那些数字，也就是0123456789



import os



def rename_files():

    # 从文件夹获取文件名称,r告诉python 接收这个字符串本身，不要用其他方式解读它

    rename_list = os.listdir(r"C:\OOP\prank")



    # 针对每一个文件名称，对其重新命名


