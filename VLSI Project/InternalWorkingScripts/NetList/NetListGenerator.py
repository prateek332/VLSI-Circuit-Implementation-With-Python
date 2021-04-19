from InternalWorkingScripts.Gates.GateCodesGenerator import createGateCodes
from InternalWorkingScripts.FilesPath.file_paths import filePath
from InternalWorkingScripts.Circuit_Simulation.all_nets import parse_all_nets

from pathlib import Path
import json

# Path to gate_codes.json, used for making netlist
gate_codes_file_path = filePath().gate_codes_path()

Gate_Codes = {}

def _gateAndIndex(gate,Gate_Codes):
    '''Helper func, reads gate_code and gate_index from `gate_codes.json`'''
    gate_code = Gate_Codes[gate][0]
    gate_index = Gate_Codes[gate][1]
    Gate_Codes[gate][1] += 1
    return gate_code, str(gate_index)

def _netListHelper(gate, inputs = 1, quantity = 1):
    result = ""
    tmp = inputs
    while quantity != 0:
        g_code, g_index = _gateAndIndex(gate,Gate_Codes)
        netlist = g_code + g_index
        pins = netlist
        k = 1
        while tmp != 0:
            pins += " " + g_code + g_index + str(k)
            tmp -= 1
            k += 1
        pins += " " + g_code + g_index + 'o' # For the output pin
        result = result + pins + '\n' # Final netlist data for one Gate component
        tmp = inputs
        quantity -= 1
    return result

def _netListCreator(netlist_data):
    # Create fresh set of gate_codes for making NetList
    createGateCodes()

    global Gate_Codes, gate_codes_file_path

    with open(gate_codes_file_path) as gc:
        Gate_Codes = json.load(gc)
        print("Gate_Codes Loaded Successfully")
    
    net_list_file_path = filePath().netlist_txt_path()

    with open(net_list_file_path,'w') as nl:
        for data in netlist_data:
            if data[0] == 'not':
                netlist = _netListHelper(data[0],inputs=1, quantity=int(data[1]))
            else:
                netlist = _netListHelper(data[0], int(data[1]), int(data[2]))
            nl.write(netlist)
            nl.write('\n')
    
    # Finally modify the gate counts used in netlist generation
    # for future changes
    with open(gate_codes_file_path,'w') as gc:
        json.dump(Gate_Codes,gc)

def createNetlist():
    '''This is this script's main function, to be called to create a `netlist.txt` file'''
    parsed_components_file_path = filePath().parsed_comp_data_path()
    with open(parsed_components_file_path) as pc:
        data = json.load(pc)
        print(data, type(data))
        _netListCreator(data)
    
    # parse all nets data to `/DataFiles/all_nets.json`
    parse_all_nets()