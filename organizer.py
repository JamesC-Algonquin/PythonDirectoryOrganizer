from os import mkdir, path, listdir

image_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
text_ext = (".txt", ".doc", ".docx", ".rtf")
video_ext = (".mp4", ".wmv", ".mov")
file_list = []


def get_directory(file_path):
    total_dir = listdir(file_path)
    for file in total_dir:
        if path.isfile(file_path + "/" + file):
            file_list.append(file)