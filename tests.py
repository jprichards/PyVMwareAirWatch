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

def post_create_og_test(parentgrpid, newgroupid):
    ogid = get_og_id_test(parentgrpid)
    ogdata = {'GroupId': '%s' % str(newgroupid),
              'LocationGroupType': '%s' % 'Container',
              'Name': '%s' % str(newgroupid)}
    response = a.groups.create(parent_id=ogid, ogdata=json.dumps(ogdata))
    print response
    # og_id = response.get('Value')
    # print 'OG ID for {}: {}'.format(ogdata.get('GroupId'), og_id)
    # return og_id

def get_sg_id_test(og_id, sg):
    params = {'managedbyorganizationgroupid': str(og_id),
              'orderby': 'smartgroupid'}
    r = a.get('mdm', '/smartgroups/search?', params=params)
    for keys in r['SmartGroups']:
        if keys['Name'] == sg:
            sg_id = keys.get('SmartGroupID')
            print 'SG ID for {}: {}'.format(sg, keys.get('SmartGroupID'))
            return sg_id

def get_device_id_from_serial_test(serial):
    """TODO"""

def move_device_to_sg_test(serial, sgid):
    """TODO"""
    # C02H3SE7DJWT
    deviceid = get_device_id_from_serial_test(serial)
    move = {'DeviceAdditions':[{ 'Id':'{}'.format(deviceid)}]}
    response = a.put('mdm', '/smartgroups/{}'.format(sgid), data=move)
    print response

def main():
    rand = random.randint(1111,9999)
    # postogid = post_create_og_test('jr', 'apitest{}'.format(rand))
    # sg_id = get_sg_id_test(getogid, 'apitest')
    # move_device_to_sg_test('C02H3SE7DJWT', sg_id)
    g = a.groups.get_id_from_groupid('jr')
    print 'new test: {}'.format(g)

    #print postogid

if __name__ == '__main__':
    main()
