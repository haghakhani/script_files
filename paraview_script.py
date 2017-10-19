#### import the simple module from the paraview
from paraview.simple import *
import numpy as np
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
dgae_q_0 = FindSource('dgae_q_0*')
point = np.genfromtxt ('/h1/aghakhani/old_builds/build/dgea_trilinos_dbg/local/bin/zapas/receiver_position.csv', delimiter=" ")

for i in range(0,64):
  # create a new 'Probe Location'
  probeLocation = ProbeLocation(Input=dgae_q_0,
              ProbeType='Fixed Radius Point Source')
  
  # Properties modified on probeLocation1
  probeLocation.Tolerance = 2.22044604925031e-16
  
  # Properties modified on probeLocation1.ProbeType
  probeLocation.ProbeType.Center = [point[i,0], point[i,1], point[i,2]]
  filename="/h1/aghakhani/old_builds/build/dgea_trilinos_dbg/local/bin/zapas/receiver%d.csv" % i
  # save data
  SaveData(filename, proxy=probeLocation, WriteAllTimeSteps=1)
