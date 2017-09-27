from __future__ import print_function
import pylab as pl
import os
import json
import sys
import numpy as np
pl.rc('font', size=15)

mtakey = sys.argv[1]
bus = sys.argv[2]
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
numbus=np.size(buses)
print ("Bus Line : %s"%(bus))
print ("Number of Active Buses : %d" %(numbus))
for i in range(len(buses)):
        lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print("Bus %s is at latitude %s and longtitude %s" %(i,lat,lon))
