"""
1. input函数的意义
    - 程序接受一个输入，并且把输入理解为字符串类型
    - input('请输入第一个整数，并且以回车结束: ')
2. int函数的意义
    - 把函数内的任何东西，转化为int也就是整数类型
3. if 关键字的含义
    - 添加判断条件，如果判断条件满足，则运行对应的内容
4. for 循环的意义
    - 不断反复执行几行代码
5. list 列表的意义
    - 一个变量里面存储了一大堆变量（这些变量可以是数字，也可以是别的）
    - list变量是可以被迭代的
    - list变量可以索引，来获得里面的每个变量
6. \n换行符的意义，转义字符的意义
7. enumerate的意义
    - 返回列表的每一项序号和元素值
8. github的使用
    1. 上传代码
        - git init 在本地文件夹中，创建一个git文件，让github能够识别我们这个文件夹
        - git remote add origin git@github.com:RocStone/python_tutorial.git 本地文件夹链接到远程库
        - git branch -M main 设置主分支的名字
        - git config --global user.email "you@example.com"，告诉github，我的邮箱
        - git config --global user.name "Your Name"，告诉github，我的昵称
        - ssh-keygen -t rsa -C 你的邮箱地址， 生成秘钥，并且要上传到github，设置，ssh and GPR keys里面添加进去
        - git add * 把本地所有代码添加到暂存区域
        - git commit -m"注释内容"，把在暂存区域的内容提交到上传区域
        - git push origin main 把上传区域的代码提交到远程仓库
    2. 下载代码
        - git clone 你的仓库地址
        - 仓库地址就在你的项目网站上
    3. 下次上传新内容的时候，照做这三步
        - git add * 把本地所有代码添加到暂存区域
        - git commit -m"注释内容"，把在暂存区域的内容提交到上传区域
        - git push origin main 把上传区域的代码提交到远程仓库
9. 字典dict
    a = dict()
    a['卢'] = '这是一种常用的姓氏'

    1. 这里的卢是一个key，也就是键
    2. 这里的'这是一种常用的姓氏'，是一个value，也就是值
    3. 字典就是由一大堆的键值对组成的。
    4. 值可以是各种数据类型，比如说str, int, float, list, tuple


链接：
1. pycharm下载链接，https://www.jetbrains.com/pycharm/download/#section=windows
2. 身高体重数据，http://people.ucsc.edu/~cdobkin/NHIS%202007%20data.csv
3. python中文文档，docs.python.org/zh-cn/3/library
4. seaborn 中文文档，https://www.kancloud.cn/apachecn/seaborn-doc-zh/1946247
5. 国内下载python的好去处，http://npm.taobao.org/mirrors/python/3.8.8/
6. 清华pip镜像 https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
7. 安装 jupyter lab 3: pip install jupyterlab==3
8. 安装 jupyter lab 中文包: https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/jupyterhub/jupyterlab_language_pack_zh_CN-0.0.1.dev0-py2.py3-none-any.whl
"""

