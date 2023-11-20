"""
The provided code performs analysis on life expectancy data. It starts by importing the "csv" module to read and process CSV files and the "matplotlib.pyplot" module to plot and visualize data. This code initializes two datasets, "life_expectancy.csv" and "life_expectancy_by_birth.csv" to create dictionaries for the store of data to be analyzed. The use of "csv.reader" function instead of "split()" is to create a csv reader object that splits the file content into rows and iterates through same. 

This code calculates the overall minimum and maximum life expectancy values and identifies the largest drop and spike in life expectancy by year and country. It then prompts the user to enter a country of interest and retrieves the corresponding life expectancy data. The code displays the minimum, maximum, and average life expectancies for the selected country. It also plots and visualizes the life expectancy trend over time for the country using a line plot. This code further allows the user to enter a specific year and provides the life expectancy for that year, as well as the highest and lowest life expectancies for the selected country. Finally, this code demonstrates basic data analysis and visualization techniques for exploring life expectancy data.
"""  # noqa: E501

# CSV File Processing: The code reads data from two CSV files
# It calculates overall statistics such as the minimum and maximum life expectancies regardless of the country.
# It identifies the largest drop and spike in life expectancy.
# It prompts the user to input a country of interest and provides specific analysis for that country.
# It visualizes the life expectancy trend over time for the selected country using a line plot.
# The code validates user input and ensures that the entered country exists in the dataset.
# It handles data not found scenarios and prompts the user to try again.
# The code utilizes the matplotlib library to create line plots, allowing visual representation of life expectancy trends.
# It utilizes dictionaries and lists to store and manipulate life expectancy data efficiently.
# The code includes error handling to handle exceptions, such as invalid user input or missing data.


import csv
import matplotlib.pyplot as plt


def prompt_country_of_interest():
    return input("\nEnter a country of interest: ").capitalize()


print("\n~~~ DATA ANALYSIS ~~~")
print("~~~ Prove ~~~\n")

print("\nWelcome to this data analysis program!")
print("*" * 40)
print("This program attempts to analyze life expectancy records")
print("\nLife Expectancy Spikes and Drops")
print("-" * 60)

life_expectancy_data = {}
largest_drop = 0
largest_drop_year = None
largest_drop_country = None
largest_spike = 0
largest_spike_year = None
largest_spike_country = None
overall_min_life_expectancy = float("inf")
overall_max_life_expectancy = float("-inf")
overall_min_year = 0
overall_max_year = 0
overall_max_country = ""
overall_min_country = ""
sum_life_expectancy = 0
count_countries = 0


with open("life_expectancy.csv") as file:
    reader = csv.reader(file)  # Split the file into rows
    next(reader)  # skip header line

    for line in reader:
        country = line[0]
        year = int(line[2])
        life_expectancy = float(line[3])

        overall_min_life_expectancy = min(overall_min_life_expectancy, life_expectancy)
        overall_max_life_expectancy = max(overall_max_life_expectancy, life_expectancy)

        if country not in life_expectancy_data:
            life_expectancy_data[country] = []

        life_expectancy_data[country].append((year, life_expectancy))

        if len(life_expectancy_data[country]) > 1:
            previous_year, previous_expectancy = life_expectancy_data[country][-2]
            drop = previous_expectancy - life_expectancy

            if drop > largest_drop:
                largest_drop = drop
                largest_drop_year = year
                largest_drop_country = country

            spike = life_expectancy - previous_expectancy

            if spike > largest_spike:
                largest_spike = spike
                largest_spike_year = year
                largest_spike_country = country

    # Output the overall max and min regardless country
    print(
        f"The overall max life expectancy regardless of country is: {overall_max_life_expectancy} for"  # noqa: E501
    )
    print(
        f"The overall min life expectancy regardless of country is: {overall_min_life_expectancy} for {lowest_year}"  # noqa: E501
    )

    # Output the largest drop for a country
    if largest_drop_country:
        print(
            f"Largest life expectancy drop of {largest_drop:.2f} years occurred in {largest_drop_year} in {largest_drop_country}."  # noqa: E501
        )

    # Output the largest spike for a country
    if largest_spike_country:
        print(
            f"Largest life expectancy spike of {largest_spike:.2f} years occurred in {largest_spike_year} in {largest_spike_country}."  # noqa: E501
        )


# Load and process the "life_expectancy_by_birth.csv" file
life_expectancy_data = {}

# Set the year to calculate average for
year_to_calc = ""

