import requests 

Base = "http://127.0.0.1:5000"

response2 = requests.get(Base + "/img/0")
response = requests.post(Base + "/img/1", json={"fileName": "Iain"})

print(response.json())
print(response2.json())