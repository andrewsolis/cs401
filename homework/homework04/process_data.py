#!/usr/bin/env python3

'''
Process Data for multiple movie csv files into one file.

Author: Andrew Solis
'''

import os.path
import sys
import csv
import json

from ast import literal_eval

def prepend_path( files, *args ) -> list[ str ]:
    '''
    Given a list of file names and a list of directories, prepend each file name with each directory.

    Args:
        files (list): The list of file names.
        *args (list): The list of directories.

    Returns:
        files (list): The list of file names with each directory prepended.
    '''

    # Prepend each file name with each directory
    # use the * operator to unpack "args" into a list of strings
    files = [os.path.join( *args, file ) for file in files ]

    return files

def get_header(file_path) -> list[ str ]:
    '''
    Given a file path, return the header of the CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        header (list): The header of the CSV file.
    '''

    header = []
    
    
    with open(file_path, 'r', encoding='utf-8') as f:

        # Read the CSV file and retrieve header information on first row
        reader = csv.reader(f)
        header = next(reader)
        
    return header

def combine_csv_files(csv_files, header=True) -> list[ list[ str ] ]:
    '''
    Given a list of file paths, return the combined data of the CSV files.

    Args:
        csv_files (list) : The list of file paths.
        header (bool)    : Whether the header is included in each dataset or not.

    Returns:
        combined_data (list): The combined data of the CSV files.
    '''

    # Initialize the combined data list
    combined_data = []

    first = True

    # Read and combine the CSV files
    for file in csv_files:
        
        # Read the CSV file
        with open(file, 'r', encoding='utf-8') as f:
            
            # Read the CSV file and store into temporary variable
            reader = csv.reader(f)
            temp_data = list(reader)

            # If header is included, remove the first row
            if header:
                if not first:
                    combined_data.extend(temp_data[1:11])
                else:
                    first = False
                    combined_data.extend(temp_data[1:12])
            else:
                combined_data.extend(temp_data[:10])

    return combined_data

def fix_column_string(data, column_index) -> list[ str ]:
    '''
    Given a list of lists and a column index, remove any numbers, period, or whitespace from the beginning 
    if the string in the specified column.

    Args:
        data (list): The list of lists.
        column_index (int): The index of the column to fix.

    Returns:
        data (list): The list of lists with the fixed column.
    '''

    for row in data:
        
        # remove any numbers, period, or whitespace from the beginning of the string
        row[column_index] = row[column_index].lstrip('0123456789. ')

    return data

def convert_to_json( data, header ) -> list[ dict ]:
    '''
    Given a list of lists, convert the data into a list of dictionaries.

    Args:
        data (list): The list of lists.

    Returns:
        json_data (list): The list of dictionaries.
    '''

    # Get the header from the first row

    # Initialize the json data list
    json_data = []

    # Iterate through each row in the data
    for row in data[1:]:
        
        # Create a dictionary for each row using the header as keys
        json_data.append( dict( zip( header, row ) ) )

    return json_data

def format_data( data ) -> list[ dict ]:
    
    id = 1
    for entry in data:
        for key, value in entry.items():
            if value.isdigit():
                entry[key] = int(value)
            elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
                entry[key] = float(value)
            elif value.startswith('[') and value.endswith(']'):
                try:
                    entry[key] = literal_eval( entry[key] )
                    # json.loads(value)
                except json.JSONDecodeError:
                    pass
        entry['id'] = id
        id += 1
    return data

def main():

    if len(sys.argv) < 2:

        print("Error: No command line argument provided. Please provide a file name. i.e. python process_data.py output_file.json")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    # Access the command line argument
    output_file = sys.argv[1]

    # List of CSV files to read
    csv_files = [
        'merged_movies_data_2021.csv',
        'merged_movies_data_2022.csv',
        'merged_movies_data_2023.csv',
        'merged_movies_data_2024.csv',
        'merged_movies_data_2025.csv'
    ]

    # prepend data directory to each file
    csv_files = prepend_path( csv_files, 'data', 'imdb_movies' )

    print("Reading header and data from CSV files...")

    # Get the header from the first CSV file
    header = get_header(csv_files[0])

    # Combine the data from all CSV files
    data = combine_csv_files(csv_files)

    print("Fixing data...")

    # Remove the first 3 characters of each title in the 'Title' column at index 0
    data = fix_column_string( data, 0 )  

    # convert data to json format
    print("Converting data into json format")

    data_json = convert_to_json( data, header )

    data_json = format_data( data_json )

    with open( output_file, "w", encoding="utf-8" ) as f:
        json.dump( data_json, f, indent=4 )

    print("Writing complete.")

if __name__ == '__main__':
    main()