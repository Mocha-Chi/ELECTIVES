# main, edit this, not master branch.

# vars
grades = {
    # default is empty, user must manually add both name and percentage of grade
}
name = None
percentage = None



# brain

print("----- GRADE CALCULATOR -----")
name = input(f"INPUT SUBJECT #{len(grades)+1} NAME: ")
percentage = input(f"INPUT SUBJECT #{len(grades)+1} PERCENTAGE: ")
grades[name] = percentage

print(grades)
