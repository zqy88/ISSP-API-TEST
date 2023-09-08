
import json
import allure
import urllib3
urllib3.disable_warnings()
import requests
import time
import jsonpath


url="https://admin.s-iis.com/api/issp/"
token=" 296f538a-b0e9-432c-b987-9571c1158c94"
headersyy = {"Content-Type": "application/json", "authorization": "Bearer " + token}



#
# data={
#     "content": "ceshi",
#     "name": "ceshi",
#     "price": -1,
#     "enterpriseName": "爱门",
#     "detail": "<p>ceshi</p>",
#     "status": 1,
#     "isShow": 0,
#     "type": "6",
#     "showType": "0",
#     "isDefaultImg": "0",
#     "img": "",
#     "platform": 2
# }
# requests.packages.urllib3.disable_warnings()
# res = requests.post(url + "content/service/info?r="+"{}".format(int(round(time.time() * 1000))), data=json.dumps(data), verify=False, headers=headersyy)
# code = jsonpath.jsonpath(json.loads(res.text), "code")
# print(res.text)
# assert code[0] == 0


# res1=requests.get(url+"content/service/info/page?platform=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
# data=jsonpath.jsonpath(json.loads(res1.text),"data")
# records=data[0]["records"]
# ids=records[0]["id"]
# print(ids)
# data2={
#     "ids": [
#         ids
#     ]
# }
# res2=requests.post(url+"content/service/info/pull?r="+"{}".format(int(round(time.time() * 1000))),data=json.dumps(data2),headers=headersyy)
# code = jsonpath.jsonpath(json.loads(res2.text), "code")
# assert code[0] == 0

res1 = requests.get(
    url + "content/service/info/page?platform=2&current=1&size=15&r=" + "{}".format(int(round(time.time() * 1000))),
    headers=headersyy)
data = jsonpath.jsonpath(json.loads(res1.text), "data")
records = data[0]["records"]
ids = records[0]["id"]
data={
    "id": ids,
    "name": "ceshi"+"{}".format(int(round(time.time() * 1000))),
    "content": "ceshi",
    "price": -1,
    "enterpriseName": "爱门",
    "detail": "<p>ceshi</p>",
    "status": 0,
    "isShow": 0,
    "type": "6",
    "isDefaultImg": "0",
    "img": "",
    "showType": "0",
    "platform": 2
}
res2 = requests.put(url + "content/service/info?r=" + "{}".format(int(round(time.time() * 1000))),
                     data=json.dumps(data), headers=headersyy)
code = jsonpath.jsonpath(json.loads(res2.text), "code")
assert code[0] == 0
