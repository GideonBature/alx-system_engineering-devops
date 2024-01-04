#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employeeId = int(sys.argv[1])

    api_url = "https://jsonplaceholder.typicode.com/todos/"

    api_name_url = "https://jsonplaceholder.typicode.com/users/"

    response = requests.get(api_url)
    data = response.json()

    name_response = requests.get(api_name_url)
    name_data = name_response.json()

    cc = 0
    tc = 0

    for i in range(len(data)):
        if data[i]["userId"] is employeeId:
            if (data[i]["completed"] is True):
                cc += 1
                tc += 1
            else:
                tc += 1

    u_name = name_data[employeeId - 1]["username"]
    file_name = f"{employeeId}.json"
    dict_key = f"{employeeId}"

    with open(file_name, mode='w') as json_file:
        _dict = {}
        _dict[dict_key] = []

        for i in range(len(data)):
            if data[i]["userId"] is employeeId:
                task_completed_status = data[i]["completed"]
                title = data[i]["title"]

                _dict[dict_key].append({"task": title,
                                        "completed": task_completed_status,
                                        "username": u_name
                                        })
        json.dump(_dict, json_file)
