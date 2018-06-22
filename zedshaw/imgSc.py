from bs4 import BeautifulSoup
import requests

resp = requests.get('https://www.fifa.com/worldcup/matches/match/300331518/#match-lineups')

soup = BeautifulSoup(resp.text, 'lxml')
links = soup.select('a')
print(links)
