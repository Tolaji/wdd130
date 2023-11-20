# Importing necessary modules
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from datetime import datetime
import math
import random
import time
import os

# Class for calculating tire volume
class TireVolumeCalculator:
    # Constructor to initialize width, aspect_ratio, and diameter
    def __init__(self, width, aspect_ratio, diameter):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.diameter = diameter

    # Method to calculate tire volume
    def calculate_tire_volume(self):
        pi = math.pi
        volume = (pi * (self.width**2) * self.aspect_ratio * (self.width * self.aspect_ratio + 2540 * self.diameter)) / 10000000000
        return volume

# Class for getting current date and time
class CurrentDateAndTime:
    # Static method to get current date and time
    @staticmethod
    def get_current_date():
        today = datetime.today()
        return today.strftime("%Y-%m-%d %H:%M:%S")

# Class for fetching online tire prices
class OnlineTirePricesFetch:
    # Embedded list of URLs for tire prices
    EMBEDDED_URLS = [
        "https://www.discounttiredirect.com/",
        "https://simpletire.com/S",
        "https://www.goodyear.com/",
        "https://www.michelinman.com/",
        "https://www.walmart.com/cp/auto-tires/1077064"
    ]

    # Constructor to initialize variables and prompt user for options
    def __init__(self):
        self.visited_urls = set()
        self.user_agent = "Mozilla/5.0"
        self.max_depth = 5 # Default value for maximum depth of url to crawl
        self.urls = self.EMBEDDED_URLS

        # Prompt the user to choose between embedded list and personal input
        choice = input("Do you want to use the embedded list of sites? (y/n): ").lower()
        if choice == "y":
            self.urls = self.EMBEDDED_URLS  # Predefined list urls
            respect_robots = input("Respect robots.txt rules? (y/n): ").lower()
            if respect_robots != "y":
                print("Warning: You chose not to respect robots.txt rules.")
        elif choice == "n":
            self.prompt_user_for_urls()

    # Method to prompt user for URLs
    def prompt_user_for_embedded_urls(self):
        num_urls = int(input("How many URLs do you want to provide for the embedded list? "))
        for i in range(num_urls):
            url = input(f"Enter URL {i + 1}: ").strip()
            self.urls.append(url)

    # Method to prompt user for maximum depth of crawl
    def prompt_user_for_max_depth(self):
        while True:
            try:
                # Prompt user for input
                user_input = int(input("Enter the maximum depth to crawl: "))

                # Check if user_input is a positive integer and within valid range
                if user_input <= 0:
                    print("Please enter a positive integer.")
                elif user_input > 5:
                    print("Maximum depth cannot exceed 5.")
                else:
                    # Assign valid input to self.max_depth and exit loop
                    self.max_depth = user_input
                    break
            except ValueError:
                # Handle ValueError if user enters non-integer input
                print("Invalid input. Please enter a valid integer.")

    # Method to prompt user for custom list of URLs
    def prompt_user_for_urls(self):
        """Prompt user for a list of URLs to scrape."""
        urls = []
        while len(urls) < 5:
            url = input(f"Enter URL {len(urls)+1} (or press Enter to finish): ").strip()
            if url:
                urls.append(url)
            else:
                break
        self.urls = urls  # Assign the user-provided URLs to self.urls

    # Method to check if a URL can be fetched
    def _can_fetch_url(self, url):
        """Check if the URL can be fetched."""
        parsed_url = urlparse(url)
        respect_robots = input("Respect robots.txt rules? (y/n): ").lower() == "y"

        if parsed_url.scheme not in ["http", "https"]:
            return False
        elif "/search?" in parsed_url.path:
            return False
        elif respect_robots:
            rp = RobotFileParser()
            rp.set_url(f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt")
            rp.read()
            return rp.can_fetch(self.user_agent, url)
        else:
            return True

    # Method to prompt user for type of information to extract
    def _prompt_information_type(self):
        """Prompt user to choose the type of information to extract."""
        print("\n INFORMATION TO EXTRACT")
        print("-" * 30)
        print("Choose the type of information you want to extract:")
        print("1. Tire width")
        print("2. Tire Aspect Ratio")
        print("3. Wheel diameter")
        print("4. Tire Price")

        info_list = []
        while True:
            user_choice = input("Enter your choice (comma-separated): ")
            print("If no choice, Press 'Enter' to proceed")
            if user_choice:
                info_list.extend(user_choice.split(","))
            else:
                break

        return info_list

    # Method to prompt user for retry or skip decision in case of error
    def _prompt_retry_or_skip(self, url, retry_count):
        """Prompt user for retry or skip decision in case of error."""
        while True:
            choice = input(f"An error occurred. Retry ({retry_count} retries left) or skip URL '{url}'? (r/s): ")
            if choice.lower() in ["r", "s"]:
                return choice.lower()
            print("Invalid choice. Please enter 'r' to retry or 's' to skip.")
            
    # Method to crawl a single URL and extract information
    def crawl_url(self, url, delay_range, storage_option):
        """Crawl a URL and extract information."""
        self._crawl_url(url, 0, delay_range, storage_option)
    
    # Method to crawl a list of URLs and extract information
    def crawl_urls(self, delay_range, storage_option):
        """Crawl a list of URLs and extract information."""
        for url in self.urls:
            self._crawl_url(url, 0, delay_range, storage_option)
            choice = input("Do you want to input another URL to crawl? (y/n): ").lower()
            if choice != "y":
                break
            
    def _prompt_retry_or_exit(self):
        while True:
            choice = input("An error occurred. Do you want to try another URL? (y/n): ")
            if choice.lower() == "y":
                return True
            elif choice.lower() == "n":
                return False
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
     
    # Recursive method to crawl a URL and extract information
    
    def _crawl_url(self, url, depth, delay_range, storage_option, retry_count=3):
        """Recursively crawl a URL and extract information."""
        if depth > self.max_depth:
            return

        if url in self.visited_urls:
            return

        if not self._can_fetch_url(url):
            print(f"Cannot fetch URL: {url}. Skipping.")
            return

        try:
            print(f"Crawling URL: {url}")
            response = requests.get(url, headers={"User-Agent": self.user_agent})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to crawl url: {url} due to a network issue: {e}")
            if retry_count > 0:
                retry = self._prompt_retry_or_exit()
                if retry:
                    self._crawl_url(url, depth, delay_range, storage_option, retry_count - 1)
                else:
                    return
            else:
                print("Max retries reached. Skipping URL.")
                return
        except Exception as e:
            print(f"An error occurred while trying to crawl url: {url}: {e}")
            return

        self.visited_urls.add(url)
        soup = BeautifulSoup(response.content, "html.parser")

        extraction_functions = {
            "1": self._extract_tire_width,
            "2": self._extract_tire_aspect_ratio,
            "3": self._extract_tire_diameter,
            "4": self._extract_tire_price,
        }

        information_types = self._prompt_information_type()
        choices = input("Enter your choice (comma-separated): ")
        types_to_extract = information_types + choices.split(",")

        if not types_to_extract:
            print("No information types selected. Exiting.")
            return

        for information_type in types_to_extract:
            if information_type in extraction_functions:
                try:
                    info = extraction_functions[information_type](soup, url)
                    self.store_data(url, info, information_type, storage_option)
                except Exception as e:
                    print(f"An error occurred while extracting information for {information_type}: {e}")
                    if retry_count > 0:
                        choice = self._prompt_retry_or_skip(url, retry_count)
                        if choice == "r":
                            self._crawl_url(url, depth, delay_range, storage_option, retry_count - 1)
                        elif choice == "s":
                            print(f"Skipping URL: {url}")
                            return
            else:
                print(f"Invalid option: {information_type}. Skipping.")

        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href and href.startswith("http"):
                delay = random.uniform(delay_range[0], delay_range[1])
                time.sleep(delay)
                self._crawl_url(href, depth + 1, delay_range, storage_option, retry_count)

        delay = random.uniform(delay_range[0], delay_range[1])
        time.sleep(delay)

    # Method to prompt user for retry or skip decision in case of error
    def _prompt_retry_or_skip(self, url, retry_count):
        """Prompt user for retry or skip decision in case of error."""
        while True:
            choice = input(f"An error occurred. Retry ({retry_count} retries left) or skip URL '{url}'? (r/s): ")
            if choice.lower() in ["r", "s"]:
                return choice.lower()
            print("Invalid choice. Please enter 'r' to retry or 's' to skip.")

    # Method to extract tire width information
    def _extract_tire_width(self, soup, url):
        """Extract tire width information."""
        width_element = soup.find("span", {"class": "width"})
        if width_element is not None:
            return {"Tire Width": width_element.text.strip()}
        else:
            print(f"Tire width not found on {url}")
            return None

    # Method to extract tire aspect ratio information
    def _extract_tire_aspect_ratio(self, soup, url):
        """Extract tire aspect ratio information."""
        aspect_ratio_element = soup.find("span", {"class": "aspect_ratio"})
        if aspect_ratio_element is not None:
            return {"Tire Aspect Ratio": aspect_ratio_element.text.strip()}
        else:
            print(f"Tire aspect ratio not found on {url}")
            return None

    # Method to extract wheel diameter information
    def _extract_tire_diameter(self, soup, url):
        """Extract wheel diameter information."""
        diameter_element = soup.find("span", {"class": "diameter"})
        if diameter_element is not None:
            return {"Wheel Diameter": diameter_element.text.strip()}
        else:
            print(f"Wheel diameter not found on {url}")
            return None

    # Method to extract tire price information
    def _extract_tire_price(self, soup, url):
        """Extract tire price information."""
        price_element = soup.find("span", {"class": "price"})
        if price_element is not None:
            return {"Tire Price": price_element.text.strip()}
        else:
            print(f"Tire price not found on {url}")
            return None

    # Method to store extracted data to a text file
    def store_data(self, url, info, information_type, storage_option):
            """Store extracted data to a text file."""
            with open(f"tire_prices_{storage_option}.txt", "a") as file:
                file.write(f"URL: {url}\n")
                for key, value in info.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

    # Iterator methods for the class
    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.urls):
            raise StopIteration
        else:
            url = self.urls[self.current_index]
            self.current_index += 1
            return url

