#
# retrieving data from the internet
#

import urllib.request

def main():
  #webdata = urllib.request.urlopen("http://nevosial.me")
  webdata = urllib.request.urlopen("https://www.sofascore.com/morocco-portugal/eUbsDVb")
  print("Status code "+str(webdata.getcode()))

  contents = webdata.read()
  #print(contents)

if __name__ == "__main__":
  main()
