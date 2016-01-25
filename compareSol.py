import json
import sys
import collections

"""
to compare solutions 
"""

class KeyValueOrganise:
  def __init__(self,data):
    self.aggregateDict = {}
    self.data = data

  def organise(self):
      for line in self.data:
        record = json.loads(line,encoding='latin-1') #assume each line is a key value pair
        # record[1].sort() #if need to sort list when value is list
        self.aggregateDict[record[0]] = record[1]


  def sortDict(self):
    self.organise()
    od = collections.OrderedDict(sorted(self.aggregateDict.items()))
    self.aggregateDict = od


        
# =============================
if __name__ == '__main__':
  solData= open(sys.argv[1])
  sol= KeyValueOrganise(solData)
  sol.sortDict()

  myData = open(sys.argv[2])
  mySol = KeyValueOrganise(myData)
  mySol.sortDict()

  solDict = sol.aggregateDict
  myDict = mySol.aggregateDict



  for k,v in solDict.iteritems():
    if len( set(myDict[k]).intersection(v)) < len(v):
    # if myDict[k] != v:
      print "{} ans wrong".format([k])


