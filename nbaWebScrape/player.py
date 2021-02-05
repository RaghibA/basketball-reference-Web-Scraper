# player.py
import requests
from bs4 import BeautifulSoup
import nbaWebScrape as n
import plot as p
# Player
class Player:
    def __init__(self, name): # INIT
        self.name = name

    # CAREER STAT SET METHODS
    def setPPG(self, c_ppg):
        self.c_ppg = c_ppg # points per game

    def setRPG(self, c_rpg):
        self.c_rpg = c_rpg # rebounds per game

    def setAPG(self, c_apg):
        self.c_apg = c_apg # assists per game

    def setFGP(self, c_fg):
        self.c_fg = c_fg   # field goal percentage 

    def setTPP(self, c_tpp):
        self.c_tpp = c_tpp # 3 point percentage

    def setFTP(self, c_ftp):
        self.c_ftp = c_ftp # Free throw percentage

    def setEFG(self, c_efg):
        self.c_eFG = c_efg # effective field goal percentage

    def setST(self, c_st):
        self.c_st = c_st # steals per game

    def setBK(self, c_bk):
        self.c_bk = c_bk # blocks per game

    def setTOV(self, c_tov):
        self.c_tov = c_tov # turnovers per game

    def setMPG(self, c_mpg):
        self.c_mpg = c_mpg # minutes per game

    def setGP(self, c_gp):
        self.c_gp = c_gp # games played

# CAREER STAT GET METHODS
    def getName(self): # player name
        return self.name

    def getPPG(self):
        return round(self.c_ppg, 2) # points per game

    def getRPG(self):
        return round(self.c_rpg, 2) # rebounds per game

    def getAPG(self):
        return round(self.c_apg, 2) # assists per game

    def getFGP(self):
        return round(self.c_fg, 2)   # field goal percentage 

    def getTPP(self):
        return round(self.c_tpp, 2) # 3 point percentage

    def getFTP(self):
        return round(self.c_ftp, 2) # Free throw percentage

    def getEFG(self):
        return round(self.c_eFG, 2) # effective field goal percentage

    def getST(self):
        return round(self.c_st, 2) # steals per game

    def getBK(self):
        return round(self.c_bk, 2) # blocks per game

    def getTOV(self):
        return round(self.c_tov, 2) # turnovers per game

    def getMPG(self):
        return round(self.c_mpg, 2) # minutes per game
    
    def getGP(self):
        return round(self.c_gp, 2) # games played

    def printStats(self):
        print('\n\nCareer Per Game Stats for {} [{} Games]'.format(self.name, self.c_gp))
        print('Points: {}'.format(self.c_ppg))
        print('Rebounds: {}'.format(self.c_rpg))
        print('Assists: {}'.format(self.c_apg))
        print('Field Goal %: {}%'.format(self.c_fg))
        print('Three Point %: {}%'.format(self.c_tpp))
        print('Free Throw %: {}%'.format(self.c_ftp))
        print('Effective FG %: {}%'.format(self.c_eFG))
        print('Steals: {}'.format(self.c_st))
        print('Blocks: {}'.format(self.c_bk))
        print('Turnovers: {}'.format(self.c_tov))
        print('Minutes: {}'.format(self.c_mpg))

def attrAssign(player, ppg, rpg, apg, fgp, tpp, ftp, efg, gp, st, bk, tov, mpg):
    # set attrb
    player.setPPG(float(ppg))
    player.setRPG(float(rpg))
    player.setAPG(float(apg))
    player.setFGP(float(fgp))
    player.setTPP(float(tpp))
    player.setFTP(float(ftp))
    player.setEFG(float(efg))
    player.setGP(int(gp))
    player.setST(float(st))
    player.setBK(float(bk))
    player.setTOV(float(tov))
    player.setMPG(float(mpg))

    return player

def stats(p):
    # splice html to get the stats_pullout div
    page = requests.get(p.url)
    soup = BeautifulSoup(page.content, 'html.parser') 

    # init player
    name = soup.find('h1', itemprop='name')
    name = name.find('span').getText() # name var for player object
    pl = Player(name)

    stats = soup.find('div', {'id': 'all_per_game'})
    stats = stats.find('div', {'id': 'div_per_game'}) # name var for player object
    stats = stats.find('tfoot')
    stats = stats.find('tr')

    # get career stats - need to convert from str - double/float
    ppg = stats.find('td', {'data-stat': 'pts_per_g'}).getText()
    rpg = stats.find('td', {'data-stat': 'trb_per_g'}).getText()
    apg = stats.find('td', {'data-stat': 'ast_per_g'}).getText()
    fgp = stats.find('td', {'data-stat': 'fg_pct'}).getText()
    tpp = stats.find('td', {'data-stat': 'fg3_pct'}).getText()
    ftp = stats.find('td', {'data-stat': 'ft_pct'}).getText()
    efg = stats.find('td', {'data-stat': 'efg_pct'}).getText()
    gp = stats.find('td', {'data-stat': 'g'}).getText()
    st = stats.find('td', {'data-stat': 'stl_per_g'}).getText()
    bk = stats.find('td', {'data-stat': 'blk_per_g'}).getText()
    tov = stats.find('td', {'data-stat': 'tov_per_g'}).getText()
    mpg = stats.find('td', {'data-stat': 'mp_per_g'}).getText()

    # set attrb
    pl = attrAssign(pl, ppg, rpg, apg, fgp, tpp, ftp, efg, gp, st, bk, tov, mpg)

    return pl

def comp(p1, p2):
    player1 = stats(p1)
    player2 = stats(p2)

    # print 
    player1.printStats()
    player2.printStats()

    #plot
    print("\nClose graph to continue...")
    p.plot(player1, player2)

