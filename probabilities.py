class probabilityDistribution:
    def __init__(self, hyperParameters, data):
        self.hypers = hyperParameters
        self.totalHypers = sum(hyperParameters)
        self.totalMeasures = 0
        self.paramCounts = [0 for i in range(100)]
        self.update(data)

    def probability(self, param):
        return (self.hypers[param] + self.paramCounts[param]) / (self.totalMeasures + self.totalHypers)

    def update(self, data):
        for val in data:
            self.paramCounts[val] += 1
        self.totalMeasures += len(data)
