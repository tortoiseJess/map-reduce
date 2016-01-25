import MapReduce
from matrix_multiply_getDim import MapReduceGetMatrixDim
import sys

"""
second part matrix multiply map reducer
"""

mr = MapReduce.MapReduce()

# =============================


def mapper(record):
    # print record
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]

    if matrix == "a":
      for k in range(0,dim[1]):
        mr.emit_intermediate((i,k), ("A",j,value))
        # print "main mapper emit ", (i,k)
    elif matrix == "b":
        for k in range(0,dim[0]):
          mr.emit_intermediate((k,j),("B",i,value))
          # print "main mapper emit ", (k,j)

def reducer(key, list_of_values):
    print "main reducer key ", key
    print "main reducer " , list_of_values
    
    rowA={}
    colB = {}
    total = 0

    for record in list_of_values:

      #divide into row i of A then divide into col k of B
      matrix = record[0]
      idx = record[1]
      value = record[2]
      if matrix == "A":
        rowA[idx]= value
      else:
        colB[idx]=value
    print rowA
    print colB

    for idx in range(0,dim[2]):
        total += rowA[idx]*colB[idx]

    mr.emit((key, total))




# =============================
if __name__ == '__main__':

  matrix = open(sys.argv[1])
  mr2 = MapReduce.MapReduce()
  dimFinder = MapReduceGetMatrixDim(mr2)
  mr2.execute(matrix, dimFinder.mapper, dimFinder.reducer)
  dim = dimFinder.dim
  print "main", dim
  matrix.close()
  matrix = open(sys.argv[1])
  mr.execute(matrix,mapper,reducer)


