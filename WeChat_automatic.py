# weixin_Image.bat 自动化文件解密
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e
# 微信.bat 16进制 e1 c6 e1
# key 值 1e1e 0x1e  weixin.bat-jpg

import os
def Jane():
    print("\033[34m+------------------------------------------\033[0m")
    print('+  \033[34mTitle :      Jane WeChat_automatic                                            \033[0m')    
    print('+  \033[34m公众号 :           天禧信安                                                   \033[0m')
    print('+  \033[34mEmail  :      admin@janekr.com                         \033[0m')
    print('+  \033[34m文件模式 :        多文件解密                                                   \033[0m')
    print('+  \033[36m用途描述 ：  解密weixin加密的图片信息                            \033[0m')
    print('+  \033[36m使用方法 :  python WeChat_automatic.py                                           \033[0m')    
    print('+  \033[36m默认路径 ：C:\\Users\\Administrator\\Documents\\WeChat Files\\wxid_xxx\\FileStorage\\Image\\date  \033[0m')
    print('+------------------------------------------')
Jane()

# 图片字节头信息，
#[0][1]为jpg头信息，
#[2][3]为png头信息，
#[4][5]为gif头信息
pic_head = [0xff, 0xd8, 0x89, 0x50, 0x47, 0x49]
# 解密码
decode_code = 0

def get_code(file_path):
    """
    自动判断文件类型，并获取dat文件解密码
    :param file_path: dat文件路径
    :return: 如果文件为jpg/png/gif格式，则返回解密码，否则返回0
    """
    dat_file = open(file_path, "rb")
    dat_read = dat_file.read(2)
    head_index = 0
    while head_index < len(pic_head):
    # 使用第一个头信息字节来计算加密码
    # 第二个字节来验证解密码是否正确
        code = dat_read[0] ^ pic_head[head_index]
        idf_code = dat_read[1] ^ code
        head_index = head_index + 1
        if idf_code == pic_head[head_index]:
            dat_file.close()
            return code
        head_index = head_index + 1

    print("Not jpg, png, gif")
    return 0


def decode_dat(file_path):
    """
    解密文件，并生成图片
    :param file_path: dat文件路径
    :return: 无
    """
    decode_code = get_code(file_path)
    dat_file = open(file_path, "rb")
    pic_name = file_path + ".jpg"
    pic_write = open(pic_name, "wb")
    for dat_data in dat_file:
        for dat_byte in dat_data:
            pic_data = dat_byte ^ decode_code
            pic_write.write(bytes([pic_data]))
    print(pic_name + " 解密完成")
    dat_file.close()
    pic_write.close()


def find_datfile(dir_path):
    """
    获取dat文件目录下所有的文件
    :param dir_path: dat文件目录
    :return: 无
    """
    files_list = os.listdir(dir_path)
    for file_name in files_list:
        file_path = dir_path + "\\" + file_name
        decode_dat(file_path)


path = input("\033[35m 请输入需要解密微信dat文件的目录: \033[0m")
find_datfile(path)
print("\033[35m 如报错请检查子文件夹是否有bat加密文件！\033[0m")