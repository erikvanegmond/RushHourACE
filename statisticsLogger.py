
class StatisticsLogger(object):

    statisticsFile = None

    """docstring for StatisticsLogger"""
    def __init__(self, game, alg, statistics):
        fname = "statisticsGame%s-%s.csv" %(str(game), str(alg))
        self.statisticsFile = open(fname, 'w')
        self.statisticsFile.write(",".join(statistics)+"\n")


    def log(self, statistics):
        statistics = map(str, statistics)
        self.statisticsFile.write(",".join(statistics)+"\n")
