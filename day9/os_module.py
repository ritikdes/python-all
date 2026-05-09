import os

directory = os.getcwd()
dir_list = os.listdir(directory)


print(f"Files and directories in '{directory}':")
for dir in dir_list:
    if dir.endswith(".py"):
        file_path = os.path.join(directory, dir)
        print(f"{dir} | {os.path.getsize(file_path)} bytes")