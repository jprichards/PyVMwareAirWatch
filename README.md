PyVMwareAirWatch
=========

PyVMwareAirWatch is a Python API library for [VMware AirWatch](https://www.air-watch.com/)

Usage:
```
from pyairwatch.client import AirWatchAPI

a = AirWatchAPI(env='your_environment_url',
                apikey='your_api_token_key',
                username='username',
                password='password')


# Get the OG ID for a specified Group ID
a.groups.get_id_from_groupid(groupid='testog')

# Create a Child OG for a specified Parent OG Group ID (Type/Name optional)
a.groups.create_child_og(parent_groupid='testog', groupid='newog', og_type='Container', name='newog')

# Get the Smart Group ID for a specified OG ID and Smart Group Name
a.smartgroups.get_id_from_og_id(og_id=7, sg_name='apitest')

# Get a Device ID via an alternate device identifier
a.devices.get_id_by_alt_id(serialnumber='C09Z1TC8FJWT')
```

Supported Functionality
---
* Devices
  * Get Device Details by Alt ID (Macaddress, Udid, Serialnumber, ImeiNumber, EasId)
  * Get Device ID by Alt ID (Macaddress, Udid, Serialnumber, ImeiNumber, EasId)
* Groups
  * Get OG ID from Group ID
  * Create Customer type OG (On-Prem only)
  * Create Child OG
* Smart Groups
  * Get SG ID by Name and OG ID


Requirements
---
* [requests](http://docs.python-requests.org/en/latest/)
