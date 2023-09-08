from var import *
import requests
import json
import jsonpath
import allure
import time
import datetime

url="https://admin.s-iis.com/"


# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("我的代办-意向咨询”")
# def test_1():
#     res=requests.get(url+"apply/task/todo?platform=&applyType=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("短信管理")
# @allure.title("模板管理”")
# def test_2():
#     res = requests.get(url + "msg/template/page?current=1&size=10&r=" + "{}".format(
#         int(round(time.time() * 1000))), headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res.text), "code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("短信管理")
# @allure.title("发送记录管理”")
# def test_3():
#     res = requests.get(url + "msg/send/page?current=1&size=15&r=" + "{}".format(
#         int(round(time.time() * 1000))), headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res.text), "code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("我的代办-demo申请”")
# def test_4():
#     res=requests.get(url+"apply/task/todo?platform=&applyType=1&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("我的代办-企业认证”")
# def test_5():
#     res=requests.get(url+"apply/task/todo?platform=&applyType=8&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("我的代办-联盟申请”")
# def test_6():
#     res=requests.get(url+"apply/alliance/apply/todo?platform=&startTime=&endTime=&downloadType=0&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("我的代办-供需发布申请”")
# def test_7():
#     res=requests.get(url+"apply/supply/apply/todo?downloadType=0&platform=&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("我的代办-产品申请”")
# def test_8():
#     res=requests.get(url+"apply/task/todo?platform=&productApplyType=3%2C4%2C5%2C6%2C7&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("全部事项-意向咨询”")
# def test_9():
#     res=requests.get(url+"apply/task/all?platform=&applyType=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("全部事项-demo申请”")
# def test_10():
#     res=requests.get(url+"apply/task/all?platform=&applyType=1&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("全部事项-企业认证”")
# def test_11():
#     res=requests.get(url+"apply/task/all?platform=&applyType=8&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("全部事项-联盟申请”")
# def test_12():
#     res=requests.get(url+"apply/alliance/apply/all?platform=&startTime=&endTime=&downloadType=0&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("全部事项-供需发布申请”")
# def test_13():
#     res=requests.get(url+"apply/supply/apply/all?downloadType=0&platform=&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("用户申请")
# @allure.title("全部事项-产品申请”")
# def test_14():
#     res=requests.get(url+"apply/task/all?platform=&productApplyType=3%2C4%2C5%2C6%2C7&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code=jsonpath.jsonpath(json.loads(res.text),"code")
#     assert code[0] == 0
#
#
#
# @allure.epic("运营平台")
# @allure.feature("内容管理")
# @allure.title("banner管理-新增banner”")
# def test_15():
#     data={
#         "openType": 0,
#         "bannerType": 1,
#         "bannerTitle": "ceshi",
#         "bannerImg": "",
#         "bannerLink": "",
#         "description": "",
#         "platformList": [
#             2
#         ],
#         "status": 1,
#         "locations": [
#             {
#                 "img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png",
#                 "location": "pc端",
#                 "tick": True
#             },
#             {
#                 "img": "",
#                 "location": "小程序端",
#                 "tick": True
#             }
#         ],
#         "platform": "2"
#     }
#     requests.packages.urllib3.disable_warnings()
#     res = requests.post(url + "content/banner?r="+"{}".format(int(round(time.time() * 1000))), data=json.dumps(data), verify=False, headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res.text), "code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("内容管理")
# @allure.title("banner管理-删除banner”")
# def test_16():
#     res1=requests.get(url+"content/banner/page?size=15&current=1&bannerType=1&platform=2&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     data=jsonpath.jsonpath(json.loads(res1.text),"data")
#     records=data[0]["records"]
#     id=records[len(records)-1]["id"]
#
#     res2=requests.delete(url+"content/banner/"+str(id)+"?r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res2.text), "code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("服务管理")
# @allure.title("服务应用上架-新增”")
# def test_17():
#     data={
#         "content": "ceshi",
#         "name": "ceshi",
#         "price": -1,
#         "enterpriseName": "爱门",
#         "detail": "<p>ceshi</p>",
#         "status": 1,
#         "isShow": 0,
#         "type": "6",
#         "showType": "0",
#         "isDefaultImg": "0",
#         "img": "",
#         "platform": 2
#     }
#     requests.packages.urllib3.disable_warnings()
#     res = requests.post(url + "content/service/info?r="+"{}".format(int(round(time.time() * 1000))), data=json.dumps(data), verify=False, headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res.text), "code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("服务管理")
# @allure.title("服务应用上架-下架”")
# def test_18():
#     res1=requests.get(url+"content/service/info/page?platform=2&current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),headers=headers_admin)
#     data=jsonpath.jsonpath(json.loads(res1.text),"data")
#     records=data[0]["records"]
#     ids=records[0]["id"]
#     data2={
#         "ids": [
#             ids
#         ]
#     }
#     res2=requests.post(url+"content/service/info/pull?r="+"{}".format(int(round(time.time() * 1000))),data=json.dumps(data2),headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res2.text), "code")
#     assert code[0] == 0
#
# @allure.epic("运营平台")
# @allure.feature("服务管理")
# @allure.title("服务应用上架-编辑”")
# def test_19():
#     res1 = requests.get(
#         url + "content/service/info/page?platform=2&current=1&size=15&r=" + "{}".format(int(round(time.time() * 1000))),
#         headers=headers_admin)
#     data = jsonpath.jsonpath(json.loads(res1.text), "data")
#     records = data[0]["records"]
#     ids = records[0]["id"]
#     data={
#         "id": ids,
#         "name": "ceshi"+"{}".format(int(round(time.time() * 1000))),
#         "content": "ceshi",
#         "price": -1,
#         "enterpriseName": "爱门",
#         "detail": "<p>ceshi</p>",
#         "status": 0,
#         "isShow": 0,
#         "type": "6",
#         "isDefaultImg": "0",
#         "img": "",
#         "showType": "0",
#         "platform": 2
#     }
#     res2 = requests.put(url + "content/service/info?r=" + "{}".format(int(round(time.time() * 1000))),
#                          data=json.dumps(data), headers=headers_admin)
#     code = jsonpath.jsonpath(json.loads(res2.text), "code")
#     assert code[0] == 0



