import urllib.request
import json
import re

# Get IP


def getPublicIP():
    data = str(urllib.request.urlopen('52.6.132.144').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)


IP = ("52.6.132.144")

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urllib.request.urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']

# Print Extracted Details
print("Your Region : " + region)
print("Your Country : " + country)
print("Your City : " + city)
print("Your Location : " + location)
