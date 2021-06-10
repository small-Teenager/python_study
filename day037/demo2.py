import requests

url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=43139143227&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
response = requests.get(url)
print(response.status_code)
content = response.text
rest = content.replace('fetchJSON_comment98(', '').replace(');', '')
print(rest)
