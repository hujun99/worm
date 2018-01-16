import urllib
import re
import urllib.request as urllib2
page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    # print(response.read())
except urllib2.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)

content = response.read().decode('utf-8')
with open('html_content.txt', 'wt') as f:
    f.write(content)
pattern = re.compile('<div class=(.*?)>')
# print(content)
all_item = re.findall(pattern, content)
for item in all_item:
    #print('have items')
    print(item)


