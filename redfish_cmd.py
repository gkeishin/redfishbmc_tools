#!/usr/bin/env python

r"""
Command line tool to process redfish related operations.
"""

import argparse
import redfish_connect as redcon
import redfish_resource_model_crawler

parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTIONS]',
    description='Process cronus commands.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prefix_chars='-+')

parser.add_argument(
    '--target_ip',
    help='BMC target IP.'
)

parser.add_argument(
    '--username',
    default='root',
    help='BMC target user name.'
)

parser.add_argument(
    '--password',
    default='0penBmc',
    help='BMC target password.'
)

parser.add_argument(
    '--request',
    default='GET',
    help='GET, PUT, POST, PATCH, DELETE.'
)

parser.add_argument(
    '--url',
    help='URL path /redfish/v1/<meta-data>'
)

args = parser.parse_args()


def main():
    r"""
    Command line tool entry point main() function.
    """
    print ("IP: %s" % (args.target_ip))

    con = redcon.redfish_connect(args.target_ip, args.username, args.password)

    if args.request == "GET":
        con.get_method(args.url)


# Main
if not main():
    exit(1)

