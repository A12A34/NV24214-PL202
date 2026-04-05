import pandas as pd
import numpy as np

SPAS_data = {
    "Student_ID": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "Name": ["Alice","Bob","Charlie","David","Eve","Frank","Grace","Henry","Ivy","Jack","Kate","Liam","Mia","Noah","Olivia","Peter","Quinn","Rachel","Steve","Tina"],
    "Department": ["Computer Science","Mathematics","Physics","Chemistry","Biology","English","History","Philosophy","Psychology","Sociology","Economics","Business","Engineering","Medicine","Law","Architecture","Art History","Music","Theater","Education"],
    "Maths": np.array([85,92,78,95,88,90,82,89,91,87,84,93,86,94,83,96,81,97,80,98]),
    "Python": np.array([88,95,82,96,90,91,85,92,94,89,87,96,88,97,84,98,83,99,82,100]),
    "Statistics": np.array([90,93,80,97,89,92,84,91,95,88,86,94,87,98,85,99,82,100,81,100]),
    "Attendance": np.array([90,69,65,98,92,94,88,91,96,89,87,45,93,99,70,100,84,100,83,100])
}

SPAS_df = pd.DataFrame(SPAS_data)

# Calculate total and average
SPAS_df["Total"] = SPAS_df["Maths"] + SPAS_df["Python"] + SPAS_df["Statistics"]
SPAS_df["Average"] = SPAS_df["Total"] / 3


# Grade function
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

SPAS_df["Grade"] = SPAS_df["Average"].apply(assign_grade)


if __name__ == "__main__":

    while True:

        print("\nSPAS Student Performance Analysis System")
        print("1. View all student records")
        print("2. Display first 5 and last 5 records")
        print("3. Statistics of subjects")
        print("4. Save data to CSV")
        print("5. Top 3 students")
        print("6. Students with attendance below 75%")
        print("7. Department average marks")
        print("8. Subject highest marks")
        print("9. Students scoring >80 in Python")
        print("10. Grade distribution")
        print("11. Sort students by Average")
        print("12. NumPy operations")
        print("13. Update a student record")
        print("14. Delete a column")
        print("15. Handle missing values")
        print("16. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(SPAS_df)

        elif choice == 2:
            print("\nFirst 5 students")
            print(SPAS_df.head())

            print("\nLast 5 students")
            print(SPAS_df.tail())

        elif choice == 3:

            for col in ["Maths","Python","Statistics"]:

                print(f"\nStatistics for {col}")
                print("Mean:", np.mean(SPAS_df[col]))
                print("Median:", np.median(SPAS_df[col]))
                print("Standard deviation:", np.std(SPAS_df[col]))
                print("Minimum:", np.min(SPAS_df[col]))
                print("Maximum:", np.max(SPAS_df[col]))

        elif choice == 4:

            SPAS_df.to_csv("TASKS\\Project\\SPAS_data.csv", index=False)
            print("CSV file saved")

        elif choice == 5:

            top = SPAS_df.sort_values(by="Average", ascending=False).head(3)
            print(top)

        elif choice == 6:

            low_attendance = SPAS_df[SPAS_df["Attendance"] < 75]
            print(low_attendance)

        elif choice == 7:

            dept_avg = SPAS_df.groupby("Department")["Average"].mean()
            print(dept_avg)

        elif choice == 8:

            highest = SPAS_df[["Maths","Python","Statistics"]].max()
            print(highest)

        elif choice == 9:

            python_high = SPAS_df[SPAS_df["Python"] > 80]
            print(python_high)

        elif choice == 10:

            grades = SPAS_df["Grade"].value_counts()
            print(grades)

        elif choice == 11:

            sorted_students = SPAS_df.sort_values(by="Average", ascending=False)
            print(sorted_students)

        elif choice == 12:

            print("\nNumPy Demonstration")

            math_marks = SPAS_df["Maths"].values

            print("Original array:")
            print(math_marks)

            print("\nMean:", np.mean(math_marks))
            print("Median:", np.median(math_marks))
            print("Std Dev:", np.std(math_marks))
            print("Min:", np.min(math_marks))
            print("Max:", np.max(math_marks))

            print("\nIndexing example")
            print("First element:", math_marks[0])

            print("\nSlicing example")
            print("First five marks:", math_marks[:5])

            print("\nReshape array")
            reshaped = math_marks.reshape(4,5)
            print(reshaped)

            print("\nElement-wise bonus (+5)")
            bonus = math_marks + 5
            print(bonus)

            print("\nStudents scoring above 90")
            print(math_marks > 90)

        elif choice == 13:

            SPAS_df.loc[0,"Attendance"] = 95
            print("Record updated")
            print(SPAS_df.head())

        elif choice == 14:
            temp_df = SPAS_df.drop("Statistics", axis=1)
            print("Column deleted (temporary view)")
            print(temp_df.head())

        elif choice == 15:

            print("Missing values check")
            print(SPAS_df.isnull().sum())

            SPAS_df.fillna(0, inplace=True)
            print("Missing values handled")

        elif choice == 16:

            print("Exiting system")
            break

        else:
            print("Invalid choice")