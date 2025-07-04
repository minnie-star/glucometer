"""
Author: Minenhle Nkanyezi Hlongwane
Purpose: Blood Glucose Meter
"""

import csv
import datetime
import matplotlib.pyplot as plt


# Function to read glucose data from a CSV file
def read_glucose_data(file_path):
    try:
        data = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    'date': datetime.datetime.strptime(row['date'], '%Y-%m-%d'),
                    'glucose_level': float(row['glucose_level'])
                })
        return data
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading glucose data: {e}")
        return []

# Function to write new glucose data to a CSV file
def write_glucose_data(file_path, glucose_entry):
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'glucose_level'])
            writer.writerow(glucose_entry)
    except Exception as e:
        print(f"Error writing glucose data: {e}")

# Function to calculate average glucose level
def calculate_average_glucose(data):
    try:
        if not data:
            raise ValueError("No data available to calculate average.")
        total = sum(entry['glucose_level'] for entry in data)
        return round(total / len(data), 2)
    except ZeroDivisionError:
        print("Error: Division by zero when calculating average.")
        return 0
    except Exception as e:
        print(f"Error calculating average glucose: {e}")
        return 0

# Function to find the minimum glucose level
def find_min_glucose(data):
    try:
        return min(entry['glucose_level'] for entry in data)
    except ValueError:
        print("Error: No data available to find minimum.")
        return None
    except Exception as e:
        print(f"Error finding minimum glucose: {e}")
        return None

# Function to find the maximum glucose level
def find_max_glucose(data):
    try:
        return max(entry['glucose_level'] for entry in data)
    except ValueError:
        print("Error: No data available to find maximum.")
        return None
    except Exception as e:
        print(f"Error finding maximum glucose: {e}")
        return None

# Function to generate and plot glucose trends
def generate_trend_analysis(data):
    try:
        dates = [entry['date'] for entry in data]
        glucose_levels = [entry['glucose_level'] for entry in data]
        if not dates or not glucose_levels:
            raise ValueError("No data available for trend analysis.")
        plt.plot(dates, glucose_levels, marker='o')
        plt.title("Blood Glucose Trend")
        plt.xlabel("Date")
        plt.ylabel("Glucose Level")
        plt.show()
    except ValueError as ve:
        print(f"Error in trend analysis: {ve}")
    except Exception as e:
        print(f"Error generating trend analysis: {e}")

# Main function
def main():
    try:
        # Call the file and read the file
        file_path = 'glucose_data.csv'
        glucose_data = read_glucose_data(file_path)

        # Adding a new glucose entry
        new_entry = {'date': datetime.datetime.now().strftime('%Y-%m-%d'), 'glucose_level': 120}
        write_glucose_data(file_path, new_entry)

        # Analyzing data
        average = calculate_average_glucose(glucose_data)
        min_glucose = find_min_glucose(glucose_data)
        max_glucose = find_max_glucose(glucose_data)

        print("Glucometer Statistics")
        print(f"Average Glucose Level: {average:.1f}")
        print(f"Minimum Glucose Level: {min_glucose}")
        print(f"Maximum Glucose Level: {max_glucose}")

        # Displaying trends
        generate_trend_analysis(glucose_data)

    except Exception as e:
        print(f"Error in main program: {e}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()