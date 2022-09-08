#!/usr/bin/python

import dmenu
import os
import subprocess
import pyperclip
import sys
# from zenipy import zenipy

BASE_PATH = "/home/gerry/Documents/Notes"
NUM_LINES = 20
view_command = "gvim -R"
edit_command = "gvim"


def dir_prompt(path):
    # directories, filenames = get_dir_contents(path)
    # selection = dmenu_prompt(directories + filenames)

    # if selection in directories:
        # dir_prompt(os.path.join(path, selection))
    # elif selection in filenames:
        # file_prompt(path, selection)
    # else:
        # new_file_prompt(path, selection)

    contents = get_dir_contents(path)
    contents.sort()
    selection = dmenu_prompt(contents)
    if selection in contents:
        file_prompt(path, selection)
    else:
        new_file_prompt(path, selection)


def file_prompt(dirpath, filename):
    # action = dmenu_prompt(["Copy", "View", "Edit", "Rename", "Delete"])
    action = dmenu_prompt(["Copy", "View", "Edit"])
    if action == "View":
        view_file(dirpath, filename)
    elif action == "Copy":
        copy_file(dirpath, filename)
    elif action == "Edit":
        edit_file(dirpath, filename)
    elif action == "Rename":
        print("Rename")
    elif action == "Delete":
        print("Delete")


def view_file(dirpath, filename):
    # file = open(os.path.join(dirpath, filename), "r")
    # file_contents = file.read()
    # zenipy.entry(title=filename, placeholder=file_contents, width=330, height=120, timeout=None) # NOQA
    command = view_command.split() + [os.path.join(dirpath, filename)]
    print(command)
    subprocess.call(command, shell=False)


def edit_file(dirpath, filename):
    command = edit_command.split() + [os.path.join(dirpath, filename)]
    print(command)
    subprocess.call(command, shell=False)


def copy_file(dirpath, filename):
    file = open(os.path.join(dirpath, filename), "r")
    file_contents = file.read()
    file.close()
    print(file_contents)
    pyperclip.copy(file_contents)


def new_file_prompt(dirpath, filename):
    subprocess.call(EDIT_COMMAND.split() + [os.path.join(dirpath, filename)])


def get_dir_contents(path):
    contents = []
    for (dirpath, subdirs, files) in os.walk(path, topdown=True):

        for file_ in files:
            base_path_slash = os.path.join(BASE_PATH, "")
            item = os.path.join(dirpath, file_).replace(base_path_slash, "")
            contents.append(item)

    return contents


def dmenu_prompt(options):
    return dmenu.show(options, lines=NUM_LINES, case_insensitive=True)


if len(sys.argv) > 1:
    view_command = sys.argv[1]
    edit_command = sys.argv[1]

dir_prompt(BASE_PATH)
