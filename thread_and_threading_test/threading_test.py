# coding=utf-8

# threading模块中Thread类的一个测试程序

#我提交到我自己的GitHub仓库啦

#在远程仓库被修改之后pull到本地 再次修改然后推到远程仓库

import threading
from time import sleep, ctime

def function0():
    print "start function0 at: ", ctime()
    sleep(5)
    print "stop function0 at: ", ctime()

def function1():
    print "start function1 at: ", ctime()
    sleep(3)
    print "stop function1 at: ", ctime()

def main():
    print "starting at: ", ctime()
    t0 = threading.Thread(target=function0)
    t1 = threading.Thread(target=function1)

    t0.start()
    t1.start()

    t0.join()
    t1.join()

    print "all done at: ", ctime()
if __name__=='__main__':
    main()
