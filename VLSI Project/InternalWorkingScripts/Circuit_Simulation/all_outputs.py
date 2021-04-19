from InternalWorkingScripts.FilesPath.file_paths import filePath

import json
import re

netlist_path = filePath().netlist_txt_path()
all_outputs_path = filePath().all_outputs_path()

def create_json(data):
    with open(all_outputs_path, 'w') as fp:
        json.dump(data, fp, indent=4)

def if_output(comp_name, net):
    '''If output net found, returns it, otherwise returns `None`'''
    regex = re.compile(rf'{comp_name}o\d*')
    match = regex.search(net)
    if match == None:
        return None
    else:
        return match.group()

def parse_output_nets():

    global all_outputs_path
    all_outputs = {}

    with open(netlist_path,'r') as fp:
        for line in fp:
            if line.startswith('#'): # This is when we reach the `#inputs` section
                break
            if line == '\n':
                continue
            if line[0:2] == 'op':
                nets_with_op = line.split()
                #removing "op"
                nets = nets_with_op[1:]
                #saving comp_name
                comp_name = nets[0]
                # finding and collecting all output nets for this component
                for n in nets:
                    if if_output(comp_name, n) != None:
                        all_outputs[n] = "ND" # Using `ND` for not defined

        # Now reading all the outputs mentioned in `#outputs` section
        # right now readline() is one line after '#inputs` line
        # Till we reach the `#output` section
        for line in fp:
            if line.startswith('#output'):
                break

        for more_outputs in fp:
            if more_outputs.startswith('#'):
                break
            more_outputs = more_outputs.split()
            for m in more_outputs:
                all_outputs[m] = "ND"
    
    # Creating `/DataFiles/all_outputs.json`
    create_json(data=all_outputs)