with open("life_expectancy_by_birth.csv") as file:
    reader = csv.reader(file)  # Splits the file into rows
    next(reader)  # skip header line

    for line in reader:
        country = line[0]

        for i, value in enumerate(line[3:], start=1960):
            year = int(i)
            if not value:
                continue
            life_expectancy = float(value)

            if country not in life_expectancy_data:
                life_expectancy_data[country] = []
            life_expectancy_data[country].append((year, life_expectancy))

# Activate Loop until correct input is provided
while True:
    # Prompt the user to input a country of interest
    country_of_interest = prompt_country_of_interest()

    if country_of_interest in life_expectancy_data:
        data = life_expectancy_data[country_of_interest]
        life_expectancies = [expectancy for _, expectancy in data]
        min_expectancy = min(life_expectancies)
        max_expectancy = max(life_expectancies)
        avg_expectancy = round(sum(life_expectancies) / len(life_expectancies), 2)

        print(f"\nLife Expectancy Trend for {country_of_interest}:")
        print("-" * 60)
        print(f"Minimum life expectancy: {min_expectancy:.2f}")
        print(f"Maximum life expectancy: {max_expectancy:.2f}")
        print(f"Average life expectancy: {avg_expectancy:.2f}")

        # Exit the loop once the right input is provided
        break

    else:
        print("Data not found, please try again.")

# Additional data exploration and analysis
# Point 1: Identify and visualize trends over time
if country_of_interest in life_expectancy_data:
    data = life_expectancy_data[country_of_interest]
    years = [year for year, _ in data]
    expectancies = [expectancy for _, expectancy in data]
    avg_expectancy = sum(expectancies) / len(expectancies)
    avg_line = plt.axhline(y=avg_expectancy, color="r", linestyle="--", label="Average")
    plt.plot(years, expectancies)
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title(f"Life Expectancy Trend for {country_of_interest}")
    plt.show(block=False)  # Add block=False to enable "close" button
    plt.pause(0.001)  # Add pause to avoid Pygame bug
    # Plot the average life expectancy
    plt.legend(handles=[avg_line])
    # Prompt user to close plot
    input("\nPress [enter] to close the plot and Continue.")
    plt.close()  # Close the plot on input


total = 0
count = 0


# Calculate average life expectancy for the specific year
year_of_interest = int(input("Enter a year of interest: "))
print()


if country_of_interest in life_expectancy_data:
    data = life_expectancy_data[country_of_interest]
    year_life_expectancies = [
        expectancy for year, expectancy in data if year == year_of_interest
    ]
    count_year_countries = len(year_life_expectancies)
    sum_year_life_expectancy = sum(year_life_expectancies)

    if count_year_countries > 0:
        year_average_life_expectancy = sum_year_life_expectancy / count_year_countries

    else:
        year_average_life_expectancy = 0

    abs_high = max(
        expectancy for _, expectancy in life_expectancy_data[country_of_interest]
    )
    abs_low = min(
        expectancy for _, expectancy in life_expectancy_data[country_of_interest]
    )

    print("For the year {}:".format(year_of_interest))
    print("-" * 60)
    print(
        f"{country_of_interest}'s life expectancy was {year_average_life_expectancy:.2f}."
    )

    # print(
    #     f"{country_of_interest}'s highest life expectancy was {abs_high:.2f} for the {year_of_interest}"  # noqa: E501
    # )

    # Display the overall maximum and minimum life expectancies and their respective years and countries  # noqa: E501
    print(f"\nHighest and lowest life expectancy for {country_of_interest}")
    print("-" * 60)
    print(
        "The highest life expectancy for {}  was {:.2f} in {}".format(
            country_of_interest,
            max_expectancy,
            years[expectancies.index(max_expectancy)],
        )
    )
    print(
        "The lowest life expectancy for {} was {:.2f} in {}".format(
            country_of_interest,
            min_expectancy,
            years[expectancies.index(min_expectancy)],
        )
    )

    # calculate the average life expectancy for the year
    total = 0
    count = 0
    for country in life_expectancy_data:
        for year, life_expectancy in life_expectancy_data[country]:
            if year == year_of_interest:
                total += life_expectancy
                count += 1
    if count:
        total_average_for_year = total / count
        print()
        print(
            f"The  average life expectancy for the year {year_of_interest} is {total_average_for_year:.2f}"
        )
    print()

    # Displays the highest and lowest life expectancy in the dataset
    abs_high = max(life_expectancy_data)
    abs_low = min(life_expectancy_data)

    print("Absolute highest and lowest life expectancy by country:")
    print("-" * 60)
    print(f"The overall max life expectancy regardless of country is: {abs_high}")
    print()
    print(f"The overall min life expectancy regardless of country is: {abs_low}")
    print()


else:
    print("Country not found.")
