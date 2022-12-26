import requests
import json

url = 'https://gorest.co.in/public/v2/users'
headers={}
payload ={}
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.text)
print("//////////")
result1 = response.text
print(result1[0])
print("/////////////")
result = response.json()
print(result)
print("///////////")
print(result[0]["name"])

payload=json.dumps( {
    "name": "morpheus",
    "job": "leader"
})

response= requests.post("https://reqres.in/api/users",headers=headers,data=payload)
print(response)
print(response.json())

payload =json.dumps(
{
    "first_name": "Janet warner",
    "last_name": "Weave asdsadr"
}
)
response = requests.put("https://reqres.in/api/users/2",headers=headers,data=payload)
print(response)
print(response.json())


response = requests.delete("https://reqres.in/api/users/2",headers=headers)
print(response)
