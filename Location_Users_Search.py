#!/usr/bin/python
import requests

auth = ("PaddyViking", "65bbd523eca11c0376208a9a23e4c4dd5c8d8188")

def get_follow_number(url):
    r = requests.get(url, auth=auth)
    j = r.json()
    return j.get("followers")
    



location = raw_input('Press enter to continue: ')
# Confirming they want to continue
def get_users(location, page):
    url = "https://api.github.com/search/users?q=location:{}&per_page=100&page={}".format(location, page)
    r = requests.get(url, auth=auth)
    with open("output.txt", "w") as f:
    
        for user in r.json()["items"]:
	    follows = get_follow_number(user["url"])
	    f.write("{}|{}\n".format(user["login"], follows))
            print user["login"]
get_users(location, 1)
print "The User Data is printed in Output.txt"


