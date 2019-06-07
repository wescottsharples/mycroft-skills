#!/usr/bin/env python3
"""Util contains helper functions for the init."""
import os
import json


def read_data():
    """Reads current data and returns it's json in dict format.

    Returns:
        current_data (dict): Current read data from projects.json.
    """
    with open("projects.json", "r") as rf:
        data = json.load(rf)

    return data

def write_data(data=None, newdata=None):
    """Updates current data and writes to projects.json.

    This function will update all key to new values in current projects.json.

    Args:
        data (dict): Current projects.json data.
        newdata (dict): New data to update to projects.json.
    """
    newkeys = list(newdata)
    for k in data.keys():
        for i in newkeys:
        if k == i:
            data[k] = newdata[i]

    with open("projects.json", "w") as wf:
        json.dump(data, wf)
        
def data_checker():
    """Checks if projects data exists (projects.json). If it does not exist,
    creates a template of the project data.
    """
    exists = os.path.isfile('projects.json')

    if exists:
        pass
    else:
        template = {"current_project": "None", "max_projects": "0"}
        with open("projects.json", "w") as wf:
            json.dump(template, wf)
