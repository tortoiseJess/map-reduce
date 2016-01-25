import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    docName = record[0]
    value = record[1]
    words = value.split()
    uniqueWords = set(words) #another mapReduce task
    for w in uniqueWords:
      mr.emit_intermediate(w, docName)  #word is key and value is freq


      
def reducer(key, list_of_values):
    # key: word
    # list of values = list of doc name

    mr.emit((key, list_of_values ))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
