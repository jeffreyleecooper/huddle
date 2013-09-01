#!/usr/bin/python

import csv
import json

def ClientTaskFeeder():
    f=csv.DictReader(open('Asana_TSM_2013-08-13_10.49.csv','r'))
    
    clients={}
    for each in f:
        if each['Status']=='Not Complete' and each['Task'] != '':
            if each['Company'] not in clients:
                clients[each['Company']]={}
            if each['Project'] not in clients[each['Company']]:
                clients[each['Company']][each['Project']]=[]                
            clients[each['Company']][each['Project']].append(each)
    return json.dumps(clients, sort_keys=True)

def ShipmateTaskFeeder():
    f=csv.DictReader(open('Asana_TSM_2013-08-13_10.49.csv','r'))
    
    staff={}
    for each in f:
        if each['Status']=='Not Complete' and each['Task'] != '':
            if each['Task Owner'] not in staff:
                staff[each['Task Owner']]={}
            if each['Project'] not in staff[each['Task Owner']]:
                staff[each['Task Owner']][each['Project']]=[]                
            staff[each['Task Owner']][each['Project']].append(each)
    return json.dumps(staff, sort_keys=True)


def main():
    
    print ClientTaskFeeder()
    print ShipmateTaskFeeder()

if __name__=='__main__':main()