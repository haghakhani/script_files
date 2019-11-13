import shutil as st
import os

result = open('result', 'w')
for i in range(0,64):
  error=0.
  proc='N/A'
  print i
  for j in range(8):  
    file=os.path.join(os.getcwd(),'sample'+str(i)+'/hmax_func000'+str(j))
    if os.path.isfile(file):	      
      if os.path.getsize(file) > 0:
	with open(file) as f:
	  for line in f:
	    words=line.split(" ")       
	    if words[0]=='Normalized':
	      if error<float(words[3]):
		error=float(words[3])
		proc=j
    else:
      error='N/A'
      break	  
  result.write("%d , %s , %s \n" % (i, str(proc) ,str(error)))
  print error	  
result.close()

