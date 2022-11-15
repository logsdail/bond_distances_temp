#!/usr/bin/env python3

def read_structure(filename=None):
    if filename==None:
        raise Exception("Sorry, no filename provided?")
    else:
        from ase.io import read
        return read(filename)

def get_distance_matrix(atoms=None, verbose=True):
    if atoms==None:
        raise Exception("Sorry, no atoms object provided?")
    else:
        import numpy as np
        distance_matrix = []
        for i in range(len(atoms.positions)):
            i_distances = []
            for j in range(len(atoms.positions)):
                # Wanted to do this with initialisation outside loop but couldn't get working!
                if j < i:
                    i_distances.append(-1)
                elif i == j:
                    i_distances.append(0)
                else:
                    # This provides a top right (?) matrix of distances, with -1 for invalid entries
                    # To make complete, could also set distance_matrix[j,i], but then we'd double count
                    print(i,j,np.linalg.norm(atoms.positions[i]-atoms.positions[j]))
                    i_distances.append(np.linalg.norm(atoms.positions[i]-atoms.positions[j]))
            distance_matrix.append(i_distances)
        return distance_matrix

if __name__ == "__main__":
    filename="geometry.in"
    atoms = read_structure(filename)
    print(get_distance_matrix(atoms[0:3]))
