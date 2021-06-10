'''
1 获取数据
2 获取想要的数据
3 将数据写入excel
'''
import json
import requests
import openpyxl

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10031120626719&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
resp = requests.get(url, headers=headers)
content = resp.text
result = content.replace('fetchJSON_comment98(', '').replace(');', '')
json_content = json.loads(result)

comments = json_content.get('comments')
# 创建sheet
wk = openpyxl.Workbook()
sheet = wk.create_sheet()

for item in comments:
    productColor = item.get('productColor')
    productSize = item.get('productSize')
    sheet.append([productColor, productSize])
    wk.save('data/20210610.xlsx')
