# print('1')
#
#
# j = {'aweme_list': [{'1':1}, {'2':2}], '3': 3, 'c1': 123,}
# a = j.get('13', 'c1')
# j.qwe = 'qwe'
# print(a)
# print(type(a))
# import random
# import time
#
# now = int(time.time())
# print(now)
#
# num = random.randint(100, 800)
# a = str(now) + str(num)
# print(a)
# import base64
# import random

# def mix(x):
#     """mix params for request videos"""
#     rst = ''
#     for _ in range(x):
#         tmp = random.choice(character)
#         rst += tmp
#     return rst
#
# character = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<>./#:@()`^'
# patern = '{}i33@)@t@{};3@)u)@g3w)@fhuyq1fshhdf;4@{}_----/ss-o#o#{}../i:b-o#:`-o#pbfrh^+jt:#/.^'.format(mix(13), mix(15), mix(9), mix(13))
#
#
#
# str3 = base64.b64encode(patern.encode('utf8')).decode()
#
#
# # print(patern)
# # print(len(str3))
# print(str3)
# # print(type(str3))

print(len('B062BBEAF3F9DD73B30B5B52BC86216B')) # md5, 32大写
print(len('v0200f520000bg1vfrcthbi3gkli9du0540p')) # 36

# d1 = {'params': {'1': 1, '2': 2}}
#
# d1.update({'params': {'3': 3}})
#
# print(d1)

d = {}
d.setdefault('qwe', 1)
print(d)


