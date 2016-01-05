
class StatisticsLogger(object):

    statisticsFile = None

    """docstring for StatisticsLogger"""
    def __init__(self, game, alg, statistics):
        fname = "statisticsGame%s-%s.csv" %(str(game), str(alg))
        self.statisticsFile = open(fname, 'w')
        for element in statistics:
            self.statisticsFile.write(element+";")
        self.statisticsFile.write("\n")


    def log(self, statistics):
        statistics = map(str, statistics)
        for element in statistics:
            self.statisticsFile.write(element+";")
        self.statisticsFile.write("\n")

