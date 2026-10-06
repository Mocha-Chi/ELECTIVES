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
    if len(grades) != 0: # to rpevent index error, if index 0 and subtracted 1, will be -1 which doesn't exist in py's 0-index sys
        print(f"Making subject #{len(grades)}, previous was {list(grades.items())[len(grades) - 1]}.)")
    name = input(f"input subject #{len(grades)+1} name: ") # asking simple questions to user, find a way to make this more user friendly
    percentage = input(f"Input subject #{len(grades)+1} percentage: ")
    grades[name] = percentage # adds it to main dictionary
    answer = input(f"Finish with {len(grades)} subjects? Y/N: ")
    if answer == "Y": 
        end = True
