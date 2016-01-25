import MapReduce
import sys

"""
to count the number of friends for each person.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    person = record[0]
    # friend = record[1]
    mr.emit_intermediate(person, 1)

def reducer(key, friend_list_of_1):

    total = 0
    for v in friend_list_of_1:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
