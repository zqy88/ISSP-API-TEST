from var import *
import requests
import json
import jsonpath
import allure


url="https://www.cz-iis.com/api/s-iis/"

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("对接需求首页")
def test_1():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url+"customer-center/supply/apply/portal/record?pageNum=1&pageSize=6",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("供需查看（已完成筛选）")
def test_2():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/supply/apply/portal/record?pageNum=1&pageSize=6&status=3",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("已完成筛选的需求详情查看")
def test_3():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/supply/apply/portal/record/51?recordId=51",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("供需查看（待对接筛选）")
def test_4():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/supply/apply/portal/record?pageNum=1&pageSize=6&status=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("点击供需进入查看待对接供需详情")
def test_5():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/account/enterprise/list?pageNum=1&pageSize=5&enterpriseTag=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("联盟企业点击供需对接")
def test_6():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/supply/apply/portal/record/71?recordId=71",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("联盟企业点击推荐服务商")
def test_7():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?enterpriseName=%E5%A5%BD%E7%9A%84%E6%94%B6%E5%88%B0&status=1&pageSize=4&pageNum=1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("供需对接搜索框搜索“陆保金”")
def test_8():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/supply/apply/portal/record?pageNum=1&pageSize=6&demandName=%E9%99%86%E4%BF%9D%E9%87%91"
    ,verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("保存需求草稿”")
