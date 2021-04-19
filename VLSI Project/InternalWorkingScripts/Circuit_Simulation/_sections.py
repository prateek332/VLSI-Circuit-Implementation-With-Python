from InternalWorkingScripts.FilesPath.file_paths import filePath

def create_in_out_conn_sections():
    ''' Create `#input`, `#output` & `#connections` sections in the `netlist.txt`'''
    netlist_path = filePath().netlist_txt_path()
    with open(netlist_path,'a') as fp:
        fp.write('''
        \n#inputs\n\n
        \n#outputs\n\n
        \n#connections\n\n''')