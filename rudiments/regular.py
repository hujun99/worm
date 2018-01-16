import re
pattern = re.compile(r'<div class="(.*?)">.*?href', re.S)

with open('regular_test.txt','rt') as f:
    data = f.readlines()
print('data:', data)
all_item = re.findall(pattern, ''.join(data))
# if result1:
#     print(result1.group())
# print(result1.start())
for item in all_item:
    print('have items')
    print(item)

