from api_login import *



url_individual="https://www.cz-iis.com/login"
url_enterprise="https://www.cz-iis.com/login"
url_admin="https://admin.s-iis.com/"

URL = "https://www.cz-iis.com/api/s-iis/"
URLG= "https://changzhou-custom.s-iis.com/api/s-iis/"
URLY = "https://124.71.137.232:8888/"



username_individual="15956088951"
username_enterprise="15222222222"
username_admin="port_yz"

pwd_individual="Sino123456"
pwd_enterprise="Sino123456"
pwd_admin="Sino123456"

# token_individual, Userid_individual=login_individual(url_individual,username_individual,pwd_individual)
token_enterprise, Userid_enterprise=login_enterprise(url_enterprise,username_enterprise,pwd_enterprise)
token_admin=login_admin(url_admin,username_admin,pwd_admin)



# headers_individual={"Content-Type": "application/json","authorization": "bearer " + token_individual ,"Userid":Userid_individual,"Platform":"2"}
headers_enterprise={"Content-Type": "application/json","authorization": "bearer " + token_enterprise ,"Userid":Userid_enterprise,"Platform":"2"}
header_enterprise_upload_file={"authorization": "bearer " + token_enterprise ,"Userid":Userid_enterprise}
headers_admin={"Content-Type": "application/json", "authorization": "Bearer " + token_admin}
headers_admin_upload_file={"authorization": "Bearer " + token_admin}























