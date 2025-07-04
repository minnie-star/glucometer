"""
Author: Minenhle Nkanyezi Hlongwane
Purpose: Blood Glucose Meter Program Test 
"""

from pathlib import Path
import pytest
import datetime
from blood_glucose_meter import (
    read_glucose_data, write_glucose_data, calculate_average_glucose,
    find_min_glucose, find_max_glucose
)

# Sample data for testing
sample_data = [
    {'date': datetime.datetime(2025, 4, 10), 'glucose_level': 110},
    {'date': datetime.datetime(2025, 4, 11), 'glucose_level': 140},
    {'date': datetime.datetime(2025, 4, 12), 'glucose_level': 90},
]

# Test for reading glucose data
def test_read_glucose_data():
    data = read_glucose_data('glucose_data.csv')
    assert len(data) > 0, "Data should not be empty."
    assert isinstance(data[0]['glucose_level'], float), "Glucose level should be a float."

# Test for writing glucose data
def test_write_glucose_data(tmp_path):
    file_path = tmp_path / 'glucose_data.csv'
    write_glucose_data(file_path, {'date': datetime.datetime(2025, 4, 13), 'glucose_level': 120})
    data = read_glucose_data(file_path)
    assert len(data) == 1, "Data should have one entry."
    assert data[0]['glucose_level'] == 120, "Glucose level should match."

# Test for calculating average glucose
def test_calculate_average_glucose():
    avg = calculate_average_glucose(sample_data)
    assert round(avg, 2) == 113.33, f"Expected 113.33, but got {avg:.2f}"

# Test for finding minimum glucose
def test_find_min_glucose():
    min_glucose = find_min_glucose(sample_data)
    assert min_glucose == 90, f"Expected 90, but got {min_glucose}"

# Test for finding maximum glucose
def test_find_max_glucose():
    max_glucose = find_max_glucose(sample_data)
    assert max_glucose == 140, f"Expected 140, but got {max_glucose}"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
