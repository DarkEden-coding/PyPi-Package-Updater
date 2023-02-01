import os
import shutil
from dotenv import load_dotenv
import subprocess
from time import sleep

username = "__token__"


def remove_build_files(input_dir):
    # get the list of all files and directories in the input directory
    files = os.listdir(input_dir)

    # loop through the files
    for file in files:
        # get the full path of the file
        file_path = os.path.join(input_dir, file)
        # check if the file is a directory
        if os.path.isdir(file_path):
            # if the dir is named dist or ends in .egg-info remove it
            if file == "dist" or file.endswith(".egg-info"):
                shutil.rmtree(file_path)
            else:
                # if the dir is not named dist call the function again
                remove_build_files(file_path)


# load environment variables from .env file
load_dotenv()

# get token from environment variables
token = os.getenv("TOKEN")

# get the input directory
input_dir = input("Enter the input directory: ")

# remove quotes from the input directory
input_dir = input_dir.replace('"', '')

# get the list of all files and directories in the input directory
files = os.listdir(input_dir)

# open pyproject.toml file
with open(os.path.join(input_dir, "pyproject.toml"), "r") as f:
    # read the file
    data = f.read()

    # get the version number
    version = data.split("version = ")[1].split('"')[1]
    print(f"Current version: {version}")

    # get the name of the package
    package_name = data.split("name = ")[1].split('"')[1]
    print(f"Package name: {package_name}")

    # change the version number to add one to the patch number
    new_version = version.split(".")
    new_version[2] = str(int(new_version[2]) + 1)
    new_version = ".".join(new_version)

    # change the version number in the file
    data = data.replace(f'version = "{version}"', f'version = "{new_version}"')

    print(f"New version: {new_version}")

    # write the new data to the file
    with open(os.path.join(input_dir, "pyproject.toml"), "w") as d:
        d.write(data)


# remove past build files
remove_build_files(input_dir)


# make commands
cmd1 = "py -m build"
cmd2 = f"twine upload --username={username} --password={token} dist/*"
cmd3 = f"pip install --upgrade {package_name}"

# run commands
subprocess.call(cmd1, cwd=input_dir, shell=True)
subprocess.call(cmd2, cwd=input_dir, shell=True)

# ask if the user wants to install the new version
install = input("Install new version? (y/n): ")

if install == "y":
    print("Installing new version...")
    sleep(10)
    for i in range(5):
        subprocess.call(cmd3, shell=True)
        sleep(1)
    print("Done!")
