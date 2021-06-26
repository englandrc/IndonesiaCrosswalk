# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:55:27 2021

@author: englandrc
"""
"""
Edit the parselist, level, and output file to be the relevant one
# Going through province list as parent gives districts
# Going through district list as parent gives subdistrict
# Going through subdistrict list as parent gives villages
"""
import wget
import requests
import json
import pandas as pd
import time

root = '~/IndonesiaCrosswalk/'
prov = pd.read_csv(root+'parentcode/provid.csv', names=['list'], header=0)
kab = pd.read_csv(root+'parentcode/kabid.csv', names=['list'], header=0)
kec = pd.read_csv(root+'parentcode/kecid.csv', names=['list'], header=0)
def main():
    parselist = prov.copy()
    level = 'kabupaten'
    total = str(len(parselist))
    for i in range(0,len(parselist)):
        index = str(i + 1)
    
        item = str(parselist.list[i])
        print('Doing Item '+item+', Number '+index+' of '+total)
        
        address = 'https://sig.bps.go.id/rest-bridging/getwilayah?level=' + level + '&parent=' + item
        
        try:
            req = requests.get(address,timeout=100, verify=False)
        except:
            time.sleep(60)
            req = requests.get(address,timeout=100, verify=False)
            
        df = pd.read_json(req.content)
        
        rcode = str(req)
        rcode = int(''.join(filter(str.isdigit, rcode)))
        rcode = str(rcode)
        
        if i == 0:
            df.to_csv (root+'crosswalk_'+level+'.csv', index = None)
        else:
            df.to_csv(root+'crosswalk_'+level+'.csv', mode='a', header=False, index=None)
        print('Return Code: '+rcode)
        
main()