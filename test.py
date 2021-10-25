import requests

BASE="http://127.0.0.1:5000/"

response = requests.get(BASE + "profile/dewashish3590@gmail.com")

print(response.status_code)