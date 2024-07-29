#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Maluleke Masingita
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()
    done = 0
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
