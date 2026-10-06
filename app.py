# main, edit this, not master branch.

# vars
grades = {
    # default is empty, user must manually add both name and percentage of grade
}
name = None
percentage = None
end = False

# brain
print("----- GRADE CALCULATOR -----")
while not end:
    if len(grades) != 0:  # prevent index error when reading the previous subject name
        print(f"Making subject #{len(grades)}, previous was {list(grades.keys())[-1]}.")

    name = input(f"Input subject #{len(grades) + 1} name: ").strip()
    if name is None or name == "":
        print("Invalid name, must be a genuine subject name.")
        continue  # restarts the loop if invalid name is given.

    while True:
        try:
            percentage = float(input(f"Input subject #{len(grades) + 1} percentage: "))
            if percentage > 100 or percentage < 0:
                print("Invalid percentage, must be between 0 and 100.")
                continue  # restarts the loop if invalid percentage is given.
            if 0 <= percentage <= 100:
                break
            print("Invalid percentage, must be between 0 and 100.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue

    grades[name] = percentage  # adds it to main dictionary

    answer = input(f"Finish with {len(grades)} subjects? Y/N: ").strip().upper()
    if answer == "Y":
        end = True

if len(grades) > 0:
    average = sum(grades.values()) / len(grades)  # calculates average of all subjects
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(
        f"""Your average grade is: {average:.2f}% 
Letter_Grade: {letter_grade} - Grades: {grades}"""
    )