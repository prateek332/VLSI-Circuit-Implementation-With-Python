from InternalWorkingScripts.FilesPath.file_paths import filePath
from InternalWorkingScripts.PopUpMessage import popUp

def logicGatesList():
    lg_path = filePath().logic_gates_info_path()

    logic_gates = None
    try:
        with open(lg_path) as lg:
            logic_gates = lg.read().split()  # List of logic gates
    except FileNotFoundError:
        print("'DataFiles/DigitalComponents/logic_gates.txt' is corrupt or does not exists. Please reinstall the program.")
        exit()
    
    return  logic_gates

def check_parsed_value(gate, i_q):
    '''Checks for invalid gates input from the user. Return `True` if all components are correct'''

    logic_gates = logicGatesList()

    if gate not in logic_gates:
        popUp.popUp('Gate Name Error', f'{gate} - Does not exists')
        print(f"Gate name: '{gate}' does not exits")
        return False
        #exit()
    
    if i_q[0] == None:
        popUp.popUp('Inputs/Quantity Error',f"No inputs/quantity provided for Gate:'{gate}'")
        print(f"No inputs/quantity provided for Gate: '{gate}'")
        return False

    if len(i_q) == 1:
        # Gate should be not gate
        if gate != 'not':
            popUp.popUp('Inputs/Quantity Error',f"Invalid values provided for Gate: '{gate}'.")
            print(f"Invalid values provided for Gate: '{gate}'.")
            return False
        if int(i_q[0]) < 1:
            popUp.popUp('Quantity Error',"not gate quantities are invalid.")
            print("NOT gate quantity are invalid.")
            return False
            #exit()
            
    else:
        if int(i_q[0]) < 1:
            popUp.popUp('Gate Input Info Error', f'{gate}-inputs are invalid')
            print("Wrong number of inputs for Gate:",gate)
            return False
            #exit()
        if int(i_q[1]) < 1:
            popUp.popUp('Gate Quantity Info Error', f'{gate}-quantity are invalid')
            print("Invalid quantity for Gate:",gate)
            return False
            #exit()
    return True