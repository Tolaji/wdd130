# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


class BodyFitnes:
      
    def __init__(self, gender = any, birthdate = any, weight = any, height = any):
        self.gender = gender
        self.birthdate = birthdate
        self.weight = weight
        self.height = height
    
    def compute_age(self, birth_str):
        """Compute and return a person's age in years.
        Parameter birth_str: a person's birthdate stored
            as a string in this format: YYYY-MM-DD
        Return: a person's age in years.
        """
        # Convert a person's birthdate from a string
        # to a date object.
        birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
        today = datetime.now()

        # Compute the difference between today and the
        # person's birthdate in years.
        years = today.year - birthdate.year

        # If necessary, subtract one from the difference.
        if birthdate.month > today.month or \
            (birthdate.month == today.month and \
                birthdate.day > today.day):
            years -= 1

        return years


    def kg_from_lb(self, weight):
        """Convert a mass in pounds to kilograms.
        Parameter pounds: a mass in U.S. pounds.
        Return: the mass in kilograms.
        """
        weight_kg = weight * 0.45359237
        return weight_kg


    def cm_from_in(self, height):
        """Convert a length in inches to centimeters.
        Parameter inches: a length in inches.
        Return: the length in centimeters.
        """
        height_cm = height * 2.54
        return height_cm


    def body_mass_index(self, weight_kg, height_cm):
        """Compute and return a person's body mass index.
        Parameters
            weight: a person's weight in kilograms.
            height: a person's height in centimeters.
        Return: a person's body mass index.
        """
        bmi = weight_kg / (height_cm /100)**2
        return bmi


    def basal_metabolic_rate(self, bmr_women, bmr_men, gender, weight_kg, height_cm, age):
        """Compute and return a person's basal metabolic rate.
        Parameters
            weight: a person's weight in kilograms.
            height: a person's height in centimeters.
            age: a person's age in years.
        Return: a person's basal metabolic rate in kcals per day.
        """
        bmr_women = 447.593 + 9.247 * weight_kg + 3.098 * height_cm - 4.330 * age
        bmr_men = 88.362 + 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age
        return bmr_men, bmr_women

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender (M or F):   ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD):   ")
    weight = float(input("Enter your weight in U.S. pounds:   "))
    height = float(input("Enter your height in U.S. inches:   "))
    
    # Create an instance of BodyFitness class
    fitness = BodyFitnes(gender, birthdate, weight, height)
    
    print()
    
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = fitness.compute_age(birthdate) # Return age from birthdate input
    weight_kg = fitness.kg_from_lb(weight) # converts weight from pound to kg
    height_cm = fitness.cm_from_in(height) # Converts height from inches
    bmi = fitness.body_mass_index(weight_kg, height_cm) # calculate bmi using weight in kg and height in cm
    bmr_men, bmr_women = fitness.basal_metabolic_rate(None, None, gender, weight_kg, height_cm, age) # Calculates bmr for both genders

    # Age, weight_kg, height_cm, bmi, bmr_men, and bmr_women store the results of the respective calculations.

    # Print the results for the user to see.
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_kg}")
    print(f"Height (cm): {height_cm}")
    print(f"Body Mass Index: {bmi}")
    print(f"Basal Metabolic Rate for Men (kcal/day): {bmr_men}")
    print(f"Basal Metabolic Rate for Women (kcal/day): {bmr_women}")

# Call the main function so that
# this program will start executing.

main()