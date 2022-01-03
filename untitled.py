# @TODO: Import and csv library
from pathlib import Path
import csv

# @TODO: Check the current directory where the Python program is executing from

# Check the current directory where the Python program is executing from
print(f"Current Working Directory: {Path.cwd()}")
# set the file path
csvpath = Path('budget_data.csv')
