# weixin_Image.bat 单文件解密
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e
# 微信.bat 16进制 e1 c6 e1
# key 值 1e1e 0x1e  weixin.bat-jpg

import os
def Jane():
    print("\033[34m+------------------------------------------\033[0m")
    print('+  \033[34mTitle :     Jane WeChat_Image alone                                           \033[0m')    
    print('+  \033[34m公众号 :           天禧信安                                                   \033[0m')
    print('+  \033[34mEmail  :      admin@janekr.com                         \033[0m')
    print('+  \033[34m文件模式 :         单文件解密                                                   \033[0m')
    print('+  \033[36m用途描述 ： 解密weixin加密的图片信息                            \033[0m')
    print('+  \033[36m使用方法 :    python WeChat_alone.py                                           \033[0m')    
    print('+  \033[36m默认路径 ： C:\\Users\\Administrator\\Documents\\WeChat Files\\wxid_xxx\\FileStorage\\Image\\date  \033[0m')
    print('+------------------------------------------')
Jane()

#微信image文件路径
into_path  = input("\033[35m 请输入需要解密微信dat文件的目录: \033[0m")
#微信图片转码后的保存位置
out_path = into_path + "/"

def imageDecode(f,fn):
    """
    解码
    :param f: 微信图片路径
    :param fn:微信图片目录下的.bat
    :return:
    """
    # 读取.bat
    dat_read = open(f,"rb")
    # 图片输出路径
    out = out_path + fn + ".jpg"
    # 图片写入
    png_write = open(out,"wb")
    # 循环字节
    for now in dat_read:
        for nowByte in now:
            # 转码计算
            newByte = nowByte ^ 0xF4 #此处F4为解密码
            # 转码后重新写入
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()
    # pass

def findFile(f):
    """
    查找文件
    :param f:微信图片路径
    :return:
    """
    # 把路径文件夹下的文件以列表呈现
    fsinfo = os.listdir(f)
    # 逐步读取文件
    for fn in fsinfo:
        # 拼接路径：微信图片路径+图片名
        temp_path = os.path.join(f,fn)
        # 判断目录还是.bat
        if not os.path.isdir(temp_path):
            print('文件解密路径：{}'.format(temp_path) + " 文件解密完成")
            print('解密存放路径：{}'.format(temp_path) +".jpg"+"文件存储正常" )
            # 转码函数
            imageDecode(temp_path,fn)
        else:
            pass

# 运行
findFile(into_path)
