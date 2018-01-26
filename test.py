import requests
import json

url = 'http://127.0.0.1:8000/users/api/v1/hello_2/' 
#url = 'http://192.168.1.199:8000/users/api/v1/hello_2/'
parms = {
	'name':'client',
	'hello_message':'Knock, knock'
}
headers = {
	'User-agent':'none/ofbusiness',
	'Spam':'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)
print resp
result = resp.text
print(json.loads(result))
