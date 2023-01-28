from pathlib import Path
import csv

def Overheads_Calculator():
    """
    This function finds the Highest Overhead Category using the data in Overheads.csv
    It then returns the Highest Overhead Category, along with its percentage

    """
    file_path = Path.cwd() / "Project_Group_1" / "csv_reports" / "Overheads.csv"
    Checker = []
    Loop2 = []

    with file_path.open(mode="r",newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            Loop2.append(line)

    with file_path.open(mode= "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            Checker.append(float(line[1]))
        
        for value in Loop2:
            if float(value[1]) == float(max(Checker)):
                return (f"[HIGHEST OVERHEADS] {value[0].upper()}: {value[1]}%")



   

            


