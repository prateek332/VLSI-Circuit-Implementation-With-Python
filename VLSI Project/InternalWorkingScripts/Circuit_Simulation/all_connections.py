from InternalWorkingScripts.FilesPath.file_paths import filePath

import json
import re

from itertools import zip_longest


netlist_file_path = filePath().netlist_txt_path()
all_components_path = filePath().all_components_path()

def create_json(data):
    with open(all_components_path, 'w') as fp:
        json.dump(data, fp, indent=4)

def find_op_connections_nets(comp_name, nets, flag=0):
    output_nets = re.compile(rf'{comp_name}o\d*')
    if flag == 0:
        return output_nets.findall(nets)
    else:
        regx = re.compile(rf'^{comp_name}o?\d*')
        connections = []
        for n in nets:
            if regx.search(n) != None:
                continue
            connections.append(n)
        return connections


def parse_component_nets():
    '''Maps one-to-one, or one-to-many type of net connections'''
    global netlist_file_path, all_components_path

    all_components = {}

    with open(netlist_file_path,'r') as fp:
        for line in fp:
            if line.startswith('#'): # This is when we reach the `#inputs` section
                break
            if line in ('\n',""):
                continue

            nets = line.split()
            if len(nets) > 0:
                # checking if line has `in` or `op` at the beg
                if nets[0] in ('in','op'):
                    nets = nets[1:]
                #getting comp_name
                comp_name = nets[0]
                # Getting all outputs from the net string
                output_nets = find_op_connections_nets(comp_name=comp_name,nets=line)
                connection_nets = find_op_connections_nets(comp_name, nets, 1)

                if len(connection_nets) > 0:
                    tmp_dict = dict(zip_longest(connection_nets, output_nets, fillvalue=output_nets[len(output_nets)-1]))
                    all_components.update(tmp_dict)

        # Now reading all the connections mentioned in`#connections` section
        # right now readline() is one line after `#inputs` line
        # Reading till we reach `#connections` section
        for line in fp:
            if line.startswith('#connections'):
                break
        
        for more_connections in fp:
            if more_connections.startswith('#'): # For sections if added in the future
                break
            more_connections = more_connections.split()
            size = len(more_connections)
            i = 1
            while size > 1:
                # if connections specified like `a1o o11 o12 o13`, then all the nets `o11,o12,o13`,
                # to be connected to `a1o`
                # else just one to one connections will also be mapped
                all_components[more_connections[i]] = more_connections[0]
                i += 1
                size -= 1
    
    # Creating `/DataFiles/all_components.json`
    create_json(data=all_components)

