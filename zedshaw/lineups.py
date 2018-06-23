#Get the formation from lineups

import urllib.request
import json

def gethomeFormation(data):
    pJSON = json.loads(data)

    if "formation" in pJSON["homeTeam"]:
        #print(pJSON["homeTeam"]["formation"])
        hFormation = pJSON["homeTeam"]["formation"]
        #print(hFormation)
        print("-".join(hFormation))
    else:
        print("Error")

    if "formation" in pJSON["awayTeam"]:
        #print(pJSON["homeTeam"]["formation"])
        aFormation = pJSON["awayTeam"]["formation"]
        #print(hFormation)
        print("-".join(aFormation))
    else:
        print("Error")



def main():
    urlData = "https://www.sofascore.com/event/7551827/lineups/json"
    webUrl = urllib.request.urlopen(urlData)
    #print("result code: "+str(webUrl.getcode()))

    if webUrl.getcode()==200:
        data = webUrl.read()
        #print(data)
        gethomeFormation(data)
    else:
        print("Error... Cannot fetch data!")

if __name__ == "__main__":
  main()
