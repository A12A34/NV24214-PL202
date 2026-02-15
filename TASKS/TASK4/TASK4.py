import csv 
with open("TASK4\\TASK4.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["sno", "name", "nvno"])
    writer.writerow([1, "abc", "nv123"])
    writer.writerow([2, "def", "nv456"])

with open("TASK4\\TASK4.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)