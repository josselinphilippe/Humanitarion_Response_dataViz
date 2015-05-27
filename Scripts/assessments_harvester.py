#import necessary modules
import urllib, json

#define source data URL, open it, and read it
url = "http://www.humanitarianresponse.info/api/v1.0/assessments"
response = urllib.urlopen(url);
data = json.loads(response.read())

#print out 
print data

##next step: parse through response and feed to CartoDB table
