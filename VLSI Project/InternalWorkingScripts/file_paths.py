from pathlib import Path
from Checkers.pathCheck import checkPath

class filePath:
    '''Class Methods returns path to required file. Creates path directory(without file) if filepath does not exits'''
    def __init__(self):
        pass

    def _create_directory(self, filepath):
        if checkPath(filepath):
            print("passed")
            pass
        else:
            checkPath(filepath, True)

    def default_components_mssg_path(self):
        path = Path(str(Path('.').absolute()) + '/DataFiles/comp_mssg.txt')
        print(path)
        self._create_directory(path)
        return path

    def components_txt_path(self):
        path = Path(str(Path('.').absolute()) + '/UserFiles/components.txt')
        self._create_directory(path)
        return path
    
    def netlist_txt_path(self):
        path = Path(str(Path('.').absolute()) + '/UserFiles/netlist.txt')
        #self._create_directory(path)
        return path
    
    def logic_gates_info_path(self):
        path = Path(str(Path('.').absolute()) + '/DataFiles/DigitalComponents/logic_gates.txt')
        self._create_directory(path)
        return path
    
    def parsed_comp_data_path(self):
        path = Path(str(Path('.').absolute()) + '/DataFiles/ParsedComponents/parsed_components.json')
        self._create_directory(path)
        return path
    
    def gate_codes_path(self):
        path = Path(str(Path('.').absolute()) + '/DataFiles/gate_codes.json')
        self._create_directory(path)
        return path