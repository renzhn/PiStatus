发送树莓派和小米路由器的状态信息到微博
===


### 环境
在树莓派2上安装Arch Linux Arm，然后easy_install pip和pip install weibo
安装cronie来定时运行

### 获取 token
运行weibo_token.py将URL打开并登录微博账号授权，然后将获得的callback token输入，再将输出的token中'替换为"以获得json格式的token，然后将这个token填入weibo_status.py中TOKEN变量即可发送微博


在小米路由器URL中寻找stok参数，其值即为路由器的token，填入weibo_status.py中的OPENWRT_TOKEN变量即可获取小米路由器状态信息（本人小米路由版本2.1.67）
