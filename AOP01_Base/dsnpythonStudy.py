
# -*- coding: UTF-8 -*-
from dns import resolver
ans = resolver.query("www.baidu.com","A")
print ans
print ans.qname
print ans.response
print ans.response.answer[1]

