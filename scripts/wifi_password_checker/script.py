import subprocess
import os
import platform

pswd_txt = open(f"{os.getlogin()}-{platform.node()}", "w")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split(
    '\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

pswd_txt.write(f'{"{:<30}|  {:<}".format("WIFI", "Password")} \n')
pswd_txt.write(f'{"-" * 50} \n')

print("{:<30}|  {:<}".format('WIFI', 'Password'))
print("-" * 50)

for i in profiles:
    try:

        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8',
                                                                                                       errors="backslashreplace").split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:

            pswd_txt.write(f'{"{:<30}|  {:<}".format(i, results[0])} \n')
            pswd_txt.write(f'{"-" * 50} \n')

            print("{:<30}|  {:<}".format(i, results[0]))
            print("-" * 50)


        except IndexError:

            pswd_txt.write(f'{"{:<30}|  {:<}".format(i, "")} \n')
            pswd_txt.write(f'{"-" * 50} \n')
            print("{:<30}|  {:<}".format(i, ""))
            print("-" * 50)


    except subprocess.CalledProcessError:

        pswd_txt.write(f'{"{:<30}|  {:<}".format(i, "ENCODING ERROR")} \n')
        pswd_txt.write(f'{"-" * 50} \n')
        print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
        print("-" * 50)

pswd_txt.close() 