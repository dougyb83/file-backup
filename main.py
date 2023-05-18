import os
import datetime

def main():
    get_file_last_modified_date()

def get_folder_to_search():
    pass

def get_destination_folder():
    pass

def get_datetime_to_search_from():
    #option to enter custom date/time
    #option to select date time from of last backup
    pass

def search_files():
    pass

def get_file_last_modified_date():
    #os.path.getmtime(path)  Cross-platform way to get file modification time in Python. It returns the Unix timestamp of when the file was last modified.
    path = r"C:\Users\dougy\Desktop\MS2 Ideas.txt"
    time = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%d-%m-%Y %H:%M:%S')
    print(time)

def copy_files():
    pass

def save_backup_datetime():
    pass


if __name__ == "__main__":
    main()