#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
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

    u_name = name_data[employeeId - 1]["name"]

    print(f"Employee {u_name} is done with tasks({cc}/{tc}):")

    for i in range(len(data)):
        if data[i]["userId"] is employeeId:
            if (data[i]["completed"] is True):
                title = data[i]["title"]
                print(f"\t{title}")
