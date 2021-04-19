from pathlib import Path
from shutil import rmtree

def checkPath(filepath, create_dir = False):
    '''Checks if a filepath exists, returns `True` if does, otherwise `False`.
     Creates filepath directory (not the file) if 2nd optional argument set `True` & returns `None`'''
    if type(filepath) is str:
        filepath = Path(filepath)
    if not create_dir:
        if Path.exists(filepath):
            return True
        else:
            return False
    else:
        try:
            rmtree(filepath)
        except FileNotFoundError:
            pass
        except FileExistsError:
            pass   
