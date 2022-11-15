numberOfCourses = int(input('How many courses do you offer?\n'))
print()

courses = []
grades = []

while len(grades)!= numberOfCourses:
   courseInput = input('Course: ')
   gradeInput = input('Grade: ')
   if gradeInput == "":
      gradeInput = 0
   else:
      gradeInput = int(gradeInput)
   courses+=[courseInput]
   grades+=[gradeInput]
   print()

print()

mean=sum(grades)/numberOfCourses

print(f'    {"Courses Offered":<20}  {"GRADE":<5}')
for x in range(numberOfCourses):
   print(f'{(x+1):>2}  {(courses[x]).title():<20}  {grades[x]:<5}')

print(f'\n--  Average: {mean:.2f}\n')