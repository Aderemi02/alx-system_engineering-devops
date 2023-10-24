#!/usr/bin/python3
"""
exporting to csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [write.writerow(
            [sys.argv[1], username, new.get("completed"), new.get("title")]
            ) for new in todos]
