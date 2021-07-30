# WeChat-decryption
微信公众号:天禧信安
下载解密工具的hxd记得点个⭐⭐
📫 Email:admin@janekr.com
## :gear: 前言
PC版的weixin会自动加密用户接受到的所有图片信息,文件均以dat格式加密储存。
默认的数据储存路径为 C:\\Users\\Administrator\\Documents\\WeChat Files\\wxid_xxx\\FileStorage\\Image\\date
用户名获取可命令行执行 echo %UserName% 获得
## :💾 解密思路
一般来说这种对文件加密的方式大多是“异或法加密”，即每个文件逐个字节与加密码进行"异或计算"得出加密文件。
我们可参考以下加密码算出源文件
```shell
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e
# weixin.bat 16进制 e1 c6 e1
# key 值 1e1e 0x1e  weixin.bat-jpg
```
我们可以自动化的对每个加密文件的所有字节与相应的加密码进行"异或计算"，可解出dat文件。

## :sparkles: 特性
* :cloud: 支持 单/多 文件批量解密

## :hammer_and_wrench: 部署使用

```shell
# 启动主启动器
python WeChat_tool.py 

# 单个文件解密
python WeChat_alone.py 

# 多文件解密
python WeChat_automatic.py
```