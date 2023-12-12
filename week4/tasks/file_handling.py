import os
import shutil
from datetime import datetime, timedelta

def files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def is_file_modified(file, threshold_hours=24):
    now = datetime.now()
    threshold_time = now - timedelta(hours=threshold_hours)

    mtime = os.path.getmtime(file)
    ctime = os.path.getctime(file)

    return datetime.fromtimestamp(mtime) >= threshold_time or datetime.fromtimestamp(ctime) >= threshold_time

def update_files(files):
    for file in files:
        with open(file, 'a') as f:
            f.write(f"\nUpdated")

def create_last_24hours_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_files_to_folder(files, destination_folder):
    for file in files:
        shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))

def main():
    current_directory = os.getcwd()

    directory_files = files_in_directory(current_directory)

    recent_files = [file for file in directory_files if is_file_modified(file)]

    update_files(recent_files)

    create_last_24hours_folder("last_24hours")

    move_files_to_folder(recent_files, "last_24hours")

if __name__ == "__main__":
    main()

Updated