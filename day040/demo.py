import requests
import re
import pandas

# 1、模拟浏览器发起请求

url = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=112274088&date=2021-06-09'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    # cookie  存放用户的账号密码
    "cookie": "_uuid=7CA38D86-157C-7B75-4155-91094C1E6B2840215infoc; buvid3=9E79709B-97DA-4565-9180-8A8E9FAE6878184984infoc; buvid_fp=9E79709B-97DA-4565-9180-8A8E9FAE6878184984infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(kmJYYJmulR0J'uYu~))Ykm~; dy_spec_agreed=1; fingerprint3=e2c8e8428b5dd20a53fb6c8510486617; fingerprint_s=f31bf1c2362afc03f7757fc30ece046b; SESSDATA=212d0975%2C1637407046%2Cb2c6f%2A51; bili_jct=2a0e751c5d0536036916cfe4d06d4ddc; DedeUserID=26390853; DedeUserID__ckMd5=8d24b1d50476c5e5; sid=ao0x3oqd; fingerprint=a4e0c9b54195baf670cf3f3e1cafde57; buvid_fp_plain=9E79709B-97DA-4565-9180-8A8E9FAE6878184984infoc; CURRENT_QUALITY=64; PVID=1; bfe_id=1bad38f44e358ca77469025e0405c4a6"
}
response = requests.get(url, headers=headers)

# 2、获取响应内容
# 爬虫 状态码不为200全为错
print(response.text)

# 3、解析内容
# re.findall('解析规则'，解析文件)
# 解析规则  bs4 xpath 正则表达式
# （） 获取当前位置的内容  .当前位置字符  * 0次或者多次匹配  ？ 满足当前规则下尽可能少的匹配 +至少出现一次
result = re.findall('.*?([\u4E00-\u9FA5]+).*?', response.text)
print(result)
# 4、保存到本地
dm = pandas.DataFrame(result)
dm.to_csv('danmu.csv')
