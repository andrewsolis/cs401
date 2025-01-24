#!/usr/bin/env python3

'''
Matrix Vector writer for CS 401

Author: Andrew Solis
'''

# system import
import sys

# outside import
import numpy as np


def write_matrix_and_vector(filename):
    '''
    Writes a file with 10 random 10x10 matrices and 10 random 1x10 vectors.

    Args: 
        filename (str): name of the file to write the matrices and vectors to.
    '''

    # Open the file in write mode
    with open(filename, 'w') as f:
       

        # Set the seed so always the same numbers are printed
        np.random.seed(50)

        # Write 10 random 10x10 matrices and 10 random 1x10 vectors
        for _ in range(10):

            # Generate a 10x10 matrix
            
            matrix = np.random.randint(1, 100, size=(10, 10))
            
            for row in matrix:
                f.write(' '.join(map(str, row)) + '\n')
            
            f.write('\n')  # Empty line after the matrix

            # Generate a 1x10 vector
            
            vector = np.random.randint(1, 100, size=(1, 10))
            f.write(' '.join(map(str, vector[0])) + '\n')
            f.write('\n')  # Empty line after the vector

if __name__ == "__main__":
    write_matrix_and_vector(sys.argv[1])
