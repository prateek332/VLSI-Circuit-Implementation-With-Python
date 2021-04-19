import os, time
from shutil import Error
from pathlib import Path
from Checkers.pathCheck import checkPath
from concurrent.futures import ThreadPoolExecutor as pool
from InternalWorkingScripts.FilesPath.file_paths import filePath
from InternalWorkingScripts.PopUpMessage.popUp import popUp


# Components.txt file path for creation, for user interactions
comp_path = filePath().components_txt_path()

sample_data_mssg = "" # Will save sample_data text

def components_mssg_find():
    global sample_data_mssg
    comp_mssg_path = filePath().default_components_mssg_path()
    
    try:
        with open(comp_mssg_path,'r') as cm:
            sample_data_mssg = cm.read()
    except FileNotFoundError:
        print("File 'DataFiles/comp_mssg.txt' is missing or corrupt. Please reinstall the program.")
        exit()

def fileMaker():
    global sample_data_mssg
    # Create File Path, if it doesn't exists
    try:
        with open(comp_path,'w') as cp:
            cp.writelines(sample_data_mssg)
    except (FileNotFoundError, FileExistsError, Exception):
        print('Something went wrong with `components.txt`')


def createComponents_txt():
    # Find components sample message
    components_mssg_find()
    # Creates `components.txt`
    fileMaker()
    print("'UserFiles/components.txt' created. Open it for furthur instructions.")
    popUp("Components.txt Created","`Components.txt` is created in `/(Program_Dir)/UserFiles`. Open it for furthur instructions")

