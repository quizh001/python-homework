# python-homework
# Unit 2 | Homework Assignment: Automate Your Day Job with Python

## Background

You've made it! It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete the required PyBank Python activity, and if you wish to stretch your skills even further, the optional PyRamen Python activity. Both activities present a real-world situation in which your newfound Python skills will come in handy. These activities are far from easy, though, so expect some hard work ahead!

## Before You Begin

1. Create a new GitHub repo called `python-homework`. Then, clone it to your computer.

2. In your local git repository, create a directory for both of the Python activities. Use folder names that correspond to the activities: **PyBank** and **PyRamen**.

3. In each folder you just created, add a new file called `main.ipynb`. Remember that to create this file you will need to use JupyterLab to correctly generate the .ipynb file format. This will be the main notebook to run for each analysis.

4. Push the above changes to GitHub.

## PyBank (Required)

![Revenue](Images/revenue-per-lead.jpg)

In this activity, you are tasked with creating a Python script for analyzing the financial records of your company. You will be provided with a financial dataset in this file: [budget_data.csv](PyBank/Resources/budget_data.csv). This dataset is composed of two columns, Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset.

* The net total amount of Profit/Losses over the entire period.

* The average of the changes in Profit/Losses over the entire period.

* The greatest increase in profits (date and amount) over the entire period.

* The greatest decrease in losses (date and amount) over the entire period.

Your resulting analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

Your final script should print the analysis to the terminal and export a text file with the results.


## Resources

* [Stack Overflow](https://www.stackoverflow.com): A wealth of community-driven questions and answers, particularly effective for IT solution seekers.

* [Python Basics](https://pythonbasics.org/): Contains example materials and exercises for the Python 3 programming language.

* [Python Documentation](https://docs.python.org/3/): Official Python documentation

---

## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down you tasks into discrete mini-objectives. This will be a *much* better course of action than attempting to Google search for a miracle.

* As you will discover, for some of these activities, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct as data analysts is often to head straight to Excel, creating scripts in Python can provide us with more robust options for handling "big data."

* Your scripts should work for each dataset provided. Run your script for each dataset separately to make sure that the code works for different data.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

* **Start early**, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." Come prepared to show your effort and thought patterns, we'll be happy to help along the way.

* Always commit your work (and do it often!) and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

## Submission

* Upload homework files to your GitHub repo.

* Submit the link to your GitHub repo on Bootcamp Spot.

---
### Requirements

#### Set Up Project  (35 points)

##### To receive all points, you must:

* Create a GitHub repo named: `python-homework`. (10 points)
* Create a directory within your repository to store the activity. (5 points)
* Add a notebook file named `main.ipynb` to your directory. (10 points)
* Update the repository with your latest changes. (10 points)

#### Analysis and Calculations (35 points)

##### To receive all points, your code must:

* Include a calculation of the total number of months in the dataset. (2 points)
* Calculate the net total amount of Profit/Losses over the entire period. (3 points)
* Calculate the average of the changes in Profit/Losses over the entire period. (5 points)
* Calculate the greatest increase in Profits over the entire period (Date and Amount). (10 points)
* Calculate the greatest decrease in Losses over the entire period (Date and Amount). (10 points)
* Print the analysis and export the analysis to a text file that contains the final results. (5 points)

#### Coding Conventions and Formatting (10 points)

##### To receive all points, your code must:

* Place imports at the beginning of the file, just after any module comments and docstrings and before module globals and constants. (3 points)
* Name functions and variables with lowercase characters and with words separated by underscores. (2 points)
* Follow Don't Repeat Yourself (DRY) principles by creating maintainable and reusable code. (3 points)
* Use concise logic and creative engineering where possible. (2 points)

#### Deployment and Submission (10 points)

##### To receive all points, you must:

* Submit a link to a GitHub repository that’s cloned to your local machine and contains your files. (5 points)
* Include appropriate commit messages in your files. (5 points)

#### Code Comments (10 points)

##### To receive all points, your code must:

* Be well commented with concise, relevant notes that other developers can understand. (10 points)

---

© 2021 Trilogy Education Services

