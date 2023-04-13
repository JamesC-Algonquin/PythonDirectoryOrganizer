from os import mkdir, path, listdir
import shutil
import json


def get_json_data(exception_callback):
    try:
        json_file = open("config.json")
    except OSError:
        exception_callback("Config.json not found.")
        return
    else:
        json_data = json.load(json_file)
        return json_data


def restore_default(exception_callback):
    shutil.copyfile("config_default.json", "config.json")
    exception_callback("Restored Default Configuration\n")


def get_directory(file_path, exception_callback):
    file_list = []
    try:
        total_dir = listdir(file_path)
    except FileNotFoundError:
        exception_callback("Directory Not Found\n")
        return
    else:
        for file in total_dir:
            if path.isfile(file_path + "/" + file):
                file_list.append(file)
        return file_list


def sort_files(file_path, exception_callback):
    # get file list from directory
    file_list = get_directory(file_path, exception_callback)

    if not file_list:
        exception_callback("Process Failed: No Files Found\n")
        return

    # get ruleset from JSON file
    json_data = get_json_data(exception_callback)

    if not json_data:
        exception_callback("Please restore configuration files\n")
        return

    # loop for each file found
    for file in file_list:

        # get file extension
        file_ext = path.splitext(file)

        # loop for each rule in ruleset
        for rule in json_data["ext_sort_rules"]:
            # if extension found in rule
            if file_ext[1] in rule["extensions"]:
                # create path if non-existing
                if not path.exists(file_path + "/" + rule["directory"]):
                    mkdir(file_path + "/" + rule["directory"])
                    exception_callback("Created Directory: " + file_path + "/" + rule["directory"])

                # move file to new directory
                try:
                    shutil.move(file_path + "/" + file, file_path + "/" + rule["directory"])
                    exception_callback("File " + file + " was moved to directory "
                                       + file_path + "/" + rule["directory"])
                except shutil.Error:
                    exception_callback("File " + file + " already exists at destination")
    exception_callback("Process Finished\n")
