#!/usr/bin/python3
"""
 a Python script that, using this REST API,
 Using what you did in the task #0,
 extend your Python script to export data in the
 JSON format.for a given employee ID,
 """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            newId.get("id"): [{
                "task": new.get("completed"),
                "completed": new.get("completed"),
                "username": newId.get("username")
                }
                for new in requests.get(url + "todos", params={
                    "userId": newId.get("id")}).json()]
            for newId in user}, jsonfile)
