#!/usr/bin/env python3

'''
Collatz code for CS 401

Author: Andrew Solis
'''

from typing import List


def compute_collatz( num : int ) -> List[int]:
    '''
    Calculates the sequence for the collatz conjecture given number 'num'. 
    Return the list of sequence.

    Args: 
        num (int): initial number for starting collatz computation.

    Returns:
        result( List[int] ): Collatz sequence.
    '''

    result = []

    result.append( num )

    while num != 1:

        if num % 2 == 0:
             
            num = num // 2
            result.append( num )

        else:

            num = 3 * num + 1
            result.append( num )

    return result

def print_collatz( collatz_list : List[int] ):

    '''
    Print out list for collatz conjecture of number.

    Args:
        collatz_list( List[int] ): collatz conjecture for number in list form.
    '''

    print( collatz_list[0], end="")
    # print( collatz_list)

    for i in range( 1, len(collatz_list ) ):
        print( f' -> { collatz_list[i] }', end="" )
    
    # put ending of line 
    print()


def main():

    print('Collatz')
    print('=======\n')

    with open('input.txt') as file:

        lines = [line.rstrip() for line in file]

        for line in lines:

            print( line )

            num = int( line )

            num_collatz = compute_collatz( num )

            print_collatz( num_collatz )

            print(f'num sequences: {len(num_collatz) - 1}\n' )




if __name__ == '__main__':
    main()