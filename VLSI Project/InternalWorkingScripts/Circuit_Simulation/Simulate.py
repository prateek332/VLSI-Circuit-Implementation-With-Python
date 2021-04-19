from .all_nets import parse_all_nets
from .all_inputs import parse_input_nets
from .all_outputs import parse_output_nets
from .all_connections import parse_component_nets

def simulate():
    '''Calls all simulation scripts one-by-one in correct order'''
    print("Simulate Called")
    #parse_all_nets() Remove it later
    parse_input_nets()
    parse_output_nets()
    parse_component_nets()
