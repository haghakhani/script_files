import shutil as su
import os

for i in range(0,64):
#  print i
  CWD=os.getcwd()
  src=os.path.join(CWD,'sample'+str(i))
  files=glob.glob('hmax_func*')
#  print src
  if os.path.isfile(src): 
    print 'yes'
    dst=os.path.join(CWD,'pileheights/'+str(i))
    print dst
    su.copyfile(src,dst)

