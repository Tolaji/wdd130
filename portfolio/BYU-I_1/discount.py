"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""
import datetime

class MidweekDiscounts:
    # Define Constructor
    def __init__(self, discount_threshold, discount_percentage, sales_tax_rate):
        self.discount_threshold = discount_threshold
        self.discount_percentage = discount_percentage
        self.sales_tax_rate = sales_tax_rate
    
    # Define function to get the current day of the week
    def get_current_day_of_week(self):
        today = datetime.datetime.today().weekday()
        return today
    
    #Define function to get the current date
    def get_current_date(self):
        today = datetime.datetime.today()
        return today.strftime("%Y-%m-%d")
    
    # Define function to calculate discounts and totals
    def calculate_totals(self, subtotal):
        current_day = self.get_current_day_of_week()

        # Initialize variables
        discount_amount = 0
        sales_tax = 0
        total_due = 0

        # Check if it's Tuesday (1) or Wednesday (2)
        if current_day == 1 or current_day == 2:
            if subtotal >= self.discount_threshold:
                # Apply the 10% discount
                discount_amount = subtotal * self.discount_percentage
                subtotal -= discount_amount
                
                # Calculate sales tax and total amount due
                sales_tax = subtotal * self.sales_tax_rate
                total_due = subtotal + sales_tax

        return subtotal, discount_amount, sales_tax, total_due
    
# Define constants
discount_threshold = 50  # Subtotal threshold for discount
discount_percentage = 0.10  # 10% discount
sales_tax_rate = 0.06  # 6% sales tax rate

# Get the subtotal from the customer
subtotal = float(input("Enter the subtotal: "))


# Create instance of MidweekDiscount class
discount_calculator = MidweekDiscounts(discount_threshold, discount_percentage, sales_tax_rate)

# Calculate totals
subtotal, discount_amount, sales_tax, total_due = discount_calculator.calculate_totals(subtotal)

# Display the current date
current_date = discount_calculator.get_current_date()
print(f"Today's Date: {current_date}")

#Display the current day
current_day = discount_calculator.get_current_day_of_week()
# Convert current day to a string from a method object
day_names =  ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_day_name = day_names[int(current_day)]
print(f"Today is:{day_names[current_day]}")


# Print the results
if discount_amount > 0:
    print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Sales Tax Amount: ${sales_tax:.2f}")
print(f"Total Amount Due: ${total_due:.2f}")
print()
print("-"*50)
