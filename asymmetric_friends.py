import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if
I am your friend, you are my friend. Implement a MapReduce algorithm
to check whether this property holds

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    record.sort()
    friend_pair = tuple(record)
    mr.emit_intermediate(friend_pair,1)

def reducer(friend_pair, list_of_values):

    if len(list_of_values) < 2:
      mr.emit(friend_pair)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
