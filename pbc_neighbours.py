from ase.build import bulk
import numpy as np
import sys
from itertools import product

a = bulk('MgO','rocksalt', 4.2)
cell_images = np.array(list(product([-1, 0, 1], repeat=3))) @ a.cell.array
positions_images = a.positions[None, ...] + cell_images[:, None, :]

D = positions_images[:, :, None, :] - a.positions[None, None,...]
d = np.linalg.norm(D, axis=-1)
np.savetxt(sys.stdout, np.array(a.symbols)[None, :], fmt='%6s')
np.savetxt(sys.stdout, np.sort(d.reshape((-1, d.shape[-1])), axis=0), fmt='%6.2f')
