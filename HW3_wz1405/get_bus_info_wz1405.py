import os
import csv
import io
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import json
from pandas.io.json import json_normalize
import sys

puidata= os.getenv("PUIDATA")
if puidata is None:
    os.environ["PUIDATA"] = "%s/PUIdata"%os.getenv("HOME")
    
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

    
ApiKey = sys.argv[1]
Route = sys.argv[2]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?&key=" + (ApiKey) + "&OperatorRef=MTA&VehicleMonitoringDetailLevel=calls&LineRef=MTA%20NYCT_" + (Route) 
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

with open(sys.argv[2]+'.csv', "w", newline='') as outputWriter:
        outputFile = open(sys.argv[2]+'.csv', "w", newline='')
        outputWriter = csv.writer(outputFile) 
        outputWriter.writerow(['Latitude', 'Longitude', 'Stop Name' ,'Stop Status'])
with open(sys.argv[2]+'.csv', "w", newline='') as outputWriter:
    for i in range(BusNum):
        B = str(parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])
        C = str(parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
       
        try: 
            D = parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
        except LookupError: 
            D = "N/A"
        try:         
            E = parsed_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
        except LookupError: 
            E = "N/A"
        #G =  (B + ", %s" % C + ", %s" % D + ", %s" % E)
        G =  [B , " %s" % C , " %s" % D , " %s" % E]
        outputFile = open(sys.argv[2]+'.csv', "a", newline='')
        outputWriter = csv.writer(outputFile) 
        outputWriter.writerows([G])
        outputFile.close()
    