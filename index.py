import MDAnalysis as mda
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

u = mda.Universe('pull2.gro','pull2.xtc')
prot = u.select_atoms('resname LIG')
system = u.select_atoms('resid 1-81429')
com = prot.center_of_mass()

halfz = u.dimensions[2]/2 ## Get the half of the z-dimension
UP = u.select_atoms('name P and prop z > %f' %halfz)
LP = u.select_atoms('name P and prop z < %f' %halfz)
c318 = u.select_atoms('name C318')
com_bil = u.select_atoms('bynum 30:35410')

with mda.selections.gromacs.SelectionWriter('leaflet.ndx', mode='w') as ndx:
	ndx.write(LP,name='lower_leaflet')
	ndx.write(UP,name='upper_leaflet')
	ndx.write(prot,name='prot')
	ndx.write(system,name='all')
	ndx.write(c318,name='c318')
	ndx.write(com_bil,name='com_bil')