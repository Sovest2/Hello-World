import requests


# response = requests.get("http://google.com")
# print(response.headers)
# print(response.headers["Content-Type"])
# print(response.headers["Date"])

# response = requests.get("http://google.com/search", params={"q":"Space oddity"})
# # print(response.content)

# with open("google.html","wb") as file:
#     file.write(response.content)

# response = requests.get("http://yandex.ru/search", params={"text":"Country roads"})

# with open("yandex.html","wb") as file:
#     file.write(response.content)

session = requests.Session()

response = session.get("http://google.com")
response = session.get("http://google.com/search", params={"q":"Space oddity"})




