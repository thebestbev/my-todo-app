import glob
import csv
import webbrowser
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


def read_textfiles(directory):
    """Reads and prints all text files in a directory - import glob"""
    myfiles = glob.glob(f"{directory}/*.txt")
    for filepath in myfiles:
        with open(filepath, "r") as file:
            filenames = file.read()
            return filenames


def read_csv(file):
    """Reads a CSV file and stores the data as a list - import CSV"""
    with open(file, "r") as file:
        data = list(csv.reader(file))
        return data


def web_search(search_term):
    """Google search for any term"""
    webbrowser.open("https://www.google.com/search?q=" + search_term)

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

if __name__ == "__main__":
    feet = 10
    inches = 2
    print(convert(feet, inches))