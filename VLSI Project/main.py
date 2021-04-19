from ChangeDetectors.netlist_txt_detect import MonitorNetlistChanges
from ChangeDetectors.components_txt_detect import MonitorComponentsChanges
from os import terminal_size
from InternalWorkingScripts import createComponents_txt
from InternalWorkingScripts import _createNetlist_txt
from ChangeDetectors import MonitorComponentsChanges
from ChangeDetectors import MonitorNetlistChanges

from concurrent.futures import ProcessPoolExecutor as pool
from multiprocessing import Process
import time

if __name__ == '__main__':
    createComponents_txt()
    _createNetlist_txt()

    with pool() as p:
        p.submit(MonitorComponentsChanges)
        p.submit(MonitorNetlistChanges)

    