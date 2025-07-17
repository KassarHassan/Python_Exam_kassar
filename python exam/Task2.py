# --- Task 2: Define check_grades(grades) ---
def check_grades(grades):             # function takes a list of numeric grades
    for grade in grades:              # iterate over each grade in the list
        if grade >= 75:               # check if grade is at least 75
            print(f"{grade}: Pass")   # print Pass when grade ≥ 75
        else:
            print(f"{grade}: No")     # print No otherwise       
# Test Task 2 with at least 5 grades
sample_grades = [82, 74, 90, 67, 100]  # example list of 5 grades
check_grades(sample_grades)            # call function to show output
print()  # blank line
