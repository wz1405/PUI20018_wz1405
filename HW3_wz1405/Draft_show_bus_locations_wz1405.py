
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
  
%pylab inline
pl.rc('font', size=15)

url = " " + ` "New York&APPID=" + os.getenv("OPENWEATHERKEY")
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data.keys()

urllib2.urlopen('actual_url')

http://bustime.mta.info/api/siri/vehicle-monitoring.json 里面内容：
{"Siri":{"ServiceDelivery":{"ResponseTimestamp":"2018-09-21T16:33:07.060-04:00","VehicleMonitoringDelivery":[{"ResponseTimestamp":"2018-09-21T16:33:07.060-04:00","ErrorCondition":{"OtherError":{"ErrorText":"API key required."},"Description":"API key required."}}]}}}

python show_bus_locations.py 7f84d332-2f33-49c1-94f5-fdc4cf2231ae B52

url = "https://data.cityofnewyork.us/resource/wece-v9d7.json"

#use the appropriatepandas function to read in the json file
df = pd.read_json(url)

# print it out
df.head(3)

#For example, using your key, you can retrieve all vehicle information for a bus line, e.g. B52, by accessing the following URL http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52 after replacing YOUR_KEY in the URL string with your own API key.

import urllib2
import json
api = .....
url = '...'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
print data

for item in data['objects']:
    print item['name']
    print item['locality']
    

['{}']
