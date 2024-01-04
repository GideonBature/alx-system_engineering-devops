#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import csv
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

    u_name = name_data[employeeId - 1]["username"]
    file_name = f"{employeeId}.csv"

    with open(file_name, mode='w', newline='') as csv_file:
        field_names = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                       "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names,
                                quoting=csv.QUOTE_ALL)

        # writer.writeheader()

        for i in range(len(data)):
            if data[i]["userId"] is employeeId:
                user_id = data[i]["userId"]
                task_completed_status = data[i]["completed"]
                title = data[i]["title"]

                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": u_name,
                    "TASK_COMPLETED_STATUS": task_completed_status,
                    "TASK_TITLE": title
                    })
