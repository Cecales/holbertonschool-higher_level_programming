#!/usr/bin/python3
"""
Module 7-add_item
Adds all arguments to a python list,
and then save them to a file
"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []

for element in argv[1:]:
    my_list.append(str(element))
save_to_json_file(my_list, filename)