# Class for handling tire purchase
class TirePurchase:
    # Method to ask user if they want to buy tires
    @staticmethod
    def ask_to_buy_tires():
        """Ask user if they want to buy tires."""
        user_input = input("Do you want to buy tires with these dimensions? (yes/no): ")
        return user_input.lower() == "y"

    # Method to get user's name and phone number
    @staticmethod
    def get_user_information():
        """Get user's name and phone number."""
        name = input("Please enter your name: ")
        phone_number = input("Please enter your phone number: ")
        return name, phone_number

# Class for handling user input
class UserInput:
    # Method to get user dimensions
    @staticmethod
    def get_user_dimensions():
        width = float(input("Enter the width of the tire in mm (e.g. 205): "))
        aspect_ratio = int(input("Enter the aspect ratio of the tire (e.g. 60): "))
        diameter = int(input("Enter the diameter of the wheel in inches (e.g. 15): "))
        return width, aspect_ratio, diameter

# Main program
online_tire_prices_fetch = OnlineTirePricesFetch()

try:
    online_tire_prices_fetch.crawl_urls((1, 3), "user_input")
    while True:
        # Get user dimensions
        width, aspect_ratio, diameter = UserInput.get_user_dimensions()

        # Calculate tire volume
        tire_volume_calculator = TireVolumeCalculator(width, aspect_ratio, diameter)
        tire_volume = tire_volume_calculator.calculate_tire_volume()

        # Print tire volume
        print(f"The volume of the tire is {tire_volume:.2f} liters.")

        # Get current date
        current_date = CurrentDateAndTime.get_current_date()

        # Ask if user wants to buy tires
        if TirePurchase.ask_to_buy_tires():
            name, phone_number = TirePurchase.get_user_information()

            # Append data to volume.txt
            with open("volume.txt", "a") as file:
                file.write(f"Current Date: {current_date}\n")
                file.write(f"Name: {name}\nPhone Number: {phone_number}\n")
                file.write(f"Tire Width: {width} mm\n")
                file.write(f"Tire Aspect Ratio: {aspect_ratio}\n")
                file.write(f"Wheel Diameter: {diameter} inches\n")
                file.write(f"Tire Volume: {tire_volume:.2f} liters\n\n")

            # Notify user
            print(f"Data has been successfully written to volume.txt at path: {os.path.abspath('volume.txt')}")
        else:
            break

except Exception as e:
    print(f"An error occurred: {e}")
