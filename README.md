## 项目背景

一天早上，我找不到房子的钥匙了，不久我收到朋友发来的信息，信息上说：“你房子的钥匙被我们藏起来了，要找到钥匙必须解决一个谜题，在你的电脑上有一个文件夹，里面有很多张照片，当照片的文件名中的数字被移除时，这些重命名后的照片会显露出一个隐秘的信息，它能够指引你找到房子的钥匙”。

逐个命名这50张照片会花上好长时间，于是我必须在我朋友回来之前想办法解决这个谜题。

## 项目目标

写一个程序，移除照片名称中的数字，使得重新命名后的照片显示出一个隐秘的信息。

打开文件夹，里面大约有50张照片，现在照片的顺序是乱的，无法得知其隐含的隐秘消息：
![未重命名前的照片](/image/original.png)

使用程序去除文件名称中的数字后，你将得到这样的照片顺序：
![重命名后的照片](/image/new.png)

这些重命名后的照片显露出了一个隐秘的信息：
KEYS ARE IN THE CLOSET. BEHIND THE SHOE BOX.


## 程序实现过程

思考如何编写这个程序呢？需要几个步骤？其实就两个步骤：
1. 打开文件夹，并获取文件的文件名称
2. 给这些文件重命名，去除文件名称中的数字

**1.打开文件夹，并获取文件的文件名称**

我们Google一下如何获取文件中的文件名称，发现有一个os模块的listdir()可用，
```
# -*- coding:utf-8 -*-

# 导入 os 模块
import os
def rename_files():
    '''
    函数用于获取文件的文件名称，并去除文件名称中指定的数字
    '''
    # 第一步：从文件夹获取文件的文件名称
    rename_list = os.listdir(r"/Users/cunxi/Python_Project/private_news/prank")
    print(rename_list)
    # 第二步：针对每一个文件的文件名称，去除数字，对其重新命名

rename_files()
```

打印输出，证明os.listdir()是否可用：
```
['68pune.jpg', '45ithaca.jpg', '47london.jpg', '72bucharest.jpg', '97oakland.jpg', '.DS_Store', '89berkeley.jpg', '48sunnyvale.jpg', '93manchester.jpg', '4istanbul.jpg', '17cairo.jpg', '83gainesville.jpg', '72bangalore.jpg', '47singapore.jpg', '9barcelona.jpg', '35miami.jpg', '90beijing.jpg', '22rochester.jpg', '41seoul.jpg', '74tel aviv.jpg', '37athens.jpg', '45austin.jpg', '2chennai.jpg', '36sydney.jpg', '28houston.jpg', '2hyderabad.jpg', '73delhi.jpg', '54dallas.jpg', '47sao paulo.jpg', '50san diego.jpg', '64seattle.jpg', '16los angeles.jpg', '52new york.jpg', '61edinbrugh.jpg', '46colombo.jpg', '25madrid.jpg', '29buenos aires.jpg', '5bogota.jpg', '88jacksonville.jpg', '29bristol.jpg', '69shanghai.jpg', '96karachi.jpg', '69chicago.jpg', '66san jose.jpg', '55kiev.jpg']
```

虽然输出结果不是那么美观，但的确证明os.listdir()可用。

下面，我们开始做第二步，去除文件名称中的数字，给文件名称重命名。

**2.给这些文件重命名，去除文件名称中的数字**

我们查看[os文档](https://docs.python.org/3.6/library/os.html),有一个叫rename(src,dst,src_dir_fd=None, dst_dir_fd=None)函数，它可以读取文件的来源或者当前名称，并将其改为目标地址或更改为新的名称。

我们要给50张照片重命名，因此这里要用到for循环:
```
# -*- coding:utf-8 -*-

# 导入 os 模块
import os
def rename_files():
    '''
    函数用于获取文件的文件名称，并去除文件名称中指定的数字
    '''
    # 第一步：从文件夹获取文件的文件名称
    rename_list = os.listdir(r"/Users/cunxi/Python_Project/private_news/prank")

    # 第二步：针对列表中每一个文件的文件名称，去除数字，对其重新命名
    for rename_file in rename_list:
        os.rename(rename_file,rename_file.translate(None,'0123456789'))

rename_files()
```

```
os.rename(rename_file,rename_file.translate(None,'0123456789'))
```
rename_file 是文件的原始名称，
rename_file.translate(None,'0123456789')是去除文件名称中的数字，以达到重命名的目的。

字符串函数 translat() 接收2个参数，
第一个参数是一个数据表，其能将一个字符集转译程另一个字符集，我们这里不需要，因此可以使用关键字None。
第二个参数是一个列表，包含了我们想要从字符串中移除的所有字符，这里指的是那些数字，也就是0123456789

运行上述代码：
```
Traceback (most recent call last):
  File "/Users/cunxi/Python_Project/private_news/private_news.py", line 17, in <module>
    rename_files()
  File "/Users/cunxi/Python_Project/private_news/private_news.py", line 14, in rename_files
    os.rename(rename_file,rename_file.translate(None,'0123456789'))
OSError: [Errno 2] No such file or directory
```

错误显示找不到文件，显示是os.rename()出现了问题，可能是我们在重命名文件名称时，程序浏览的文件夹中找不到要命名的文件。
大白话解释就是：程序想对列表rename_list中文件名称为ABC进行重命名，于是在当前工作目录找这个文件，但是却找不到。必须找到要重命名文件的文件夹才能给文件重命名。
因此，我们获取下当前的工作目录看一下，看当前的工作目录和要重命名文件的工作目录是否相同。

os.getcwd()方法获取当前的工作目录：
```
# -*- coding:utf-8 -*-

# 导入 os 模块
import os
def rename_files():
    saved_path = os.getcwd()
    # 打印工作目录
    print('当前的工作目录是：' + saved_path)

rename_files()
```

结果显示工作目录是：
```
当前的工作目录是：/Users/cunxi/Python_Project/private_news
```

而我们要重命名的文件在 /Users/cunxi/Python_Project/private_news/prank，两个目录不相同，程序在文件夹private_news中找不到要命名的文件，所以程序才报错。

为了解决这个问题，需要将当前的工作目录 切换至 /Users/cunxi/Python_Project/private_news/prank，可以使用方法os.chdir()。

```
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
```

在输出区可以看到输出结果，返回到之前的文件夹中，查看文件，发现已经被成功重命名：
![重命名后的照片](/image/new.png)


## 用到的库和方法

1. os文件

os文件的其他方法请查看[os文档](https://docs.python.org/3.6/library/os.html)

2. os.listdir()

方法用于返回指定的文件夹包含的文件或文件夹名称的** 列表 ** 。

3. translat()

字符串函数translat()接收2个参数，第一个参数是一个数据表，其能将一个字符集转译程另一个字符集，我们这里不需要，因此可以使用关键字None。第二个参数是一个列表，包含了我们想要从字符串中移除的所有字符，这里指的是那些数字，也就是0123456789

4. os.getcwd()

该方法返回当前工作目录。

5. os.chdir()

该方法改变当前的工作目录

## 如何使用

1. Python 3.6 版本

