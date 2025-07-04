"""
Author: Minenhle Nkanyezi Hlongwane
Purpose: Blood Glucose Meter
"""

import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from blood_glucose_meter import (
    read_glucose_data, write_glucose_data, calculate_average_glucose,
    find_min_glucose, find_max_glucose, 
)
import datetime

def load_csv_data(filepath):
    
    data = []
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'date': datetime.datetime.strptime(row['date'], '%Y-%m-%d'),
                'glucose_level': float(row['glucose_level'])
            })
    return data


def main():
    root = tk.Tk()
    root.title("Blood Glucose Tracker")
    
    # Functionality for GUI
    def add_glucose_entry():
        try:
            date = datetime.datetime.strptime(entry_date.get(), '%Y-%m-%d')
            glucose_level = float(entry_glucose.get())
            new_entry = {'date': date.strftime('%Y-%m-%d'), 'glucose_level': glucose_level}
            write_glucose_data('glucose_data.csv', new_entry)
            messagebox.showinfo("Success", "New glucose entry added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid data format. Ensure date is YYYY-MM-DD and glucose level is numeric.")

    def display_statistics():
        try:
            data = read_glucose_data('glucose_data.csv')
            avg = calculate_average_glucose(data)
            min_glucose = find_min_glucose(data)
            max_glucose = find_max_glucose(data)
            stats_label.config(text=f"Average: {avg:.1f}, Min: {min_glucose}, Max: {max_glucose}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate statistics: {e}")


    # Input section for new entries
    frame_input = ttk.LabelFrame(root, text="Add Glucose Entry")
    frame_input.pack(pady=10, padx=10, fill="x")

    ttk.Label(frame_input, text="Date (YYYY-MM-DD):").pack(pady=5)
    entry_date = ttk.Entry(frame_input)
    entry_date.pack(pady=5)

    ttk.Label(frame_input, text="Glucose Level:").pack(pady=5)
    entry_glucose = ttk.Entry(frame_input)
    entry_glucose.pack(pady=5)

    ttk.Button(frame_input, text="Add Entry", command=add_glucose_entry).pack(pady=10)

    # Display section for statistics
    frame_stats = ttk.LabelFrame(root, text="Statistics")
    frame_stats.pack(pady=15, padx=15, fill="x")

    ttk.Button(frame_stats, text="Show Statistics", command=display_statistics).pack(pady=10)
    stats_label = ttk.Label(frame_stats, text="Average: -, Min: -, Max: -")
    stats_label.pack(pady=15)
 
    

# Run the application
    root.mainloop()

# Call the main function to execute the program
if __name__ == "__main__":
  main()