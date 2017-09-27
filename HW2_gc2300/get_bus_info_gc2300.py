from __future__ import print_function
import pylab as pl
import os
import json
import sys
import pandas as pd
import numpy as np
pl.rc('font', size=15)

mtakey = sys.argv[1]
bus = sys.argv[2]
filename = sys.argv[3]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
        mtakey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

buses= data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
buscsv = []
print ("Latitude,Longitude,Stop Name,Stop Status")
for i in range(len(buses)):
        lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        if buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'] == {}:
            stopname= "N/A"
            stopstatus = "N/A"
        else:    
            stopname = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            stopstatus = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        print("%s,%s,%s,%s" %(lat,lon,stopname,stopstatus))
        buscsv.append((lat,lon,stopname,stopstatus))

        
buscsv = pd.DataFrame(buscsv, columns = ('Latitude', 'Longitude', 'Stop Name', 'Stop Status'))
buscsv.to_csv(filename,index = False)
