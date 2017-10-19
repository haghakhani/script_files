import csv
import itertools
import numpy as np

for i in range(0,64):
  for j in range(0,13):
    filename="/h1/aghakhani/old_builds/build/dgea_trilinos_dbg/local/bin/zapas/receiver%d.%d.csv" % (i,j)
    with open(filename) as fd:
      row=next(csv.reader(itertools.islice(fd, 1, 2)))
      print row[0],row[1],row[2]  
