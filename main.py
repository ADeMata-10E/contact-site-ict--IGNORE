from pyscript import display, document # type: ignore 



restaurant_name = ' Baked Flower' # String
owner_name = "ADM" # String
year_established = "2024" # String
popular_item_price = 1003 #Integer
has_delivery = False # Boolean
product_names = ['', 'Cotton candy', 'Lollipops', 'Cupcakes', 'Fried squid'] # List
menu_prices = 10.99, 12.99, 8.99, 15.99 # Tuple
business_hours = 'Monday', 'Saturday' # dictionary
tax_rate = '0.07' # Float

business_email = ""
business_location = "Location: 123 Flower St., Bloom City" 

display (f' Established by {owner_name}', target='topheader2')
display (f' Items', target='column2')
display (f' Since October 12, {year_established}', target='topheader2')

display (f'ALL ITEM PRICES (in ₱)', target='column3')

chosen_item1 = product_names[1]
chosen_item2 = product_names[2]
chosen_item3 = product_names[3]
chosen_item4 = product_names[4]

price1= menu_prices[1]
price2= menu_prices[2]
price3= menu_prices[3]
price4= menu_prices[0]

display (f' {chosen_item1}', target='information')
display (f' {chosen_item2}', target='information2')
display (f' {chosen_item3}', target='information3')
display (f' {chosen_item4}', target='information4')

display (f' Open: 10:03 PM - 9: 27 AM', target='footer')

display (f'₱{price1}', target='price')
display (f'₱{price2}', target='price2')
display (f'₱{price3}', target='price3')
display (f'₱{price4}', target='price4')

display (f' Contact Information', target='contactinfo2')
display (f' {business_location}', target='contactinfo3')
display (f' Phone Number: +0123455432', target='contactinfo')