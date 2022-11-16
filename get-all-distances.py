def get_distances():
    from ase.io import read, write
    from ase import Atoms
    import numpy as np


    # atoms = read('bulk_eos.traj@:')
    #atoms = read('aims.out')
    atoms = read('geometry.in')
    position_list = atoms.get_positions()
    distance_list = []
    for a1 in position_list:
        for a2 in position_list[::-1]:
            if np.array_equal(a1, a2):
                break
            D = ((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2 + (a1[2] - a2[2]) ** 2) ** 0.5
            print(a1, a2, D)
    return 0
    #print('position\n', position_list)


