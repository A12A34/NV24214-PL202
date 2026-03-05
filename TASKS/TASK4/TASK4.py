import csv
from pathlib import Path

csv_path = Path(__file__).with_name("TASK4.csv")

with csv_path.open("w", newline='') as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["sno", "name", "nvno"])
    writer.writerow([1, "abc", "nv123"])
    writer.writerow([2, "def", "nv456"])

with csv_path.open("r", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
