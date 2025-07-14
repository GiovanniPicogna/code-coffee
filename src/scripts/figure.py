import numpy as np
import matplotlib.pyplot as plt
import paths
from dustpy import hdf5writer

cm_to_au = 6.684587e-14

#Load the data
writer = hdf5writer()
writer.datadir = paths.data
data = writer.read.output(21)

# Plot the results
fig, ax = plt.subplots(2, layout='tight')
ax[0].semilogy(data.grid.r*cm_to_au, data.gas.Sigma)
ax[0].set_title('Final gas distribution')
ax[0].set_xlabel('R [au]')
ax[0].set_ylabel('$\Sigma_g$ [g/cm$^{-2}$]')
ax[0].set_ylim(1.e-2,1e3)
ax[0].set_xlim(0,400)
ax[1].semilogy(data.grid.r*cm_to_au, data.dust.Sigma)
ax[1].set_title('Final dust distribution')
ax[1].set_xlabel('R [au]')
ax[1].set_ylabel('$\Sigma_D$ [g/cm$^{-2}$]')
ax[1].set_ylim(1.e-4,1e1)
ax[1].set_xlim(0,400)
fig.savefig(paths.figures / "figure.pdf")
