from pyairwatch.client import *
import random
import json
import csv

credentials = []
with open('creds.txt', 'rU') as datafile:
    for line in datafile:
        credentials.append(line.strip())

env = credentials[0]
token = credentials[1]
un = credentials[2]
pw = credentials[3]

a = AirWatchAPI(env, token, un, pw)

def get_og_id_test():
    params = {'groupid':'jr'}
    response = a.get('system', '/groups/search', params=params)
    og_id = json.loads(response.text)['LocationGroups'][0]['Id']['Value']
    print 'OG ID for {}: {}'.format(params.get('groupid'), og_id)
    return og_id

def post_create_og_test():
    ogid = get_og_id_test()
    rand = random.randint(1111,9999)
    ogdata = {'GroupId': '%s' % 'apitest{}'.format(rand),
              'LocationGroupType': '%s' % 'Container',
              'Name': '%s' % 'apitest{}'.format(rand)}
    response = a.post('system', 'groups/{}'.format(ogid), data=json.dumps(ogdata), header={'Content-Type': 'application/json'})
    og_id = json.loads(response.text).get('Value')
    print 'OG ID for {}: {}'.format(ogdata.get('GroupId'), og_id)
    return ogid

def main():
    post_create_og_test()

if __name__ == '__main__':
    main()
