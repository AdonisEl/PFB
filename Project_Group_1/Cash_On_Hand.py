from pathlib import Path
import csv

def COH_Calculator():
    Checked_COH = 0
    Checker = True
    Data = []
    file_path = Path.cwd() / "Project_Group_1" / "csv_reports" / "Cash On Hand.csv"

    with file_path.open(mode="r", newline = "") as file:
        Checked_COH = float(Checked_COH)
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            Day = float(line[0])
            if Checked_COH < float(line[1]):
                Checked_COH = float(line[1])
            elif Checked_COH > float(line[1]):
                Net_COH = Checked_COH - float(line[1])
                Data.append(f"[CASH DEFICIT] DAY: {Day}, AMOUNT: {Net_COH}")
            else:
                Checker =  False
        
        if Checker == False:
            return ("[CASH SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        else:
            return Data

     