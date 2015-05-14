import os
import statisticsLogger as sl

games = range(-5,8)

for i in games:
    if i:
        try:
            os.system("python game.py --game "+str(i)+" --alg astar --gatherStatistics")
        except:
            print "some error!!! game: "+str(i)

for i in games:
    if i:
        try:
            os.system("python game.py --game "+str(i)+" --alg breadthfirst --gatherStatistics")
        except:
            print "some error!!! game: "+str(i)

for i in games:
    if i:
        stats = sl.StatisticsLogger(str(i), "random", ["time","path lenght"])
        for numRuns in range(0,1000):
            try:
                os.system("python game.py --game "+str(i)+" --alg random --gatherStatistics --storePath")
            except KeyboardInterrupt:
                print "exit"
                exit()
            except:
                print "some error!!! game: "+str(i)