#!/usr/bin/env python3

'''
Matrix Vector Verifier for CS 401

Author: Andrew Solis
'''

# system import
import sys
import time

# outside import
import numpy as np
from alive_progress import alive_bar

def verify_results(results_arr, answers_arr):
    '''
    Verify that the results array matches the answers array element by element.

    Args:
        results_arr (numpy.ndarray): array of computed results to verify.
        answers_arr (numpy.ndarray): array of expected answers to compare against.

    Returns:
        bool: True if all elements match, False otherwise.
    '''

    with alive_bar(5000, title="verifying results", spinner="loving", bar="checks") as bar:
        for x, y in zip(results_arr.flat, answers_arr.flat):
            if x != y:
                print(f"Incorrect answer: {x} != {y}")
                return False
            time.sleep(.001)
            bar()
        print("\U0001F973 \U0001F973 \U0001F973  Congratulations! Program successfully completed.")
        return True

if __name__ == "__main__":
    results_filename = sys.argv[1]
    answers_filename = sys.argv[2]

    results = np.loadtxt(results_filename, dtype=int)
    answers = np.loadtxt(answers_filename, dtype=int)

    verify_results(results, answers)
