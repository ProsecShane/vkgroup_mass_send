import requests as reqs
from time import sleep

TOKEN = open("token.txt", "r").read().strip('\n')

def usernames_to_ids(usernames):
	response = reqs.post("https://api.vk.com/method/users.get",
						 {"access_token": TOKEN, "v": "5.131",
				 	 	  "user_ids": ",".join([elem.split('/')[-1] for elem in usernames])}).json()["response"]
	return [str(elem["id"]) for elem in response]


USERNAMES = list(set(list(filter(lambda x: x != "", open("pages.txt", "r").read().split('\n')))))
MESSAGE = open("message.txt", "r", encoding="utf-8").read().strip('\n')
range_ = len(USERNAMES) // 100 + 1
print("Done: 0%")
for i in range(range_):
	req = reqs.post("https://api.vk.com/method/messages.send",
					{"v": "5.131", "access_token": TOKEN, "random_id": 0,
					 "message": MESSAGE, "peer_ids": ",".join(usernames_to_ids(USERNAMES[100*i: 100*(i+1)]))})
	if (i < range_ - 1):
		sleep(10)
	print(f"Done: {int((i+1)/range_*10000)/100}%")
