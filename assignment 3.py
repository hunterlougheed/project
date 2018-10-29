courses = 0

while (courses < 5) or (courses > 8):
    courses = int(input("How many courses have you taken: ")) #dosent allow the secleting course of 5 and 8
print("") #for formatting

total = 0.0

for t in range(courses):
    grade = float(input("What grade did you receive in course %d: " % (i+1))) #asks user for their grade in each of the courses
    total += grade

average = total/courses #this calculates the average

if average >= 79.5:
    average = str(round(average, 2)) + "%"
    print("Congratulations you have earned the principals award with an average of %s" % average)