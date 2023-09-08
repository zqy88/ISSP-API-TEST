import jsonpath
import requests
import json

#api url
url = "https://reqres.in/api/users?page=2"


#get requests
response = requests.get(url)


print(response)
print(response.headers)

#parse requests to json form
json_response = json.loads(response.text)
print(json_response)

#fetch value using json path,
#retern a list ,which, in the following case, only has a single value
pages = jsonpath.jsonpath(json_response, "total_pages")
print(pages[0])
assert pages[0] == 2


