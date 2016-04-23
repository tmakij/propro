from data import tableAt, loadData
from sys import stdin
from probabilities import probabilityDistribution

class probabilityOutput:
    def __init__(self):
        startData = tableAt(0)
        hyperParams = [1 for x in range(100)]
        self.distribution = probabilityDistribution(hyperParams, startData)

    def readRadioData(self, radio):
        radioData = tableAt(radio)
        self.distribution.update(radioData)

    def printProbabilities(self):
        res = str(self.distribution.probability(0))
        for i in range(1, 100):
            prob = self.distribution.probability(i)
            res += ','
            res += str(prob)
        print(res)

def main():
    out = probabilityOutput()
    out.readRadioData(0)
    out.printProbabilities()
    for i in range(1, 303):
        radio = int(stdin.readline())
        out.readRadioData(radio)
        out.printProbabilities()
        
loadData()
main()
