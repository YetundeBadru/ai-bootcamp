# Concept 1: Modules and Import
from helpers import average, grade_model

scores = [0.92, 0.65, 0.83, 0.75, 0.95]
avg = average(scores)
print(round(avg, 2), grade_model(avg))

# Concept 2: Error handling with try/except
try:
    print("Before")
    with open("missing.txt", "r") as f:
        print ("Opened")
        text = f.read()
    print("After")
except FileNotFoundError:
    print("That file does not exist")

try:
    with open("missing.txt", "r") as f:
        text = f.read()
    print(text)
except FileNotFoundError:
    print("That file does not exist")

try:
    number = int("abc")
except ValueError:
    print("Not a number")

# Concept 3: Classes (the basics)
class student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def average(self):
        return sum(self.scores) / len(self.scores)
bimpe = student("Bimpe", [0.95, 0.83, 0.75, 0.69])
print(bimpe.name)
print(round(bimpe.average(), 2))

# My exercises (Day 3)
# Create helpers.py and main.py as shown, and run py main.py.
# Done ! , file created: helperss.py

# Move your count_above and max_number functions into helpers.py, then import and call them from main.py.
from helpers import count_above

numbers = [0.91, 0.85, 0.93, 0.78]
threshold = 0.9
print(count_above(numbers, threshold))

# Write a function read_scores(filename) in helpers.py that reads scores.txt (the file you made yesterday) and returns the numbers as a list. Wrap the file reading in try/except FileNotFoundError and print a friendly message if the file is missing. Hint: each line is text, so convert it with float(line). You can loop over the file with for line in f:.
from helpers import read_scores

print(read_scores("scores.txt"))
print(read_scores("nothing.txt"))

# Challenge: Create a Student class like the one above, make two students, and print each one’s name and average.
class student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def average(self):
        return sum(self.scores) / len(self.scores)

john = student("John", [0.59, 0.43, 0.50, 0.61])
mark = student("Mark", [0.95, 0.87, 0.70, 0.92])
print(john.name)
print(round(john.average(), 2))
print(mark.name)
print(round(mark.average(), 2))

    