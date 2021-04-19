from InternalWorkingScripts.FilesPath.file_paths import filePath


netlist_path = filePath().netlist_txt_path()

def _createNetlist_txt():
    '''Creates an empty `UserFiles/netlist.txt` file for proper execution'''
    with open(netlist_path, 'w') as fp:
        pass

