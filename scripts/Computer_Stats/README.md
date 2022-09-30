## Computer Stats Checker

It is a python program that shows about user's computer stats. Such as cpu, memory, disk, ip_adress etc.

The response of the program is in json fromat and if say yes it will be automatically saved to log.js so it is easier to reach those stats in the future.

### Modules Used

- psutil==5.8.0

### How to Use

* Clone the repo
* Make sure you are at the same folder as the main file in. (1)
* run `python main.py`
* Congrats!!


(1) = if not program creates new file named log.js instead of the one we want it to save to


#### Example Output

./daily-python-scripts/scripts/Computer_Stats/main.py

======================================== System Information ========================================
System: Windows
Nodes:
Release:
Version:
Machine:
Processor:
Ip adress:
Mac adress:
Ram:
======================================== CPU Info ========================================
Physical cores:
Total cores:
Max frequency:
Min frequency:
Current frequency:
Total cpu usage:
======================================== Memory Info ========================================
Total:
Available:
Used:
Percentage:
======================================== Disk Info ========================================
Total:
Used:
Free:
======================================== Boot Time ========================================
Time: 2022/9/24 8:35:45
Save the stats [y, n]: y
Stats saved successfully. You can find the logs at logs.json
