import sys
from selenium import webdriver

#Open browser
driver = webdriver.Firefox()
driver.get('https://www.fifa.com/worldcup/matches/match/300331518/#match-lineups')

#Extract lineups
