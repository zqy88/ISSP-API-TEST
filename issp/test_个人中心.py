from var import *
import requests
import json
import jsonpath
import allure
import time

url="https://changzhou-custom.s-iis.com/api/s-iis/"
url1="https://changzhou-custom.s-iis.com/api/s-iis/"
url_admin="https://admin.s-iis.com/"

@allure.epic("常州issp个人中心")
@allure.feature("我的团队")
@allure.title ("开通咨询跳转至提示")
def test_1():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/team/service/sale?customerId=464103894448513024&saasType=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp个人中心")
@allure.feature("我的团队")
@allure.title ("进入团队跳转")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_2():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/team?userId=464103894448513024",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'超级管理员'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..list..teamRole")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "超级管理员"


@allure.epic("常州issp个人中心")
@allure.feature("我的团队")
@allure.title ("基本信息跳转")
# @allure.description('步骤1.面熟设计师设计  ')
def test_3():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"auth/account/phone?phone=15956088951",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'15956088951'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..list..phone")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "15956088951"



@allure.epic("常州issp个人中心")
@allure.feature("我的团队")
@allure.title ("查看基本信息")
# @allure.description('步骤1.面熟设计师设计  ')
def test_4():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/account/upgrade?id=464103894448513024",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'464103894448513024'"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..list..userId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == 464103894448513024



@allure.epic("常州issp个人中心")
@allure.feature("基本信息")
@allure.title("修改密码错误提示")
def test_5():
    requests.packages.urllib3.disable_warnings()
    data={"userId":"464103894448513024","oldPassword":"eI+CG6Rx/sH77+Oqp8pMhV5vtc6AFn0AlEMvPSkS4WOtxRQIyTaGMXK6xoZ2EuB6DxYZcN6NFY0xbjMyDuGjhRy0gblAorUPQBNBQg3rAjcCfjTDWfvJBiZdR9raHhM3h24oBcSeoODUrOTGSKjJ+tF+44BzAqFvznXDM0txReg=","newPassword":"ZnfXOvoQ0gc6IUg0aUDH6H96MTHrn7pXEArKEcWsJZj3jAhtIFOlt+dvLCjPIRrfZ68TBm5n13COXYY8t4tlGbuzYUFTWfslX/bzm4QQ+KFrjdT25r3HJQrruagv50KNhdWSFfAIoTGu9W/jJq9wyNnpycy5l/ov6UXPIJI0Jpg="}
    res = requests.post(url1 + "customer-center/personal/password",
                data=json.dumps(data),verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'旧密码不正确！'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "旧密码不正确！"



@allure.epic("常州issp个人中心")
@allure.feature("基本信息")
@allure.title("用户名修改重复会提示")
def test_6():
    requests.packages.urllib3.disable_warnings()
    data={"userId":"464103894448513024","userName":"小魔头"}
    res = requests.post(url1 + "customer-center/personal/username",
                data=json.dumps(data),verify=False, headers=headers_enterprise)
    print(res.content.decode(encoding="utf-8"))
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'此用户名已存在！'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "此用户名已存在！"




@allure.epic("常州issp个人中心")
@allure.feature("基本信息")
@allure.title("用户名修改成功")
def test_7():
    requests.packages.urllib3.disable_warnings()
    try:
        data={"userId": "464103894448513024", "userName": "大妖怪"}
        res = requests.post(url1 + "customer-center/personal/username",
                    data=json.dumps(data),verify=False, headers=headers_enterprise)
        print(res.content.decode(encoding="utf-8"))
        with allure.step("结果检查"):
            with allure.step(f"1.字段msg检查，预期结果为'success.'"):
                result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "success."
    except:
        data = {"userId": "464103894448513024", "userName": "小接口"}
        res = requests.post(url1 + "customer-center/personal/username",
                     data=json.dumps(data), verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段msg检查，预期结果为'success.'"):
                result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "success."



@allure.epic("常州issp个人中心")
@allure.feature("消息中心")
@allure.title("消息中心跳转")
def test_8():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"message/message/getCenterList?type=&module=2&status=&current=1&size=15",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为null"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..data...all")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result >= 0



@allure.epic("常州issp个人中心")
@allure.feature("消息中心")
@allure.title("实名认证不为空")
def test_9():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"message/message/getCenterList?type=&module=2&status=&current=1&size=15",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data..all检查，预期结果不等于0"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..data..all")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result != 0

