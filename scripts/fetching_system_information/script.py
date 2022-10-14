import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system. Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")
