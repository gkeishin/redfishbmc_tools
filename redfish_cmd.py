#!/usr/bin/env python

r"""
Command line tool to process redfish related operations.
"""

import argparse
import os
import pprint
import json

import redfish_connect
import redfish_resource_model_crawler

parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTIONS]',
    description='Process cronus commands.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prefix_chars='-+')

parser.add_argument(
    '--target_ip',
    '-ip',
    help='BMC target IP.'
)

parser.add_argument(
    '--username',
    '-u',
    default='root',
    help='BMC target user name.'
)

parser.add_argument(
    '--password',
    '-p',
    default='0penBmc',
    help='BMC target password.'
)

parser.add_argument(
    '--request',
    '-r',
    help='GET, PUT, POST, PATCH, DELETE.'
)

parser.add_argument(
    '--url',
    '-u',
    help=''
)

args = parser.parse_args()


def main():
    r"""
    Command line tool entry point main() function.
    """

    redfish.login(args.target_ip,
                       args.username,
                       args.password,
                       args.system_type)

