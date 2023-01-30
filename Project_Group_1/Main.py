# Importing modules that are required 
import Cash_On_Hand, Overheads, Profit_Loss

# Import path method from pathlib
from pathlib import Path
# Extending file path to with the use of '/'
file_path = Path.cwd() / "Project_Group_1" / "summary_report.txt"
# Creating the file "summary_report.txt"
file_path.touch()

# Calling the functions in respective modules using module.function(), then assigning it to a variable 
Overheads_Report = Overheads.Overheads_Calculator()
COH_Report = Cash_On_Hand.COH_Calculator()
Profit_Report = Profit_Loss.Profit_Calculator()

# Opening the created file and appending the data from the modules:Cash on Hand, Overheads and Profit Loss, into the created file
with file_path.open(mode="a",encoding= "UTF-8") as file:
    file.write(f"{Overheads_Report}")
    for line in COH_Report:
        file.write(f"\n{line}")
    for line in Profit_Report:
        file.write(f"\n{line}")

    
    
    

