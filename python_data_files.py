# ==================================
# DAY 2 - PYTHON + TITANIC + MARKS DATASET
# ==================================

import csv

# ==============================
# 1. LIST COMPREHENSION
# ==============================
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)


# ==============================
# 2. DICTIONARY COMPREHENSION
# ==============================
squares = {n: n**2 for n in range(1,6)}
print("Squares:", squares)


# ==============================
# 3. LAMBDA FUNCTION (SORT)
# ==============================
students = [("A", 80), ("B", 95), ("C", 70)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted Students:", sorted_students)


# ==============================
# 4. MAP FUNCTION
# ==============================
names = ["manju", "ravi", "priya"]
upper_names = list(map(str.upper, names))
print("Uppercase Names:", upper_names)


# ==============================
# 5. FILTER FUNCTION
# ==============================
words = ["apple", "cat", "banana", "dog", "orange"]
long_words = list(filter(lambda x: len(x) > 4, words))
print("Long Words:", long_words)


# ==============================
# 6. TXT FILE ANALYSIS
# ==============================
try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    print("Lines:", len(lines))
    print("Words:", sum(len(line.split()) for line in lines))

except FileNotFoundError:
    print("sample.txt not found")


# ==============================
# 7. ERROR HANDLING
# ==============================
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Execution completed")


# ==============================
# 8. MARKS CSV FILTER (NEW ADDED TASK)
# ==============================
try:
    with open("marks.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("\nStudents with marks > 70:\n")

        for row in reader:
            try:
                if float(row["marks"]) > 70:
                    print(row["name"], "-", row["marks"], "-", row["subject"])
            except:
                continue

except FileNotFoundError:
    print("marks.csv not found")


# ==============================
# 9. TITANIC CSV FILTER (TASK PART)
# ==============================
try:
    with open("titanic.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("\nPassengers with Fare > 50:\n")

        for row in reader:
            try:
                if row["Fare"] != "" and float(row["Fare"]) > 50:
                    print(row["Name"], "-", row["Fare"])
            except:
                continue

except FileNotFoundError:
    print("titanic.csv not found")


# ==============================
# 10. MAIN TASK - CLEAN TITANIC DATA
# ==============================
input_file = "titanic.csv"
output_file = "cleaned_titanic.csv"

try:
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow([h.strip().lower() for h in header])

        for row in reader:

            cleaned_row = [col.strip().lower() for col in row]

            if "" in cleaned_row:
                continue

            writer.writerow(cleaned_row)

    print("\nTitanic CSV Cleaning Completed Successfully")

except FileNotFoundError:
    print("titanic.csv not found")