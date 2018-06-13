# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  theJSON = json.loads(data)
  #print(theJSON)
  
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])

  # output the number of events, the magnitude and each event name  
  count = theJSON["metadata"]["count"]
  print(str(count)+" events have occured in last two and half days.")

  # for each event, the place where it occurred
  for i in theJSON["features"]:
    print (i["properties"]["place"])
  print ("--------------\n")
  
  
def main():
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))

  if webUrl.getcode()==200:
    data = webUrl.read()
    #print(data)
    printResults(data)
  else:
    print("Error encountered... Cannot fetch data.")


if __name__ == "__main__":
  main()