def test_9():
    data = {
	"demandName": "1",
	"demandDesc": "1",
	"company": "test陆保金",
	"mobile": "15956088951",
	"industry": "建筑业/建筑装饰、装修和其他建筑业",
	"customerId": "461109704605212672",
	"customerName": "小妖怪",
	"logoUrl": "",
	"price": "面议"
}
    requests.packages.urllib3.disable_warnings()
    res = requests.post(URL + "customer-center/supply/apply/draft",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."
    # try:
    #     sql = f'SELECT * FROM "bdt_supply_apply_record" where status=-1 ORDER BY handle_time desc;'
    #     status_db = requests.sqlCheck(sql)
    #     print(status_db)
    #     with allure.step(f"实际订单状态为：\"{status_db}\""):
    #         assert status_db == -1
    # except:
    #     print("数据库连接时间过长")
    #     pass


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("服务商资源首页")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_10():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/account/enterprise/list?pageNum=1&pageSize=9&enterpriseTag=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("需求提交审核”")
def test_11():
    requests.packages.urllib3.disable_warnings()
    data = {"demandName":"1@2.com","demandDesc":"11111@2.com","company":"好的收到","mobile":"13113113131","industry":"电力、热力、燃气及水生产和供应业/水的生产和供应业","customerId":"462192218425958400","customerName":"pds5xeyv7h22y1b","logoUrl":"","price":"面议"}
    res = requests.post(URL + "customer-center/supply/apply/start",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("查看服务商详情")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_12():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/account/enterprise/list?pageNum=1&pageSize=9&enterpriseTag=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("服务商服务详情")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_13():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/id?id=46",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("服务申请”")
def test_14():
    requests.packages.urllib3.disable_warnings()
    data = {"name":"pds5xeyv7h22y1b","phone":"13113113131","email":"1@2.com","des":"1@2.com","applyUser":"462192218425958400","serviceId":46,"enterpriseId":"2098","serviceName":"陆保金测试服务1"}
    res = requests.post(URL + "resource-center/service/apply",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("专家资源首页")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_15():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/supply/specialist?pageNum=1&pageSize=6&status=1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("专家详情查看")
# #步骤描述
# @allure.description('步骤1.面熟设计师设计  ')
def test_16():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL+"resource-center/supply/specialist?pageNum=1&pageSize=6&status=1",
                  verify=False,headers=headers_enterprise)
    id_id=jsonpath.jsonpath(json.loads(res1.text),"$..list..id")[0]
    res2 = requests.get(URL + "resource-center/supply/specialist/detail?id="+"{}".format(id_id),
                verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res2.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("首页")
@allure.title ("首页跳转")
def test_17():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/web/resource?pageSize=6&pageNum=1&resourceType=1,2,3&status=1&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("政策资讯（联盟动态）跳转")
def test_18():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=4&status=1&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("内容查看跳转")
def test_19():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/resource/info?id=2995",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("精选服务点击进入")
def test_20():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&isShow=1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("全部服务点击进入")
def test_21():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=-1&pageNum=-1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("风险评估服务点击，可查看")
def test_22():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/id?id=54",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("服务申请成功”")
def test_23():
    requests.packages.urllib3.disable_warnings()
    data = {"name":"pds5xeyv7h22y1b","phone":"13113113131","email":"yushu@3.com","des":"yushu@3.com","applyUser":"462192218425958400","serviceId":54,"enterpriseId":"2098","serviceName":"风险评估"}
    res = requests.post(URL + "resource-center/service/apply",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("资源大厅")
@allure.title ("资源大厅（法规标准）跳转成功")
def test_24():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/tool?status=1&pageNum=1&pageSize=10&platform=2&downloadType=0&resourceType=0",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("资源大厅")
@allure.title ("安全工具跳转成功")
def test_25():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/tool?status=1&pageNum=1&pageSize=9&platform=2&downloadType=1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("人才培育")
@allure.title ("在线课程页面（人才培育）跳转正常")
def test_26():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/course?pageNum=1&pageSize=10&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("首页")
@allure.title ("非个人企业申请联盟")
def test_27():
    requests.packages.urllib3.disable_warnings()
    #1.用户发起联盟申请
    data={
 "company": "323",
 "taxId": "646546646464646546",
 "industry": "采矿业/石油和天然气开采业",
 "city": "",
 "mobile": "15222222222",
 "name": "jiekou@jiekou",
 "email": "jiekou@jiekou.com",
 "comment": "jiekou@jiekou",
 "customerId": "464103894448513024",
 "customerName": "接口测试别动"
}
    res = requests.post(URL + "customer-center/alliance/apply",
                                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success.'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
        with allure.step(f"实际结果为：\"{result}\""):
            assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("供需大厅")
@allure.title ("供需大厅提交审核接口")
def test_28():
    requests.packages.urllib3.disable_warnings()
    data = {
    "demandName": "api_test",
    "demandDesc": "api_test",
    "company": "323",
    "mobile": "15222222222",
    "industry": "采矿业/石油和天然气开采业",
    "customerId": "464103894448513024",
    "customerName": "大妖怪",
    "logoUrl": "https://issp-test-enterprise.obs.cn-east-3.myhuaweicloud.com:443/1.jpg",
    "price": "面议"}
    res = requests.post(URL + "customer-center//supply/apply/start",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("行业资讯跳转")
def test_29():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=1&status=1&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("行业资讯，内容查看跳转")
def test_30():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL + "resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=1&status=1&platform=2",
                verify=False, headers=headers_enterprise)
    id_id=jsonpath.jsonpath(json.loads(res1.text),"$..list..id")[0]

    res2 = requests.get(URL+"resource-center/view/resource/info?id="+"{}".format(id_id),
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res2.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("政策法规跳转")
def test_31():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=2&status=1&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("政策法规，内容查看跳转")
def test_32():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL + "resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=2&status=1&platform=2",
                verify=False, headers=headers_enterprise)
    id_id=jsonpath.jsonpath(json.loads(res1.text),"$..list..id")[0]

    res2 = requests.get(URL+"resource-center/view/resource/info?id="+"{}".format(id_id),
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res2.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."





@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("通知公告跳转")
def test_33():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=3&status=1&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("政策资讯")
@allure.title ("通知公告，内容查看跳转")
def test_34():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL + "resource-center/view/web/resource?pageSize=4&pageNum=1&resourceType=2&status=1&platform=2",
                verify=False, headers=headers_enterprise)
    id_id=jsonpath.jsonpath(json.loads(res1.text),"$..list..id")[0]

    res2 = requests.get(URL+"resource-center/view/resource/info?id="+"{}".format(id_id),
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res2.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("安全合规跳转")
def test_35():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("安全评估跳转")
def test_36():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("安全产品跳转")
def test_37():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=3",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("应急响应跳转")
def test_38():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=4",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("安全运维跳转")
def test_39():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=5",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("合规跳转")
def test_40():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=6",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("解决方案跳转")
def test_41():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=7",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."


@allure.epic("常州issp门户")
@allure.feature("服务大厅")
@allure.title ("安全培训跳转")
def test_42():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/service/page?status=1&pageSize=8&pageNum=1&type=8",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("资源大厅")
@allure.title ("行业报告跳转成功")
def test_43():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/tool?status=1&pageNum=1&pageSize=10&platform=2&downloadType=0&resourceType=1",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("资源大厅")
@allure.title ("法规标准下载200状态码")
def test_44():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL+"resource-center/view/tool?status=1&pageNum=1&pageSize=10&platform=2&downloadType=0&resourceType=0",
                  verify=False, headers=headers_enterprise)
    name_id = jsonpath.jsonpath(json.loads(res1.text), "$..list..toolFile..name")
    data = {"objectName": name_id}
    res2 = requests.post(URL + "resource-center/resource/download", verify=False,
                 headers=headers_enterprise, data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果中有'RawDisplay truncated at 128 characters'"):
            result = res2.status_code
            with allure.step(f"实际结果为：\"{result}\""):
                assert  result == 200


@allure.epic("常州issp门户")
@allure.feature("资源大厅")
@allure.title ("行业报告下载200状态码")
def test_45():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL+"resource-center/view/tool?status=1&pageNum=1&pageSize=10&platform=2&downloadType=0&resourceType=1",
                  verify=False, headers=headers_enterprise)
    name_id = jsonpath.jsonpath(json.loads(res1.text), "$..list..toolFile..name")
    data = {"objectName": name_id}
    res2 = requests.post(URL + "resource-center/resource/download", verify=False,
                 headers=headers_enterprise, data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果中有'RawDisplay truncated at 128 characters'"):
            result = res2.status_code
            with allure.step(f"实际结果为：\"{result}\""):
                assert  result == 200


@allure.epic("常州issp门户")
@allure.feature("资源大厅")
@allure.title ("安全工具下载200状态码")
def test_46():
    requests.packages.urllib3.disable_warnings()
    res1 = requests.get(URL+"resource-center/view/tool?status=1&pageNum=1&pageSize=10&platform=2&downloadType=0&resourceType=1",
                  verify=False, headers=headers_enterprise)
    name_id = jsonpath.jsonpath(json.loads(res1.text), "$..list..toolFile..name")
    data = {"objectName": name_id}
    res2 = requests.post(URL + "resource-center/resource/download", verify=False,
                 headers=headers_enterprise, data=json.dumps(data))
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果中有'RawDisplay truncated at 128 characters'"):
            result = res2.status_code
            with allure.step(f"实际结果为：\"{result}\""):
                assert  result == 200

@allure.epic("常州issp门户")
@allure.feature("人才培育")
@allure.title ("在线课程页面（人才培育）跳转正常")
def test_47():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"resource-center/view/course?pageNum=1&pageSize=10&platform=2",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."



@allure.epic("常州issp门户")
@allure.feature("关于我们")
@allure.title ("关于我们跳转正常")
def test_47():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL+"customer-center/personal/information",
                  verify=False,headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("首页")
@allure.title ("退个人中心跳转")
def test_48():
    requests.packages.urllib3.disable_warnings()
    res = requests.get(URL + "area-route/saas/route/exit?channelName=changzhou&serviceName=issp",
                  verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success.'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."

@allure.epic("常州issp门户")
@allure.feature("首页")
@allure.title ("退出")
def test_49():
    requests.packages.urllib3.disable_warnings()
    data = {"username":"464103894448513024"}
    res = requests.post(URL + "auth/login/exit",
                 data=json.dumps(data), verify=False, headers=headers_enterprise)
    with allure.step("结果检查"):
        with allure.step(f"1.字段msg检查，预期结果为'success.'"):
            result=jsonpath.jsonpath(json.loads(res.text),"$..msg")[0]
            with allure.step(f"实际结果为：\"{result}\""):
                assert result == "success."








