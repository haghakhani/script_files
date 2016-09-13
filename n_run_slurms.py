import os

for i in range(0,64):
    path='n_sample'+str(i)
    if os.path.isdir(path):
      os.chdir(path)    
      os.system('sbatch sample_slurm')
      os.chdir('..')

