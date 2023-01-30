# Import path method from pathlib
from pathlib import Path
# Allows us to use excel functions
import csv

# Creating a function Overheads_Calculator() 
def Overheads_Calculator():
    """
    This function finds the Highest Overhead Category using the data in Overheads.csv
    It then returns the Highest Overhead Category, along with its percentage

    """
    # Extending file path to with the use of '/'
    file_path = Path.cwd() / "Project_Group_1" / "csv_reports" / "Overheads.csv"
    Checker = [] 
    Loop2 = []
    # Opening the created file and reading the data from the csv file, "Overheads.csv"
    with file_path.open(mode="r",newline="") as file:
        reader = csv.reader(file) # This will allow for the iteration of the excel file
        next(reader) # Removing the headers for the respective columns in the excel file
        # Using a for loop to go through the data in the excel file
        for line in reader:
            Loop2.append(line) # Appending data to Loop2 to be used as a second loop to check the highest overheads name

    # Opening the created file and reading the data from the csv file, "Overheads.csv"
    with file_path.open(mode= "r", newline="") as file:
        reader = csv.reader(file) # This will allow for the iteration of the excel file
        next(reader) # Removing the headers for the respective columns in the excel file
        # Using a for loop to go through the data in the excel file
        for line in reader:
            Checker.append(float(line[1])) # The data appended to Checker is later used to find the highest Overheads expense 
        
        # As the same variable cannot be iterated through twice, we use Loop2 as a substitute to go through the data in Excel file again
        for value in Loop2:
            # Conditional Statement where if the expense  is the same as the highest expense in list "Checker" which is the same data that we have in Loop 2
            if float(value[1]) == float(max(Checker)):
                return (f"[HIGHEST OVERHEADS] {value[0].upper()}: {value[1]}%") # We return the Overhead Category along with the percentage of the condition is fulfilled



   

            


