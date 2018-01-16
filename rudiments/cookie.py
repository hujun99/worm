import urllib
import http.cookiejar as cookielib
import urllib.request as urllib2
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)
cookie.save(ignore_discard= True, ignore_expires= True)

