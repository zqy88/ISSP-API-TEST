import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

file = open("E:\\pythonWorkSpace\\api_test_1\\requests\\put.json", 'r')
request_json = json.loads(file.read())

print(request_json)

response = requests.put(url, request_json)

#parse response format
response_json = json.loads(response.text)
print(response_json)

updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt[0])

assert response.status_code == 200
