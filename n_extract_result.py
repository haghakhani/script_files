import shutil as st
import os
import glob

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
#      os.mkdir(os.path.join(os.getcwd(),'n_sample'+str(i)))
#      st.copy(os.path.join(os.getcwd(),'sample'+str(i)+'/simulation.data'),os.path.join(os.getcwd(),'n_sample'+str(i)+'/simulation.data'))
      fp = open(os.path.join(os.getcwd(),'sample'+str(i)+'/simulation.data'),'r')
      simdata = fp.read()
      fp.close
      rp_simdata = simdata.replace(str('1800'), str('1200'))
      fp = open(os.path.join(os.getcwd(),'n_sample'+str(i)+'/simulation.data'),'w')
      fp.write(rp_simdata)
      fp.close
      st.copy(os.path.join(os.getcwd(),'sample'+str(i)+'/frict.data'),os.path.join(os.getcwd(),'n_sample'+str(i)+'/frict.data'))
      st.copy(os.path.join(os.getcwd(),'sample'+str(i)+'/scale.data'),os.path.join(os.getcwd(),'n_sample'+str(i)+'/scale.data'))
      st.copy(os.path.join(os.getcwd(),'sample'+str(i)+'/sample_slurm'),os.path.join(os.getcwd(),'n_sample'+str(i)+'/sample_slurm'))
      st.copy(os.path.join(os.getcwd(),'sample'+str(i)+'/titan'),os.path.join(os.getcwd(),'n_sample'+str(i)+'/titan'))
      file=os.path.join(os.getcwd(),'n_sample'+str(i)+'/simulation.data')
      with open(file) as f:
	for line in f:
	  line.replace('1800', '1200')

      mother_dir=os.path.join(os.getcwd(),'mother')
      for filename in glob.glob(os.path.join(mother_dir, 'fun*')):
        st.copy(filename, os.path.join(os.getcwd(),'n_sample'+str(i)))
      break	  
  result.write("%d , %s , %s \n" % (i, str(proc) ,str(error)))
  print error	  
result.close()

