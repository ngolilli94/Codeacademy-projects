# Mini project for practicing functions, lists, & translating math formula into programming statements

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# Helper function
def print_grades(grades_input):
    for grade in grades_input:
        print grade

print_grades(grades)

# Manually computing sum of all test grades
def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

print grades_sum(grades)

# Calculating avg using sum function
def grades_average(grades_input):
    total = grades_sum(grades_input)
    avg = total / float(len(grades_input))
    return avg

print grades_average(grades)

# Computing variance (how grades varied against average)
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        squared_diff = (average - score) ** 2
        variance += squared_diff
    return variance / len(scores)

print grades_variance(grades)

# Standard deviation
def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)