from pathlib import Path
from Checkers.pathCheck import checkPath

class filePath:
    '''Class Methods returns path to required file. Creates path directory(without file) if filepath does not exits'''

    # Absoulute path to the cwd
    absolute_path = str(Path('.').absolute())

    def __init__(self):
        pass

    def _create_directory(self, filepath):
        if checkPath(filepath):
            pass
        else:
            checkPath(filepath, True)

    def default_components_mssg_path(self):
        path = Path(self.absolute_path + '/DataFiles/comp_mssg.txt')
        print(path)
        self._create_directory(path)
        return path

    def components_txt_path(self):
        path = Path(self.absolute_path + '/UserFiles/components.txt')
        self._create_directory(path)
        return path
    
    def netlist_txt_path(self):
        path = Path(self.absolute_path + '/UserFiles/netlist.txt')
        #self._create_directory(path)
        return path
    
    def logic_gates_info_path(self):
        path = Path(self.absolute_path + '/DataFiles/DigitalComponents/logic_gates.txt')
        self._create_directory(path)
        return path
    
    def parsed_comp_data_path(self):
        path = Path(self.absolute_path + '/DataFiles/ParsedComponents/parsed_components.json')
        self._create_directory(path)
        return path
    
    def gate_codes_path(self):
        path = Path(self.absolute_path + '/DataFiles/gate_codes.json')
        self._create_directory(path)
        return path
    
    def all_nets_path(self):
        path = Path(self.absolute_path + '/DataFiles/all_nets.json')
        self._create_directory(path)
        return path

    def all_inputs_path(self):
        path = Path(self.absolute_path + '/DataFiles/all_inputs.json')
        self._create_directory(path)
        return path

    def all_outputs_path(self):
        path = Path(self.absolute_path+ '/DataFiles/all_outputs.json')
        self._create_directory(path)
        return path

    def all_components_path(self):
        path = Path(self.absolute_path + '/DataFiles/all_connections.json')
        self._create_directory(path)
        return path