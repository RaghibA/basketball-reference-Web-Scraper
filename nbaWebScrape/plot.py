# plot.py
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import nbaWebScrape as n
import player as p

labels = ['PPG', 'TRB', 'APG', 'FG%', '3P%', 'FT%', 'EFG%', 'ST', 'BK', 'TO', 'MP']

def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
def plot(p1,p2):
    player1 = [p1.getPPG(), p1.getRPG(), p1.getAPG(), p1.getFGP() * 100, p1.getTPP() * 100, p1.getFTP() * 100, p1.getEFG() * 100, p1.getST(), p1.getBK(), p1.getTOV(), p1.getMPG()]
    player2 = [p2.getPPG(), p2.getRPG(), p2.getAPG(), p2.getFGP() * 100, p2.getTPP() * 100, p2.getFTP() * 100, p2.getEFG() * 100, p2.getST(), p2.getBK(), p2.getTOV(), p2.getMPG()]

    #labels
    l = np.arange(len(labels))
    w = .5

    fig, ax = plt.subplots()
    rects1 = ax.bar(l - w/2, player1, w, label=p1.getName())
    rects2 = ax.bar(l + w/2, player2, w, label=p2.getName())

    # Graph Labels
    ax.set_ylabel('Value')
    ax.set_title(p1.getName() + ' vs. ' + p2.getName())
    ax.set_xticks(l)
    ax.set_xticklabels(labels)
    ax.legend()
    autolabel(rects1, ax)
    autolabel(rects2, ax)
    fig.tight_layout()
    plt.show()
