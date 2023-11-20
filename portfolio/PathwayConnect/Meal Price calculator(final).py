#Formatted values with dollar sign and two decimal places.
#Added creative touch receipt-like output.
#Added drink, appetizer and tips values calculations to exceed core requirements


print('\n~~~~~~~~~~~ Meal Price Calculator ~~~~~~~~~~~~~\n')

# Function to format float values with dollar sign and 2 decimal places
def format_currency(value):
    return "${:.2f}".format(value)

#Meals and appetizers for children and adults block
childs_meal = float(input('What is the price of children meals? '))
adults_meal = float(input('What is the price of an adults meal? '))
drink_price = float(input('What is the price of a drink? '))
appetizer_price = float(input('Enter the price of an appetizer: '))

#Quantity block
num_of_children = int(input('How many children are there? '))
num_of_adults = int(input('How many adults are there? '))
num_drinks = int(input('How many drinks are required? '))
num_appetizers = int(input('Enter the number of appetizers: '))

#Tax and tip block
payment_amount = float(input('What is the payment amount? '))
sales_tax = float(input('what is the sales tax? '))
tip_percentage = float(input('Enter the tip percentage (%): '))
print()

#Calculations block
children_subtotal = childs_meal * num_of_children
adults_subtotal = adults_meal * num_of_adults
subtotal = (children_subtotal + adults_subtotal)
tax = subtotal * (sales_tax / 100)
total = subtotal + sales_tax
tip_amount = total * (tip_percentage / 100)
total_price_with_tip = total + tip_amount
change = payment_amount - total_price_with_tip
print()

# Actual payments receipt
print('*********************************')
print('           RECEIPT               ')
print('*********************************')
print('Tip Amount:      ', format_currency(tip_amount))
print('Total (incl.tip):', format_currency(total_price_with_tip))
print('---------------------------------')
print('Subtotal:        ', format_currency(subtotal))
print('Sales Tax:       ', format_currency(tax))
print('---------------------------------')
print('Total Price:     ', format_currency(total))
print('Payment Amount:  ', format_currency(payment_amount))
print('Change:          ', format_currency(change))
print('*********************************')
print('*********************************')
print()

