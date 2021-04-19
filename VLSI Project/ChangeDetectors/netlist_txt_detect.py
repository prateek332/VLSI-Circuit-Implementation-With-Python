# Make this script so that it will run, only after the first chages are observed in `netlist.txt`

from InternalWorkingScripts.FilesPath.file_paths import filePath
from Checkers import ifModified
from InternalWorkingScripts import simulate

from time import sleep
from pathlib import Path

filepath = filePath().netlist_txt_path()

def detect_change(filepath):
    change = ifModified(filepath)
    return change


def MonitorNetlistChanges():
    '''Continuously Monitor `netlist.txt` file for changes and take appropriate actions'''

    global filepath
    
    while True:
        print("Detecting")
        changed = detect_change(filepath)
        if changed:
            print("Netlist Change Detected")
            simulate()
        else:
            sleep(1)


