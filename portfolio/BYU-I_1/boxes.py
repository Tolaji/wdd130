from math import ceil

class BoxesRequired:
    # Define Constructor
    def __init__(self, items_per_box, total_items):
        self.total_items = total_items
        self.items_per_box = items_per_box
    
    # Define function to calculate number of boxes needed
    def calculate_boxes(self):
        boxes_needed = ceil(total_items / items_per_box) #Calculate boxes needed precisely to the nearest whole number using 'ceil' instead of 'round' ensuring enough boxes to hold all items
        return boxes_needed

# Ask for user input
total_items = int(input("Enter the number of manufactured items: "))
items_per_box = int(input("Enter the number of items to pack per box: "))

# Create an instance of BoxesRequired class
boxes_calculator = BoxesRequired(items_per_box, total_items)

# Calculate boxes needed
boxes_needed = boxes_calculator.calculate_boxes()

# Print the result
print(f"The number of boxes necessary to hold the items is: {boxes_needed}")