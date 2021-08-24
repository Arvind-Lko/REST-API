import requests

base_url = 'http://127.0.0.1:5000/cert'

resp = requests.get(base_url)

data = resp.json()

print("Enter Certification Name")
user_input=input()
# print(data)

for cert in data:
    if data['name'].upper() == user_input.upper():
        print("Cost of {} is {}".format(user_input,cert['cost']))

