import MapReduce
import sys

"""
query join using map reduce 
"""

mr = MapReduce.MapReduce()

# =============================


def mapper(record):
    # print record

    joinKey = record[1]
    mr.emit_intermediate(joinKey, record)


def reducer(key, list_of_values):
    
    orderEntry = []
    line_itemEntry = []

    for row in list_of_values:
      #divide the tables
      table = row[0]
      if table == "order":
        orderEntry.append(row)
      else:
        line_itemEntry.append(row)


    for order in orderEntry:
      for lineItem in line_itemEntry:
          mr.emit( order+lineItem)




# =============================
if __name__ == '__main__':


  matrix = open(sys.argv[1])
  mr.execute(matrix,mapper,reducer)


