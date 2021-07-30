# WeChat-decryption
微信公众号:天禧信安
下载解密工具的hxd记得点个⭐⭐
📫 Email:admin@janekr.com
## :gear: 前言
PC版的weixin会自动加密用户接受到的所有图片信息,文件均以dat格式加密储存。
默认的数据储存路径为 C:\\Users\\Administrator\\Documents\\WeChat Files\\wxid_xxx\\FileStorage\\Image\\date
用户名获取可命令行执行 echo %UserName% 获得
## :💾 解密思路

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