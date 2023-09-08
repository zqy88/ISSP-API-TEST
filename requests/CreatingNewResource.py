import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

file = open("E:\\pythonWorkSpace\\api_test_1\\requests\\post.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

#make post requests with json data
response = requests.post(url, request_json)
print(response.content)
print(response.headers.get("Content-Length"))

#parse response to json format
# jsonpath always returns a list
response_json = json.loads(response.text)
id = jsonpath.jsonpath(response_json, "id")
print(id[0])

#validate response code
assert response.status_code == 201