@allure.epic("常州issp个人中心")
@allure.feature("服务管理")
@allure.title ("服务管理页面跳转")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_10():
    requests.packages.urllib3.disable_warnings()

    res = requests.get(url1+"resource-center/service/apply?pageNum=1&pageSize=15&enterpriseId=2344&applyUser=464103894448513024",
                  verify=False,headers=headers_enterprise)
    # , cookies = ck,params=GCG
    with allure.step("结果检查"):
        with allure.step(f"1.字段data..all检查，预期结果'15222222222"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..list..phone")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "15222222222"


@allure.epic("常州issp个人中心")
@allure.feature("服务管理")
@allure.title ("我申请的服务服务管理详情页面")
def test_11():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"resource-center/service/id?id=52",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data..all检查，预期结果'托管式检测与响应服务"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..list...name")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "托管式检测与响应服务"



@allure.epic("常州issp个人中心")
@allure.feature("服务管理")
@allure.title ("我发布的服务页面")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_12():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1 + "resource-center/service/page?pageNum=1&pageSize=10&enterpriseId=2344",
                verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data..all检查，预期结果'接口自动化服务应用"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..list..name")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "1112222"



@allure.epic("常州issp个人中心")
@allure.feature("服务管理")
@allure.title ("申请记录详情")
def test_13():
    requests.packages.urllib3.disable_warnings()

    res = requests.get(url1+"resource-center/service/apply?pageNum=1&pageSize=20&serviceId=47",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我发布的需求查看待对接")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_14():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/supply/apply/todo?pageNum=1&pageSize=15&status=2&demandName=&userName=464103894448513024",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果不小于0"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result > 0




@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我发布的需求，提交需求草稿”")
def test_16():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1 + "customer-center/supply/apply/todo?pageNum=1&pageSize=15&userName=464103894448513024",
                verify=False, headers=headers_enterprise)
    recordId_id = jsonpath.jsonpath(json.loads(res.text),"$..list..recordId")[0]
    data = {
 "demandName": "1",
 "demandDesc": "1",
 "company": "test陆保金",
 "mobile": "15956088951",
 "industry": "建筑业/建筑装饰、装修和其他建筑业",
 "price": "面议",
 "attachmentUrl": "",
 "attachmentName": "",
 "logoUrl": "",
 "customerId": "464103894448513024",
 "customerName": "小妖怪",
 "recordId": recordId_id
}
    res = requests.post(url1 + "customer-center/supply/apply/update/start",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，全部列表")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_17():
    requests.packages.urllib3.disable_warnings()

    res = requests.get(url1+"customer-center/supply/apply/join?pageNum=1&pageSize=15&userName=464103894448513024",
                  verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果不小于0"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result > 0


@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，全部列表")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_18():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/supply/apply/my/join?pageNum=1&pageSize=20&userName=464103894448513024",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为'success.'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，全部列表筛选")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_19():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/supply/apply/join?pageNum=1&pageSize=15&status=-1&demandName=&userName=464103894448513024",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为大于等于0"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result >= 0

@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，全部列表筛选包含1的需求")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_20():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/supply/apply/join?pageNum=1&pageSize=15&status=&demandName=1&userName=464103894448513024",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为大于等于0"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result >= 0

@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，发布需求页面跳转")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_21():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1+"customer-center/personal/information",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为大于等于0"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..list..userId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "464103894448513024"

@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，保存发布需求")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_22():
    requests.packages.urllib3.disable_warnings()
    data = {
        "demandName": "接口测试需求",
        "demandDesc": "接口测试需求",
        "company": "323",
        "mobile": "15222222222",
        "industry": "采矿业/石油和天然气开采业",
        "price": "面议",
        "attachmentUrl": "",
        "attachmentName": "",
        "logoUrl": "",
        "customerId": "464103894448513024",
        "customerName": "大妖怪"
    }
    res = requests.post(url1 + "customer-center/supply/apply/draft",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，发布需求页面文件上传")
def test_23():
    requests.packages.urllib3.disable_warnings()

    files = {'file': ('pdf文件.pdf', open('C:/test/pdf/pdf文件.pdf', 'rb'), 'application/pdf', {})}
    res = requests.post(url1 + "customer-center/supply/apply/upload/file", files=files, verify=False, headers=header_enterprise_upload_file)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'pdf文件.pdf'"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..list..fileName")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "pdf文件.pdf"

@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，用户侧-发布需求上传logo接口")
def test_24():
    requests.packages.urllib3.disable_warnings()

    files = {'file': ('1.jpg', open('C:/test/tp/1.jpg', 'rb'), 'image/jpeg', {})}
    res = requests.post(url1 + "customer-center/supply/apply/upload/logo", files=files, verify=False, headers=header_enterprise_upload_file)
    with allure.step("结果检查"):
        with allure.step(f"1.字段data检查，预期结果为'1.jpg'"):
            result = jsonpath.jsonpath(json.loads(res.text), "$..list..fileName")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "1.jpg"


@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，发布需求页面文件下载")
def test_25():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url1 + "customer-center/supply/apply/download/pdf%E6%96%87%E4%BB%B6.pdf?name=pdf%E6%96%87%E4%BB%B6.pdf",
        verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为PDF"):
            result = res.text
            with allure.step(f"实际结果为：\"{result}\""):
                assert "PDF" in result


@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，待办列表页提交审核接口")
def test_26():
    requests.packages.urllib3.disable_warnings()
    data = {"demandName":"1","demandDesc":"1我","company":"test陆保金","mobile":"15956088951","industry":"建筑业/建筑装饰、装修和其他建筑业","price":"面议","attachmentUrl":"","attachmentName":"","logoUrl":"","customerId":"464103894448513024","customerName":"小妖怪","recordId":180}
    res = requests.post(url1 + "resource-center/service/apply",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."





@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，待办列表不通过后的提交审核接口")
def test_27():
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    with allure.step("第一步，新增需求"):
        data = {
	"demandName": "接口测试需求",
	"demandDesc": "接口测试需求",
	"company": "323",
	"mobile": "15222222222",
	"industry": "采矿业/石油和天然气开采业",
	"price": "面议",
	"attachmentUrl": "",
	"attachmentName": "",
	"logoUrl": "",
	"customerId": "464103894448513024",
	"customerName": "大妖怪"
}
        res1 = requests.post(url1 + "customer-center/supply/apply/start",
                     data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("2运营测查找任务id"):
        res2 = requests.get(url_admin + "api/issp/apply/supply/apply/todo?downloadType=0&current=1&size=15&r" + "{}".format(int(round(time.time() * 1000))),
                   verify=False, headers=headers_admin)
        taskId_id = jsonpath.jsonpath(json.loads(res2.text),"$..data..records..taskId")[0]
        recordId_id = jsonpath.jsonpath(json.loads(res2.text), "$..data..records..recordId")[0]
    with allure.step("3运营主管进行同意操作"):
        data={
 "taskFlag": 1,
 "comment": "port_yz确认接收",
 "taskId": taskId_id,
 "recordId": recordId_id,
 "userName": "port_yz"
}
        res3 = requests.post(url_admin + "api/issp/apply/supply/apply/submit?r="+"{}".format(int(round(time.time() * 1000))),
                     data = json.dumps(data),
                     verify=False, headers=headers_admin)

        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为操作成功"):
                result = jsonpath.jsonpath(json.loads(res3.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "操作成功"
    with allure.step("4运营主管进行审核"):
        #先筛选
        res4 = requests.get(url_admin + "api/issp/apply/supply/apply/todo?status=1&downloadType=0&current=1&size=15&r=" + "{}".format(int(round(time.time() * 1000))),
                    verify=False, headers=headers_admin)
        taskId_id = jsonpath.jsonpath(json.loads(res4.text),"$..data..records..taskId")[0]
    with allure.step("5运营主管进行后拒绝代办"):
        data={
	"recordId": recordId_id,
	"taskId": taskId_id,
	"taskFlag": 9,
	"comment": "11111",
	"userName": "464103894448513024"
}
        res5 = requests.post(url_admin+"api/issp/apply/supply/apply/submit?r="+"{}".format(int(round(time.time() * 1000))),
                     data=json.dumps(data),verify=False, headers = headers_admin)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为操作成功"):
                result = jsonpath.jsonpath(json.loads(res5.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "操作成功"
    with allure.step("6用户侧点击退回提交按钮"):
        #筛选已退回
        res6 = requests.get(url1 + "customer-center/supply/apply/todo?pageNum=1&pageSize=15&status=9&demandName=&userName=464103894448513024",
                         verify = False, headers = headers_enterprise )
        recordId=  jsonpath.jsonpath(json.loads(res6.text), "$..list..recordId")[0]
        taskId= jsonpath.jsonpath(json.loads(res6.text), "$..list..taskId")[0]
        data={
	"customerId": "464103894448513024",
	"customerName": "大妖怪",
	"taskId":  taskId,
	"taskFlag": 1,
	"userName": "port_yz",
	"comment": "需求修改",
	"recordId": recordId
}
        res7 = requests.post(url1 + "customer-center/supply/apply/submit",
                     data=json.dumps(data), verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为success"):
                result = jsonpath.jsonpath(json.loads(res7.text),"$..msg")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "success."

@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，待办列表页点击完成按钮")
def test_28():
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    with allure.step("第一步，新增需求"):
        data = {
	"demandName": "接口测试需求",
	"demandDesc": "接口测试需求",
	"company": "323",
	"mobile": "15222222222",
	"industry": "采矿业/石油和天然气开采业",
	"price": "面议",
	"attachmentUrl": "",
	"attachmentName": "",
	"logoUrl": "",
	"customerId": "464103894448513024",
	"customerName": "大妖怪"
}
    res1 = requests.post(url1 + "customer - center / supply / apply / start",
                     data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("2运营测查找任务id"):
        res2 = requests.get(url_admin + "api/issp/apply/supply/apply/todo?downloadType=0&current=1&size=15&r" + "{}".format(int(round(time.time() * 1000))),
                   verify=False, headers=headers_admin)
        taskId_id = jsonpath.jsonpath(json.loads(res2.text), "$..data..records..taskId")[0]
        recordId_id = jsonpath.jsonpath(json.loads(res2.text), "$..data..records..recordId")[0]
    with allure.step("3运营主管进行同意操作"):
        data={
 "taskFlag": 1,
 "comment": "port_yz确认接收",
 "taskId": taskId_id,
 "recordId": recordId_id,
 "userName": "port_yz"
}
        res3 = requests.post(url_admin + "api/issp/apply/supply/apply/submit?r="+"{}".format(int(round(time.time() * 1000))),
                     data = json.dumps(data),
                     verify=False, headers=headers_admin)

        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为操作成功"):
                result = jsonpath.jsonpath(json.loads(res3.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "操作成功"
    with allure.step("4运营主管进行审核"):
        #先筛选
        res4 = requests.get(url_admin + "api/issp/apply/supply/apply/todo?status=1&downloadType=0&current=1&size=15&r=" + "{}".format(int(round(time.time() * 1000))),
                    verify=False, headers=headers_admin)
        taskId_id=jsonpath.jsonpath(json.loads(res4.text),"$..data..records..taskId")[0]
    with allure.step("5运营主管进行接受操作后同意代办"):
        data={"recordId":recordId_id,"taskId":taskId_id ,"taskFlag":1,"comment":"通过"}
        res5 = requests.post(url_admin+"api/issp/apply/supply/apply/submit?r="+"{}".format(int(round(time.time() * 1000))),
                     data=json.dumps(data),verify=False, headers = headers_admin)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为操作成功"):
                result = jsonpath.jsonpath(json.loads(res5.text), "$..data")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "操作成功"
    with allure.step("6用户侧点击对接完成按钮"):

        res6 = requests.get(url1+"customer-center/supply/apply/todo?pageNum=1&pageSize=15&status=2&demandName=&userName=464103894448513024",
                         verify = False, headers = headers_enterprise )

        recordId= jsonpath.jsonpath(json.loads(res6.text), "$..list..recordId")[0]

        data ={"recordId":recordId,"serviceCompany":"1","feedbackDescription":"1"}
        res7 = requests.post(url1 + "customer-center/supply/apply/docked",
                     data=json.dumps(data), verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为success."):
                result = jsonpath.jsonpath(json.loads(res7.text),"$..msg")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "success."





@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我对接的需求，用户侧-待提交状态删除接口")
def test_29():
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    with allure.step("第一步，保存需求到草稿"):
        data = {
	"demandName": "接口测试需求删除",
	"demandDesc": "接口测试需求删除",
	"company": "323",
	"mobile": "15222222222",
	"industry": "采矿业/石油和天然气开采业",
	"price": "面议",
	"attachmentUrl": "",
	"attachmentName": "",
	"logoUrl": "",
	"customerId": "464103894448513024",
	"customerName": "大妖怪"
}
    res = requests.post(url1 + "customer-center/supply/apply/draft",
                     data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("2筛选待提交的状态"):
        res = requests.get(url1 + "customer-center/supply/apply/todo?pageNum=1&pageSize=15&status=-1&demandName=&userName=464103894448513024",
                   verify=False, headers=headers_enterprise)
        recordId_id = jsonpath.jsonpath(json.loads(res.text), "$..list..recordId")

    with allure.step("3点击删除按钮删除"):
        r1 = requests.delete(url1 + "customer-center/supply/apply/" + "{}".format(recordId_id),
                             verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为success."):
                result = jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result == "success."





@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我发布的需求，用户侧-供需管理待办列表")
def test_30():
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    with allure.step("查看列表项"):
        res = requests.get(url1+ "customer-center/supply/apply/todo?pageNum=1&pageSize=15&userName=464103894448513024",
                   verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为数量大于0"):
                result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result >= 0



@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我发布的需求，用户侧-供需管理全部参与列表")
def test_31():
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    with allure.step("查看列表项"):
        res = requests.get(url1+ "customer-center/supply/apply/join?pageNum=1&pageSize=15&userName=464103894448513024",
                   verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为数量大于0"):
                result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result >= 0


@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title ("我发布的需求，用户侧-供需管理待办列表接口")
def test_32():
    false = False
    true = True
    null = ''
    requests.packages.urllib3.disable_warnings()
    with allure.step("查看列表项"):
        res = requests.get(url1+ "customer-center/supply/apply/todo?pageNum=1&pageSize=15&status=&demandName=&userName=464103894448513024",
                   verify=False, headers=headers_enterprise)
        with allure.step("结果检查"):
            with allure.step(f"1.字段data检查，预期结果为数量大于0"):
                result = jsonpath.jsonpath(json.loads(res.text), "$..total")[0]
                with allure.step(f"实际结果为：\"{result}\""):
                    assert result >= 0


@allure.epic("常州issp个人中心")
@allure.feature("供需管理")
@allure.title("我对接的需求，用户侧-供需管理全部参与列表详情接口")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_33():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(url1 + "customer-center/supply/apply/my/join?pageNum=1&pageSize=20&userName=464103894448513024",
                verify=False, headers=headers_enterprise)
    demandId= jsonpath.jsonpath(json.loads(res1.text),"$..list..demandId")[0]
    res2 = requests.get(url1 + "customer-center/supply/apply/my/join/info?demandId="+"{}".format(demandId),
                verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为{demandId}"):
            result = jsonpath.jsonpath(json.loads(res2.text), "$..list..recordId")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == demandId





@allure.epic("常州issp个人中心")
@allure.feature("服务管理")
@allure.title ("我发布的服务查服务")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_34():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(url1+"resource-center/service/page?pageNum=1&pageSize=10&enterpriseId=2344",
                  verify=False,headers=headers_enterprise)
    id_id=jsonpath.jsonpath(json.loads(res1.text),"$..list..id")[0]
    res2 = requests.get(url1 + "resource-center/service/id?id="+"{}".format(id_id),
                verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段total检查，预期结果为success."):
            result = jsonpath.jsonpath(json.loads(res2.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

