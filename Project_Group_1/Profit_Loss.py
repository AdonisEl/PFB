from pathlib import Path
import csv

def Profit_Calculator():
    """
    This function checks whether the Profit for the current day is lower than the previous day.
    It returns the days, along with the net difference between the current and previous day where the profit for the current day is lower than the previous day

    """
    Checked_Day_Profit = 0
    Checker = True
    Data = []
    file_path = Path.cwd() / "Project_Group_1" / "csv_reports" / "Profit and Loss.csv"

    with file_path.open(mode="r", newline ="") as file:
        Checked_Day_Profit = float(Checked_Day_Profit) 
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            Day = float(line[0])
            if Checked_Day_Profit < float(line[4]):
                Checked_Day_Profit = float(line[4])
            
            elif Checked_Day_Profit > float(line[4]):
                Net_Profit = Checked_Day_Profit - float(line[4])
                Data.append(f"[PROFIT DEFICIT] DAY: {Day}, AMOUNT: {Net_Profit}")
            else:
                Checker == False
        if Checker == False:
            return ("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        else:
            return Data