@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("我的代办可以收到用户的申请信息”")
def test_1():
    #操作账号15222222222
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    data = {"userId": "464103894448513024",
            "enterpriseName": "323",
            "certificateNumber": "646546646464646546",
            "name": "12321",
            "province": "天津市",
            "city": "",
            "industry": "采矿业/石油和天然气开采业",
            'file': ('40293605_1.png', open('C:/test/tp/40293605_1.png', 'rb'), 'image/png', {})
            }
    # 1用户发起变更信息操作
    with allure.step("1用户发起变更信息操作"):
        res1 = requests.post(URLG + "customer-center/account/upgrade",
                     headers=headers_enterprise, data=data, verify=False, )
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res1.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

    # 2获取手机号码来对比
    with allure.step("2获取手机号码来对比"):
        res2 = requests.get(URLY + "api/issp/apply/task/todo?current=1&size=15&r="+"{}".format(int(round(time.time() * 1000))),
                    verify=False, headers=headers_admin)
        with allure.step("结果检查"):
            with allure.step(f"1.字段mobile检查，预期结果为15222222222]"):
                result = jsonpath.jsonpath(json.loads(res2.text), "$..data..records..mobile")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "15222222222"
    taskId_id = jsonpath.jsonpath(json.loads(res2.text), "$..data..records..taskId")[0]
    recordId_id = jsonpath.jsonpath(json.loads(res2.text), "$..data..records..recordId")[0]
    #3运营主管进行同意操作后查看当前代办情况
    with allure.step("3运营主管进行同意操作后查看当前代办情况"):
        data={"taskFlag":1,
              "comment":"9100098_yz确认接收",
              "taskId":taskId_id,
              "recordId":recordId_id,
              "userName":"9100098_yz"}
        res3 = requests.post(URLY + "api/issp/apply/task/submit?r="+"{}".format(int(round(time.time() * 1000))),
                     data = json.dumps(data),
                     verify=False, headers=headers_admin)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为true"):
                result = jsonpath.jsonpath(json.loads(res3.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == true
    #4运营主管进行同意操作后拒绝当前代办
    with allure.step("4运营主管进行同意操作后拒绝当前代办"):

        taskId_id = int(taskId_id)+100
        data={"recordId":recordId_id,"taskId": taskId_id,"taskFlag":9,"comment":"11111"}
        res4 = requests.post(URLY+"api/issp/apply/task/submit?r="+"{}".format(int(round(time.time() * 1000))),
                     data=json.dumps(data),verify=False, headers = headers_admin)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为true"):
                result =jsonpath.jsonpath(json.loads(res4.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == True

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("我的代办进行综合条件筛选")
def test_2():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/apply/task/todo?r=" + "{}".format(
        int(round(time.time() * 1000))) + "&keyWord=323&status=3&applyType=8&current=1&size=15",
                verify=False, headers=headers_admin)
    res2 = requests.get(URLY + "api/apply/task/todo?r=" + "{}".format(int(round(time.time() * 1000))) + "&current=1&size=15",
                verify=False, headers=headers_admin)
    # result = jsonpath.jsonpath(json.loads(res2.text), "$...records..mobile")[0]
    recordid = jsonpath.jsonpath(json.loads(res2.text), "$...records..recordId")[0]
    with allure.step("结果检查"):
        with allure.step(f"1.字段recordId检查，预期结果为{recordid}]"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$...data..records..recordId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == recordid
@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("我的代办重置筛选项")
def test_3():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/apply/task/todo?r="+"{}".format(int(round(time.time() * 1000)))+"&current=1&size=15",
                    verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段code检查，预期结果为0"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..code")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == 0
@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("参与事项跳转需要>0")
def test_4():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/task/join?current=1&size=15&r"+"{}".format(int(round(time.time() * 1000))),
                    verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段recordId检查，预期结果为>0"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result > 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("参与事项综合条件筛选")
def test_5():
    requests.packages.urllib3.disable_warnings()

    res1 = requests.get(URLY + "api/apply/task/join?r="+"{}".format(int(round(time.time() * 1000)))+"&keyWord=%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95%E5%88%AB%E5%8A%A8&applyType=8&current=1&size=15",
                    verify=False, headers=headers_admin)
    res2 = requests.get(URLY + "api/apply/task/join?r="+"{}".format(int(round(time.time() * 1000)))+"&keyWord=%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95%E5%88%AB%E5%8A%A8&applyType=8&current=1&size=15",
                    verify=False, headers=headers_admin)
    recordid = jsonpath.jsonpath(json.loads(res2.text), "$...records..recordId")[0]
    with allure.step("结果检查"):
        with allure.step(f"1.字段recordId检查，预期结果为{recordid}"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result ==recordid

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("参与事项导出")
def test_6():
    requests.packages.urllib3.disable_warnings()
    data = {
        }

    res1 =requests.post(URLY+"api/issp/apply/task/export?r="+"{}".format(int(round(time.time() * 1000))),
                data=json.dumps(data), verify=False, headers=headers_admin)

    with allure.step("结果检查"):
        with allure.step(f"状态码检查，预期结果为'200']"):
            result = res1.status_code
            assert result == 200


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("参与事项详细信息查看")
def test_7():
    requests.packages.urllib3.disable_warnings()
    res2 = requests.get(URLY + "api/issp/apply/task/join/record/577?r="+"{}".format(int(round(time.time() * 1000))),
                    verify=False, headers=headers_admin)
    recordid = jsonpath.jsonpath(json.loads(res2.text), "$...data..recordId")[0]

    res1 = requests.get(URLY + "api/issp/apply/task/join/record/577?r="+"{}".format(int(round(time.time() * 1000))),
                    verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段recordId检查，预期结果为{recordid}"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..recordId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result ==recordid


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("参与事项企业附件信息查看")
def test_8():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/task/todo?r=" + "{}".format(int(round(time.time() * 1000))) + "&current=1&size=15",
                                                              verify=False, headers=headers_admin)

    with allure.step("结果检查"):
        with allure.step(f"状态码检查，预期结果为'200']"):
            result = res1.status_code
            assert result == 200

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("参与事项企业退出成功")
def test_9():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/task/join?r="+"{}".format(int(
                round(time.time() *1000)))+"1&current=1&size=15",
                verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"code检查，预期结果为'0']"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..code")[0]
            assert result == 0

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("用户在门户发起联盟申请")
def test_10():
    requests.packages.urllib3.disable_warnings()
    #1.用户发起联盟申请
    data={
	"company": "12213",
	"taxId": "213123213",
	"industry": "农、林、牧、渔业/农业",
	"city": "",
	"mobile": "17454545454",
	"name": "test",
	"email": "test@test.com",
	"comment": "test",
	"customerId": "468493464002797568",
	"customerName": "nsj3trywir51e7r"
}
    res1 = requests.post(URL + "customer-center/alliance/apply",
                                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res1.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("运营侧拒绝联盟申请")
def test_11():
    requests.packages.urllib3.disable_warnings()
    #1.用户发起联盟申请
    data={
	"company": "12213",
	"taxId": "213123213",
	"industry": "农、林、牧、渔业/农业",
	"city": "",
	"mobile": "17454545454",
	"name": "taskId@w.com",
	"email": "taskId@w.com",
	"comment": "taskId@w.com",
	"customerId": "468493464002797568",
	"customerName": "nsj3trywir51e7r"
}
    res1 = requests.post(URL + "customer-center/alliance/apply",
                                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res1.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."
    #查看刚刚的请求
    res1 = requests.get(URLY + "api/issp/apply/alliance/apply/todo?r=167896624102&downloadType=0&current=1&size=15",
                verify=False, headers=headers_admin)
    PrecordId_id = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
    taskId_id = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..taskId")[0]
    #2.运营测接受申请
    data={
 "taskFlag": 1,
 "comment": "port_yz确认接收",
 "taskId": taskId_id,
 "recordId": PrecordId_id,
 "userName": "port_yz"
}
    res1 = requests.post(URLY + "api/issp/apply/alliance/apply/submit?r="+"{}".format(int(round(time.time()*1000))),
                                 data=json.dumps(data), verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'操作成功'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "操作成功"
    taskId_id=int(taskId_id)+100
    #点击拒绝
    data = {"recordId":PrecordId_id,
            "taskId":taskId_id,
            "taskFlag":9,"comment":"1"}
    res1 = requests.post(URLY + "api/issp/apply/alliance/apply/submit?r="+"{}".format(int(round(time.time() * 1000))),
                 data=json.dumps(data), verify=False, headers=headers_admin)
    try:
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为'操作成功'"):
                result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "操作成功"
    except:
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为'操作成功'"):
                result=jsonpath.jsonpath(json.loads(res1.text),"$..msg")[0]
                with allure.step(f"实际结果为：'该待办任务不属于当前用户'"):
                    assert result == "该待办任务不属于当前用户"
@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("联盟申请参与事项查看")
def test_12():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/alliance/apply/join?r="+
               " {}".format(int(round(time.time() * 1000)))+"&downloadType=0&current=1&size=15",
                verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        #数量绝对大于0
        with allure.step(f"code检查，预期结果为>0"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
            assert result > 0
@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title ("联盟申请筛选")
def test_13():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/alliance/apply/join?r="+
               " {}".format(int(round(time.time() * 1000)))+"&downloadType=0&current=1&size=15",
                verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        #数量绝对大于0
        with allure.step(f"code检查，预期结果为>0"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
            assert result > 0


@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("联盟申请参与事项今日筛选")
def test_14():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/alliance/apply/join?r="+"{}".format(int(round(time.time() * 1000)))+
                "&startTime="+str(TodayStartDate())+"&endTime="+str(TodayEndtDate())+
                "&provinceList=&district=&downloadType=0&current=1&size=15",
          verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        # 数量绝对大于0
        with allure.step(f"code检查，预期结果为>0"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
        assert result > 0

@allure.epic("运营平台")
@allure.feature("用户申请")
@allure.title("联盟申请参与事项今日筛选后重置")
def test_15():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/apply/alliance/apply/join?r="+"{}".format(int(round(time.time() * 1000)))+
                "&startTime="+str(getweekagoDate())+"&endTime="+str(TodayEndtDate())+
                "&provinceList=&downloadType=0&current=1&size=15",
          verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        # 数量绝对大于0
        with allure.step(f"code检查，预期结果为'>0'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..recordId")[0]
        assert result > 0





@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面新增添加图片")
def test_16():
    requests.packages.urllib3.disable_warnings()

    files = {'file':('40293605_1.png',open('C:/test/tp/40293605_1.png','rb'),'image/png',{})}
    res1 = requests.post(URLY + "api/issp/content/banner/upload",files=files,verify=False,headers=headers_admin_upload_file)

    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png"

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面新增")
def test_17():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    data ={
	"openType": 0,
	"bannerType": 1,

	"bannerTitle": "首页展示接口测试111",
	"bannerLink": "首页展示接口测试111",
	"bannerImg": "",
	"description": "",
	"platformList": [1, 2],
	"status": 1,
	"locations": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png",
		"location": "小程序端",
		"tick": true
	}],
	"platform": "1,2"
}
    data1 = {
	"openType": 0,
	"bannerType": 1,
	"bannerTitle": "首页展示接口测试22222",
	"bannerLink": "1",
	"bannerImg": "",
	"description": "",
	"platformList": [1, 2],
	"status": 1,
	"locations": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/2.jpg",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/2.jpg",
		"location": "小程序端",
		"tick": true
	}],
	"platform": "1,2"
}
    r0 = requests.post(URLY + "api/issp/content/banner?r="+"{}".format(int(round(time.time() * 1000))), verify=False,
                 headers=headers_admin,data=json.dumps(data))
    res1 = requests.post(URLY + "api/issp/content/banner?r="+"{}".format(int(round(time.time() * 1000))), verify=False,
                 headers=headers_admin, data=json.dumps(data1))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(r0.text), "$..data")[0]
            result1 = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result1}\""):
                assert result,result1== true



