import json
import allure
import urllib3
urllib3.disable_warnings()
import requests
import time
import jsonpath


url="https://admin.s-iis.com/api/issp/"
token="8b21496f-34d7-455a-a466-64960b0b1f6f"
headersyy = {"Content-Type": "application/json", "authorization": "Bearer " + token}


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("我的代办-意向咨询”")
def test_1():
    res=requests.get(url+"apply/task/todo?platform=&applyType=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("短信管理")
@allure.title("模板管理”")
def test_2():
    res = requests.get(url + "msg/template/page?current=1&size=10&r=" + "{}".format(
        int(round(time.time() * 1000))), headers=headersyy)
    code = jsonpath.jsonpath(json.loads(res.text), "code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("短信管理")
@allure.title("发送记录管理”")
def test_3():
    res = requests.get(url + "msg/send/page?current=1&size=15&r=" + "{}".format(
        int(round(time.time() * 1000))), headers=headersyy)
    code = jsonpath.jsonpath(json.loads(res.text), "code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("我的代办-demo申请”")
def test_4():
    res=requests.get(url+"apply/task/todo?platform=&applyType=1&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("我的代办-企业认证”")
def test_5():
    res=requests.get(url+"apply/task/todo?platform=&applyType=8&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("我的代办-联盟申请”")
def test_6():
    res=requests.get(url+"apply/alliance/apply/todo?platform=&startTime=&endTime=&downloadType=0&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("我的代办-供需发布申请”")
def test_7():
    res=requests.get(url+"apply/supply/apply/todo?downloadType=0&platform=&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("我的代办-产品申请”")
def test_8():
    res=requests.get(url+"apply/task/todo?platform=&productApplyType=3%2C4%2C5%2C6%2C7&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("全部事项-意向咨询”")
def test_9():
    res=requests.get(url+"apply/task/all?platform=&applyType=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("全部事项-demo申请”")
def test_10():
    res=requests.get(url+"apply/task/all?platform=&applyType=1&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("全部事项-企业认证”")
def test_11():
    res=requests.get(url+"apply/task/all?platform=&applyType=8&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("全部事项-联盟申请”")
def test_12():
    res=requests.get(url+"apply/alliance/apply/all?platform=&startTime=&endTime=&downloadType=0&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("全部事项-供需发布申请”")
def test_13():
    res=requests.get(url+"apply/supply/apply/all?downloadType=0&platform=&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("全部事项-产品申请”")
def test_14():
    res=requests.get(url+"apply/task/all?platform=&productApplyType=3%2C4%2C5%2C6%2C7&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code=jsonpath.jsonpath(json.loads(res.text),"code")
    assert code[0] == 0



@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理-新增banner”")
def test_15():
    data={
        "openType": 0,
        "bannerType": 1,
        "bannerTitle": "ceshi",
        "bannerImg": "",
        "bannerLink": "",
        "description": "",
        "platformList": [
            2
        ],
        "status": 1,
        "locations": [
            {
                "img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png",
                "location": "pc端",
                "tick": True
            },
            {
                "img": "",
                "location": "小程序端",
                "tick": True
            }
        ],
        "platform": "2"
    }
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url + "content/banner?r="+"{}".format(int(round(time.time() * 1000))), data=json.dumps(data), verify=False, headers=headersyy)
    code = jsonpath.jsonpath(json.loads(res.text), "code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理-删除banner”")
def test_16():
    res1=requests.get(url+"content/banner/page?size=15&current=1&bannerType=1&platform=2&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    data=jsonpath.jsonpath(json.loads(res1.text),"data")
    records=data[0]["records"]
    id=records[len(records)-1]["id"]

    res2=requests.delete(url+"content/banner/"+str(id)+"?r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    code = jsonpath.jsonpath(json.loads(res2.text), "code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("服务管理")
@allure.title("服务应用上架-新增”")
def test_17():
    data={
        "content": "ceshi",
        "name": "ceshi",
        "price": -1,
        "enterpriseName": "爱门",
        "detail": "<p>ceshi</p>",
        "status": 1,
        "isShow": 0,
        "type": "6",
        "showType": "0",
        "isDefaultImg": "0",
        "img": "",
        "platform": 2
    }
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url + "content/service/info?r="+"{}".format(int(round(time.time() * 1000))), data=json.dumps(data), verify=False, headers=headersyy)
    code = jsonpath.jsonpath(json.loads(res.text), "code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("服务管理")
@allure.title("服务应用上架-下架”")
def test_18():
    res1=requests.get(url+"content/service/info/page?platform=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headersyy)
    data=jsonpath.jsonpath(json.loads(res1.text),"data")
    records=data[0]["records"]
    ids=records[0]["id"]
    data2={
        "ids": [
            ids
        ]
    }
    res2=requests.post(url+"content/service/info/pull?r="+"{}".format(int(round(time.time() * 1000))),data=json.dumps(data2),headers=headersyy)
    code = jsonpath.jsonpath(json.loads(res2.text), "code")
    assert code[0] == 0

@allure.epic("运营平台")
@allure.feature("服务管理")
@allure.title("服务应用上架-编辑”")
def test_19():
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

