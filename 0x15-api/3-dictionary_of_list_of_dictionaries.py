#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests


if __name__ == "__main__":

    api_url = "https://jsonplaceholder.typicode.com/todos/"

    api_name_url = "https://jsonplaceholder.typicode.com/users/"

    response = requests.get(api_url)
    data = response.json()

    name_response = requests.get(api_name_url)
    name_data = name_response.json()

    file_name = "todo_all_employees.json"

    with open(file_name, mode='w') as json_file:
        todo_all_employee = {}

        for i in range(len(name_data)):
            u_name = name_data[i]["username"]
            dict_key = name_data[i]["id"]

            _lists = []

            for j in range(len(data)):
                if data[j]["userId"] == dict_key:
                    task_completed_status = data[j]["completed"]
                    title = data[j]["title"]

                    _lists.append({
                        "task": title,
                        "completed": task_completed_status,
                        "username": u_name
                        })

            todo_all_employee[dict_key] = _lists

        json.dump(todo_all_employee, json_file)
