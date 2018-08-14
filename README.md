# redfishbmc_tools
A redfish tools for performing operation using redfish API from DMTF

Refer for more on DMTF: https://github.com/DMTF/python-redfish-library
   ```
   $ pip install redfish
   ```

# Usage: #

* Command line support: 

```
usage: redfish_cmd.py [OPTIONS]

Process redfish request.

optional arguments:
  -h, --help            show this help message and exit
  --target_ip TARGET_IP
                        BMC target IP. (default: None)
  --username USERNAME   BMC target user name. (default: root)
  --password PASSWORD   BMC target password. (default: 0penBmc)
  --request REQUEST     GET, PUT, POST, PATCH, DELETE. (default: GET)
  --url URL             URL path /redfish/v1/<meta-data> (default: None)
  --op OP               list, enumerate RESTful like (default: None)
```

* For root: /redfish/v1/

```
    $ python redfish_cmd.py --target_ip xx.xx.xx.xx --request GET --url ""
    IP: xx.xx.xx.xx
    {
        "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot", 
        "@odata.id": "/redfish/v1/", 
        "@odata.type": "#ServiceRoot.v1_1_1.ServiceRoot", 
        "AccountService": {
        "@odata.id": "/redfish/v1/AccountService"
        }, 
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        }, 
        "Id": "RootService", 
        "Links": {
            "Sessions": {
               "@odata.id": "/redfish/v1/SessionService/Sessions"
            }
        }, 
        "Managers": {
        "@odata.id": "/redfish/v1/Managers"
        }, 
        "Name": "Root Service", 
        "RedfishVersion": "1.1.0", 
        "SessionService": {
        "@odata.id": "/redfish/v1/SessionService/"
        }, 
        "Systems": {
            "@odata.id": "/redfish/v1/Systems"
        }, 
        "UUID": "00000000-0000-0000-0000-000000000000", 
        "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
       }
    }
```

* For other resource say "Systems"

```
    $ python redfish_cmd.py --target_ip xx.xx.xx.xx --request GET --url "Systems"
    IP: xx.xx.xx.xx
    {
        "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection", 
        "@odata.id": "/redfish/v1/Systems", 
        "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection", 
        "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/motherboard"
        }
        ], 
        "Members@odata.count": 1, 
        "Name": "Computer System Collection"
    }
```

* For resource listing

```
    $ python redfish_cmd.py --target_ip xx.xx.xx.xx --url "" --op list
    IP: xx.xx.xx.xx

    /redfish/v1/list

    /redfish/v1/Managers
    /redfish/v1/Links
    /redfish/v1/AccountService
    /redfish/v1/UpdateService
    /redfish/v1/Chassis
    /redfish/v1/Systems
    /redfish/v1/SessionService

```
