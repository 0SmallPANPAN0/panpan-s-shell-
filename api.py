import os
import time
print('panpan shell vesion 0.1 for windows by bilibili-Small_PANPAN\nautoz sus!!!')
command=['cmd（打开windws cmd）','exit(退出)','autoz-sus(彩蛋)','sys（执行系统命令）','111.py透明窗口']
def main():
    a=input('shell~')

    if a=='cmd':
        os.system('cmd')
    elif a=='exit':
        exit()
    elif a=='autoz-sus':
        for i in range(500):
            print('锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷',i)
            time.sleep(0.09)
    elif a=='sys':
        b=input('sys:')
        os.system(b)
    elif a=='help':
        print(command)
    elif a=='win':
        os.system('python 111.py')