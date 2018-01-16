import urllib.request as urllib2
import urllib
enable_proxy = False
proxy_handler = urllib2.ProxyHandler({'http':'http://some-proxy.com:8080'})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(urllib2.ProxyHandler({}))

urllib2.install_opener(opener)

url = 'https://www.zhihu.com/signup?next=%2F'
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'
values = {'username': '100227557@qq.com',  'password': 'adfsoboring26'}
headers = {'User-Agent': user_agent, 'Referer':'https://www.zhihu.com/'}
data = urllib.parse.urlencode(values).encode(encoding = 'UTF8')
request = urllib2.Request(url, data, headers)
try:
    response = urllib2.urlopen(request, timeout= 5)
except urllib2.HTTPError as e:
    print(e.code, e.reason)
page = response.read()
print(page)
print('end')
