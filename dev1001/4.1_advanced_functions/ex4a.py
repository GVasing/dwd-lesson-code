# map() Exercises
#
# Exercise 1
# ----------
# You have a list of product prices.
# Use `map` and a lambda to create a new list where each price
# has a 20% tax added to it (price * 1.20).
# Remember to format the output nicely if you can
# (e.g., to two decimal places, but the core is the map).

prices = [10.99, 5.49, 20.00]

prices_taxed = list(map(lambda x: round(x * 1.20, 2), prices))

print(f"The final prices inclusive of tax comes to {prices_taxed}") 



# Exercise 2
# ----------
# Given a list of scores, use map() to get a list of the grade level for each score.
#
# HD if >=90
# D if >=80
# C if >=70
# P if >=50
# F if <50

scores = [85, 92, 78, 60, 42, 95, 70, 53]

def score_to_grade(score):
    if score >= 90:
        return 'HD'
    elif score >= 80:
        return 'D'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'P'
    else:
        return 'F'
    
grades = map(score_to_grade, scores)
print(scores)
print(list(grades))

# graded_scores = []

# for grade in scores:
#     if grade >= 90:
#         graded_scores.append('HD')
#     elif grade >=80:
#         graded_scores.append('D')
#     elif grade >=70:
#         graded_scores.append('C')
#     elif grade >=50:
#         graded_scores.append('P')
#     elif grade < 50:
#         graded_scores.append('F')

# print(graded_scores)