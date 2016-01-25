
import MapReduce
import sys

"""
 remove the last 10 characters from each string of
 nucleotides, then remove any duplicates generated.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    trimmed_dna = record[1][:-10]

    mr.emit_intermediate(trimmed_dna, "dummy")

def reducer(trimmed_dna_as_key, list_of_values):

    mr.emit(trimmed_dna_as_key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
