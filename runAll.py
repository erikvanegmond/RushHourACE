import os

for i in range(1,8):
    os.system("game.py --game "+str(i)+" --onlyStatistics")