# @TODO: Import and csv library
from pathlib import Path
import csv

# @TODO: Check the current directory where the Python program is executing from

# Check the current directory where the Python program is executing from
print(f"Current Working Directory: {Path.cwd()}")
# set the file path
csvpath = Path('budget_data.csv')
# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('')
sales_filepath = Path('')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list