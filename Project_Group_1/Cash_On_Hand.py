# Import path method from pathlib
from pathlib import Path
# Allows us to use excel functions
import csv

# Creating the function COH_Calculator()
def COH_Calculator():
    """
    This function checks whether the Cash on Hand for the current day is lower than the previous day.
    It returns the days, along with the difference in Cash on Hand between the current and previous day if the Cash on Hand for the current day is lower than the previous day

    """ 
    Checked_COH = 0 # This variable allows us to compare the Cash on Hand between the current and previous day
    Checker = True # Allow us to find out whether there is no event of current day Cash On Hand being lower than the previous day. 
    Data = [] # This List will be used to append data from csv file and will be returned so that it can be displayed in the text file, "summary_report.txt"
    # Extending file path to with the use of '/'
    file_path = Path.cwd() / "Project_Group_1" / "csv_reports" / "Cash On Hand.csv"

    # Opening the created file and reading the data from the csv file, "Cash on Hand.csv"
    with file_path.open(mode="r", newline = "") as file:
        Checked_COH = float(Checked_COH) # Converting the class of Checked_COH to float type 
        reader = csv.reader(file) # This will allow for the iteration of the excel file
        next(reader) # Removing the headers for the respective columns in the excel file
        # Using a for loop to go through the data in the excel file
        for line in reader:
            Day = float(line[0]) # The day of the amount of Cash on Hand
            # Conditional Statements with two conditions
            # If the Cash on Hand of the current day is higher than that of the previous day
            if Checked_COH < float(line[1]): 
                Checked_COH = float(line[1])
            # If the Cash on Hand of the current day is lower than that of the previous day
            elif Checked_COH > float(line[1]): 
                Net_COH = Checked_COH - float(line[1]) # Formula we use to calculate the change in Cash on Hand
                Data.append(f"[CASH DEFICIT] DAY: {Day}, AMOUNT: {Net_COH}") # Appending the Net Cash on Hand to the the list "Data"
        if Data == []:
            # If there is no instances where the Cash on Hand of the current day is lower than the Cash on Hand of the previous day
            Checker =  False
        #  In the event of having no instances, it will return an indication that there were no instances of Cash on Hand of the current day being lower than the Cash on Hand of the previous day
        if Checker == False:
            return ("[CASH SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        else: # Otherwise, if there were such instances, return the data 
            return Data

     