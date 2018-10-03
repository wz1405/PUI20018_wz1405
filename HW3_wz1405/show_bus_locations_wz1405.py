import os
import io
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import json
import pylab as pl
import sys
from pandas.io.json import json_normalize

puidata= os.getenv("PUIDATA")
if puidata is None:
    os.environ["PUIDATA"] = "%s/PUIdata"%os.getenv("HOME")
    
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

key = sys.argv[1]
route = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?&key=" + (key) + "&OperatorRef=MTA&VehicleMonitoringDetailLevel=calls&LineRef=MTA%20NYCT_" + (route) 
response = urllib.urlopen(url)
a = pd.read_json(url)
data = response.read().decode("utf-8")
parsed_data = json.loads(data)

print ("Bus Line : %s" % (parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]
      ["VehicleActivity"][0]["MonitoredVehicleJourney"]["PublishedLineName"]))
      
BusNumbers = (parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]
      ["VehicleActivity"])
print ("Number of Active Buses : %d" % len (BusNumbers))

BusNum = len (BusNumbers)

for i in range(BusNum):
    B = parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    C = parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    print ("Bus %s" % i + " is at Latitude %s" % B + " Longitude %s" % C )