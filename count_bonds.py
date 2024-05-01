#!/usr/bin/env python3

def read_structure(filename=None):
    if filename==None:
        raise Exception("Sorry, no filename provided?")
    
    from ase.io import read
    return read(filename)

def get_distance_matrix(atoms=None, verbose=False):
    if atoms==None:
        raise Exception("Sorry, no atoms object provided?")
    
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
                if verbose:
                    print(i,j,np.linalg.norm(atoms.positions[i]-atoms.positions[j]))
                i_distances.append(np.linalg.norm(atoms.positions[i]-atoms.positions[j]))
        distance_matrix.append(i_distances)
    return distance_matrix

def get_bond_counts(distance_matrix=None, symbols=None, verbose=True):
    if distance_matrix==None:
        raise Exception("Sorry, no distance matrix provided?")
    if symbols==None:
        raise Exception("Sorry, no symbols provided?")

    # This is horrible - should be softcoded!
    bond_cutoff=4.0
    # Collect the individual labels
    unique_labels=list(set(symbols))
    # Create an object to store the bond labels
    bond_counts = {}
    # This feels pretty inefficient - think the loops are the wrong way round?
    for atom_A in range(len(unique_labels)):
        for atom_B in range(atom_A, len(unique_labels)):
            bond_counts[unique_labels[atom_A]+"-"+unique_labels[atom_B]]=0
 
    for i in range(len(symbols)):
        for j in range(i+1, len(symbols)):
            if distance_matrix[i][j] < bond_cutoff:
                try:
                    bond_counts[symbols[i]+"-"+symbols[j]]=bond_counts[symbols[i]+"-"+symbols[j]]+1
                except KeyError:
                    bond_counts[symbols[j]+"-"+symbols[i]]=bond_counts[symbols[j]+"-"+symbols[i]]+1
 
    return bond_counts

if __name__ == "__main__":
    filename="geometry.in"
    atoms = read_structure(filename)
    distance_matrix = get_distance_matrix(atoms)
    bond_counts = get_bond_counts(distance_matrix, atoms.get_chemical_symbols())
    print("Bond Counts:", bond_counts)
