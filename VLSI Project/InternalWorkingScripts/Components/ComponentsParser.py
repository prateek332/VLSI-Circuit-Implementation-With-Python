from Checkers import pathCheck, parsed_component_checker
from InternalWorkingScripts.PopUpMessage import popUp
from InternalWorkingScripts.FilesPath.file_paths import filePath
from InternalWorkingScripts.NetList.NetListGenerator import createNetlist

import re, json
from pathlib import Path
from threading import Thread


# Stores the parsed-components data, later to be written in json file, stored in
# Datafiles/parsed_components.json
parsed_components_list = []

# path to `components.txt`
comp_path = filePath().components_txt_path()


def _componentsParser(gate_info):
    global parsed_components_list

    gate_info = gate_info.strip()

    gate_name = re.compile(r'\w{2,4}')
    gate_inputs_quantity = re.compile(r'(-)?\d+(\s(-)?\d+)?')

    # Getting info
    try:
        gate = gate_name.search(gate_info).group()
    except AttributeError:
        gate = None
    try:
        _x = gate_inputs_quantity.search(gate_info).group().split()
    except AttributeError:
        _x = [None, None]
    # _x[0] = quantity, for NOT gate
    # _x[0] = no_of_inputs, _x[1] = quantity, for all other gates

    return_check = parsed_component_checker.check_parsed_value(gate, _x)
    if return_check is True:
        if gate == 'not':
            parsed_components_list.append([gate,_x[0]])
        else:
            parsed_components_list.append([gate,_x[0], _x[1]])
    return return_check

def writeParsedComponents():
    '''Write the succesfully parsed components to `DataFiles/parsed_components.json`'''
    filepath = filePath().parsed_comp_data_path()
    
    global parsed_components_list

    with open(filepath, 'w') as wpc:
        json.dump(parsed_components_list,wpc)
    

def parseComponents():
    '''Reads `components.txt` and parse it to create a components list, for NetListGenerator script. Returns `None`'''
    global parsed_components_list, comp_path
    parsed_components_list.clear()

    # Keeps track of valid compnents, and stops parsing when encounters
    # an invalid compoenent entry
    comp_validity_check = True
    with open(comp_path) as cp:
        for line in cp:
            if line == '\n' or line[0] == '#':
                continue
            if comp_validity_check is True:
                comp_validity_check = _componentsParser(line)
            else:
                break

    # If all components are valid, then components are written to file
    # for Net_List generation
    if comp_validity_check:
        writeParsedComponents()
        print("Components parsed")
        createNetlist()
        popUp.popUp('Components Read Successfully', "Proceed to 'NetList.txt'")
        


