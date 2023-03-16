from os import mkdir, path, listdir
import shutil
import json


def get_json_data():
    json_file = open("config.json")
    json_data = json.load(json_file)
    return json_data


def get_directory(file_path):
    file_list = []
    total_dir = listdir(file_path)
    for file in total_dir:
        if path.isfile(file_path + "/" + file):
            file_list.append(file)
    return file_list


def sort_files(file_path):
    # get file list from directory
    file_list = get_directory(file_path)
    # loop for each file found
    for file in file_list:

        # get file extension
        file_ext = path.splitext(file)
        # get ruleset from JSON file
        json_data = get_json_data()

        # loop for each rule in ruleset
        for rule in json_data["ext_sort_rules"]:
            # if extension found in rule
            if file_ext[1] in rule["extensions"]:
                # create path if non-existing
                if not path.exists(file_path + "/" + rule["directory"]):
                    mkdir(file_path + "/" + rule["directory"])
                # move file to new directory
                shutil.move(file_path + "/" + file, file_path + "/" + rule["directory"])
