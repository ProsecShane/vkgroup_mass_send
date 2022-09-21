import requests as reqs

TOKEN = open("токен.txt", "r").read().strip('\n')

def usernames_to_ids(usernames):
	response = reqs.post("https://api.vk.com/method/users.get",
						 {"access_token": TOKEN, "v": "5.131",
				 	 	  "user_ids": ",".join([elem.split('/')[-1] for elem in usernames])}).json()["response"]
	return [str(elem["id"]) for elem in response]


USERNAMES = list(filter(lambda x: x != "", open("страницы.txt", "r").read().split('\n')))
MESSAGE = open("сообщение.txt", "r", encoding="utf-8").read().strip('\n')
req = reqs.post("https://api.vk.com/method/messages.send",
				{"v": "5.131", "access_token": TOKEN, "random_id": 0,
				 "message": MESSAGE, "peer_ids": ",".join(usernames_to_ids(USERNAMES))})
print(req.text)
