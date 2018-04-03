PyVMwareAirWatch
=========

PyVMwareAirWatch is a Python API library for [VMware AirWatch](https://www.air-watch.com/) 9.1+

Usage:
```
from pyairwatch.client import AirWatchAPI

a = AirWatchAPI(env='your_environment_url',
                apikey='your_api_token_key',
                username='username',
                password='password')


# Get a Device ID via an alternate device identifier
a.devices.get_id_by_alt_id(serialnumber='C09Z1TC8FJWT')

# Get the OG ID for a specified Group ID
a.groups.get_id_from_groupid(groupid='testog')

# Get the User ID for a specified Username
a.users.get_id_from_username('jdoe')
```

Supported Functionality
---
* Devices
  * Get Device Details by Alt ID (Macaddress, Udid, Serialnumber, ImeiNumber, EasId)
  * Get Device ID by Alt ID (Macaddress, Udid, Serialnumber, ImeiNumber, EasId)
* Users
  * Search for users by Username, Firstname, Lastname, Email,
  OrganizationGroupID, or Role
  * Get User ID from Username
* Groups
  * Get OG ID from Group ID
  * Create Customer type OG (On-Prem only)
  * Create Child OG
* Smart Groups
  * Get SG ID by Name and OG ID
  * Get SG Details by ID
* Admins
  * Search for admins by Username, Firstname, Lastname, Email,
  OrganizationGroupID, or Role
  * Get Admin User ID from Username
* Tags
  * Get Tag ID by Name and OG ID

Requirements
---
* [requests](http://docs.python-requests.org/en/latest/)
