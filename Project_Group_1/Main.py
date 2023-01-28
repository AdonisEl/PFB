import Cash_On_Hand, Overheads, Profit_Loss

from pathlib import Path
file_path = Path.cwd() / "Project_Group_1" / "summary_report.txt"

Overheads_Report = Overheads.Overheads_Calculator()
COH_Report = Cash_On_Hand.COH_Calculator()
Profit_Report = Profit_Loss.Profit_Calculator()


with file_path.open(mode="a",encoding= "UTF-8") as file:
    file.write(f"{Overheads_Report}")
    for line in COH_Report:
        file.write(f"\n{line}")
    for line in Profit_Report:
        file.write(f"\n{line}")

    
    
    


# for line in Overheads_Report:
#         print(f"{line}")
# for line in COH_Report:
#         print(f"{line}")
# for line in Profit_Report:
#         print(f"{line}")