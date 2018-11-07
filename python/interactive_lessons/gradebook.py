# Python Lesson 6 - Challenge Course

kashima = {
    "name": "Ryuuichi",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

kamitani = {
    "name": "Hayato",
    "homework": [90.0, 87.0, 75.0, 88.0],
    "quizzes": [90.0, 75.0, 88.0],
    "tests": [99.0, 97.0]
}

inomata = {
    "name": "Maria",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [95.0, 98.0, 96.0],
    "tests": [100.0, 100.0]
}

# Student Roster
students = [kashima, kamitani, inomata]

for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]
    print

# Using built-in sum(), float(), & len() functions to obtain class avg
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Calculating weighted avg using built-in average() function
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.10 * homework + 0.30 * quizzes + 0.60 * tests

# Using if/else statement to convert student avg to letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "Fail"
    
# print get_letter_grade(get_average(kashima))