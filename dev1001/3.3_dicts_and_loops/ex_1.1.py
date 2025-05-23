# **Create 1.1: Student Report Card Generator**

# *   **Problem:** You need to store and display student grades for several subjects.
# *   **Task:**
#     1.  Create a dictionary where keys are student names (strings) and values are *another dictionary*. This inner dictionary should store subject names (strings) as keys and their corresponding grades (integers, 0-100) as values.
#     2.  Populate this main dictionary with data for at least 3 students, each with at least 3 subjects (e.g., "Math", "Science", "History").
#     3.  Write code that iterates through the main dictionary. For each student, print their name and then list each subject and their grade.
#     4.  Calculate and print the average grade for one specific student of your choice.
# *   **Example Structure:**
#     ```python
#     student_data = {
#         "Alice Wonderland": {"Math": 90, "Science": 85, "Literature": 92},
#         "Bob The Builder": {"Math": 70, "Science": 75, "Workshop": 95},
#         # ... more students
#     }
#     ```
# *   **Advanced Challenge 1.1:**
#     *   After printing each student's report, also identify and print their highest-scoring subject and their lowest-scoring subject. If there are ties, any of the tied subjects is fine.
#     *   *(Hint: You'll need to iterate through the inner dictionary's items and keep track of the max/min score found so far.)*

# Dictionary/List = student names(keys):subjects/grades(dictionary acting as a value)
# Second Dictionary/List = subjects(keys):grades(ints: 0-100)(values)

Students = {
    "Student_1":{"Maths":85 , "English":70 , "P.E.":80 ,},
    "Student_2":{"Maths":60 , "English":95 , "P.E.":70 ,},
    "Student_3":{"Maths":70 , "English":70 , "P.E.":70 ,}
}
for student, grade in Students.items():
    print(f"- {student.replace("_", " ")}: {grade}")

# average = total sum divided by amount
average = 

print(average)

# # 4. `for...in iterable` (dictionary items): Accessing keys and values
# # (Re-using product_prices from dictionary section for context)
# product_prices = {"laptop_stand": 25, "usb_c_hub": 30, "ergonomic_keyboard": 75}
# print("--- For...in iterable (Dictionary items) ---")
# print("Product Pricelist:")
# for product, price in product_prices.items():
#     print(f"- {product.replace('_', ' ').title()}: ${price}")
# print("-" * 20)