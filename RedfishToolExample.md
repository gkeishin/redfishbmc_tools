
Refer https://github.com/DMTF/Redfishtool  for more information and usage

*Install*
```
pip install redfishtool
```

*Tested on:*
```
$ python -V
Python 3.4.2
```

------------------------------------
*OpenBMC REST interface GET/PUT/POST/DELETE*
------------------------------------
* Enable REST logging*
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw PUT /xyz/openbmc_project/logging/rest_api_logs/attr/Enabled --data='{"data":true}'
{
    "data": null,
    "message": "200 OK",
    "status": "ok"
}
```

* GET REST logging Property*
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw GET /xyz/openbmc_project/logging/rest_api_logs/attr/Enabled
{
    "status": "ok",
    "data": true,
    "message": "200 OK"
}
```

* Host soft power off*
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw PUT /xyz/openbmc_project/state/host0/attr/RequestedHostTransition --data='{"data":"xyz.openbmc_project.State.Host.Transition.Off"}'
{
    "message": "200 OK",
    "status": "ok",
    "data": null
}
```

* Create dump * 
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw POST /xyz/openbmc_project/dump/action/CreateDump --data='{"data":[]}'
{
    "message": "200 OK",
    "data": 1,
    "status": "ok"
}
```

* GET dump*
```
$  redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw GET /xyz/openbmc_project/dump/entry/1
{
    "data": {
        "Elapsed": 1568210144,
        "Size": 198072
    },
    "status": "ok",
    "message": "200 OK"
}
```

* Delete DUMP*
```
$  redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw DELETE /xyz/openbmc_project/dump/entry/1
{
    "message": "200 OK",
    "data": null,
    "status": "ok"
}
```

----------------------------
*Redfish GET/PATCH/POST*
----------------------------

* GET Managers* 
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw GET /redfish/v1/Managers/
{
    "@odata.id": "/redfish/v1/Managers",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/bmc"
        }
    ],
    "@odata.context": "/redfish/v1/$metadata#ManagerCollection.ManagerCollection",
    "Members@odata.count": 1,
    "Name": "Manager Collection",
    "@odata.type": "#ManagerCollection.ManagerCollection"
}
```

```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always Managers list
{
    "_Path": "/redfish/v1/Managers",
    "Members": [
        {
            "UUID": "e1b3f31f-2c0e-4d2a-b873-12bba16b5d04",
            "Id": "bmc",
            "@odata.id": "/redfish/v1/Managers/bmc"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Manager Collection"
}
```

* Clear Event logs *
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw POST /redfish/v1/Systems/system/LogServices/EventLog/Actions/LogService.Reset --data='{"data":[]}'
```

* POST Host soft power off*
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw POST /redfish/v1/Systems/system/Actions/ComputerSystem.Reset --data='{"ResetType": "GracefulShutdown"}'
{
    "@Message.ExtendedInfo": [
        {
            "MessageId": "Base.1.4.0.Success",
            "Severity": "OK",
            "Message": "Successfully Completed Request",
            "@odata.type": "/redfish/v1/$metadata#Message.v1_0_0.Message",
            "MessageArgs": [],
            "Resolution": "None"
        }
    ]
}
```

* PATCH Apply time*
```
$ redfishtool -r xx.xx.xx.xx -u root -p 0penBmc -S Always raw PATCH /redfish/v1/UpdateService --data='{"ApplyTime":"OnReset"}'
{
    "Name": "Update Service",
    "@odata.type": "#UpdateService.v1_2_0.UpdateService",
    "@odata.id": "/redfish/v1/UpdateService",
    "FirmwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory"
    },
    "Id": "UpdateService",
    "HttpPushUri": "/redfish/v1/UpdateService",
    "@odata.context": "/redfish/v1/$metadata#UpdateService.UpdateService",
    "ServiceEnabled": true,
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "TransferProtocol@Redfish.AllowableValues": [
                "TFTP"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        }
    },
    "Description": "Service for Software Update"
}
```
