# nbaWebScrape.py
#! I DO NOT OWN ANY OF THE DATA USED IN THIS PROGRAM & THE PROGRAM IS NOT USED FOR PROFIT
#! source: basketball-reference.com

# NBA WEBSCRAPE
# Scrapes Basketball-reference.com to compare the careers of two nba players.
# The data from basketball-reference.com is used visualize the stats of the players
import requests
from bs4 import BeautifulSoup
import player 

searchURL = "https://www.basketball-reference.com/search/search.fcgi?search="

class q_player:
    # INIT PLAYER QUERY
    def __init__(self, name, url):
        self.name = name
        self.url = url
    # Getter fucntion for player name
    def getName(self):
        return self.name
    # page url for player
    def getUrl(self):
        return self.url

# process the query 
def query():
    # create list of up to 10 players 
    p = []
    # take user input for players & create request
    qInput = input('\nPlayer Name: ')
    print()

    if qInput == '.exit':
        quit()

    page = requests.get(searchURL + qInput)

    # parse html w/ BS4
    soup = BeautifulSoup(page.content, 'html.parser') 
    if soup.find('h1', itemprop='name'):
        x = soup.find('h1', itemprop='name')
        name = x.find('span').getText()
        cn = soup.find('link', rel='canonical')
        url = cn['href']
        temp_p = q_player(name, url)
        p.append(temp_p)
        return p
    else:
        # no matching player
        if not soup.find(id='players'):
            print('No results')
            main()
        else: # players found
            qParse = soup.find(id='players')
            qParse = qParse.find_all(class_='search-item-name')

            # store first 10 results in a list of query player objects
            if len(qParse) < 10:
                for x in range(len(qParse)):
                    st_h = qParse[x].find('a', href=True)

                    # get player data
                    url = 'https://www.basketball-reference.com' + st_h['href']
                    name = st_h.getText()
                    temp_p = q_player(name,url)
                    p.append(temp_p)
                return p
            else:
                for x in range(10):
                    st_h = qParse[x].find('a', href=True)

                    # get player data
                    url = 'https://www.basketball-reference.com' + st_h['href']
                    name = st_h.getText()
                    temp_p = q_player(name,url)
                    p.append(temp_p)
                return p
    
def main():
    print('\n\n[BasketBall-Reference Web Scraper]\nSelect 2 Players to compare.\n[.exit to quit]')

    while(1):
        q_pl = []
        q_pl = query()

        # select player 1
        if q_pl != None:
            print('\n\nResults:\n')
            for i in range(len(q_pl)):
                print(str(i+1) + ': ' + q_pl[i].name)
            x = None
            while not x in range(len(q_pl) + 1):
                x = input('\nSelect Player 1: ')
                x = int(x) - 1

            print(q_pl[x].name)
            p1 = q_pl[x]
        
        # clear list and re query
        q_pl.clear()
        q_pl = []
        q_pl = query()

        # select player 2
        if q_pl != None:
            print('\n\nResults:\n')
            for i in range(len(q_pl)):
                print(str(i+1) + ': ' + q_pl[i].name)
            j = None
            while j == None or not j in range(len(q_pl) + 1):
                j = input('\nSelect Player 2: ')
                j = int(j) - 1

            print(q_pl[j].name)
            p2 = q_pl[j]

        # compare stats
        print('\n' + p1.name + ' vs. ' + p2.name)
        player.comp(p1,p2)
    

if __name__ == "__main__":
    main()