# weixin_Image.bat 单文件解密
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e
# 微信.bat 16进制 e1 c6 e1
# key 值 1e1e 0x1e  weixin.bat-jpg
import subprocess
import os
import lxml
def Jane():
    print("\033[34m+------------------------------------------\033[0m")
    print('+  \033[34mTitle :     Jane WeChat_Image Tools                                            \033[0m')    
    print('+  \033[34m公众号 :           天禧信安                                                   \033[0m')
    print('+  \033[34mEmail  :      admin@janekr.com                         \033[0m')
    print('+  \033[36m用途描述 ： 解密weixin加密的图片信息                            \033[0m')
    print('+  \033[36m使用方法 :   python WeChat_tool.py                                           \033[0m')    
    print('+  \033[36m默认路径 ： C:\\Users\\Administrator\\Documents\\WeChat Files\\wxid_xxx\\FileStorage\\Image\\date  \033[0m')
    print('+------------------------------------------')
Jane()

print("\033[35m 1、单文件解密\033[0m",
      "\033[35m 2、多文件解密\033[0m")

option = int(input("\033[35m 请输入你使用的编号：\033[0m"))

if  option==1:
    os.system('WeChat_alone.py')
    exit()
elif option==2:
    os.system('WeChat_automatic.py')
    exit()
