#
# retrieving data from the internet
#

import urllib.request
from selenium import webdriver
import requests
import json

url = 'http://nevosial.me'
driver = webdriver.Firefox()

def main():
  webdata = urllib.request.urlopen("http://nevosial.me")
  print("Status code "+str(webdata.getcode()))

  contents = webdata.read()
  print(contents)


if __name__ == "__main__":
  main()
