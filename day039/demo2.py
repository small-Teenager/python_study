# 
import json
import requests
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10031120626719&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
resp = requests.get(url, headers=headers)
content = resp.text
result = content.replace('fetchJSON_comment98(', '').replace(');', '')
json_content = json.loads(result)
print(result)
print(type(json_content))
comments = json_content.get('comments')
for item in comments:
    productColor = item.get('productColor')
    productSize = item.get('productSize')
    print(productColor, productSize)