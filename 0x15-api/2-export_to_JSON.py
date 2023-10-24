#!/usr/bin/python3
"""
exporting to json
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.json".format(sys.argv[1]), "w", newline="") as jsonfile:
        json.dump({sys.argv[1]: [{
            "task": new.get("title"),
            "completed": new.get("completed"),
            "username": username
            } for new in todos]}, jsonfile)
