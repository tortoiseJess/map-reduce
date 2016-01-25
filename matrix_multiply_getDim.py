import MapReduce
import sys

"""
two step matrix multiply
"""

class MapReduceGetMatrixDim(object):
  print "MapReduceGetMatrixDim" 

  def __init__(self,mr):
    self.mr = mr
    self.dim=[0,0,0]


  def mapper(self,record):
      # print  record
      matrix = record[0]
      i = record[1]
      j = record[2]
      value = record[3]

      if matrix == u"a":
        self.mr.emit_intermediate("A", (i,j))
      elif matrix == "b":
        self.mr.emit_intermediate("B",j)

  def reducer(self,key, list_of_values):

      if key =="A":
        self.dim[0] = max([ tupl[0] for tupl in list_of_values])+1
        self. dim[2] = max([ tupl[1] for tupl in list_of_values])+1
      elif key =="B":
        self.dim[1]= max(list_of_values)+1
      # print "get dim reducer"
      # print self.dim 



