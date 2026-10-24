students = {"arraw":75,"priya":83,"max":91,"arya":23,"adwid":25}

total = 0
for score in students.values():
    total = total + score
average = total/len(students)
print(average)