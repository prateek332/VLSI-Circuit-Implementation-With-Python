from pathlib import Path

path = Path(str(Path('.').absolute()) + '/DataFiles/comp_mssg.txt')

print(Path.exists(path))