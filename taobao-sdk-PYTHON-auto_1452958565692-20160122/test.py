# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api
import socket


'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了
'''

top.setDefaultAppInfo("appkey", "*******")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com",80)

使用自定义的域名（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com")

使用默认的配置（调用线上环境）
a = top.api.UserGetRequest()
'''

'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(top.appinfo("appkey","*******"))
'''

req = top.api.AlibabaAliqinFcSmsNumSendRequest("gw.api.taobao.com/router/rest", 80)
# req.set_app_info(top.appinfo("appkey", "*******"))

req.sms_type = "normal"
req.sms_free_sign_name = "变更验证"
req.sms_param = "{'code':'311052','product':'不逗你玩了:('}"
req.rec_num = "18********"
req.sms_template_code = "SMS_*****"
try:
    resp = req.getResponse()
    print(resp)
# except Exception as e:
except socket.gaierror as e:
    print(e)