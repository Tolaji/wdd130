print("\n******Wind Chill and Temperature******\n")

# Welcome
print("\nWelcome to this windchill and temperature programme")
print("*" * 55)

wind_speed = 0
wind_chill = 0


# Function to  initialize windchill calculations
def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 0.0

    if temperature < 50 and wind_speed > 3.0:
        wind_chill = (
            35.74
            + (0.6215 * temperature)
            - (35.75 * wind_speed**0.16)
            + (0.4275 * temperature * wind_speed**0.16)
        )

    return wind_chill


# Celsius conversion formula function
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# Fahrenheit conversion formula function
def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32


# Temperature declared as none
temperature = None
# Loop to get user input
while temperature is None:
    temperature_input = input("Enter the temperature (Fahrenheit or Celsius): ")

    try:  # Initialize error handling
        temperature = float(temperature_input)  # Input conversion to float
    except ValueError:  # If input not numerical value error message is triggered
        print("Invalid temperature. Please enter a numerical value.")
print()
print(f"What is the temperature? {temperature_input}")
is_celsius = input("Fahrenheit or Celsius? (F/C): ")


if is_celsius.upper() == "C":  # Conditional statement to determine temperature
    temperature = fahrenheit_to_celsius(temperature)

# A `for` loop loop to iterate over range of wind speed values for calculation
for wind_speed in range(5, 61, 5):
    wind_chill = calculate_wind_chill(temperature, wind_speed)

    # Print temperature unit with formatting
    print(
        f"At a temperature of {temperature:.2f} {'Celsius' if is_celsius.upper() == 'C' else 'Fahrenheit'}, and wind speed of {wind_speed:.2f}, the wind chill is {wind_chill:.2f}."
    )
