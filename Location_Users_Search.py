#!/usr/bin/python
import requests
import requests_cache
requests_cache.install_cache("github")

auth = ("PaddyViking", "65bbd523eca11c0376208a9a23e4c4dd5c8d8188")

def get_user_profile(url):
    r = requests.get(url, auth=auth)
    j = r.json()
    return j
    



location = raw_input('Press enter to continue: ')
# Confirming they want to continue
def get_users(location, page):
    url = "https://api.github.com/search/users?q=location:{}&per_page=100&page={}".format(location, page)
    r = requests.get(url, auth=auth)
    
    for user in r.json()["items"]:
	    profile = get_user_profile(user["url"])

	    f.write(u"{}|{}|{}|{}\n".format(user["login"], profile["name"], profile.get("followers"), user["html_url"]).encode("utf-8"))
    return len(r.json()["items"])
      

with open("output.txt", "w") as f:
    page = 1
    while get_users(location, page):
        page = page + 1
        print page
print "The User Data is printed in Output.txt"


