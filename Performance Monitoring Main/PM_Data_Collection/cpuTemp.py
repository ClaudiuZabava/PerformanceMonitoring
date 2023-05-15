import clr
import System
clr.AddReference("LibreHardwareMonitorLib")
assemblies = System.AppDomain.CurrentDomain.GetAssemblies()

# Print the name of each loaded assembly
for assembly in assemblies:
    print(assembly.FullName)

from LibreHardwareMonitorLib import *