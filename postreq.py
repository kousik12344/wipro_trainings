import requests
url="https://jsonplaceholder.typicode.com/posts/1"
data={
    "title":"Hii students",
    "body":"Wipro Geeks",
    "userid":1
    }

response=requests.post(url,json=data)
print("Status code: ",response.status_code)
print("response.json: ",response.json())

