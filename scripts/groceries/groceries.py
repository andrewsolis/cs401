import json

def compute_average_quantity(a_list_of_dicts, a_key_string):
    total_quantity = 0
    for item in a_list_of_dicts:
        total_quantity += item[ a_key_string ]

    return float( total_quantity / len( a_list_of_dicts ) )

def calc_total_price( price, quantity ):
    total_price = price * quantity
    return total_price

with open('groceries.json', 'r') as f:
    grocery_data = json.load( f )


print( compute_average_quantity( grocery_data['items'], 'quantity' ) )

for row in grocery_data['items']:
    total_price = calc_total_price( float( row['price']), float( row['quantity'] ) )
    print(f'Total Price: {total_price:.2f}')