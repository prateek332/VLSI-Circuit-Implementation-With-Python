from os.path import getmtime
from time import sleep

def ifModified(filepath):
    '''Keeps running an infinite loop on a `filepath`, till changes in the file are detected.
    (If changes detected, returns `True`). Run in a separate thread/process, for proper execution'''

    curr_time = getmtime(filepath) # Gets the current modified time
    while True:
        sleep(1) # Stops for 1 seconds between checks
        if (getmtime(filepath) == curr_time):
            continue
        else:
            return True
                   
    return False