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

a = AirWatchAPI(env, token, un, pw)

def move_device_to_sg_test(serial, sgid):
    """TODO"""
    # C02H3SE7DJWT
    deviceid = get_device_id_from_serial_test(serial)
    move = {'DeviceAdditions':[{ 'Id':'{}'.format(deviceid)}]}
    response = a.put('mdm', '/smartgroups/{}'.format(sgid), data=move)
    print response

def main():
    # prand = 'apitest{}'.format(random.randint(1111,9999))
    # crand = 'cjr_api{}'.format(random.randint(1111,9999))
    # gcrand = 'gcjr_api{}'.format(random.randint(1111,9999))
    # g = a.groups.get_id_from_groupid('jr')
    # sg_id = a.smartgroups.get_id_from_og_id(g, 'apitest')
    # n = a.groups.create_customer_og(prand)
    # c = a.groups.create_child_og(prand, crand)
    # gc = a.groups.create_child_og(crand, gcrand)
    # print g
    # print n
    # print c
    # print gc
    # print sg_id

    d = a.devices.get_id_by_alt_id('C02H3SE7DJWT')
    print d

    # move_device_to_sg_test('C02H3SE7DJWT', sg_id)

if __name__ == '__main__':
    main()
