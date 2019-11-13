import os

for i in range(0,64):
    path='sample'+str(i)
    os.chdir(path)    
    os.system('sbatch sample_slurm')
    os.chdir('..')

