from pyairwatch.client import *
import random
import json
import csv

credentials = []
with open('creds-temp39.txt', 'rU') as datafile:
    for line in datafile:
        credentials.append(line.strip())

env = credentials[0]
token = credentials[1]
un = credentials[2]
pw = credentials[3]
serial = credentials[4]

a = AirWatchAPI(env, token, un, pw)


def main():
    # prand = 'apitest{}'.format(random.randint(1111,9999))
    # crand = 'cjr_api{}'.format(random.randint(1111,9999))
    # gcrand = 'gcjr_api{}'.format(random.randint(1111,9999))
    # a.groups.create_customer_og(prand)
    # a.groups.create_child_og(prand, crand)
    # a.groups.create_child_og(crand, gcrand)
    # di = a.devices.get_details_by_alt_id(serial)
    o = a.groups.get_id_from_groupid('jr')
    # a.smartgroups.get_id_from_og_id(g, 'apitest')
    # a.profiles.search(organizationgroupid=o)
    #
    # sgid = a.smartgroups.get_id_from_og_id(o, 'apitest')
    #
    # d = a.smartgroups.get_details(sgid)
    # print d
    #
    # print a.smartgroups.move_device_to_sg(sgid, di['Id']['Value'], di['DeviceFriendlyName'])
    #
    # print a.smartgroups.get_details(sgid)

    print a.tags.get_id_by_name('apitag', o)






if __name__ == '__main__':
    main()
