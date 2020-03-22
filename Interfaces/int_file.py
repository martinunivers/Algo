# int_file.py
"""
Interacts with persistant data in a file.
"""

from pathlib import Path


def save_data(data, file_path: str, file_name: str):
    """
    Save data into text file
    """
    data_string = ""
    # convert list and tuple to string
    if isinstance(data, list) or isinstance(data, tuple):
        data_generator = (str(item) for item in data)
        data_string = " ".join(data_generator)
    else:
        data_string = data
    try:
        with open(Path(file_path+"/"+file_name+".txt"), mode="w") \
                as fileObject:
            fileObject.write(data_string)
    except FileNotFoundError:
        print("File not found")


def load_integer_list(file_path: str, file_name: str):
    """
    Load data from file and return integer list
    """

    data_integer = []
    try:
        with open(Path(file_path+"/"+file_name+".txt"), mode="r") \
                as fileObject:
            data_integer = fileObject.read().split()
            for idx in range(len(data_integer)):
                data_integer[idx] = int(data_integer[idx])
            return data_integer
    except FileNotFoundError:
        print("File not found")
        return data_integer


def load_string_list(file_path: str, file_name: str):
    """
    Load data from file and return string list
    """

    try:
        with open(Path(file_path+"/"+file_name+".txt"), mode="r") \
                as fileObject:
            return fileObject.read().split()
    except FileNotFoundError:
        print("File not found")
        return []


def load_string(file_path: str, file_name: str):
    """
    Load data from file and return string
    """

    try:
        with open(file_path+"\\"+file_name+".txt", "r") as file_handle:
            return file_handle.read()
    except FileNotFoundError:
        print("Cannot load data from the file")
        return ""
