#!/usr/bin/env python

r"""
Command line tool to process redfish related operations.
"""

import argparse
from redfish_connect import *
from redfish_resource_model_crawler import *

parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTIONS]',
    description='Process redfish request.',
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
    help='GET, PUT, POST, PATCH, DELETE.'
)

parser.add_argument(
    '--url',
    help='URL path /redfish/v1/<meta-data>'
)

parser.add_argument(
    '--op',
    help='list, enumerate RESTful like'
)

args = parser.parse_args()


def main():
    r"""
    Command line tool entry point main() function.
    """
    print ("IP: %s" % (args.target_ip))

    con = redfish_connect(args.target_ip, args.username, args.password)

    if args.request == "GET":
        resp = con.get_method(args.url)
        print json.dumps(resp, sort_keys=True, indent=4)

    if args.op=="list":
        list_path = '/redfish/v1/' + args.url + '/list'
        print("\n%s\n" % list_path)
        resp = con.get_method(args.url)
        list_resp = get_url_list(resp)
        print('\n'.join(map(str, list_resp)))

    if args.op=="enumerate":
        list_path = '/redfish/v1/' + args.url + '/enumerate'
        print("\n%s\n" % list_path)
        resp = con.get_method(args.url)
        list_resp = get_url_list(resp)
        for enum in list_resp:
            print("\n%s" % enum)
            try:
                resp = con.get_method(enum.replace("/redfish/v1/",""))
                print json.dumps(resp, sort_keys=True, indent=4)
            except:
                # pass and continue with next resource.
                continue

# Main
if not main():
    exit(1)
