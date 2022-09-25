import psutil
import platform
import uuid
import re
import json
import socket
from datetime import datetime

### COMPUTER STATS CHECKER ###

uname = platform.uname()

boot_time_timestamp = psutil.boot_time() # Boot time timestamp
bt = datetime.fromtimestamp(boot_time_timestamp) # Boot time
cpufreq = psutil.cpu_freq() # Cpu
svmem = psutil.virtual_memory() # Memory
disk = psutil.disk_usage("/") # Disk

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

data = { # Json object to store all of the data. Values can be added and removed.
    "system": {
        "system": uname.system,
        "nodes": uname.node,
        "release": uname.release,
        "version": uname.version,
        "machine": uname.machine,
        "processor": uname.processor,
        "ip adress": socket.gethostbyname(socket.gethostname()),
        "mac adress": ':'.join(re.findall('..', '%012x' % uuid.getnode())),
        "ram": str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB",
    },
    "boot_time": {
        "time": f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    },
    "cpu_info": {
        "physical cores": psutil.cpu_count(logical=False),
        "total cores": psutil.cpu_count(logical=True),
        "max frequency": f"{cpufreq.max:.2f}Mhz",
        "min frequency": f"{cpufreq.min:.2f}Mhz",
        "current frequency": f"{cpufreq.current:.2f}Mhz",
        "total cpu usage": f"{psutil.cpu_percent()}%"
    },
    "memory_info": {
        "total": f"{get_size(svmem.total)}",
        "available": f"{get_size(svmem.available)}",
        "used": f"{get_size(svmem.used)}",
        "percentage": f"{svmem.percent}%"
    },
    "disk_info": {
        "total": f"{int(disk.total / (1024.0 ** 3))} GB",
        "used": f"{int(disk.used / (1024.0 ** 3))} GB",
        "free": f"{int(disk.free / (1024.0 ** 3))} GB",
    }
}

# All functions below do get every key and value from data object at the top and logs it to console.

def system_info(): # System Info
    system = data["system"]
    length = len(list(system.keys()))

    keys = list(system.keys())
    values = list(system.values())

    print("="*40, "System Information", "="*40)

    for i in range(length):
        print(f"{keys[i].capitalize()}: {values[i]}")


def boot_time(): # Boot Time
    time = data["boot_time"]
    length = len(list(time.keys()))

    keys = list(time.keys())
    values = list(time.values())

    print("="*40, "Boot Time", "="*40)

    for i in range(length):
        print(f"{keys[i].capitalize()}: {values[i]}")


def cpu_info(): # CPU Info
    cpu = data["cpu_info"]
    length = len(list(cpu.keys()))

    keys = list(cpu.keys())
    values = list(cpu.values())

    print("="*40, "CPU Info", "="*40)

    for i in range(length):
        print(f"{keys[i].capitalize()}: {values[i]}")


def memory_info(): # Memory Info
    memory = data["memory_info"]
    length = len(list(memory.keys()))

    keys = list(memory.keys())
    values = list(memory.values())

    print("="*40, "Memory Info", "="*40)

    for i in range(length):
        print(f"{keys[i].capitalize()}: {values[i]}")


def disk_info(): # Disk Info
    disk = data["disk_info"]
    length = len(list(disk.keys()))

    keys = list(disk.keys())
    values = list(disk.values())

    print("="*40, "Disk Info", "="*40)

    for i in range(length):
        print(f"{keys[i].capitalize()}: {values[i]}")


def print_all(): # Calling all the functions
    system_info()
    cpu_info()
    memory_info()
    disk_info()
    boot_time()


if __name__ == "__main__":
    print_all()

    save = input("Save the stats [y, n]: ")

    if save == "y":
        now = datetime.now()
        data["save_date"] = str(now) # Adding save date to data
        with open("./log.json","w") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print("Stats saved successfully. You can find the logs at logs.json")
    else:
        pass
