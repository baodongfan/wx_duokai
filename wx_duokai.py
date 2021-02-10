#coding:utf-8
# command to start WeChat App  'start "" "C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"\n'

import os


# 检测微信安装位置
path_c = "C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
path_d = "D:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
path_e = "E:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
path_f = "F:\Program Files (x86)\Tencent\WeChat\WeChat.exe"

if os.path.isfile(path_c):
	path = path_c
elif os.path.isfile(path_d):
	path = path_d
elif os.path.isfile(path_e):
	path = path_e
elif os.path.isfile(path_f):
	path = path_f
else:
	print('Not found WeChat Program, Please check it.')

# print('path is : ', path)



num = input('想要打开几个微信： ')
os.system('echo nothing : %s' % num)

# 构建cmd打开微信命令
ff = 'start "" ' + '"' + path + '"' + '\n'
name = 'mu.bat'

with open(name, 'w')  as f:
    f.write(int(num) * ff)
    f.close()

os.system(name)
os.remove(name)
