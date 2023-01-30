# Import path method from pathlib
from pathlib import Path
# Allows us to use excel functions
import csv

# Creating the function Profit_Calculator()
def Profit_Calculator():
    """
    This function checks whether the Profit for the current day is lower than the previous day.
    It returns the days, along with the net difference between the current and previous day if the profit for the current day is lower than the previous day

    """
    Checked_Day_Profit = 0 # This variable allows us to compare the Profit between the current and previous day
    Checker = True # Allow us to find out whether there is no event of current day Profit being lower than the previous day.
    Data = [] # This List will be used to append data from csv file and will be returned so that it can be displayed in the text file, "summary_report.txt"
    # Extending file path to with the use of '/'
    file_path = Path.cwd() / "Project_Group_1" / "csv_reports" / "Profit and Loss.csv"
    
    # Opening the created file and reading the data from the csv file, "Profit and Loss.csv"
    with file_path.open(mode="r", newline ="") as file:
        Checked_Day_Profit = float(Checked_Day_Profit) # Converting the class of Checked_Day_Profit to float type
        reader = csv.reader(file) # This will allow for the iteration of the excel file
        next(reader) # Removing the headers for the respective columns in the excel file
        # Using a for loop to go through the data in the excel file
        for line in reader:
            Day = float(line[0])
            # Conditional Statements with two conditions
            # If the Profit for the current day is lower than that of the previous day
            if Checked_Day_Profit < float(line[4]):
                Checked_Day_Profit = float(line[4])
            # If the Profit for the current day is higher than that of the previous day
            elif Checked_Day_Profit > float(line[4]): 
                Net_Profit = Checked_Day_Profit - float(line[4]) # Formula we use to calculate the change in Profit
                Data.append(f"[PROFIT DEFICIT] DAY: {Day}, AMOUNT: {Net_Profit}") # Appending the Net Profit to the the list "Data"
        if Data == []:
            # If there is no instances where the Profit for the current day is lower than the Profit for the previous day
            Checker == False
        #  In the event of having no instances, it will return an indication that there were no instances of Profit for the current day being lower than the Profit for the previous day
        if Checker == False:
            return ("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        else: # Otherwise, if there were such instances, return the data
            return Data