@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面无法再次新增同一个名称")
def test_18():
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    data ={
	"openType": 0,
	"bannerType": 1,
	"bannerTitle": "首页展示接口测试111",
	"bannerLink": "首页展示接口测试111",
	"bannerImg": "",
	"description": "",
	"platformList": [1, 2],
	"status": 1,
	"locations": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png",
		"location": "小程序端",
		"tick": true
	}],
	"platform": "1,2"
}
    res1 = requests.post(URLY + "api/issp/content/banner?r="+"{}".format(int(round(time.time() * 1000))),verify=False,
                 headers=headers_admin,data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'None'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == None

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面进入")
def test_19():
    requests.packages.urllib3.disable_warnings()
    # content / banner / page?size = 15 & current = 1 & bannerType = 1 & platform = 2 & r = 1693981660009
    res1 = requests.get(URLY + "api/issp/content/banner/page?size=15&current=1&bannerType=1&platform=2&r="+"{}".format(int(round(time.time() * 1000))),
                verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        # 数量绝对大于0
        with allure.step(f"id检查，预期结果为'>0'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..id")[0]
        assert result > 0

# @allure.epic("运营平台")
# @allure.feature("内容管理")
# @allure.title("banner管理页面上移")
# def test_20():
#     requests.packages.urllib3.disable_warnings()
#     false = False
#     true = True
#     null = ''
#     res1 = requests.get(URLY + "api/content/banner/page?r=" + "{}".format(int(round(time.time() * 1000))) +
#                 "&size=15&current=1&bannerType=1",
#                 verify=False, headers=headers_admin)
#     priority_id = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..createTime")
#     id_id = jsonpath.jsonpath(json.loads(res1.text),"$..data..records..id")
#     data ={
# 	{"id": id_id[1],
# 	"bannerType": 1,
# 	"openType": 0,
# 	"bannerTitle": "接口测试",
# 	"bannerImg": "[{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"pc端\",\"tick\":true},{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"小程序端\",\"tick\":true}]",
# 	"locations": [{
# 		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
# 		"location": "pc端",
# 		"tick": true
# 	}, {
# 		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
# 		"location": "小程序端",
# 		"tick": true
# 	}],
# 	"bannerLink": "",
# 	"description": "",
# 	"status": 1,
# 	"createTime":priority_id[1],
# 	"modifyTime": null,
# 	"priority": 20,
# 	"platform": "2",
# 	"newBannerImg": [{
# 		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
# 		"location": "pc端",
# 		"tick": true
# 	}, {
# 		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
# 		"location": "小程序端",
# 		"tick": true
# 	}],
# 	"location": [{
# 		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
# 		"location": "pc端",
# 		"tick": true
# 	}, {
# 		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
# 		"location": "小程序端",
# 		"tick": true
# 	}]}}
@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面下移")
def test_21():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    res1 = requests.get(URLY + "api/issp/content/banner/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&size=15&current=1&bannerType=1",
                verify=False, headers=headers_admin)
    priority_id = jsonpath.jsonpath(json.loads(res1.text), '$..data..records..createTime')[0]
    id_id=jsonpath.jsonpath(json.loads(res1.text), '$..id')[0]
    data ={
	"id": id_id,
	"bannerType": 1,
	"openType": 0,
	"bannerTitle": "接口测试下移",
	"bannerImg": "[{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"pc端\",\"tick\":true},{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"小程序端\",\"tick\":true}]",
	"locations": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "小程序端",
		"tick": true
	}],
	"bannerLink": "",
	"description": "",
	"status": 1,
	"createTime": priority_id,
	"modifyTime": null,
	"priority": 17,
	"platform": "2",
	"newBannerImg": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "小程序端",
		"tick": true
	}],
	"location": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "小程序端",
		"tick": true
	}]
}
    res1 = requests.post(URLY + "api/issp/content/banner/down?r="+"{}".format(int(round(time.time() * 1000))),verify=False,
                 headers=headers_admin,data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == true

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面下架")
def test_22():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    res1 = requests.get(URLY + "api/issp/content/banner/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&size=15&current=1&bannerType=1",
                verify=False, headers=headers_admin)
    priority_id = jsonpath.jsonpath(json.loads(res1.text), '$..data..records..createTime')[0]
    id_id = jsonpath.jsonpath(json.loads(res1.text), '$..id')[0]
    data = {
    "id": id_id,
	"openType": 0,
	"bannerType": 1,
	"bannerTitle": "接口测试下架",
	"bannerLink": "",
	"bannerImg": "[{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"pc端\",\"tick\":true},{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"小程序端\",\"tick\":true}]",
	"description": "",
	"status": 0,
	"locations": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "小程序端",
		"tick": true
	}]
}
    res1 = requests.put(URLY + "api/issp/content/banner?r="+"{}".format(int(round(time.time() * 1000))),verify=False,
                  headers=headers_admin,data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == True

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("banner管理页面上架")
def test_23():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    res1 = requests.get(URLY + "api/issp/content/banner/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&size=15&current=1&bannerType=1",
                verify=False, headers=headers_admin)
    priority_id = jsonpath.jsonpath(json.loads(res1.text), '$..data..records..createTime')[0]
    id_id = jsonpath.jsonpath(json.loads(res1.text), '$..id')[0]
    data = {
    "id": id_id,
	"openType": 0,
	"bannerType": 1,
	"bannerTitle": "接口测试上架",
	"bannerLink": "",
	"bannerImg": "[{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"pc端\",\"tick\":true},{\"img\":\"https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg\",\"location\":\"小程序端\",\"tick\":true}]",
	"description": "",
	"status": 1,
	"locations": [{
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "pc端",
		"tick": true
	}, {
		"img": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
		"location": "小程序端",
		"tick": true
	}]
}
    res1 = requests.put(URLY + "api/issp/content/banner?r="+"{}".format(int(round(time.time() * 1000))),verify=False,
                  headers=headers_admin,data=json.dumps(data))

    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == True




@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程管理照片上传")
def test_24():
    requests.packages.urllib3.disable_warnings()
    files = {'file':('40293605_1.png',open('C:/test/tp/40293605_1.png','rb'),'image/png',{})}
    res1 = requests.post(URLY + "api/issp/content/course/upload",files=files,verify=False,headers=headers_admin_upload_file)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/40293605_1.png"


@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程管理视频上传")
def test_25():
    requests.packages.urllib3.disable_warnings()
    files = {'file':('3edeccfa735697f8316633fadbdb4c38.mp4',
                     open('C:/test/sp/3edeccfa735697f8316633fadbdb4c38.mp4','rb'),'video/mp4',{})}
    res1 = requests.post(URLY + "api/issp/content/course/uploadFile",files=files,verify=False,headers=headers_admin_upload_file)
    with allure.step("结果检查"):
        with allure.step(f"1.字段name检查，预期结果为'3edeccfa735697f8316633fadbdb4c38.mp4'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..name")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "3edeccfa735697f8316633fadbdb4c38.mp4"

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程管理新增")
def test_26():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    data = {
	"courseName": "接口测试",
	"courseImg": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
	"videoFiles": [{
		"name": "3edeccfa735697f8316633fadbdb4c38.mp4",
		"url": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/3edeccfa735697f8316633fadbdb4c38.mp4",
		"fileSize": 33633198,
		"fileType": null,
		"uid": 1679306121262,
		"status": "success"
	}],
	"platformList": [2],
	"oldPrice": 0,
	"newPrice": 0,
	"status": 0,
	"shelfTime": "",
	"expireTime": "",
	"validityOfPurchase": 1,
	"platform": "0,1,2"
}
    data1 = {
        "courseName": "接口测试1",
        "courseImg": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
        "videoFiles": [{
            "name": "3edeccfa735697f8316633fadbdb4c38.mp4",
            "url": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/3edeccfa735697f8316633fadbdb4c38.mp4",
            "fileSize": 33633198,
            "fileType": null,
            "uid": 1679306121262,
            "status": "success"
        }],
        "platformList": [2],
        "oldPrice": 0,
        "newPrice": 0,
        "status": 0,
        "shelfTime": "",
        "expireTime": "",
        "validityOfPurchase": 1,
        "platform": "0,1,2"
    }
    r0 = requests.post(
        URLY + "api/issp/content/course?r=" + "{}".format(int(round(time.time() * 1000))) + "&current=1&size=15",
        data=json.dumps(data), verify=False, headers=headers_admin)
    res1 = requests.post(URLY + "api/issp/content/course?r="+"{}".format(int(round(time.time() * 1000)))+"&current=1&size=15",
                 data= json.dumps(data1),verify=False,headers=headers_admin)
    with allure.step("上传结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == true

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程管理跳转")
def test_27():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/content/course/page?r="+"{}".format(int(round(time.time() * 1000)))+"&current=1&size=15",
                verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段id检查，预期结果为>0"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$...data..records..id")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result >0

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程管理重复新增报错")
def test_28():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    data = {
	"courseName": "接口测试",
	"courseImg": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
	"videoFiles": [{
		"name": "3edeccfa735697f8316633fadbdb4c38.mp4",
		"url": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/3edeccfa735697f8316633fadbdb4c38.mp4",
		"fileSize": 33633198,
		"fileType": null,
		"uid": 1679306121262,
		"status": "success"
	}],
	"platformList": [2],
	"oldPrice": 0,
	"newPrice": 0,
	"status": 1,
	"shelfTime": "",
	"expireTime": "",
	"validityOfPurchase": 1,
	"platform": "2"
}
    res1 = requests.post(URLY + "api/issp/content/course?r="+"{}".format(int(round(time.time() * 1000)))+"&current=1&size=15",
                 data= json.dumps(data),verify=False,headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'课程名称存在重复，无法新增！'"):
            result=jsonpath.jsonpath(json.loads(res1.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "所属平台课程名称存在重复，无法新增！"



@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程名搜索")
def test_29():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URLY + "api/issp/content/course/page?r="+"{}".format(int(round(time.time() * 1000)))+
                "&status=&courseName=%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95&current=1&size=15",
          verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"courseName检查，预期结果为'接口测试'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..courseName")[0]
        assert result == "接口测试"

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("课程修改并下架")
def test_30():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    res1 = requests.get(URLY + "api/issp/content/course/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&size=15&current=1&bannerType=1",
                verify=False, headers=headers_admin)
    id_id = jsonpath.jsonpath(json.loads(res1.text), '$..id')[0]
    data = {
    "id": id_id,
	"courseName": "接口测试",
	"courseImg": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/b0767c7c2627ccde01e482ad9fd5c140.jpg",
	"videoFile": "3edeccfa735697f8316633fadbdb4c38.mp4",
	"videoFiles": [{
		"name": "3edeccfa735697f8316633fadbdb4c38.mp4",
		"url": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/3edeccfa735697f8316633fadbdb4c38.mp4",
		"fileSize": 33633198,
		"fileType": "mp4",
		"uid": 1679387025899,
		"status": "success"
	}],
	"oldPrice": 10,
	"newPrice": 10,
	"preferentialPrice": 0,
	"status": 0,
	"shelfTime": "2023-03-21 14:51:44",
	"expireTime": 4,
	"platformList": [2],
	"validityOfPurchase": 1,
	"platform": "2"
}
    res1 = requests.put(URLY + "api/issp/content/course?r="+"{}".format(int(round(time.time() * 1000))),verify=False,
                  headers=headers_admin,data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == True

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("检查未上架状态并选择单个课程删除")
def test_31():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    #选择未上架状态
    res1 = requests.get(URLY + "api/issp/content/course/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&status=0&courseName=&current=1&size=15",
                verify=False, headers=headers_admin)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'大于0'"):
            id_id = jsonpath.jsonpath(json.loads(res1.text), '$..data..records..id')[0]
            with allure.step(f"实际结果为：\"{id_id}\""):
                assert id_id > 0
    res1 = requests.delete(URLY + "api/issp/content/course?r=" +"{}".format(int(round(time.time() * 1000))), verify=False,
                         headers=headers_admin,data=json.dumps([id_id]))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == True

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("检查未上架状态并全部课程删除")
def test_32():
    import jsonpath
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    #选择未上架
    res1 = requests.get(URLY + "api/issp/content/course/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&status=0&courseName=&current=1&size=15",
                verify=False, headers=headers_admin)
    id_id = jsonpath.jsonpath(json.loads(res1.text), '$..data..records..id')[0]

    res1 = requests.delete(URLY + "api/issp/content/course?r=" +"{}".format(int(round(time.time() * 1000))), verify=False,
                         headers=headers_admin,data=json.dumps(id_id))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'true'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == True

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("删除banner首页")
def test_33():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    #获取全部的id值
    res1 = requests.get(URLY + "api/issp/content/banner/page?r=" + "{}".format(int(round(time.time() * 1000))) +
                "&size=15&current=1&bannerType=1",
                verify=False, headers=headers_admin)
    id_id = eval(str(jsonpath.jsonpath(json.loads(res1.text), "$..data..records..id")[0]))
    id_id_len= len(id_id)
    i = 0
    while i < id_id_len:
        data={"id":id_id[i]}
        res1 = requests.delete(
                URLY + "api/issp/content/banner/" + "{}".format(id_id[i]) + "?r=" + "{}".format(int(round(time.time() * 1000))),
                verify=False, headers=headers_admin, data=json.dumps(data))
        i += 1
        print("此次全部数据有{}".format(i), "个，已全部删除")
        if i >= id_id_len:
            #跳出
            break
    #门户侧观察是否删除完
    res1=requests.get(URL + 'resource-center/view/banner?pageNum=1&pageSize=10&bannerType=1&platform=2', headers=headers_enterprise,
              verify=False)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为'0'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..total")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == 0

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理pdf上传")
def test_34():
    requests.packages.urllib3.disable_warnings()
    files = {'file':('pdf文件.pdf',open('C:/test/pdf/pdf文件.pdf','rb'),'application/pdf',{})}
    res1 = requests.post(URLY + "api/issp/content/tool/uploadFile",files=files,verify=False,headers=headers_admin_upload_file)
    with allure.step("结果检查"):
        with allure.step(f"1.字段name检查，预期结果为'pdf文件.pdf'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..name")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "pdf文件.pdf"


@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理新增")
def test_35():
    requests.packages.urllib3.disable_warnings()
    false = False
    true = True
    null = ''
    data={
	"downloadType": 0,
	"publishPeople": "port_yz",
	"toolName": "接口测试",
	"sourceFile": 0,
	"toolsLink": "",
	"selectRadio": 0,
	"platformList": [2],
	"toolsImg": "",
	"toolFile": [{
		"name": "pdf文件.pdf",
		"url": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/pdf%E6%96%87%E4%BB%B6.pdf",
		"fileSize": 6026657,
		"fileType": null,
		"uid": 1679463484818,
		"status": "success"
	}],
	"status": 1,
	"resourceType": 0,
	"platform": "2"
}
    res1 = requests.post(URLY+"api/issp/content/tool?r=" +"{}".format(int(round(time.time() * 1000))),verify=False,
                 headers=headers_admin,data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'True'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == True

@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理下架")
def test_36():
    requests.packages.urllib3.disable_warnings()
    #获取已上架的第一个id
    res1 = requests.get(URLY + "api/issp/content/tool/page?r=" +"{}".format(int(round(time.time() * 1000)))+
                "&status=1&platform=&toolName=&downloadType=0&current=1&size=15"
                 , headers=headers_admin,verify=False)
    id_id = jsonpath.jsonpath(json.loads(res1.text),"$..data..records..id")[0]
    #下架
    data ={"ids":[id_id]}
    res1 = requests.post(URLY + "api/issp/content/tool/pull?r=" +"{}".format(int(round(time.time() * 1000))),headers=headers_admin
                 ,data=json.dumps(data),verify=False)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为'null'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == None


@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理上架")
def test_37():
    requests.packages.urllib3.disable_warnings()
    #获取已下架的第一个id
    res1 = requests.get(URLY + "api/issp/content/tool/page?r=" +"{}".format(int(round(time.time() * 1000)))+
                "&status=0&platform=&toolName=&downloadType=0&current=1&size=15"
                 , headers=headers_admin,verify=False)
    id_id = jsonpath.jsonpath(json.loads(res1.text),"$..data..records..id")[0]
    #上架
    data ={"ids":[id_id]}
    res1 = requests.post(URLY + "api/issp/content/tool/put?r=" +"{}".format(int(round(time.time() * 1000))),headers=headers_admin
                 ,data=json.dumps(data),verify=False)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为'null'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == None




@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理批量xia架")
def test_38():
    requests.packages.urllib3.disable_warnings()
    #获取已上架的所有id
    res1 = requests.get(URLY + "api/issp/content/tool/page?r=" +"{}".format(int(round(time.time() * 1000)))+
                "&status=1&platform=&toolName=&downloadType=0&current=1&size=15"
                 , headers=headers_admin,verify=False)
    id_id = eval(str(jsonpath.jsonpath(json.loads(res1.text), "$..data..records..id")[0]))
    #下架
    data = {"ids": id_id}
    res1 = requests.post(URLY + "api/issp/content/tool/pull?r=" +"{}".format(int(round(time.time() * 1000))), headers=headers_admin
                 , data=json.dumps(data), verify=False)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'null'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            assert result == None


@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理批量上架")
def test_39():
    requests.packages.urllib3.disable_warnings()
    #获取已下架的所有id
    res1 = requests.get(URLY + "api/issp/content/tool/page?r=" +"{}".format(int(round(time.time() * 1000)))+
                "&status=0&platform=&toolName=&downloadType=0&current=1&size=15"
                 , headers=headers_admin,verify=False)
    id_id = eval(str(jsonpath.jsonpath(json.loads(res1.text), "$..data..records..id")[0]))
    #上架
    data = {"ids": id_id}
    res1 = requests.post(URLY + "api/issp/content/tool/put?r=" + "{}".format(int(round(time.time() * 1000))), headers=headers_admin
                 , data=json.dumps(data), verify=False)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'null'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data")[0]
            assert result == None


@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理筛选和重置操作")
def test_40():
    requests.packages.urllib3.disable_warnings()
    #筛选
    res1 = requests.get(URLY + "api/issp/content/tool/page?r=" + "{}".format(int(round(time.time() * 1000)))+
                "&status=&platform=&toolName=%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95&downloadType=0&current=1&size=15"
                 , headers=headers_admin,verify=False)
    with allure.step("筛选结果检查"):
        with allure.step(f"1.字段total检查，预期结果为'接口测试'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..toolName")[0]
            assert result == "接口测试"
            id_len = len(eval(str(jsonpath.jsonpath(json.loads(res1.text), "$..data..records..id")[0])))
    #重置操作，数量应该大于等于0
    res2 = requests.get(URLY + "api/issp/content/tool/page?r=" + "{}".format(int(round(time.time() * 1000)))+
                "&status=&platform=&toolName=&downloadType=0&current=1&size=15"
                , headers=headers_admin, verify=False)
    with allure.step("筛选结果检查"):
        with allure.step(f"1.数量检查，预期结果为'比较数量应该大于等于筛选数'"):
            #重置后数量id_len2
            id_len2 = len(eval(str(jsonpath.jsonpath(json.loads(res2.text), "$..data..records..id")[0])))
            result = id_len
            assert result <= id_len2


@allure.epic("运营平台")
@allure.feature("内容管理")
@allure.title("资源发布管理筛选和重置操作")
def test_41():
    requests.packages.urllib3.disable_warnings()
    #筛选
    res1 = requests.get(URLY + "api/issp/content/tool/page?r=" + "{}".format(int(round(time.time() * 1000)))+
                "&status=&platform=&toolName=%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95&downloadType=0&current=1&size=15"
                 , headers=headers_admin,verify=False)
    with allure.step("筛选结果检查"):
        with allure.step(f"1.字段total检查，预期结果为'接口测试'"):
            result = jsonpath.jsonpath(json.loads(res1.text), "$..data..records..toolName")[0]
            assert result == "接口测试"
            id_len = len(eval(str(jsonpath.jsonpath(json.loads(res1.text), "$..data..records..id")[0])))
    #重置操作，数量应该大于等于0
    res2 = requests.get(URLY + "api/issp/content/tool/page?r=" + "{}".format(int(round(time.time() * 1000)))+
                "&status=&platform=&toolName=&downloadType=0&current=1&size=15"
                , headers=headers_admin, verify=False)
    with allure.step("筛选结果检查"):
        with allure.step(f"1.数量检查，预期结果为'比较数量应该大于等于筛选数'"):
            #重置后数量id_len2
            id_len2 = len(eval(str(jsonpath.jsonpath(json.loads(res2.text), "$..data..records..id")[0])))
            result = id_len
            assert result <= id_len2

@allure.step("获取今天零点")
def TodayStartDate(self):
    now = datetime.datetime.now()
    zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                          microseconds=now.microsecond)
    last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)
    return zero_today

@allure.step("获取今天24点")
def TodayEndtDate(self):
    now = datetime.datetime.now()
    zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                          microseconds=now.microsecond)
    last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)
    return last_today

@allure.step("获取今7天前0点")
def getweekagoDate(self):
    now = datetime.datetime.now()
    zero_week = now - datetime.timedelta(days=7, hours=now.hour, minutes=now.minute, seconds=now.second,
                                         microseconds=now.microsecond)
    return zero_week