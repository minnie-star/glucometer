import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import tkinter as tk
from glucometer.gui_glucometer import load_and_plot

class TestLoadAndPlot(unittest.TestCase):
    @patch("glucometer.gui_glucometer.filedialog.askopenfilename")
    @patch("glucometer.gui_glucometer.pd.read_csv")
    @patch("glucometer.gui_glucometer.plt.figure")
    @patch("glucometer.gui_glucometer.plt.plot")
    @patch("glucometer.gui_glucometer.plt.xlabel")
    @patch("glucometer.gui_glucometer.plt.ylabel")
    @patch("glucometer.gui_glucometer.plt.title")
    def test_load_and_plot_valid_file(
        self, mock_title, mock_ylabel, mock_xlabel, mock_plot, mock_figure, mock_read_csv, mock_askopenfilename
    ):
        # Mock the file dialog to return a valid file path
        mock_askopenfilename.return_value = "glucose_data.csv"

        # Mock the pandas read_csv to return a DataFrame
        mock_df = pd.DataFrame({
            "blood glucose": [100, 120, 140],
            "date": ["2023-01-01", "2023-01-02", "2023-01-03"]
        })
        mock_read_csv.return_value = mock_df

        # Create a dummy Tkinter root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Call the function
        load_and_plot()

        # Assertions
        mock_askopenfilename.assert_called_once_with(filetypes=[("CSV Files", "glucose_data.csv")])
        mock_read_csv.assert_called_once_with("glucose_data.csv")
        mock_figure.assert_called_once_with(figsize=(6, 4))
        mock_plot.assert_called_once_with(
            mock_df["blood glucose"], mock_df["date"], marker="o", linestyle="-", color="blue"
        )
        mock_xlabel.assert_called_once_with("blood glucose")
        mock_ylabel.assert_called_once_with("date")
        mock_title.assert_called_once_with("Blood Glucose Trend")

    @patch("glucometer.gui_glucometer.filedialog.askopenfilename")
    def test_load_and_plot_no_file_selected(self, mock_askopenfilename):
        # Mock the file dialog to return no file
        mock_askopenfilename.return_value = ""

        # Create a dummy Tkinter root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Call the function
        load_and_plot()

        # Assertions
        mock_askopenfilename.assert_called_once_with(filetypes=[("CSV Files", "glucose_data.csv")])

if __name__ == "__main__":
    unittest.main()