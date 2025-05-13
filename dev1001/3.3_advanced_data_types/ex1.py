# Tuples Exercise

# Student Info: (ID, Name, Major)
student_record = (101, "Alice Wonderland", "Computer Science")

# 1. Access and print the student's name.
print(f"Student's Name: {student_record[1]}")
# 2. Create a new tuple that includes the student's current term.
# new_student_record = student_record + ("Term One",)
new_student_record = (*student_record, 1)
print(new_student_record)
print(student_record)
#       Remember, tuples are immutable, so you'll create a NEW one.
#       Hint: You can concatenate tuples using '+'
#       (Challenge) Use unpack operator instead of concatenation.
# 3. Unpack the original student_record into three separate variables.
id, Name, Major = student_record
id, Name, Major, Term = new_student_record
print(id)
print(Name)
print(Major)
print(Term)
# 4. Use the slice operator to extract the student name only.
print(student_record[1:2])

# 