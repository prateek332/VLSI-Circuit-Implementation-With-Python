from InternalWorkingScripts.FilesPath.file_paths import filePath
from Checkers.pathCheck import checkPath

import json


Gate_Codes = {
    'and' : ['a',1],
    'or' : ['o',1],
    'not' : ['n',1],
    'nand': ['na',1],
    'nor' : ['no',1],
    'xor' : ['xo',1],
    'xnor': ['xn',1]
}

gate_codes_file_path = filePath().gate_codes_path()

def createGateCodes():
    global gate_codes_file_path, GateCodes

    try:
        with open(gate_codes_file_path,'w') as gc:
            json.dump(Gate_Codes,gc)

    except FileExistsError as e:
        print(f"Remove `Gate_Codes.json` file from: {str(gate_codes_file_path)}")
        print("Run the main_script again")
        exit()
            