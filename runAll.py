import os

for i in range(1,8):
    os.system("python game.py --game "+str(i)+" --onlyStatistics")