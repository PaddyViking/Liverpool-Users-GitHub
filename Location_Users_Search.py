#!/usr/bin/python
import requests
import requests_cache
import csv
requests_cache.install_cache("github")

def get_user_profile(url):
    r = requests.get(url)
    j = r.json()
    return j
    

location = raw_input('Enter which City you wish to search in: ')
# What city they wish to recieve the users from
def get_users(location, page):
    url = "https://api.github.com/search/users?q=location:{}&per_page=100&page={}".format(location, page)
    r = requests.get(url)
    
    for user in r.json()["items"]:
	    profile = get_user_profile(user["url"])

	    f.write(u"{},{},{},{},\n".format(user["login"], profile["name"], profile.get("followers"), user["html_url"]).encode("utf-8"))
    return len(r.json()["items"])
      

with open("Final_Output.csv", "w") as f:
    page = 1
    while get_users(location, page):
        page = page + 1
        print page
print "The User Data is printed in Final_Output.csv"


