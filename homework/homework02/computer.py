#!/usr/bin/env python3

'''
Matrix Vector Calculator for CS 401

Author: Andrew Solis
'''

# system import
import sys

import numpy as np


def read_matrices_vectors(filename) -> tuple[ list[ list[ int ] ] ,list[ int ] ]:
    '''
    Read Matrices and Vectors from file and return.
    
    Args:
        filename (str): name of the file to read the matrices and vectors from.

    Returns:
        tuple[ list[ list[ int ] ] ,list[ int ] ]: tuple of list of matrices and list of vectors.
    '''

    # store matrices and vectors
    matrices = []
    vectors = []

    # Open the file in read mode
    with open(filename, 'r') as file:

        # read all lines
        lines = file.readlines()

        # iterate over lines. There is a 10x10 matrix followed by a 1x10 vector every 13 lines
        for i in range(0, len(lines), 13):

            # read the first 10 lines as a matrix
            matrix = [list(map(int, lines[i+j].split())) for j in range(10)]
            
            # read last line as a vector
            vector = list(map(int, lines[i+11].split()))
            
            # append matrix and vector to list
            matrices.append(np.array(matrix))
            vectors.append(np.array(vector))

    return matrices, vectors

def compute_matrix_vector_products(matrices, vectors) -> list[ list [int] ]:
    '''
    Compute the product of a list of matrices and vectors.
    
    Args:
        matrices (list[ list[ int ] ]): list of matrices.
        vectors (list[ int ]): list of vectors.

    Returns:
        list[ list [int] ]: list of results of matrix vector products.
    '''

    # compute matrix vector products
    results = [np.dot(matrix, vector) for matrix, vector in zip(matrices, vectors)]
    
    return results

def write_results(filename, results):
    '''
    Write matrix vector results to file.

    Args:
        filename (str): name of the file to write the results to.
        results (list[ list [int] ]): list of results of matrix vector products.
    '''

    # Open the file in write mode
    with open(filename, 'w') as file:

        # iterate over each result
        for result in results:

            # write result to file
            file.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    matrices, vectors = read_matrices_vectors(input_filename)
    results = compute_matrix_vector_products(matrices, vectors)
    write_results(output_filename, results)
