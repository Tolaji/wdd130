"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
   

# Define a class named HeartRate
class HeartRate:
    #Initialize class attributes: user_age, lower_rate, upper_rate
    def __init__(self, user_age):
        self.user_age = user_age
        self.lower_rate = 0.65
        self.upper_rate = 0.85
        
    #Define method to calculate Maximum Heart Rate (MHR)
    def calculate_max_heart_rate(self):
        max_heart_rate = 220 - user_age
        return max_heart_rate

    #Define method to determine Target Heart Rate Range
    def determine_target_heart_rate_range(self):
        max_heart_rate = self.calculate_max_heart_rate()
        lower_range = self.lower_rate * max_heart_rate
        upper_range = self.upper_rate * max_heart_rate
        return lower_range, upper_range

#User age input
user_age = int(input("Enter your age: ")) 

#Create an instance of the Heart_rate class
heart_rate_calculator = HeartRate(user_age)


#Calculate the lower and upper heart rate ranges
lower_range, upper_range = heart_rate_calculator.determine_target_heart_rate_range()

#Print the target heart rate range
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower_range} and {upper_range} beats per minute.")

