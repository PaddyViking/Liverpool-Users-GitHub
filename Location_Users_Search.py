#!/usr/bin/python
import requests
import requests_cache
import csv
import os
requests_cache.install_cache("github")

auth = (os.environ.get("GITHUB_USERNAME"),
        os.environ.get("GITHUB_KEY"))

def get_user_profile(url):
    r = requests.get(url, auth=auth)
    j = r.json()
    return j
    
def get_users(location, page):
    url = "https://api.github.com/search/users?q=location:{}&per_page=100&page={}".format(location, page) 
    r = requests.get(url, auth=auth)
    try:
	items = r.json()["items"]
    except Exception:
        print r.json()
        raise

    for user in items:
	    profile = get_user_profile(user["url"])
            output = u"{},{},{},{},{},\n".format(user.get("login"), profile.get("name"), profile.get("followers"), profile.get("location"), user.get("html_url")).encode("utf-8")
            f.write(output)
            print output
    return len(r.json()["items"])
      

with open('Locations.txt') as fp:
    with open("Final_Output.csv", "w") as f:
        for line in fp:
            location = line
            page = 1
            while get_users(location, page):
                page = page + 1
                if page == 11:
                    break
                print page
print "The User Data is printed in Final_Output.csv"


