import sys

def read_json( ):
    
    # TODO: read the JSON file and return the data
    
    pass

def net_profit( ):
    
    # TODO: movie with the largest net profit of the past 5 years
    
    pass

# TODO: add second function to print out interesting statistics about the data


# TODO: add third function to print out interesting statistics about the data


def main():

    if len(sys.argv) < 2:

        print("Error: No command line argument provided. Please provide a file name for a json file to read. i.e. python analyze_data.py data.json")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    # Access the command line argument
    output_file = sys.argv[1]

    # TODO: call function to read JSON file and return data
    data = read_json( )

    # TODO: call function to get the movie with the largest net profit of the past 5 years
    net_profit_answer = net_profit( )

    print( f'Movie with largest net profit: {net_profit_answer}' )

    # TODO: second function to return and print out 

    # TODO: third function to return and print out result


if __name__ == '__main__':
    main()