#!/usr/bin/env python3
import json
from typing import List

def compute_average_quantity(a_list_of_dicts, a_key_string)-> float:
    """
    Iterate through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value( will enforce float type).

    Returns:
        result (float): Average value.
    """

    total_quantity = 0.
    for item in a_list_of_dicts:
        total_quantity += float(item[ a_key_string ])

    return ( total_quantity / len( a_list_of_dicts ) )

def calc_total_price( price, quantity )-> float:
    """
    Given a price and quantity, calculate to total price of items in stock and return
    the calculated amount.

    Args:
        price (float): price of an item
        quantity (float): amount of an item the grocery store has in stock

    Returns:
        total_price (float): total calculated price of item.
    """
    
    total_price = price * quantity
    return total_price

def count_categories(a_list_of_dicts, a_key_string)-> dict:
    """
    Iterate through a list of dictionaries, counting the number of times
    a particular category is found in the list. Returns a count of all
    categories found and their amount.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               string to check for counting.

    Returns:
        categories_observed(dict): categories and their count.
    """

    categories_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in categories_observed:
            categories_observed[item[a_key_string]] += 1
        else:
            categories_observed[item[a_key_string]] = 1
    return(categories_observed)

def main():
    with open('groceries.json', 'r') as f:
        grocery_data = json.load( f )

    print( compute_average_quantity( grocery_data['items'], 'quantity' ) )

    for row in grocery_data['items']:
        total_price = calc_total_price( float( row['price']), float( row['quantity'] ) ) 
        print(f'Total Price: {total_price:.2f}')

    print( count_categories( grocery_data['items'], 'category' ) )

if __name__ == '__main__':
    main()