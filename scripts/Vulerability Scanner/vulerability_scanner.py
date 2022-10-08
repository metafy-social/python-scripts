#!/usr/bin/env python3
"""A simple vulnerability scanner script.
   Uses Python 3"""

import argparse
import scanner


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-t', '--target', dest='target', help='Target URL.')

    (options, arguments) = parser.parse_args()

    return options


options = get_arguments()

target_url = options.target
links_to_ignore = [target_url]

data_dict = {'username': 'admin', 'password': 'password', 'Login': 'submit'}

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post(target_url, data=data_dict)

# vuln_scanner.crawl()
vuln_scanner.crawl()
vuln_scanner.run_scanner()
