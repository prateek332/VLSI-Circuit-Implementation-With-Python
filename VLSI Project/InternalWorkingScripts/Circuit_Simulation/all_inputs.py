from InternalWorkingScripts.FilesPath.file_paths import filePath

import json


netlist_path = filePath().netlist_txt_path()
all_inputs_path = filePath().all_inputs_path()

def create_json(data):
    with open(all_inputs_path, 'w') as fp:
        json.dump(data, fp, indent=4)

def parse_input_nets():

    global all_inputs_path
    all_inputs = {}

    with open(netlist_path) as fp:
        for line in fp:
            if line.startswith('#'): # This is when we reach the `#inputs` section
                break
            if line == '\n':
                continue
            if line.startswith('in'):
                nets_with_in = line.split()
                #removing "in"
                nets = nets_with_in[1:]
                # component_name + o = output_net_name
                nets_out = nets[0] + "o"
                #removing component_name like a1, o4, n2
                nets = nets[1:]
                # collecting inputs untill output net
                for n in nets:
                    if n == nets_out:
                        break
                    all_inputs[n] = "ND" # Using `ND` for not defined
            
        # Now reading all the inputs mentioned below the `#inputs` line
        # right now readline() would be one line after `#inputs`
        for more_inputs in fp:
            if more_inputs.startswith('#'): # i.e. reached the `#outputs` section
                break
            more_inputs = more_inputs.split()
            for m in more_inputs:
                all_inputs[m] = "ND"
    
    # writing inputs to `/DataFiles/all_inputs.json`
    create_json(data=all_inputs)
        