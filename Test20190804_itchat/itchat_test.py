

# -*- coding: UTF-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
url="http://www.tuling123.com/openapi/api"
key="720b8495c39f40ac92284c5d6b3d1dd7"
msg="hello"
userid="100000"
data={
    'key':key,
    'info':msg,
    'userid':userid
}
respon = requests.post(url,data=data).json()
print(respon.get('text'))

import itchat
@itchat.msg_register("Text")
def text_reply(msg):
	return get_reply(msg["Text"])

def get_reply(msg):
	print(msg)
	respon = requests.post(url+"?key="+key+"&info="+msg).json()
	print(respon)
	return respon.get("text")

itchat.login()
itchat.run()
