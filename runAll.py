import os

for i in range(-5,8):
    if i:
        try:
            os.system("python game.py --game "+str(i)+" --alg astar --gatherStatistics")
        except:
            print "some error!!! game: "+str(i)