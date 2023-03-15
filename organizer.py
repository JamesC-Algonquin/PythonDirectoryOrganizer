from os import mkdir, path, listdir
import shutil

image_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
text_ext = (".txt", ".doc", ".docx", ".rtf")
video_ext = (".mp4", ".wmv", ".mov")
file_list = []


def get_directory(file_path):
    total_dir = listdir(file_path)
    for file in total_dir:
        if path.isfile(file_path + "/" + file):
            file_list.append(file)
    sort_files(file_path)


def sort_files(file_path):
    for file in file_list:
        file_ext = path.splitext(file)
        if file_ext[1] in image_ext:
            if not path.exists(file_path + "/" + "Images"):
                mkdir(file_path + "/" + "Images")
            shutil.move(file_path + "/" + file, file_path + "/" + "Images")
        if file_ext[1] in text_ext:
            if not path.exists(file_path + "/" + "Text"):
                mkdir(file_path + "/" + "Text")
            shutil.move(file_path + "/" + file, file_path + "/" + "Text")
        if file_ext[1] in video_ext:
            if not path.exists(file_path + "/" + "Video"):
                mkdir(file_path + "/" + "Video")
            shutil.move(file_path + "/" + file, file_path + "/" + "Video")
